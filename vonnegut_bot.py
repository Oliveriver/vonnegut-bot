import time
import sys

prompt = input('Hi, this is Vonnegut.\n')
response = 'So it goes. '

# If you're reading this, congraulations: you got the joke.

# I considered creating an actual LLM that just happened to have its weights
# hard-coded in such a way that it would output 'So it goes' forever with 100%
# probability, but even for me, and even for this video, that was too much
# effort. Instead, you get a quick and dirty script that creates my favourite
# joke in the video. Sorry.

delay = 0.3

time.sleep(2)

for i in range(4):
  for j in range(3):
    sys.stdout.write(' ')
    sys.stdout.flush()
    time.sleep(delay / 2)
  sys.stdout.write('\r')
  sys.stdout.flush()
  time.sleep(delay / 2)

time.sleep(0.5)
sys.stdout.write('\n')
sys.stdout.flush()

while (True):
  for character in response:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(delay)
    delay = max(delay * 0.95, 0.0005)
