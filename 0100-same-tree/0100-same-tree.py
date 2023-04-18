# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p, q 가 비어있는 경우는 True
        if not p and not q :
            return True
        
        # p, q 둘중 하나가 비어있거나 루트노드가 다를경우 False
        if not p or not q or p.val != q.val:
            return False
        
        # 둘다 비어있지 않고, 루트 노드까지 같은경우는 재귀 호출을 통해 좌우 노드도 같은지 살핀다
        # 계속해서 같은 값이 나오다가 자식노드가 없어지는 시점은 첫번째 if에 걸리면서 True 반환
        # 왼쪽 오른쪽 노드 둘다 True가 나온 경우만 결과값까지 True 반환 (and로 연결하였으므로)
        if p.val == q.val :
            return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))