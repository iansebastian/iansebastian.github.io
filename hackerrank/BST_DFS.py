from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def search(self, root, data):
        found = False
        if root:
            if data < root.data:
                return self.search(root.left, data)
            if data > root.data:
                return self.search(root.right, data)
            if data == root.data:
                found = True
        else:
            pass
        if found:
            return "Found!"
        else:
            return "Not found"
    def insert(self, root, data):
        if root:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        else:
            return Node(data)
        return root
    def getHeight(self, root):
        if root:
            return max(self.getHeight(root.left), self.getHeight(root.right))+1
        else:
            return -1
    def inOrder(self, root, repre=[]):
        if root:
            self.inOrder(root.left, repre)
            repre.append(root.data)
            self.inOrder(root.right, repre)
        return repre
    def postOrder (self, root, repre=[]):
        if root:
            self.postOrder(root.left, repre)
            self.postOrder(root.right, repre)
            repre.append(root.data)
        return repre
    def preOrder(self, root, repre=[]):
        if root:
            repre.append(root.data)
            self.preOrder(root.left, repre)
            self.preOrder(root.right, repre)
        return repre
    def levelOrder(self, root):
        queue = deque()
        repre = []
        if root:
            queue.append(root)
            while queue:
                tree = queue.popleft()
                repre.append(tree.data)
                if tree.left:
                    queue.append(tree.left)
                if tree.right:
                    queue.append(tree.right)
        return repre
    def levelOrderHR(self, root):
        traversal = ''
        if root:
            queue = [root]
            while queue:
                traversal += str(queue[0].data) + ' '
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        print(traversal)

T = int(input())
myList = BST()
root = None
for i in range(T):
    data = int(input())
    root = myList.insert(root, data)
height = myList.getHeight(root)
print(height)
print(myList.inOrder(root))
print(myList.postOrder(root))
print(myList.preOrder(root))
print(myList.levelOrder(root))