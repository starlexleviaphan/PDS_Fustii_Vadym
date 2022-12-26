class Tree:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


    def insert(self, val):                      #<-----insert method
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Tree(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Tree(val)

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.val:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.val:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.val) + ' is found')

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val),
        if self.right:
            self.right.print_tree()



a  = Tree(10)
a.insert(12)
a.insert(16)
a.insert(8)


print(a.right.right)