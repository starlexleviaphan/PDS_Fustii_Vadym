class Tree:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def insert(self, val):
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

    def get_min(self):                                      #<----- min
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):                                      #<----- max
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val),
        if self.right:
            self.right.print_tree()

    def delete(self, val):                                      #<----- deletion
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return selfdef
        delete(self, val):
        if self == None:
            return self
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return selfdef
        delete(self, val):
        if self == None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self


a = Tree(10)
a.insert(12)
a.insert(16)
a.insert(8)

print(a.get_min())