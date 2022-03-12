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
