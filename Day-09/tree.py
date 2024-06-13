from collections import defaultdict


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def createNode(self, root, val):
        if root is None:
            return Node(val)
        elif val > root.data:
            root.right = self.createNode(root.right, val)
        else:
            root.left = self.createNode(root.left, val)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if  root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def sumOfNodes(self,root,s):
        if root:
            s+=root.data
            l = self.sumOfNodes(root.left,s)
            r = self.sumOfNodes(root.right,l)
            return r
        return s

    def addLikeFibnacc(self,root):
        if root==None:
            return 0
        return root.data+self.addLikeFibnacc(root.left)+self.addLikeFibnacc(root.right)

    def addEvenDatas(self,root):
        if not root:
            return 0

        if root.data%2:
            return self.addEvenDatas(root.left)+self.addEvenDatas(root.right)
        else:
            return self.addEvenDatas(root.left)+root.data+self.addEvenDatas(root.right)

    def addOddDatas(self,root):
        if not root:
            return 0

        if not root.data%2:
            return self.addOddDatas(root.left)+self.addOddDatas(root.right)
        else:
            return self.addOddDatas(root.left)+root.data+self.addOddDatas(root.right)

    def differenceOfEvenAndOddSum(self, root):

        if not root:
            return 0

        if not root.data%2:
            return -root.data+self.addOddDatas(root.left)+self.addOddDatas(root.right)

        return self.addOddDatas(root.left)+self.addOddDatas(root.right)+root.data

    def heightOfTree(self, root):
        if not root:
            return -1
        return max(self.heightOfTree(root.left),self.heightOfTree(root.right))+1

    def isTreeBalanced(self,root):
        return abs(self.heightOfTree(root.left)-self.heightOfTree(root.right)) <= 1

    def numberOfLeafNodes(self,node):
        c=0
        def dfs(root):
            nonlocal c
            if root==None:
                return
            if root.left == None and root.right==None:
                c+=1
                return
            dfs(root.right)
            dfs(root.left)
        dfs(node)
        return c

    def numberOfLeafNodes(self,node):
        s=0
        def dfs(root):
            nonlocal s
            if root==None:
                return
            if root.left == None and root.right==None:
                s+=root.data
                return
            dfs(root.right)
            dfs(root.left)
        dfs(node)
        return s

    # def searchANodeInTree(self,root,val):
    #     if not root:
    #         return False
    #     if root.data==val:
    #         return True

    #     return self.searchANodeInTree(root.left,val) or self.searchANodeInTree(root.right,val)

    def searchANodeInTree(self,root,val):
        if not root:
            return False
        if root.data==val:
            return True
        if root.data>val:
            return self.searchANodeInTree(root.left,val)
        else:
            return self.searchANodeInTree(root.right,val)

    def depthOfTree(self,root,val,c=0):
        if not root:
            return -1
        if root.data==val:
            return c
        if root.data>val:
            return self.depthOfTree(root.left,val,c+1)
        else:
            return self.depthOfTree(root.right,val,c+1)

    def left_view(self,node):
        l = []
        def view(root,level):
            if not root:
                return
            if level not in l:
                l.append(level)
                print(root.data,level)

            view(root.left,level+1)
            view(root.right,level+1)
        view(node,0)
        print(l)

    def right_view(self,node):
        l = []
        def view(root,level):
            if not root:
                return
            if level not in l:
                l.append(level)
                print(root.data,level)

            view(root.right,level+1)
            view(root.left,level+1)
        view(node,0)
        print(l)

    def top_view(self,node):
        d = defaultdict(int)
        def view(root,level):
            if not root:
                return
            if level not in d:
                d[level]=root.data
            if level<0 and level in d and d[level] < root.data:
                d[level]=root.data

            view(root.left,level+1)
            view(root.right,level-1)
        view(node,0)
        print(d)

    def bfs(self,node):
        d = defaultdict(list)
        q = [(node,0)]

        while q:
            node,h = q.pop()

            d[h].append(node.data)
            if node.right:
                q.append((node.right,h+1))
            if node.left:
                q.append((node.left,h+1))
        print(d,q)

    def top_view_bfs(self,node):
        d = defaultdict(list)
        q = [(node,0)]

        while q:
            node,h = q.pop()
            d[h].append(node.data)
            if node.right:
                q.append((node.right,h+1))
            if node.left:
                q.append((node.left,h+1))
        print(d,q)
        l = []
        for i in d:
            l.append(d[i][0])
        print(l)

    def bottom_view_bfs(self,node):
        d = defaultdict(list)
        q = [(node,0)]

        while q:
            node,h = q.pop()
            d[h].append(node.data)
            if node.right:
                q.append((node.right,h+1))
            if node.left:
                q.append((node.left,h+1))
        print(d,q)
        l = []
        for i in d:
            l.append(d[i][-1])
        print(l)




l = list(map(int,input().split()))
tree = Tree()
tree.root = Node(10)
for i in l:
    tree.createNode(tree.root,i)

# tree.inorder(tree.root)
# print()
# tree.preorder(tree.root)
# print()
# tree.postorder(tree.root)
# print()
# print(tree.sumOfNodes(tree.root,0))
# print(tree.addLikeFibnacc(tree.root))
# print(tree.addEvenDatas(tree.root))
# print(tree.differenceOfEvenAndOddSum(tree.root))
# print(tree.heightOfTree(tree.root))
# print(tree.numberOfLeafNodes(tree.root))
# print(tree.searchANodeInTree(tree.root,0))
# print(tree.depthOfTree(tree.root,3))
# print()
# # tree.left_view(tree.root)
# tree.right_view(tree.root)

# tree.top_view(tree.root)

tree.bfs(tree.root)
tree.top_view_bfs(tree.root)
tree.bottom_view_bfs(tree.root)
