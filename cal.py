print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2.0

print(2**3) #8
print(5%3) #2
print(10%3) #1
print(5//3) #1
print(10//3) #3

print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #True

print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True
print(1 != 3) #True
print(not(1 != 3)) #False

print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #True

print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
number = 2 + 3 * 4 #14
print(number) #14
number = number +2 #16
print(number)
number += 2
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)

number %= 5 #1
print(number)

print(abs(-5)) #5
print(pow(4,2)) #4^2 = 4*4 = 16
print(max(5,12)) #12
print(min(5,12)) #5
print(round(3.14)) #3
print(round(4.99)) #5

from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random()* 10) # 0.0~ 10.0 미만의 임의의 값 생성
print(int(random()*10) +1) # 0~10 이하 정수생성

print(randrange(1,46)) # 1~46 미만의 임의의 값 생성
print(randint(1,45)) # 1~45 이하의 임의의 값 생성

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")