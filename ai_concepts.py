"""Educational AI / ML / DL concept demonstrations for Mini Alexa.

Implements:
  - FR-13: a rule-based activity recommendation driven by the current
    hour of day — an explicit chain of if-elif-else rules, which is the
    whole assistant's architecture in miniature (a rule-based system),
    and structurally identical to a shallow decision tree.
  - FR-14: a simplified, NON-TRAINED perceptron. It takes 2-3 numeric
    inputs, multiplies each by a fixed weight, adds a fixed bias, and
    applies a step activation function to output 0 or 1. This is the
    building block of a neural network, demonstrated with plain Python
    arithmetic only — no TensorFlow, PyTorch, or training.

Both demos run interactively and return a transcript string.
"""

from datetime import datetime

# --- FR-13: rule-based recommendation -------------------------------------
# These hour boundaries are plain configuration values, not learned data:
# a developer wrote the rules by hand, which is exactly what makes this a
# rule-based system rather than a trained model.

BREAKFAST_START, BREAKFAST_END = 6, 10
LUNCH_START, LUNCH_END = 12, 14
DINNER_START, DINNER_END = 18, 21

# --- FR-14: perceptron configuration --------------------------------------
# Fixed weights and bias chosen by hand (not learned). A real neural
# network would *learn* these numbers by training; here they are constants
# so the arithmetic of forward propagation can be seen clearly.

PERCEPTRON_WEIGHTS = (0.6, 0.3, 0.9)   # one weight per input
PERCEPTRON_BIAS = -1.0                 # shifts the decision boundary
ACTIVATION_THRESHOLD = 0.0             # step function: 1 if sum > 0 else 0


def recommend_activity():
    """Recommend an activity based on the current hour (FR-13).

    The if-elif-else chain below is a rule-based classifier: the 'feature'
    is the current hour, and each branch assigns it to a category
    (breakfast / lunch / dinner / work / rest). Swap the hard-coded rules
    for learned thresholds and you have the same shape as a decision tree.
    """
    hour = datetime.now().hour
    if BREAKFAST_START <= hour < BREAKFAST_END:
        activity = "time for breakfast — grab something energizing!"
    elif LUNCH_START <= hour < LUNCH_END:
        activity = "lunch break! Step away from the keyboard for a bit."
    elif DINNER_START <= hour < DINNER_END:
        activity = "dinner time. You've earned a good meal."
    elif hour < 6:
        activity = "the middle of the night — some rest would be smart."
    else:
        activity = "a solid block for focused work or study."
    return ("Assistant: Based on the current time, I'd suggest: {0} "
            "(rule-based recommendation: I matched the hour against a set "
            "of if-else rules, like a tiny decision tree.)".format(activity))


def step_activation(weighted_sum):
    """Step activation function: output 1 if the sum is above the threshold, else 0.

    Real neurons use smoother activations (sigmoid, ReLU), but the step
    function is how the original 1950s perceptron worked and is the
    easiest to read.
    """
    if weighted_sum > ACTIVATION_THRESHOLD:
        return 1
    return 0


def perceptron_output(inputs, weights, bias):
    """Compute one neuron's output: the forward-propagation formula.

    out = activation( w1*x1 + w2*x2 + w3*x3 + b )

    This left-to-right flow (inputs -> weights/bias -> activation ->
    output) is exactly what 'forward propagation' means in a real network;
    a full network just stacks thousands of these calculations in layers.
    """
    weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias
    return weighted_sum, step_activation(weighted_sum)


def perceptron_demo():
    """Interactive perceptron demo (FR-14): collect 3 numbers, show the math.

    Returns:
        str: a transcript explaining inputs, weights, bias, the weighted
        sum, the activation step, and the final 0/1 output.
    """
    print("Assistant: Perceptron demo! Give me 3 numbers (this simulates a "
          "single artificial neuron — the simplest unit of a neural network).")
    inputs = []
    for n in range(1, 4):
        while True:
            try:
                value = float(input("Assistant: Input #{0}:\nYou: ".format(n)))
                break
            except ValueError:
                print("Assistant: That wasn't a number — try again.")
        inputs.append(value)

    weighted_sum, output = perceptron_output(
        inputs, PERCEPTRON_WEIGHTS, PERCEPTRON_BIAS
    )
    terms = " + ".join(
        "({0} x {1})".format(w, i) for w, i in zip(PERCEPTRON_WEIGHTS, inputs)
    )
    return (
        "Assistant: Here's the forward pass:\n"
        "  inputs          = {0}\n"
        "  weights         = {1}  (fixed, not learned)\n"
        "  bias            = {2}\n"
        "  weighted sum    = {3} + ({2}) = {4}\n"
        "  activation      = step(sum > {5} ? 1 : 0)\n"
        "  OUTPUT          = {6}\n"
        "That's one neuron doing forward propagation — a deep network is "
        "just millions of these stacked in layers!"
    ).format(inputs, list(PERCEPTRON_WEIGHTS), PERCEPTRON_BIAS,
             terms, round(weighted_sum, 4), ACTIVATION_THRESHOLD, output)
