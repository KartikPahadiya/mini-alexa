"""Number-guessing game for Mini Alexa.

Implements FR-09: the assistant picks a random number in a fixed range,
the user has a limited number of guesses, and the assistant gives
'higher'/'lower' hints until the number is found or the attempts run out.

Uses only random.randint and plain input/loops — no external libraries.
"""

import random

LOWER_BOUND = 1
UPPER_BOUND = 20
MAX_ATTEMPTS = 5


def play_guessing_game():
    """Run the full guessing-game interaction.

    Hints are printed immediately after each guess (not buffered), so the
    player always sees the higher/lower feedback right when it matters.
    """
    secret = random.randint(LOWER_BOUND, UPPER_BOUND)
    print("Assistant: I'm thinking of a number between {0} and {1}. "
          "You have {2} tries.".format(LOWER_BOUND, UPPER_BOUND, MAX_ATTEMPTS))

    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            guess = int(input("Assistant: Guess a number ({0} try left):\nYou: "
                              .format(MAX_ATTEMPTS - attempt + 1)))
        except ValueError:
            print("Assistant: That's not a number — try again.")
            continue

        if guess == secret:
            print("Assistant: You got it in {0} attempt(s)! The number was {1}."
                  .format(attempt, secret))
            return
        if guess < secret:
            hint = "higher"
        else:
            hint = "lower"
        print("Assistant: Nope — go {0}!".format(hint))

    print("Assistant: Out of tries! The number was {0}. Better luck next time!"
          .format(secret))
