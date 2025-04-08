import csv
import random

from random import randrange
x = randrange(10, 18)
print(f"pitch/10 is {x} \n")



with open("musics.csv") as file:
    reader = csv.reader(file)
    for title, bpm in reader:
        y = int(bpm)
        z = y / 10
        # musics.append({"song": song, "bpm": y})
        m = x - z
        # musics.append({"song": song, "gap": m})
        n = m ** 2
        if n < 0.16:
            class Music:
                def __init__(self, title2, bpm2):
                    self.title2 = title2
                    self.bpm2 = bpm2

                def __str__(self):
                    return f"{self.title2} is {self.bpm2}"
                
                @classmethod
                def get(cls):
                    title2 = title
                    bpm2 = bpm
                    return cls(title2, bpm2)
                
            def main():
                music = Music.get()
                print (music)

            if __name__ == "__main__":
                main()






