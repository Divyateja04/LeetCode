class Solution(object):
    def modifiedList(self, nums, head):
        nums = set(nums)        
        
        while head.val in nums:                
            head = head.next

        ans = ListNode(head.val, head)        
 
        while head and head.next:              
            if head.next.val in nums:
                head.next = head.next.next

            else:                               
                head = head.next

        return ans.next  