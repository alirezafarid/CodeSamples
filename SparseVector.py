#!/anaconda3/bin/python
class SparseVector:

  def __init__(self,denseArray):


    self.size = len(denseArray)
    self.sparseDic = {}

    for i in range(len(denseArray)):
      if denseArray[i] != 0:    
        self.sparseDic[i] = denseArray[i] 



  def get_element_at(self, index):

    if index in self.sparseDic:
      return self.sparseDic[index]
    else:
      return 0

  def length(self):
  	return self.size 
 
  def dot(self, other_vector):

    dotProductDic = {}
    if (self.length() != other_vector.length()):
      return 'Error! Vectors should have the same size.'

    set1 = set(self.sparseDic)
    set2 = set(other_vector.sparseDic)
    commonIndices = set1.intersection(set2)


    for i in commonIndices:
      dotProductDic[i] =\
      self.sparseDic[i] * other_vector.sparseDic[i]

    return sum(list(dotProductDic.values()))

  def iterate_non_zero(self):

    for index in self.sparseDic:
      yield (index, self.sparseDic[index])

def main():

  denseArray1 = [0,1,0,1,0,8]

  SP1 = SparseVector(denseArray1)

  print(SP1.length()) 
  #output: 6

  for index in range(SP1.length()):
    print(index,SP1.get_element_at(index))
  #output:
  # 0 0
  # 1 1
  # 2 0
  # 3 1
  # 4 0
  # 5 8


  
  for elm in SP1.iterate_non_zero():
     print((elm[0],elm[1]))
  #ouput:
  # (1, 1)
  # (3, 1)
  # (5, 8)


  denseArray2 = [0,1,0,0,0,1.5]

  SP2 = SparseVector(denseArray2)

  print(SP1.dot(SP2))
  #output: 13.0



#https://www.geeksforgeeks.org/python-pandas-series-get/

main()