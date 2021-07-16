#implementation of the Merge routine
import random

def Merge(a,b):
  """inputs: a and b sorted arrays
     return: c sorted array of length len(a)+len(b)(ascending)
  """
  i,j = 0,0
  sortedArray = []
  for k in range(len(a)+len(b)):
    if i == len(a):
        sortedArray += b[j:]
        break
    elif j == len(b):
        sortedArray += a[i:]
        break
    if a[i] < b[j]:
      sortedArray.append(a[i])
      i += 1
    else:
      sortedArray.append(b[j])
      j += 1 
  return sortedArray
  
def mergeSort(arr):
  if len(arr) == 1 or len(arr) == 0:
    return arr
  else:
    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]
    sortedArray = Merge(mergeSort(left), mergeSort(right))
  return sortedArray

#TEST cases
empty = []
okSorted = [i+1 for i in range(10)]
reversedList = [i for i in range(10,1,-1)]
allEqual = [1 for i in range(10)]
dupes = [random.choice([1,3,6,7]) for i in range(5)]

print(dupes, mergeSort(dupes))
