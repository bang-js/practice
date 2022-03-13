
#################################
# 특정 수열의 원소들의 연속적 승수 합[이하 '승수합']에 대한 유일성 추론
#################################
import random
from itertools import combinations

# 횟수 입력
times = int(input("times:"))

max_len = 10
max_ele = 10 

# 주어진 sequence N이 수많은 sequence M의 승수합들에 대해 유일한지를 판별
def varify(seq, sum):
    for len_sub in range(1, max_len) :    
        if len_sub == 1 : # 그냥 1승만 체크하면 되므로
            for b in range(2,max_ele) :
                if b == sum and seq != [b] :
                    print("EXIST", b)
                
        else : # 길이가 2이상 
            num_ele = len_sub
            # max = (len(seq)*(max_ele/max_ele-1)*(max_ele**len(seq)-1))
            # lst = range(1, int(max**(1/num_ele)))
            lst = range(1, max_ele)
            # num_ele 만큼 lst에서 combination으로 원소 추출
            for tuple in list(combinations(lst,num_ele)): # list(combinations(lst,num_ele))의 결과물은 [(),(),...]
                sum_M = 0 
                tuple = list(tuple)
                for k in range(num_ele) :        # 개별 튜플에 대한 승수합 계산
                    sum_M += tuple[k]**(k+1)    
                if sum_M == sum and seq != tuple : # 개별 튜플에 대한 승수합을 sum과 비교
                    print("EXIST", tuple)
                        
            # combinations() # https://mildchae.tistory.com/5

# 랜덤하게 주어진 횟수만큼 실시
for i in range(times):

    # max_len=10개 이하의 원소(1~max_ele 사이의 값을 가짐)를 갖는 임의의 sequence N 생성
    seq_N = []
    len_lst = random.randint(1,max_len)  # lst 원소 수를 랜덤하게 결정
    for i in range(len_lst) :
        a = random.randint(1,max_ele)
        seq_N.append(a)
    
    # 중복 원소를 제거한 후 정렬
    seq_N = set(seq_N)
    seq_N = list(seq_N) # 중복 원소 제거 후 랜덤하게 섞인 상태
    seq_N = sorted(seq_N) # 순서대로 정렬
    print(seq_N)
    
    len_lst = len(seq_N)
    # 승수합 계산
    sum = 0
    for i in range(len_lst) :
        sum += seq_N[i]**(i+1)
    print(sum)

    # seq_N 
    varify(seq_N, sum)
