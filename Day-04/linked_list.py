class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def addNodeBack(self,val):
        node = Node(val)
        if self.head == None:
            self.head=node
        else:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = node

    def addNodeFront(self,val):
        node = Node(val)
        if self.head == None:
            self.head=node
        else:
            # temp=self.head
            # node.next=temp
            # self.head=node
            node.next=self.head
            self.head=node

    def removeFromBack(self):
        if self.head == None:
            print("No data to delete")
        else:
            temp=self.head
            prev=None
            while temp.next:
                prev=temp
                temp.next=temp.next
            prev.next=None

    def display(self):
        temp = self.head
        if temp:
            while temp:
                print(temp.data,"->",end="")
                temp=temp.next
            print()
        else:
            print("No Nodes")

    def search(self,val):
        if self.head==None:
            print("Not found")
        else:
            temp=self.head
            i=1
            while temp:
                if temp.data==val:
                    flag=1
                    print("Found at",i,"th node",end="")
                    print()
                    break
                temp=temp.next
                i+=1
            if not temp:
                print("Not Found")

    def findMiddleNode(self):
        i = 1
        t = self.head
        p = self.head
        while t and t.next:
            i+=1
            t=t.next.next
            p=p.next

        print(p.data,i)

    def evenOrOdd(self):
        # i = 1
        f = self.head
        s = self.head
        # while t and t.next:
        #     i+=1
        #     t=t.next.next
        #     p=p.next

        # if i%2:
        #     print("odd")
        # else:
        #     print("even")
        while f and f.next:
            f=f.next.next
            s=s.next

        if f:
            print("odd")
        else:
            print("even")

    def lenghtOfLongestSubSequence(self):
        i=1
        t = self.head
        mx=1
        prev=0
        while t.next:
            if t.data==t.next.data-1:
                i+=1
            else:
                mx = max(mx,i)
                prev=i
                i=1
            t=t.next
        print(max(prev,mx))

    def printAllPairs(self):
        t1=self.head
        l=[]
        while t1:
            t2=t1.next
            while t2:
                l.append((t1.data,t2.data))
                t2=t2.next
            t1=t1.next
        print(l)

    def bubbleSort(self):
        t=self.head
        prev=None
        flag=1
        while t.next:
            t1=self.head
            while t1.next!=prev:
                if t1.data>t1.next.data:
                    flag=0
                    t1.data, t1.next.data = t1.next.data,t1.data
                t1=t1.next
            if flag:
                break
            t=t.next
            prev=t1

        self.display()

    def swapTheNodesAdj(self):
        t1 = self.head
        t2 = self.head.next
        self.display()
        self.head = t2
        while t1 and t1.next:
            print("before",t1.data,t2.data)

            t1.next = t2.next
            t2.next = t1


            print("after",t1.data,t2.data)

            t1=t1.next
            t2=t1.next




        self.display()





n = int(input())
lc = LinkedList()
m = list(map(int,input().split()))

for i in m:
    lc.addNodeBack(i)
# while n>=1:
#     lc.addNodeBack(n)
#     n-=1

# n = 5
# while n>=0:
#     lc.addNodeFront(n)
#     n-=1

lc.display()

# f = int(input("Enter a number: "))
# lc.search(f)

# lc.findMiddleNode()
# lc.evenOrOdd()

# lc.lenghtOfLongestSubSequence()
# lc.printAllPairs()
# lc.bubbleSort()
lc.swapTheNodesAdj()
