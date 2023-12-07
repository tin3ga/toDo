import datetime
import random

weekdays: list[str] = ["Monday 😛",
           "Tuesday 🍒",
           "Wednesday 😬",
           "Thursday 🥱",
           "Friday 🍻",
           "Saturday 🤗",
           "Sunday 😴"
]

random_words: list[str] = [
    "Hello, it's ",
    "Hey, it's ",
    "Smile, it's ",
    "Warm wishes, it's ",
    "Wonderful, it's ",
    "Wishing you a fantastic ",
    "Sending you a big hug, it's ",
    "Have an amazing "
]


def greet_message() -> str:
    """
    Generates a random greeting message based on the current day of the week.

    Returns:
        str: A greeting message composed of a random phrase and the corresponding day's emoji.
    """
    today = datetime.date.today().weekday()
    message = f'{random.choice(random_words)}{weekdays[today]}'
    return message


if __name__ == '__main__':
    print(greet_message())