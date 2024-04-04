#!/usr/bin/env python3

import sys

def sort(width, height, length, mass):
  bulky = False
  heavy = False

  if width >= 150 or height >= 150 or length > 150:
    bulky = True
  elif width * height * length >= 1000000:
    bulky = True

  if mass >= 20:
    heavy = True

  if heavy and bulky:
    return 'REJECTED'

  if heavy or bulky:
    return 'SPECIAL'

  return 'STANDARD'


if __name__ == "__main__":
  ans = sort(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
  print(ans)
