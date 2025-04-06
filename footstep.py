# 20秒簡振動から歩数カウント、はしりはじめ10秒間無視
import sys
import time

msg1 = "ignore..."
msg2 = "Count Start!!..."
for starting in range(7):
    sys.stdout.write("\r{} {} seconds ".format(msg1, starting + 1))
    time.sleep(0.1)
    sys.stdout.flush()
for running in range(6):
    sys.stdout.write("\r{} {} seconds ".format(msg2, running + 1))
    time.sleep(0.1)
    sys.stdout.flush()
print("\n", end = "")

# footsteps per a minutes = x
# 走り = 140 ~ 180  歩き = 100 ~ 120

from random import randrange
x = randrange(10, 18)
print(f"{x}")



if 10 <= x <= 12:
    print("YOU ARE WALLKING")
elif 14 <= x <= 18:
    print("YOU ARE RUNNING")
else:
    print("What the fuck are you doing?!: ")















