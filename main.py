from typing import Union

from fastapi import FastAPI

import random as rand
import math

app = FastAPI()

joke_set = [
    "I told my computer I needed a break, and now it won't stop sending me beach photos.",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I asked the math book for some advice, but it had too many problems of its own.",
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/joke")
def get_joke():
    randNo = math.floor(rand.random() * len(joke_set))
    print(randNo)
    return {"joke": joke_set[randNo]}
