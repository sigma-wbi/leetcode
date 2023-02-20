class Solution:
    def intToRoman(self, num: int) -> str:
        # 큰 순서대로 딕셔너리 나열
        # 4, 9 등 특별한 값도 나열한다.
        romanDict={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
            
        roman=''
        # 주어진 숫자 num 이 0 이될때까지 반복
        while num!=0:
            for key in romanDict:               # 최대한 큰수를 먼저 뺄수 있으면 빼줌
                if num >= key:
                    roman += romanDict[key]     # 그리고 뺀만큼을 로마로 변환하여 문자열에 넣어줌
                    num=num-key
                    break
        
        return roman