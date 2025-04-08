import csv
import random

from random import randrange
x = randrange(10, 18)
print(f"pitch is {x} \n")

musics = []

with open("musics.csv") as file:
    reader = csv.DictReader(file)
    for song, bpm in reader:
        y = int(bpm)
        z = y / 10
        # musics.append({"song": song, "bpm": y})
        m = x - z
        # musics.append({"song": song, "gap": m})
        n = m ** 2
        if n < 0.16:
            musics.append({"song": song, "bpm": y})

def get_bpm(music):
    return music["bpm"]

for music in sorted(musics, key=get_bpm):
    print(f"{music["song"]}, {music["bpm"]} \n")


print(f"pitch is {x}")

