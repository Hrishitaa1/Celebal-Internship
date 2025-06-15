class Node:
    """Class to represent a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage the linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added {data} as the head node.")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Added {data} to the end of the list.")

    def print_list(self):
        """Prints the elements in the list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Deletes the nth node from the list (1-based index)."""
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index should be 1 or greater.")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node {n} with value {deleted_data}.")
            return

        current = self.head
        count = 1

        while current and count < n - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            raise IndexError("Index out of range.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node {n} with value {deleted_data}.")


# ------------------ Testing the LinkedList ------------------

try:
    # Create linked list
    ll = LinkedList()

    # Add some nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.add_node(50)

    # Print the list
    ll.print_list()

    # Delete 3rd node
    ll.delete_nth_node(3)
    ll.print_list()

    # Delete 1st node
    ll.delete_nth_node(1)
    ll.print_list()

    # Try deleting an out-of-range node
    ll.delete_nth_node(10)

except Exception as e:
    print("Error:", e)
