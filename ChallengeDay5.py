# if - else
age = 12
if age >= 13:
    print("청소년입니다")
else:
    print("어린이입니다")

# if - elif - else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("성적", grade)  

# 연습문제
# 1. 정수 하나를 입력 받아 짝수인지 홀수인지 출력하세요.
number = 6
if number % 2 == 0:
    print ("짝수입니다")
else:
    print ("홀수입니다")

#2. 나이와 티켓 보유 여부가 주어질 때, 나이가 18세 이상이거나 티켓이 있으면 허용 아니면 불가를 출력하세요
age = 17
has_ticket = True
if age >= 18 or has_ticket:
    print("허용")
else:
    print("불가")

#3. 온도를 입력 받아 다음을 반환하는 함수를 작성하세요
temperature = int(input("온도를 입력하세요"))
if temperature < 5:
    print("매우 추움")
elif 5<= temperature < 15:
    print("쌀쌀하다")
elif 15<= temperature < 25:
    print("쾌적하다")
else:
    print("덥다")       

 #4. 로그인 검사
login={"alice":"wonderland", "bob":"builder"}
username = input("사용자 이름을 입력하세요")
password = input("비밀번호를 입력하세요")
if username in login and login[username] == password:
    print("로그인 성공")
else:
    print("로그인 실패")

 #배송비 계산
baggage_weight = 3
if baggage_weight <= 1:
    print("배송비는 무료입니다")
elif baggage_weight <= 5:
    print("배송비는 3000원입니다")
else:
    print("배송비는 5000원입니다")       