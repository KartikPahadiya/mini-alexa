"""Mini Alexa — a Virtual AI Assistant (rule-based, offline, console-only).

Project 1 of the Nexbridge Technologies AI Internship Program (beginner track).

This is the program entry point. It runs the main input -> normalize ->
match -> respond loop described in the PRD:

    User Input
        |
        v
    Normalize text (lowercase, strip spaces)
        |
        v
    Keyword / Pattern Match  --> route to the right module's responder
        |
        v
    Print response, loop back (until an exit command)

AI concept: this keyword-matching router is a rule-based intent
classifier. Each feature function in the other modules stands in for a
real assistant's skill, and the if-elif chain is a hand-written decision
tree — no machine learning model is trained anywhere in this project.

Standard library only — no external datasets, APIs, or AI frameworks.
"""

import sys

import greetings
import datetime_utils
import calculator
import content
import game
import ai_concepts
import help_menu

BANNER = "===========================================\n" \
         "        MINI ALEXA - VIRTUAL ASSISTANT\n" \
         "==========================================="

# Phrases that end the session (FR-11).
EXIT_COMMANDS = ("exit", "quit", "bye", "goodbye", "see you")


def normalize(text):
    """Normalize raw user input: lowercase + collapse whitespace.

    Pattern matching is far more reliable when case and extra spaces are
    removed first — this is the 'preprocessing' step of our rule-based
    pipeline.
    """
    return " ".join(text.lower().split())


def route_command(text, user_name):
    """Match the normalized command to a feature and return the response.

    Args:
        text (str): normalized user input.
        user_name (str): stored session name, reused in responses (FR-02).
    Returns:
        tuple (response:str, should_exit:bool) — the main loop prints the
        response and exits the session when should_exit is True.
    """
    # Ordered if-elif chain = a hand-written decision tree. The most
    # specific triggers are checked before the generic ones.
    if any(text.startswith(word) for word in EXIT_COMMANDS):
        return "Assistant: Goodbye, {0}! Have a great day.".format(user_name), True

    if "help" in text:
        return help_menu.print_help(), False

    if "calculate" in text or "what is" in text or "what's" in text:
        return calculator.respond_calculator(text), False

    if "time" in text:
        return datetime_utils.respond_time(), False

    if "date" in text or "day" in text:
        return datetime_utils.respond_date(), False

    if "recommend" in text or "suggest" in text or "activity" in text:
        return ai_concepts.recommend_activity(), False

    if "perceptron" in text or "neuron" in text or "neural" in text:
        return ai_concepts.perceptron_demo(), False

    if "quote" in text or "motivat" in text:
        return content.respond_quote(), False

    if "joke" in text or "funny" in text:
        return content.respond_joke(), False

    if "fact" in text:
        return content.respond_fact(), False

    if "game" in text or "guess" in text:
        # The game manages its own interactive input() and printing, so it
        # returns None — main() skips printing a response in that case.
        return game.play_guessing_game(), False

    if any(text.startswith(word) for word in ("hello", "hi", "hey")):
        return greetings.respond_greeting(user_name), False

    if "your name" in text:
        return ("Assistant: I'm {0}, your rule-based virtual assistant!"
                .format(greetings.ASSISTANT_NAME)), False

    # No keyword matched -> friendly fallback (FR-12), never a crash.
    return ("Assistant: I'm not sure I understood that, {0} — "
            "type 'help' to see what I can do.".format(user_name)), False


def main():
    """Program entry point: greet, capture name, then run the main loop."""
    print(BANNER)

    user_name = greetings.get_user_name()
    print(greetings.build_greeting(user_name))

    # Main session loop (FR-01 through FR-14 all live behind this loop).
    while True:
        try:
            raw = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            # Even Ctrl+C / Ctrl+D ends the session gracefully (FR-11).
            print("\nAssistant: Goodbye, {0}! Have a great day.".format(user_name))
            break

        response, should_exit = route_command(normalize(raw), user_name)
        if response is not None:
            print(response)
        if should_exit:
            break

    print("===========================================")
    sys.exit(0)


if __name__ == "__main__":
    main()
