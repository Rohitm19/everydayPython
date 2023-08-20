#vsCode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next

def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def main():
    nums = input("Enter a list of numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]
    head = create_linked_list(nums)
    
    n = int(input("Enter the value of n: "))

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    print("Original Linked List:")
    print_linked_list(head)

    print("Linked List after removing the nth node from the end:")
    print_linked_list(new_head)

if __name__ == "__main__":
    main()
