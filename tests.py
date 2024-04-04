import tsort

def test_sort():
  assert tsort.sort(1, 1, 1, 1) == 'STANDARD'
  assert tsort.sort(1, 1, 1, 50) == 'SPECIAL'
  assert tsort.sort(200, 1, 1, 1) == 'SPECIAL'
  assert tsort.sort(100, 100, 100, 1) == 'SPECIAL'
  assert tsort.sort(200, 1, 1, 50) == 'REJECTED'
  assert tsort.sort(100, 100, 100, 50) == 'REJECTED'
