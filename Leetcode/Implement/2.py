#2. Add Two Numbers
# Medium

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#Example
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        result = head = ListNode(0)

        while l1 or l2 or carry:
            addup = 0
            if l1:
                addup += l1.val
                l1 = l1.next
            if l2:
                addup += l2.val
                l2 = l2.next

            carry, tmp = divmod(addup + carry, 10)
            head.next = ListNode(tmp)
            head = head.next

        return result.next