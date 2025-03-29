from itertools import count
import time
import sys

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




    
