def sublist(l1, l2):
  n = len(l1)

  while len(l2) != 0:
    if take(n, l2) == l1:
      return True
    
    l2 = tail(l2)

  return False
