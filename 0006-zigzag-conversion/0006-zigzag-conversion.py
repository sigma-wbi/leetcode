'''
내 풀이  O(n2) -> 느리다
class Solution:
    def convert(self, s:str ,numRows:int) -> str:
        if numRows == 1 or len(s) == 1 :
            return s

        sero = numRows
        garo = int(len(s))

        #답을 가지고있는 배열을 생성하는 함수 (Explanation 모양)
        def result_list(sero,garo):
            arr_2d = [
                [0 for col in range(garo)]
                for row in range(sero)
            ]
            list_s = list(s)

            for col in range(garo):
                if col ==0 or col % 2 == 0 :                #열 번호가 짝수이면
                    for row in range(sero):
                        if len(list_s) == 0:                #pop할 경우가 없으면 삽입이 끝난것
                            return arr_2d
                        arr_2d[row][col] = list_s.pop(0)    #정방향으로(위에서 아래로) 원소삽입

                else :                                      #열 번호가 홀수이면
                    for row in range(sero-1,-1,-1):         #역방향으로(아래에서 위로) 원소삽입
                        if row == sero-1 or row == 0:       #처음과 끝은 0으로
                            continue
                        else :
                            if len(list_s) == 0:
                                return arr_2d
                            arr_2d[row][col] = list_s.pop(0) 
            return arr_2d

        ans_list = result_list(sero,garo)                   #일단 정답 2차원 배열을 만들고
        ans = ""
        for row in range(sero):                             #2차원 배열을 순회하면서 0이 아닌 원소 즉 알파벳인 원소만 
            for col in range(garo):                         #ans 문자열에 이어 붙인다
                if ans_list[row][col] != 0:
                    ans += ans_list[row][col]

        return ans
'''
# 빠른 풀이 O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index_dict = dict()
        zigzag_index = 0
        down = 1  # Down flag
        up = -1  # Up flag
        move = 0
        for character in s:
            if zigzag_index == 0:  # Down
                move = down
            elif zigzag_index == numRows - 1:  # Up
                move = up

            index_dict[zigzag_index] = index_dict.get(zigzag_index, '') + character
            zigzag_index +=move  # Move index

        return ''.join(index_dict.values())