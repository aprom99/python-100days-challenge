#understanding variables
apples = 5
print("사과가" + str(apples) + "개 있습니다")

balance = 10000
balance = balance - 3000
print ("잔액:" + str(balance) + "원")

#understanding types
my_age = 25
print("제 나이는" + str(my_age) + "살입니다")

num_str = "100"
print(int(num_str) +50)

items = ["사과", "바나나"]
items.append("귤")
items[1] = "포도"
print(items)

t = {1,2,3}
list_t = list(t)
print (list_t)

person = {"name":"영희","age":"12"}
person["age"] = "13" #dict[key]= value로 새 값 추가/수정
person["grade"] = "6"
print(person)

a = [1,2,3]
b = a
b.append(4)
print(a) # [1,2,3,4] a도 바뀜
#독립 복사
a = [1,2,3]
c = a.copy() # a[:] or list(a)
c.append(5)
print(a) # [1,2,3]
print(c) # [1,2,3,5]

print(0.1 + 0.2) #정확한 0.3이 나오지 않음
print(round(0.1+0.2,2)) 