import sys
import time
from time import sleep

def lirik():
  lines = [
    ("And your love's always been", 0.11),
    ("true as can be", 0.11),
    ("I give my heart to you", 0.2),
    ("I give my heart", 0.2),
    ("'Cause nothing can compare", 0.1),
    ("in this world to you", 0.1),
    ("whoa...", 0.1),
  ]

  delays = [1.1, 2.5, 3.7, 0.5, 0.1, 1.5, 15]

  for i, (line, char_delay) in enumerate(lines):
    for char in line:
      print(char, end='')
      sys.stdout.flush()
      sleep(char_delay)
    time.sleep(delays[i])
    print('')

lirik()