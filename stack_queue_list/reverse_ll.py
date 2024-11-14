# Reversing a singly linked list


# [-]


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        """
        Reverses the singly linked list in place.

        Time complexity: O(N)
        Space complexity: O(1)

        example:
        Input: 1->2->3->4->5
        Output: 5->4->3->2->1
        """
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    ll.head.next = second
    second.next = third
    ll.print_list()
    ll.reverse()
    ll.print_list()
