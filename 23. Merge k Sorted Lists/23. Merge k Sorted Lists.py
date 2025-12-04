#
# Problem: 23. Merge k Sorted Lists
# Difficulty: Hard
# Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
# Language: python3
# Date: 2025-12-04


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.mergeList(l1, l2))
            lists = temp

        return lists[0]

    def mergeList(self, l1, l2):
        ans = ListNode(0)
        res = ans

        while l1 and l2:
            if l1.val <= l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next

            ans = ans.next

        if l1:
            ans.next = l1
        else:
            ans.next = l2

        return res.next

