class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=node(root)
    def print_preorder(self,start,traversal):
        if start:
            traversal+=str(start.value)+"-"
            traversal=print_preorder(start.left,traversal)
            traversal=print_preorder(start.right,traversal)
        return traversal
    
    def print_tree(self,t_type):
        if t_type!=type(int):
            print("Wrong input.")
        if t_type=="preorder":
            return self.print_preorder(self.root,"")

tree=BinaryTree("1")
tree.root.left=node("2")
tree.root.left.left=node(4)
tree.root.right=node("3")
tree.root.left.right=node(5)
tree.root.right.left=node(6)
tree.root.right.right=node(7)
print(tree.print_preorder(tree.root,""))