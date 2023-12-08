#neetCode
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

#vsCode

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Manual Input for testing
        values = list(map(int, input("Enter the values of the linked list nodes separated by space: ").split()))
        k_input = int(input("Enter the value of k: "))

        # Creating linked list from manual input
        nodes = [ListNode(val) for val in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Example Usage
        linked_list_head = nodes[0] if nodes else None
        solution = Solution()
        result = solution.reverseKGroup(linked_list_head, k_input)

        # Printing the result
        while result:
            print(result.val, end=" ")
            result = result.next
        print()

# Example Usage
solution = Solution()
solution.reverseKGroup(None, 3)  # You can change the linked list and k for your own testing.
