# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 넣을 리스트 선언
        ans = []
        # root가 없으면 빈 리스트 반환
        if not root:
            return []
        # 왼쪽이 존재하면 왼쪽이 존재하지 않을때까지 쭉 내려감
        if root.left:
            ans += self.inorderTraversal(root.left)
        # 내려간 곳이 마지막이면 그 값을 리스트에 추가    
        ans.append(root.val)
        # 왼쪽을 다 기록한 뒤에야 오른쪽 if문에 들어감 
        # 오른쪽 트리 가지에 들어갔어도 바로 등록하는게 아니라 왼쪽이 있나부터 찾아야 함
        # 이런 이유로 left 조건 밑에만 append문이 있음
        if root.right:
            ans += self.inorderTraversal(root.right)
            
        return ans