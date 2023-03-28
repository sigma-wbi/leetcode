class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digit 의 구성요소들을(원본은 int형) 문자열로 바꾸기 위해 먼저 map으로 각각 문자열로 변환
        num_string_list = list(map(str, digits))
        # 각각의 문자 요소를 join으로 문자열 하나로 합침
        num_string = ''.join(num_string_list)
        # +1 연산을 위해 int 형으로 변환후 연산
        my_number = int(num_string) + 1
        # int 형을 다시 문자열로 바꾼뒤 리스트형으로 변환 (각각의 원소는 문자형) (int를 리스트로 바로 변환할수 없다. )
        answer_number_string = list(str(my_number))
        # 문자형인 각각의 원소를 int형으로 변환
        answer = list(map(int, answer_number_string))
        
        return answer 