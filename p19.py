class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def make_list_by_array(nums):
    result = ListNode(nums[0])
    if len(nums) == 1:
        return result
    tmp = result
    for i in nums[1: ]:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return result

def print_list(head):
    while head is not None:
        print(f'{head.val} -> ', end='')
        head = head.next
    print('')

    
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        result = head
        first = head
        last = head
        for _ in range(n):
            last = last.next
            if last is None:
                return head.next
        last = last.next
        while last is not None:
            first = first.next
            last = last.next
        first.next = first.next.next
        
        return result

if __name__ == '__main__':
    solution = Solution()
    nums = [1,8,6,2,5,4,8,25,7]
    n = 2

    init_list = make_list_by_array(nums)
    print_list(init_list)

    dst_list = solution.removeNthFromEnd(init_list, n)
    print_list(dst_list)