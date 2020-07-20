# print_tree
# insert(value)
# search(value)
# delete(value)

# with no duplicate

class Node:
   
    def __init__(self, data = None, left =None,right = None):
        self.data = data 
        self.left = left 
        self.right = right

class BST :
    def __init__ (self, node = None):
        self.root = node
    
    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else :
             self._insert(self.root , node)

    def _insert(self,parent , child ):
    
        if child.data > parent.data :
            if parent.right == None:
                parent.right = child
            else :
                self._insert(parent.right, child)

        elif child.data < parent.data :
            if parent.left == None:
                parent.left = child
            else :
                self._insert(parent.left, child)

        else :
            print("sorry this is already present in the BST ")

    def print(self):
        if self.root!= None:
            self._print(self.root)
        else :
            print (" sorry today is sunday , root is on vacation ")
    
    def _print(self, node):
        print(node.data)

        if node.left!=None:
             print("left nodes are : ")
             self._print(node.left)

        if node.right!=None:
            print("right nodes are : ")
            self._print(node.right)


    def search(self, value):
        if self.root!=None:
            if self._search(self.root,value)!=1 :
                 print("we are really very sorry , we could find it ! ")

        else :
            print("oops the tree is empty")

    def _search(self, currNode, value):
        if currNode.data == value:
            print("yeaahhh winner winner chicken dinner ")
            return 1
        elif  value <  currNode.data  and currNode.left!=None:
            return self._search(currNode.left,value)
        elif value >  currNode.data  and currNode.right!=None:
            return self._search(currNode.right,value)
    
       
        return 0




if __name__ == '__main__' :
    root  = Node(10)
    bstree = BST(root)
    bstree.insert(5)
    bstree.insert(20)
    bstree.insert(30)

    bstree.print()

    bstree.search(0)

   