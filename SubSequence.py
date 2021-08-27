def validateSubsequence(array,sequence):
  arrIdx=0
  seqidx=0
  while arrIdx<len(array) and seqidx<len(sequence):
      if array[arrIdx]==sequence[seqidx]:
          seqidx+=1
      arrIdx+=1
  return seqidx==len(sequence)
validateSubsequence([4,5,6,7,8],[4,8])