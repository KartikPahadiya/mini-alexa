"""Basic calculator for Mini Alexa.

Implements FR-05: perform add / subtract / multiply / divide on request.

Parsing strategy (rule-based, no external libraries):
  1. Remove the trigger word ("calculate", "what is", ...) if present.
  2. Split the rest into tokens and find the operator token.
  3. Convert the tokens around the operator to floats.
  4. Perform the operation inside try/except so divide-by-zero and
     non-numeric input never crash the program (reliability NFR).

This mirrors a simple decision tree: the operator token selects which
branch (add / subtract / multiply / divide) to execute.
"""

OPERATORS = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
    "plus": "add",
    "minus": "subtract",
    "times": "multiply",
    "multiplied by": "multiply",
    "divided by": "divide",
}

TRIGGER_WORDS = ("calculate", "what is", "what's", "compute")


def parse_expression(text):
    """Extract (left_operand, operator, right_operand) from free-form text.

    Args:
        text (str): normalized user input, e.g. "calculate 12 + 8".
    Returns:
        tuple (float, str, float) on success, or None if the expression
        cannot be parsed (missing numbers / unknown operator).
    """
    cleaned = text
    for trigger in TRIGGER_WORDS:
        if cleaned.startswith(trigger):
            cleaned = cleaned[len(trigger):].strip()
            break

    tokens = cleaned.split()
    for i, token in enumerate(tokens):
        op_name = OPERATORS.get(token)
        if op_name is None:
            continue
        # Need exactly one number before and one after the operator token.
        if i == 0 or i == len(tokens) - 1:
            return None
        try:
            left = float(tokens[i - 1])
            right = float(tokens[i + 1])
        except ValueError:
            return None
        return left, op_name, right
    return None


def calculate(left, operator, right):
    """Perform the arithmetic operation.

    Args:
        left (float): first operand.
        operator (str): one of 'add', 'subtract', 'multiply', 'divide'.
        right (float): second operand.
    Returns:
        float: the numeric result.
    Raises:
        ZeroDivisionError: if dividing by zero (handled by the caller so the
            program can reply with a friendly message instead of crashing).
    """
    if operator == "add":
        return left + right
    if operator == "subtract":
        return left - right
    if operator == "multiply":
        return left * right
    if operator == "divide":
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return left / right
    raise ValueError("unknown operator: {0}".format(operator))


def format_number(value):
    """Format a float result without a trailing '.0' for whole numbers."""
    if value == int(value):
        return str(int(value))
    return str(round(value, 4))


def respond_calculator(text):
    """Full calculator command handler: parse, compute, and build a reply.

    Args:
        text (str): the user's raw (normalized) input.
    Returns:
        str: the assistant's response — a result or a friendly error.
    """
    parsed = parse_expression(text)
    if parsed is None:
        return (
            "Assistant: I couldn't parse that. Try something like "
            "'calculate 12 + 8'."
        )
    left, operator, right = parsed
    try:
        result = calculate(left, operator, right)
    except ZeroDivisionError:
        return "Assistant: I can't divide by zero — try a different number."
    except (ValueError, OverflowError):
        return "Assistant: That calculation isn't valid — check your numbers."
    return "Assistant: The result is {0}.".format(format_number(result))
