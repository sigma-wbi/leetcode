class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 삼각형 배열을 모두 1로 초기화 (양 끝은 항상 1이니까 편하게)
        # 2차원 배열
        res = [[1] * i for i in range(1, numRows + 1)]
        
        # 양 끝 1제외 안의 값에 제대로된 계산값 넣기
        for r in range(2, len(res)):
            for c in range(1, len(res[r]) - 1):
                # 2차원배열의 윗행 더하기
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]
                
        return res