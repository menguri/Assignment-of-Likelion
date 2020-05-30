#문제 1: 형변환

a = '1'
b = '3'
print(a+b)
#13
print(int(a)+ int(b))
#형변환을 해주고 난 후에는 4로 알맞게 계산된다. 



#문제 2: 주민번호

c = 991214    #앞자리
d = 3391346   #뒷자리   

print(f'나이:{str(c)[0:2]}년생')
print(f'생일:{str(c)[2:4]}월{str(d)[4:6]}일')

if int(str(d)[0:1])%2 ==1:
    print('남자')
else: print('여자')


#문제 3: 구구단을 출력하라

user = int(input('몇단?(숫자만 입력하세요) \n'))

a = [1,2,3,4,5,6,7,8,9]
for i in a :
    print(f'{user}X{i}={user*i}')

for i in range(1,10):
    print(f'{user}X{i}={user*i}')

#문제 4: 100이하의 소수를 구하라 
T = []
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0 :
          i = False  
    if not i == False:
        T.append(i)

print(T)



#전역, 지역 변수 구분해주기
#아직 못풀었음!!!!!!!!!!!!


#문제 5: 합격/불합격

s = [45,67,89,34,99,100,34,23,67,56,34,89,7,90,45,98,93,45]

import statistics

for i in s:
    if i < statistics.mean(s):
        print(f'{i}번째 학생: 불합격')
    elif i > statistics.mean(s):
        print(f'{i}번쨰 학생: 합격')
    else:
        print(f'{i}번째 학생: 보류')



#문제 6: 튜플 자료에 추가하기 

a = (1,2,3,)
#튜플은 일단 만들어지면 고칠 수가 없습니다. 
b = list(a)
b.append(5)
a = tuple(b)
print(f'a=> {a}')


#문제 7: 딕셔너리 

dic = {"강민구":"010-3665-7182", "문대정":"010-2344-6786"}

u = input("찾고자 하는 사람을 입력하세요\n")

if u in dic :
    print(f'{u}의 전화번호는 {dic[u]}입니다.')
else:
    print(f'{u}님의 전화번호를 찾을 수 없습니다.')

