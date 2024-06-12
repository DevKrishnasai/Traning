from collections import defaultdict
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def insert_node(node, data):
            if node is None:
                return Node(data)
            elif node.data > data:
                node.left = insert_node(node.left, data)
            else:
                node.right = insert_node(node.right, data)
            return node

        self.root = insert_node(self.root, data)

    def in_order(self):
        print("IN ORDER ")
        def traverse(root):
            if root :
                traverse(root.left)
                print(root.data,end=" ")
                traverse(root.right)

        traverse(self.root)
        print()
    def pre_order(self):
        print("PRE ORDER ")
        def traverse(root):
            if root:
                print(root.data,end=" ")
                traverse(root.left)
                traverse(root.right)

        traverse(self.root)
        print()

    def post_order(self):
        print("POST ORDER ")
        def traverse(root):
            if root:
                traverse(root.left)
                traverse(root.right)
                print(root.data,end=" ")
        traverse(self.root)
        print()

    def even_odd_diff(self):
        even = odd = 0
        def even_odd(node):
            nonlocal even
            nonlocal odd

            if not node:
                return
            elif node.data %2 :
                odd += node.data
                even_odd(node.left)
                even_odd(node.right)

            else:
                even += node.data
                even_odd(node.left)
                even_odd(node.right)

        even_odd(self.root)
        print("even=" ,even)
        print("odd=",odd)
        print("diff=" , abs(even - odd))

    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node):
        if not node:
            return True
        left_height = self.height(node.left)
        right_height =self.height(node.right)
        return abs(left_height -right_height)<=1
    def sum_of_nodes(self):
        sum = 0
        def traverse(root):
            nonlocal sum
            if root:
                sum += root.data
                traverse(root.left)
                traverse(root.right)
            return sum
        sum = traverse(self.root)
        print(sum)

    def level_order(self):
        if self.root:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                print(node.data,end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    def leaves(self):
        leaf = 0
        def is_leaf(node):
            nonlocal leaf
            if node:
                if not node.left and not node.right:
                    print(node.data,end=" ")
                    leaf+=1

                is_leaf(node.left)
                is_leaf(node.right)
        is_leaf(self.root)
        print()
        print(leaf)
    def leaves_sum(self):
        leaf = 0
        def is_leaf(node):
            nonlocal leaf
            if node:
                if not node.left and not node.right:
                    print(node.data,end=" ")
                    leaf+=node.data

                is_leaf(node.left)
                is_leaf(node.right)
        is_leaf(self.root)
        print()
        print(leaf)
    def search(self,data):
        def binsrch(node,data):
            if node:
                if node.data==data:
                    return True
                if node.data > data:
                    return binsrch(node.left,data)
                else:
                    return binsrch(node.right,data)
        if(binsrch(self.root,data)):
            print(data,"found")
        else:
            print(data,"not found")

    def depth(self):
        depth_map = defaultdict(list)

        queue = [(self.root,0)]
        while queue:
            node,d = queue.pop(0)
            depth_map[d].append(node)
            if node.left:
                queue.append((node.left,d+1))
            if node.right:
                queue.append((node.right,d+1))
        # for i in depth_map:
        #     for node in depth_map[i]:
        #         if node.data == data:
        #             return i
        # return -1
        return depth_map
        # left_view =[]
        # right_view=[]
        # for d in depth_map:
        #     left_view.append(depth_map[d][0])
        #     right_view.append(depth_map[d][-1])

    def top_view(self):
        def traverse_left(node):
            if not node:
                return
            traverse_left(node.left)
            print(node.data,end=" ")
        def traverse_right(node):
            if node:
                traverse_right(node.right)
                print(node.data,end="")
        traverse_left(self.root)
        traverse_right(self.root.right)

    def down_view(self):
        vertical_level=defaultdict(list)
        def down_level(node,d):
            if node:
                down_level(node.left,d-1)
                vertical_level[d].append(node)
                down_level(node.right,d+1)
        down_level(self.root,0)
        for level in vertical_level:
            print(level,vertical_level[level][0].data)


    def left_view(self):
        level_wise = self.depth()
        # print(level_wise)
        for level in level_wise:
            print(level_wise[level][0].data,end=" ")
        print()

    def right_view(self):
        print()
        level_wise = self.depth()
        # print(level_wise)
        for level in level_wise:
            print(level_wise[level][-1].data,end=" ")

bst = BST()
nums = [10,15,5,7,2,1,3]
for i in nums:
    bst.insert(i)
# bst.in_order()
# # bst.pre_order()
# # bst.post_order()
# bst.even_odd_diff()
# bst.sum_of_nodes()
# bst.level_order()
# root_height = bst.height(bst.root)
# print(root_height)
# is_bal =bst.is_balanced(bst.root)
# print(is_bal)
# bst.leaves()
# bst.leaves_sum()
# bst.search(int(input()))
# data =int(input())
# print(f"DEPTH of {data} = ",bst.depth(data))
# print("TOP VIEW \n")
# bst.top_view()
# print("\nDOWN VIEW")
bst.down_view()
# print("\nLEFT VIEW ")
# bst.left_view()
# print("RIGHT VIEW")
# bst.right_view()
