from math import sqrt


class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNodeAtEnd(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail.next.prev = node
            self.tail = self.tail.next

    def addNodeAtFront(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev

    def displayFromStart(self):
        t = self.head
        while t:
            print(t.data,"->",end="")
            t=t.next
        print()

    def displayFromEnd(self):
        t = self.tail
        while t:
            print(t.data,"<-",end="")
            t=t.prev
        print()

    def linearSearch(self,val):
        h = self.head
        t = self.tail
        i = 0
        while t!=h:
            print("-->",h.data,t.data)
            # if h.data==val:
            #     print(h.data,"at",i,"from front")
            #     break
            # if t.data == val:
            #     print(t.data,"at",i,"from back")
            #     break
            # i+=1
            h=h.next
            if t==h:
                print("-->",h.data,t.data)
                break
            t=t.prev

    def evenOrOddLength(self):
        h = self.head
        t = self.tail
        i = 0
        while t!=h and t!=h.next :
            t=t.prev
            h=h.next
        if t==h:
            print("odd")
        else:
            print("even")

    def parlindromeOrNot(self):
        h = self.head
        t = self.tail
        flag=1
        while t!=h and t!=h.next:
            # print(h.data,t.data)
            if t.data!=h.data:
                flag=0
                break
            t=t.prev
            h=h.next
        # print(h.data,t.data)
        if flag and t.data==h.data:
            print("Yes")
        else:
            print("no")

    def rotateTheListByHalf(self):
        s1 = self.head
        s2 = self.head

        while s2 and s2.next:
            s1=s1.next
            s2=s2.next.next
        curr = s1
        start = self.head
        self.displayFromStart()
        # while curr:
        #     curr.data,start.data=start.data,curr.data
        #     curr=curr.next
        #     start=start.next

        self.tail.next = self.head
        self.head.prev = self.tail

        temp = s1.prev
        temp.next = None

        s1.prev = None
        self.head = s1

        #need to do
        s1.next = temp.prev


        self.displayFromStart()

    def swapTheAdjNodes(self):
        t1 = self.head
        t2 = self.head.next
        t3 = None

        while t2:
            t1.next=t2.next
            t2.next = t1
            t2.prev = t3
            t1.prev

    # def printPositionOfTheWrongBracket(self):
    #     h = self.head
    #     t = self.tail

    def DiffereneceOfEvenAndOddSum(self):
        h = self.head
        t = self.tail
        def recurr(e,o,t):
            if not t:
                return (e,o)
            if t.data%2==0:
                e+=t.data
            else:
                o+=t.data
            return recurr(e,o,t.next)

        # def recurrWithTailHead(e,o,h,t):
            print(h.data,t.data)
            #for odd
            # if t.next==h:
            #     if h.data%2==0:
            #         e+=h.data
            #     else:
            #         o+=h.data
            #     return e-o
            #for even
            if t==h :

                return e-o
            if h.data%2==0:
                e+=h.data
            else:
                o+=h.data

            if t.data%2==0:
                e+=t.data
            else:
                o+=t.data

            return recurrWithTailHead(e,o,h.next,t.prev)

        print(recurr(0,0,h))
        # print(recurrWithTailHead(0,0,h,t))

    def printPrimeFactors(self):
        def isPrime(e,i):
            if e==1:
                return False
            if e==2:
                return True
            if i==1:
                return True
            if e%i==0:
                return False
            return isPrime(e,i-1)

        def traverseTheList(t,l):
            if not t:
                return l
            if isPrime(t.data,int(sqrt(t.data))):
                l.append(t.data)
            return traverseTheList(t.next,l)

        print(traverseTheList(self.head,[]))



dl = DLL()
for i in [1,2,6,3,2,]:
    dl.addNodeAtFront(i)
# for i in range(5):
#     dl.addNodeAtEnd(i)


dl.displayFromEnd()
dl.displayFromStart()
# dl.linearSearch(6)
# dl.evenOrOddLength()
# dl.parlindromeOrNot()
# dl.rotateTheListByHalf()
# dl.printPositionOfTheWrongBracket()

# dl.DiffereneceOfEvenAndOddSum()
dl.printPrimeFactors()
