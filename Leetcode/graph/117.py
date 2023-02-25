# 117. Populating Next Right Pointers in Each Node II
# Medium

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.

# Example
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node,
# just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        q = collections.deque()
        q.append(root)
        dummy = Node(0)

        while q:
            leng = len(q)
            prev = dummy

            for _ in range(leng):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    prev.next = cur.left
                    prev = prev.next

                if cur.right:
                    q.append(cur.right)
                    prev.next = cur.right
                    prev = prev.next

        return root