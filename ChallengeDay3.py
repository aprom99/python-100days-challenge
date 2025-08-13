#연산자
a=(1+1) # +: 덧셈 연산자
print(a)

b=(2-1) # -:뺼셈 연산자
print(b)

c = (2*3)
print(c) # *: 곱셈 연산자

d= (6/3)
print(d) # /: 나눗셈 연산자

e= (9//2) # //: 몫 연산자
print(e)

f= (9%2) # %: 나머지 연산자
print(f)

g = (2**3) # **: 거듭제곱 연산자
print(g)

h= -(4) # -(): 부호 바꾸기 연산자
print(h)

# 비교 연산자
print(1==1) # == : 같다
print(1!=2) # !=: 다르다
print(1<2) # < : 작다
print(1<=2) # <=: 작거나 같다
print(2>1) # > : 크다
print(2>=1) # >= : 크거나 같다

# 논리 연산자
print(True and False) # and: 그리고(둘 다 참일 때 참)
print(True or False) # or: 또는 (둘 중 하나라도 참이면 참)
print(not True) # not: 부정 (참을 거짓으로, 거짓을 참으로)


# 연습 문제
# 1. 24개의 쿠키를 5개의 봉지에 담습니다. 가득 찬 봉지 수 와 남는 쿠키 수를 구하세요.
cookies = 24
bags = 5
full_bags = cookies // bags
print ("가득 찬 봉지 수:", str(full_bags))
remaining_cookies = cookies % bags
print ("남는 쿠키 수:",str(remaining_cookies))

#2. x=12일 떄, x가 10 이상 20 이하인지 비교식 한 줄로 쓰고 결과를 구하세요.
x = 12
range_check = (10<= x <= 20)
print("x가 10 이상 20 이하인가요?", range_check)

#3. height =129, age = 9 일 때, 탑승 조건: 130 이상 그리고 나이 8 이상" 일 때 탈 수 있나요?
height = 129 
age = 9
can_ride = (height >= 130) and age >= 8
print("탑승할 수 있나요?", can_ride)

#4. 15가 짝수인지 한 줄로 확인하세요.
number = 15
even_check = (number % 2 ==0)
print("15는 짝수인가요?", even_check)

#5. a=2, b=3, c=4 일 떄, a**b*c와 a**(b*c) 중 어떤 값이 더 큰가요?
a = 2
b = 3
c = 4
value_1= a**b*c
value_2= a**(b*c)
if value_1 > value_2:
    print("a**b*c가 더 큽니다")
elif value_1 < value_2:
    print("a**(b*c)가 더 큽니다")


#6. zoo 와 apple의 크기 비교를 해보세요.
zoo = "zoo"
apple = "apple"
print(zoo < apple) #문자열 비교는 사전식 순서로 비교 

#7. 쇼핑몰에서 개당 1990원인 물건을 37개 샀습니다. 총액과 10개 단위 백스 수와 남은 개수를 구하시오
item_price = 1990
item_count = 37
total_cost = item_price * item_count
full_boxes = item_count // 10
remaining_items = item_count % 10
print("총액은", total_cost,"원이고,","가득 찬 박스 수는", full_boxes, "개, 남은 개수는", remaining_items,"개 입니다.")

#8. 사용자 입력 name이 비어 있으면 "손님"을 쓰고, 비어 있지 않으면 원래 이름을 쓰는 코드를 작성하세요.
name = input("이름을 입력하세요: ")
if not name:
    name = "고객"
print("안녕하세요 " + name + "님!")
