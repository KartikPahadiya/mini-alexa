"""Date and time reporting for Mini Alexa.

Implements FR-03 (display the current date on request) and FR-04
(display the current time on request) using only the standard-library
datetime module — no network calls, no external services.
"""

from datetime import datetime

TIME_FORMAT = "%I:%M %p"   # 12-hour clock, e.g. "03:45 PM"
DATE_FORMAT = "%A, %B %d, %Y"  # e.g. "Monday, October 06, 2026"


def get_current_time():
    """Return the current system time as a human-readable string."""
    return datetime.now().strftime(TIME_FORMAT)


def get_current_date():
    """Return today's date as a human-readable string."""
    return datetime.now().strftime(DATE_FORMAT)


def respond_time():
    """Build the assistant's response for a 'time' command."""
    return "Assistant: It's currently {0}.".format(get_current_time())


def respond_date():
    """Build the assistant's response for a 'date' command."""
    return "Assistant: Today is {0}.".format(get_current_date())
