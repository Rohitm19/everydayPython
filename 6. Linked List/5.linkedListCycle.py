#vsCode

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

def create_linked_list(nums):
    dummy = ListNode(None)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def create_cycle(head, pos):
    if pos == -1:
        return None
    
    cycle_start = head
    while pos > 0:
        cycle_start = cycle_start.next
        pos -= 1
    
    current = cycle_start
    while current.next:
        current = current.next
    current.next = cycle_start
    
    return head

def main():
    nums = input("Enter a list of numbers separated by spaces: ").split()
    nums = [int(num) for num in nums]
    head = create_linked_list(nums)
    
    pos = int(input("Enter the position of the cycle start (-1 for no cycle): "))
    head_with_cycle = create_cycle(head, pos)

    solution = Solution()
    has_cycle = solution.hasCycle(head_with_cycle)

    if has_cycle:
        print("The linked list has a cycle.")
    else:
        print("The linked list does not have a cycle.")

if __name__ == "__main__":
    main()
