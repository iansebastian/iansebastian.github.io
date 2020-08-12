class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

class BST:    
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
            return root
    def search(self, root, data):
        found = False
        if root:
            if data > root.data:
                return self.search(root.right, data)
            if data < root.data:
                return self.search(root.left, data)
            if data == root.data:
                found = True
        if found:
            return "Found!"
        else:
            return "Not Found"
    def getHeight(self, root, x = 0, lengths = []):
        if root.left or root.right:
            if root.left:
                # print('left', root.data, x)
                self.getHeight(root.left, x+1, lengths)
            if root.right:
                # print('right', root.data, x)
                self.getHeight(root.right, x+1, lengths)
        else:
            # print('road end')
            lengths.append(x)
        return max(lengths)

    def getHeightHR(self, root):
        if root == None:
            return -1
        else:
            return max(getHeightHR(root.left), getHeightHR(root.right))+1
T = int( input() )
myTree = BST()
root = None
for i in range(T):
    data = int( input() )
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print("Height:", height)
print("Height HackerRank", height)
nemo = myTree.search(root, 5)
print("Finding value 5 in map...", end=" ")
print(nemo)