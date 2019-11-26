class MyNode:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or not self.head:
            return -1
        while self.head and index:
            self.head = self.head.next
            index -= 1
        return self.head.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        head = MyNode(val)
        head.next = self.head
        self.head = head
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        tail = MyNode(val)
        p = self.head
        while p and p.next:
            p=p.next
        p.next = tail


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        insert_node = MyNode(val)
        p = self.head
        while index:
            p = p.next
            index-=1
        tmp = p.next
        p.next = insert_node
        insert_node.next = tmp
        self.head = p


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        p = self.head
        while index-1:
            p = p.next
            index -= 1
        q = p.next.next
        p.next = q
        self.head = p

if __name__ == "__main__":
    linked_list = MyLinkedList()
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)