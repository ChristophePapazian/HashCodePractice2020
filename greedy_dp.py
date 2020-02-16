# HashCode Practice 2020 by Chistophe Papazian
# Greedy with Dynamic Programming


import sys

DP = 10000 # threshold for exhaustive research. use 200000 is enough for D, 10000 enough for all others.


def main():
  B, _ = map(int, input().split())
  V = list(map(int, input().split()))
  MAX_INIT = MAX = B+1
  RESG = []
  if sum(V)>DP: #Be greedy
    for k, v in enumerate(reversed(V)):
      if v < MAX:
        RESG.append(len(V)-1-k)
        MAX -= v
      if MAX < DP:
        break

  MAX_IDX = RESG[-1] if RESG else len(V)
  CACHE = [None]*(MAX) #Dynamic research
  CACHE[0] = 0
  for k, c in enumerate(V):
    if k >= MAX_IDX:
      break
    for i in reversed(range(MAX-c)):
      if CACHE[i] is not None and CACHE[i+c] is None:
        CACHE[i+c] = k
  for i in range(MAX):
    if CACHE[MAX-i-1] is not None:
      RES, t = [], MAX-i-1
      SCORE = t
      while t > 0:
        RES.append(CACHE[t])
        t -= V[CACHE[t]]
      break
  print(MAX_INIT-MAX+SCORE, file=sys.stderr) #Print score on stderr
  RES = list(reversed(RES))
  RES.extend(reversed(RESG))
  print(len(RES))
  print(' '.join(str(c) for c in RES))


main()
