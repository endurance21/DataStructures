# implementation of max-heap 

# Methods includes -> push() , getMin() ,popMin(),


class MinHeap : 
    def __init__(self, arr = []):
        self.heap = [0]  #we will not use the 0th index so we placed 0  at first index , you can choose to populate it with any aribitrary value of you choice 
        for index , item in enumerate(arr):
            self.heap.append(item)
            self._moveUp(index+1)

    def push(self,value):
        self.heap.append(value)
        index = self.getSize()
        self._moveUp(index ) 

    def getMin(self):
        if(self.getSize() > 0):
            return self.heap[1]
        else :
             return false

    def popMin(self):
        if(self.getSize()  == 1):
            max = self.heap[1]
            self.heap.pop()
        elif(self.getSize() > 1):
            self._swap( 1 ,self.getSize()) 
            self.heap.pop()
            self._moveDown(1)
        else :
            return False
    
    def _moveUp(self, index):
        parent = index//2

        if(index <=1):
            return 
        if(self.heap[parent] > self.heap[index]):
            self._swap(parent,index)
            self._moveUp(parent)
    
    def _moveDown(self, index):
        left = 2*index 
        right = left + 1
        smallest = index
        if(left <=self.getSize() and self.heap[left] < self.heap[index]):
           smallest = left
        
        if(right <= self.getSize() and self.heap[right] < self.heap[index]):
           smallest = right
        if(smallest!=index):
            self._swap(smallest,index)
            self._moveDown(smallest)

        else :
            return
       

    def _swap(self, index1, index2 ):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1] 

    def getSize(self):
        return (len(self.heap) - 1) 

      
if __name__ == '__main__' :
    m = MinHeap()
    m.push(20)
    m.push(-1)
    m.popMin()
    print(m.heap)