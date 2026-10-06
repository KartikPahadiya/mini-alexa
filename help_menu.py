"""Help menu for Mini Alexa.

Implements FR-10: display a help menu listing every supported command
with a one-line description, in a format a first-time user can scan.
"""

# Single source of truth for the command list: the help menu and any
# "unknown command" hint both derive from this table.
COMMANDS = [
    ("hello", "greet me again"),
    ("time", "show current time"),
    ("date", "show current date"),
    ("calculate 12 + 8", "do a calculation (+, -, *, /)"),
    ("quote", "get a motivational quote"),
    ("joke", "hear a joke"),
    ("fact", "learn a random fact"),
    ("recommend", "rule-based activity recommendation (AI demo)"),
    ("perceptron", "simplified neural-neuron demo (DL demo)"),
    ("game", "play the number guessing game"),
    ("help", "show this command list"),
    ("exit / quit / bye", "quit the assistant"),
]


def print_help():
    """Return the formatted help menu text (FR-10)."""
    width = max(len(cmd) for cmd, _ in COMMANDS)
    lines = ["Assistant: Here's what I can do:"]
    for cmd, desc in COMMANDS:
        lines.append("  {0:<{1}}  {2}".format(cmd, width, desc))
    return "\n".join(lines)
