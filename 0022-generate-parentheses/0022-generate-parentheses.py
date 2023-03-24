class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.generate('', n, n)
        return self.ans

    # if/elif/else 가 아니라 if로 연속해서 연결해 놓았으므로 가지치기로 모든 경우의 수가 나옴
    # generate('(',2,3) 이 들어가면 첫번째 if에서도 재귀호출, 두번째 if로 넘어가서도 재귀호출이 일어남
    def generate(self, prefix, left, right):
        # left 가 0이 아니면 
        if left:
            # 재귀 호출
            self.generate(prefix + '(', left-1, right)
        # left 보다 right가 크면 = '(' 가 있어야 ')'를 열수 있다. 
        if left < right:
            self.generate(prefix + ')', left, right-1)
        if right == 0:
            self.ans.append(prefix)