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
