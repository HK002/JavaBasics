class BinaryTree:

    def __init__(self,data):
        self.data=data
        self.lchild = None
        self.rchild = None

    def create(self,node,data):
        if node.data == data:
            print("Duplicate Data. Cannot insert into the tree")
            return
        if data < node.data and node.lchild is None:
            node.lchild = BinaryTree(data)
            return
        if data > node.data and node.rchild is None:
            node.rchild = BinaryTree(data)
            return    
        if data < node.data and node.lchild is not None:
            node.create(node.lchild,data)
        if data > node.data and node.rchild is not None:
            node.create(node.rchild,data)    

    def level_order_traversal(self,node):
        pass



root = BinaryTree(12)
root.create(root,5) 
root.create(root,3) 
root.create(root,4) 
root.create(root,1) 
root.create(root,15) 
root.create(root,11) 
root.create(root,18) 
root.create(root,10) 
root.create(root,20) 
root.create(root,2) 
        