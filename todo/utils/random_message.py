import datetime
import random

weekday = ["Monday 😛",
           "Tuesday 🍒",
           "Wednesday 😬",
           "Thursday 🥱",
           "Friday 🍻",
           "Saturday 🤗",
           "Sunday 😴"
]

random_word = [
    "Hello, it's ",
    "Hey, it's ",
    "Smile, it's ",
    "Warm wishes, it's ",
    "Wonderful, it's ",
    "Wishing you a fantastic ",
    "Sending you a big hug, it's ",
    "Have an amazing "
]


def greet_message():
    today = datetime.date.today().weekday()
    message = f'{random.choice(random_word)}{weekday[today]}'
    return message


if __name__ == '__main__':
    print(greet_message())