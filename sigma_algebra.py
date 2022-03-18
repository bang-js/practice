
#####
# sigma-algebra
# 전체집합(Smp)과 특정 집합족(a)이 주어짐
# 특정 집합족 내 집합의 여집합, 집합들의 합집합에 대해 닫혀있어야 함
#####

Smp = {1,2,3,4,5}
a = [{1},{1,2},{3}]
sigma_algebra = []
a_comp = []

# sigma-algebra에 전체집합과 공집합 포함
sigma_algebra.append(set()) #set()는 공집합
sigma_algebra.append(Smp)

# sigma-algebra에 a의 원소(as 집합) 포함
for i in range(len(a)) :
    sigma_algebra.append(a[i])

# a_comp에 a의 원소의 여집합 포함
for i in range(len(a)) :
    a_comp.append(Smp - a[i])
    if not(Smp - a[i] in sigma_algebra)  :  # 중복 시 포함안함
        sigma_algebra.append(Smp - a[i])

print("a: ",a)
print("a_comp:",a_comp)
empty =[]
for i in range(len(a)):
    empty.append(set())
print("empty:",empty)

###
# a의 원소 수가 n개라면 node는 3xn개이며(3은 집합 e, e의 여집합, n/a) node들을 연결하는 link는 (3^n)(2^n-1) - nx2x2 - 2 개
# node와 node 사이에는 union/intersection 두 가지 경우가 있고, n-1개의 node가 n/a를 연결하는 경우는 무의미하므로 제외(-nx(3-1)x2(합/교)), 
# 모든 node가 n/a로 연결되는 경우에도 무의미하므로 제외(U/I 2가지이므로 -2)
# link = pow(3,n)*pow(2,n-1)-n*2*2-2
###

##
# a의 원소가 2개인 제한적 케이스
##
# zip 적용 후 list 형태로 변환

# zipped = list(zip(a,a_comp,empty))  # [(),(),...]
# zipped_lst = [] 
# for i in zipped :                   # [[],[],...]
#     zipped_lst.append(list(i))
# print("zipped_lst", zipped_lst)
# for z0 in zipped_lst[0] :
#     for z1 in zipped_lst[1] :
#         # print(z0,z1)
#         # print(type(z0),type(z1))
#         if not(set.union(z0,z1) in sigma_algebra)  :  # 중복 시 포함안함
#             sigma_algebra.append(set.union(z0,z1))
#         if not(set.intersection(z0,z1) in sigma_algebra)  :
#             sigma_algebra.append(set.intersection(z0,z1))
# print("sigma_algebra:",sigma_algebra)
# print("length:",len(sigma_algebra))


###
# 이제 연쇄연산을 이용하여 n개의 zipped에 대해 각 zipped에서 하나씩 추출해서 and와 or 연산을 해준 결과를 출력해주면 됨
# 재귀함수 사용
###

# 임의의 집합족에서 중복 원소를 지우는 함수
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

# 재귀함수를 사용하여 A1~An에 대해 연쇄연산
# 그림으로 표현하면 
# A1----U/I-----A2----U/I--...--An      
# A1^c          A2^c            An^c
# null          null            null

# 먼저 An-1(+An-1^c,null)과 An(+An^c,null)에 대해 연쇄연산(합,교)(3x3=9번) 
# -> 그 결과를 중복제거한 뒤 temp에 저장, temp는 일종의 n-1과 n의 결합체
# -> temp와 An-2에 대해 연쇄연산 ((9-k)x3번 연산, k는 중복된 원소 개수) 
# -> 이를 재귀적으로 반복
def FN(n):
    while n >= 1 :
        print("n-1, n번 elements of zipped_lst : ",zipped_lst[n-1], zipped_lst[n])
        temp =[]
        for z0 in zipped_lst[n-1] :
            for z1 in zipped_lst[n] :
                if not(set.union(z0,z1) in sigma_algebra)  :  # 중복 시 포함안함
                    sigma_algebra.append(set.union(z0,z1))
                temp.append(set.union(z0,z1))                  # 합집합 연산한 결과를 temp에 저장
                if not(set.intersection(z0,z1) in sigma_algebra)  :
                    sigma_algebra.append(set.intersection(z0,z1))
                temp.append(set.intersection(z0,z1))
        del zipped_lst[n]
        del zipped_lst[n-1]
        temp = era(temp)        # temp 내 중복되는 원소 제거 (계산 효율성)
        zipped_lst.append(temp)
        # print("temp:",temp, "\n","zipped_lst:",zipped_lst)
        return FN(n-1)

FN(len(zipped_lst)-1)
print("sigma_algebra:",sigma_algebra)
print("length:",len(sigma_algebra))
