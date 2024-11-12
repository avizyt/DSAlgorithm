from os import error

from anyio import current_effective_deadline
from httpx import delete


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        # if not self.head:
        #     self.head = new_node
        #     return
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("key not found in the list.")
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            curr = curr.next
        return None

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)

    current = ll.head
    ll.print_list()

    curr = ll.head
    while curr:
        if curr.data % 2 == 0:
            ll.delete(curr)
            curr = curr.next
    ll.print_list()
