S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

def binarySearch(array, value, lo, hi):
  mid = lo + (hi - lo) // 2
  if lo > hi: return lo if lo < len(array) else hi
  if array[mid] == value: return mid
  elif array[mid] < value: return binarySearch(array, value, mid + 1, hi)
  else: return binarySearch(array, value, lo, mid - 1)

def search(array, value):
  index = binarySearch(array, value, 0, len(array) - 1)
  return array[index]

def max_subset(S, D):
  mapS = {}
  for i in range(len(S)):
    c = S[i]
    if c in mapS:
      mapS[c].append(i)
    else:
      mapS[c] = [i]

  candidates = []

  for word in D:
    i = -1
    for c in word:
      if c in mapS:
        indices = mapS[c]
        j = search(indices, i+1)
        if j <= i:
          i = -1
          break
        i = j
      else:
        i = -1
        break
    if i != -1:
      candidates.append(word)

  return max(candidates, key=lambda x: len(x)) if candidates else None