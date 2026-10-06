"""Greeting logic and user-name capture for Mini Alexa.

Implements FR-01 (greet on startup and ask for the user's name) and
supports FR-02 (the name is stored in the main session and reused).
"""

ASSISTANT_NAME = "Mini Alexa"


def get_user_name():
    """Ask the user for their name and return it (stripped of whitespace).

    If the user enters nothing, a friendly default name is used so the
    rest of the session still works.
    """
    raw = input("Assistant: Hi! I'm {}. What's your name?\nYou: ".format(ASSISTANT_NAME))
    name = raw.strip()
    if not name:
        name = "friend"  # fallback so later responses never say "Sure thing, !"
    return name


def build_greeting(name):
    """Build the short welcome message shown right after the name is captured.

    Args:
        name (str): the user's name, stored in the session.
    Returns:
        str: a personalized welcome message that hints at the 'help' command.
    """
    return (
        "Assistant: Nice to meet you, {0}! Type 'help' to see what I can do."
        .format(name)
    )


def respond_greeting(name):
    """Respond to a mid-session greeting command (e.g. 'hello', 'hi').

    Demonstrates rule-based pattern matching: the main loop detected the
    greeting keyword and routed here, like a tiny intent classifier.
    """
    return "Assistant: Hello again, {0}! How can I help?".format(name)
