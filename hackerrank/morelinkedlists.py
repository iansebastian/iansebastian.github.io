class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def delete(self, head, key):
        current = head
        while current:
            if current == head and current.data == key:
                cut = current.next
                while cut:
                    if cut.data == key:
                        cut = cut.next
                    else:
                        break
                head = cut
            elif current.next and current.next.data == key:
                cut = current.next
                while cut:
                    if cut.data == key:
                        cut = cut.next
                    else:
                        break
                current.next = cut
            if current:
                current = current.next
        return head

    def removeDuplicates(self,head):
        current = head
        while current:
            current.next = self.delete(current.next, current.data)
            # self.display(current); print("Data erased :",current.data)
            if current:
                current = current.next
                # print("Done 1 iter")
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
print("Input end")
head = mylist.removeDuplicates(head)
head = mylist.delete(head, int(input("Member to erase: ")))
mylist.display(head)