import os
import time
import sys

index = 0
internal = sys.argv[1]
out_folder = sys.argv[2]
while True:
  command = 'screencapture -t png %s/screenshot%s.png' % (out_folder, index)
  print(command)
  os.system(command)
  index += 1
  time.sleep(int(internal))