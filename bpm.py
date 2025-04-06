import csv
import random

from random import randrange
x = randrange(100, 180)
print(f"pitch is {x} \n")

musics = []

with open("musics.csv") as file:
    reader = csv.reader(file)
    for title, bpm in reader:
        y = int(bpm)
        # musics.append({"song": song, "bpm": y})
        m = x - y
        # musics.append({"song": song, "gap": m})
        n = m ** 2
        if n < 16:
            class Music:
                def __init__(self, title, bpm):
                    self.title = title
                    self.bpm = bpm
                musics.append(title)
                musics.append(bpm)
print (musics)

