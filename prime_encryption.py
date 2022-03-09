########################################
# 주어진 단어를 특정 숫자로 암호화
# n번째 알파벳 -> n번째 소수, 알파벳의 위치 i -> i승, k번 중복 시 t번째 중복 -> i에 대해 t승
# 한계 : 특수한 경우에서만 유일성 보장, 너무 큰 수가 되어 log를 취해줘야만 하는데 이 과정에서 오차가 발생하면 암호화가 무의미
########################################

chr = input("단어 입력(최대20자):")
chr = chr.upper()

# 암호코드
# ASCII code : A=65, Z=90 (ord <-> chr)
lst = []
for i in range(len(chr)) :
    lst.append(ord(chr[i])-64)
print(lst)

# n번째 소수찾기
def nth_Prime(n) :
    if n == 1 :
        return 2
    else : 
        prime_list = [2]
        a = prime_list[-1]
        while len(prime_list) < n :
            a += 1
            m = 0
            for i in range(2,int(a**(0.5)+1)+1) :  # ROOT로 근사, 3의 경우 int(3**0.5+1)=2 라서 range(2,3)을 위해 +1
                if a%i == 0 :
                    break
                else :
                    m += 1
            if m == int(a**(0.5)+1)-1 :  
                prime_list.append(a)
        return prime_list[-1]

# sum = p_n^i^m (p_n=n번째소수, i=자리수, m=이전 중복 개수+1) => sum이 곧 암호화된 결과
# 암호화
import math
mul = 0 
for i in range(len(lst)) :
    p = nth_Prime(lst[i])
    # 중복 개수 
    overlap = 0
    for ord in lst[:i] :
        if ord == lst[i] :
            overlap += 1
    m = overlap+1
    mul += math.log(p**((i+1)**m))  # 너무 큰 수이기에 log 취하고 전부 
    print(p,i+1,m,p**((i+1)**m))
print(mul)
