###
# 연쇄연산 : 하나의 seq에 대해 seq 내 원소들 사이에 2종의 operation이 있을 때 총 len(seq)-1의 2승 연산해야 하며, 그 때의 결과를 얻는 방법
#       *3 
#   *2  /3
# 1 /2  *3
#       /3
###

a = [1,2,3,4,5]

n = len(a)-1
start = [a[n-1]*a[n], a[n-1]/a[n]]

def op_iter(i,lst):
    temp = []
    for ele in lst:
        temp.append(round(i*ele,3))
        temp.append(round(i/ele,3))
    return temp

for t in range(n-1) : #n-1=3 이므로 t=0, 1, 2
    if t==0 :
        re = op_iter(a[n-2-t],start)
    else :
        re = op_iter(a[n-2-t],re)

print(re, len(re)) # len(re)=pow(2,len(a)-1)
