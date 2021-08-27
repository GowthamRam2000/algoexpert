def SortedSquaresArray(array):
    sortedSquares=[0 for _ in array]
    smallervalueidx=0
    largervalueidx=len(array)-1
    for idx in reversed(range(len(array))):
        smallervalue=array[smallervalueidx]
        largervalue=array[largervalueidx]
        if abs(smallervalue)>abs(largervalue):
            sortedSquares[idx]=smallervalue*smallervalue
            smallervalueidx+=1
        else:
            sortedSquares[idx]=largervalue*largervalue
            largervalueidx-=1
    print(sortedSquares)
    return sortedSquares.sort()


SortedSquaresArray([4,5,6,4,5,43,5,4,6])