"""Entertainment content for Mini Alexa: quotes, jokes, and facts.

Implements FR-06 (random motivational quote), FR-07 (random joke), and
FR-08 (random fact). Each is a predefined list of strings; the standard-
library random module selects one entry per request.

Concept note (ML analogy): selecting an item from a list "at random" is
the simplest possible recommendation — later projects replace this rule
with a model that predicts which item the user is most likely to enjoy.
"""

import random

QUOTES = [
    "The best way to predict the future is to invent it.",
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "Simplicity is the soul of efficiency.",
    "Every expert was once a beginner.",
    "Small steps every day add up to big results.",
    "It always seems impossible until it's done.",
    "Stay hungry, stay foolish.",
    "The only way to do great work is to love what you do.",
    "Debugging is being the detective in a crime film where you are also the murderer.",
]

JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the computer show up late to work? It had a hard drive.",
    "There are only 10 kinds of people: those who understand binary and those who don't.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "A SQL query walks into a bar, sees two tables and asks... 'May I join you?'",
    "Why was the JavaScript developer sad? They didn't Node how to Express themselves.",
    "What's a programmer's favorite hangout place? The Foo Bar.",
]

FACTS = [
    "Honey never spoils — archaeologists have tasted 3,000-year-old honey from Egyptian tombs.",
    "Octopuses have three hearts, and two of them stop beating when they swim.",
    "The first computer bug was an actual moth found in a Harvard Mark II in 1947.",
    "Bananas are berries, but strawberries are not — botanically speaking.",
    "A day on Venus is longer than a year on Venus.",
    "The Eiffel Tower grows about 15 cm taller in summer due to heat expansion.",
    "Your brain generates about 20 watts of electrical power — enough to dim a light bulb.",
    "There are more possible chess games than atoms in the observable universe.",
    "Wombat poop is cube-shaped.",
    "The first website is still online — info.cern.ch, created in 1991.",
]


def get_random_quote():
    """Return one random motivational quote (FR-06)."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return one random joke (FR-07)."""
    return random.choice(JOKES)


def get_random_fact():
    """Return one random fact (FR-08)."""
    return random.choice(FACTS)


def respond_quote():
    """Build the assistant's response for a 'quote' command."""
    return "Assistant: {0}".format(get_random_quote())


def respond_joke():
    """Build the assistant's response for a 'joke' command."""
    return "Assistant: {0}".format(get_random_joke())


def respond_fact():
    """Build the assistant's response for a 'fact' command."""
    return "Assistant: Did you know? {0}".format(get_random_fact())
