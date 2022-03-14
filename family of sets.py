#####
# power set
#####

from itertools import combinations

a = [1,2,3,4]
power = []
for e in a :
    set_e = []
    set_e.append(e)
    power.append(set(set_e)) # 원소 하나짜리의 경우 set으로 감싼 다음에 lst에 삽입
for i in range(2,len(a)+1) : # 원소 둘이상의 경우
    for c in list(combinations(a,i)) : # combination을 통해 tuple 반환 -> set으로
        power.append(set(c))
print(power)

#####
# 임의의 집합족에서 중복 원소를 지우는 함수
#####

def era(family):
    unique = []
    for i in range(len(family)-1) :
        n = 0
        for j in range(i+1, len(family)) :
            if family[i] == family[j] :
                n += 1
        if n == 0 :
            unique.append(family[i])
    unique.append(family[len(family)-1])
    return unique

###
# 예시
###
a = [{1,2,3}, set(), {2}, {2,3}, {2}, {1,2,3}] # set() : 공집합
print(era(a))
# [set(), {2, 3}, {2}, {1, 2, 3}]


#####
# family of sets 생성기 
# 정수를 원소로 하는 집합들을 원하는 만큼 원소로 넣어줄 수 있음
#####

print("한 set 입력의 끝:stop")
fam_set = []
a = 'N'
while True :
    set_temp = []
    if a == 'Y' :  
        break
    else :
        while True :
            b = input("element:")   # while문과 결합하여 무한 input
            if b == "stop" :        # stop 입력 시 while문이 깨지면서 set_temp 반환
                break
            else :
                set_temp.append(int(b))
        set_temp = set(set_temp)    # list인 set_temp를 set으로 변환
        fam_set.append(set_temp)    # fam_set에 하나의 set_temp를 원소로 추가
    a = input("want to end?(Y/N)")
print(fam_set)
# [{1,3,4}, {2,3}] 등의 집합족 반환
