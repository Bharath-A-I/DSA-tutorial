class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def removeduplicates(self,head):
        temp=head
        prev=None
        seen=set()
        while temp:
            if temp.data in seen:
                prev.next=temp.next
            else:
                seen.add(temp.data)
                prev=temp
            temp=temp.next
        return head

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("")
if __name__=="__main__":
    t=int(input())
    while t>0:
        ll=LinkedList()
        values=list(map(int,input().strip().split()))
        for i in reversed(values):
            ll.push(i)
        ll.head=Solution().removeduplicates(ll.head)
        ll.printlist()
        t-=1
        print("~")


