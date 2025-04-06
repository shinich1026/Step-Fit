import csv
import random

from random import randrange
x = randrange(100, 180)
print(f"pitch is {x} \n")

musics = []

with open("musics.csv") as file:
    reader = csv.reader(file)
    for song, bpm in reader:
        y = int(bpm)
        # musics.append({"song": song, "bpm": y})
        m = x - y
        # musics.append({"song": song, "gap": m})
        n = m ** 2
        if n < 16:
            musics.append({"song": song, "bpm": y})

def get_bpm(music):
    return music["bpm"]

for music in sorted(musics, key=get_bpm):
    print(f"{music["song"]}, {music["bpm"]} \n")


print(f"pitch is {x}")

