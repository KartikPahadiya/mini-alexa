# Mini Alexa — Virtual AI Assistant

A text-based, rule-based virtual assistant that runs entirely offline in a
terminal. Built with the Python standard library only — no external
datasets, APIs, or AI frameworks.

Project 1 of the Nexbridge Technologies AI Internship Program (beginner
track). See `PRD.docx` for the full product requirements document.

## What it does

The assistant simulates conversational behavior using pattern matching and
keyword detection. On every loop iteration it: reads your text → normalizes
it → matches it against keyword rules → routes to a feature function →
prints the response. That if-elif router is a hand-written decision tree —
the same *shape* as a real assistant's intent classifier, but fully
rule-based and trained on nothing.

## Requirements

- Python 3.x (standard install — nothing else needed)
- No internet connection required

## How to run

```bash
python main.py
```

The assistant greets you, asks for your name, and then waits for commands.

## Commands

| Command | What it does |
| --- | --- |
| `hello` | greet you again |
| `time` | show the current time |
| `date` | show today's date |
| `calculate 12 + 8` | basic arithmetic (`+`, `-`, `*`, `/`; also `plus`, `minus`, `times`, `divided by`) |
| `quote` | random motivational quote |
| `joke` | random joke |
| `fact` | random fact |
| `recommend` | rule-based activity recommendation based on the time of day (AI demo) |
| `perceptron` | simplified artificial-neuron demo: inputs × weights + bias → step activation → 0/1 (DL demo) |
| `game` | number guessing game (1–20, 5 attempts, higher/lower hints) |
| `help` | show the full command list |
| `exit` / `quit` / `bye` | end the session gracefully |

Anything unrecognized gets a friendly fallback message — the program never
crashes on bad input (division by zero, non-numeric text, etc. are all
handled with `try/except`).

## Project structure

```
virtual-ai-assistant/
|-- main.py            # entry point: main loop, normalization, command routing
|-- greetings.py       # get_user_name(), build_greeting(), respond_greeting()
|-- datetime_utils.py  # get_current_time(), get_current_date()
|-- calculator.py      # parse_expression(), calculate()
|-- content.py         # QUOTES / JOKES / FACTS lists + random selectors
|-- game.py            # play_guessing_game()
|-- ai_concepts.py     # recommend_activity(), perceptron_demo()
|-- help_menu.py       # print_help()
|-- README.md          # this file
```

## AI / ML / DL concepts demonstrated

| Concept | Where it appears |
| --- | --- |
| Rule-based system | The entire assistant: explicit if/elif rules map input patterns to responses |
| Intent recognition | Keyword detection decides which "intent" (time, joke, calculate…) your text expresses |
| Pattern matching | `.lower()`, `in`, `.split()` detect trigger words in free-form input |
| Decision tree / classification | `recommend_activity()` assigns the current hour to a category via an if-elif chain |
| Recommendation | Random quote/joke/fact selection — the simplest stand-in for a recommender |
| Perceptron (single neuron) | `ai_concepts.perceptron_output()`: inputs × weights + bias → step activation → 0/1 |
| Forward propagation | The left-to-right flow of the perceptron demo (inputs → weights/bias → activation → output) |

No real model is trained anywhere — the goal is to make the vocabulary and
arithmetic of AI tangible with plain Python before moving to real ML/DL
libraries in later projects.
