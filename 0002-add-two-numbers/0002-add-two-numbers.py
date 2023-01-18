# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
내 풀이 연결리스트를 쓰지 않아서 오류가 나는듯
class Solution:
    def addTwoNumbers(self, l1, l2) :
        l1str = "".join(str(elem) for elem in l1)   #리스트를 문자열로 변환 
        l2str = "".join(str(elem) for elem in l2)
        
        l1int , l2int = int(l1str), int(l2str)      #문자열을 정수로 변환 (+ 연산이 가능하도록)
        resultint = l1int + l2int
        
        resultStr = str(resultint)                  #리스트로 바꾸기 위해 일단 문자열로 전환
        resultList = list(resultStr)                #이후 문자열을 리스트로 전환
        
        resultList.reverse()       #리스트 뒤집기
        
        return resultList
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next