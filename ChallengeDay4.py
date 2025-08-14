# if 조건문
age = 20
if age >= 18:
    print("성인입니다.")


# 연습문제 
#1. 점수가 70점 이상이면 "합격"을 출력하세요
my_score = 82
if my_score >= 70:
    print("합격")

#2. 나이가 13세 미만이면 어린이 요금을 출력하세요\
age = 11
if age < 13: 
    print("어린이 요금")

#3.문자열 s가 빈 문자열이면 비었음을 출력하세요
s = ""
if s == "":
    print("비었습니다")

#4. 리스트 Items가 비어있지 않으면, 리스트의 첫 요소를 출력하세요.
items = [1,2,3,4]
if items:
    print(items[0])

#5. 정수 n이 짝수면 짝수를 출력하세요.
n = 10
if n % 2 == 0 : 
    print("짝수입니다")

#6. 문자열 email에 @가 포함되어 있으면 형식 Ok를 출력하세요.
email = "good@pypy.com"
if "@" in email:
    print("형식 OK")

#7. 파일명 name이 .Png로 끝나면 이미지를 출력하세요
name = "picture.png"
if name.endswith(".png"):
    print("이미지")

#8. 문자열 word가 모두 대문자라면 "shout"을 출력하세요
word = "HELLO"
if word.isupper():
    print("shout")

#9. 사용자 입력 문자열 nickname이 비어있지 않으면 반가워요, {nickname}을 출력하세요
nickname = input("닉네임을 입력하세요")
if not nickname =="":
    print(f"반가워요, {nickname}")
    