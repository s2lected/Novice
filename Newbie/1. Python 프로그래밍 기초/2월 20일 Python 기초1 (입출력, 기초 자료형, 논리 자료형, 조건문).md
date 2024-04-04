## 01-1 파이썬 알아보기
### [수업자료] 파이썬 알아보기
Python : 데이터 분석 및 인공지능 구축에 최적화

공부의 방향 : 코드를 작성하는 것보다 코드를 이해하는 능력이 더 중요한 시대

이해하는 방법 : 위에서부터 아래로, 안에서부터 밖으로 해석

,(콤마)로 print를 찍게 되면 반드시 공백이 발생

Jupyter Notebook : cell 단위로 나누어 코드를 작성하는 개발환경, 데이터 분석이나 교육에 활용하기 좋음

리스트는 대괄호([])로 정의, 리스트는 원소의 순서 존재, 중복 원소 허용

대입연산자는 서열이 가장 마지막!, 변수는 항상 수식의 왼쪽에 존재해야함

---
## 01-2 파이썬 알아보기 실습
### 어서와~ 엘리스는 처음이지?

```python
print('Welcome to Elice~')
```

---
## 02-1 기초 자료형과 연산
### [수업자료] 기초 자료형과 연산
<숫자형 자료의 연산>

곱하기 : *

나누기 : / (실수형 나눗셈)

몫 : //

나머지 : %

제곱 : **

<문자형 자료의 연산>

더하기 : + (이어붙이는 형태) 반드시 같은 자료형끼리!

곱하기 : * (반복하는 형태)

<문자열 접근하기>

인덱스 : 각 원소에 순서를 기준으로 0번부터 매겨지는 번호

인덱싱 : 인덱스를 이용해서 원소 하나 가져오기, [] 사용

슬라이싱 : 일부분 가져오기, [시작:종료], 이상-미만의 법칙, 자료형 유형 유지

---
## 02-2 파이썬 기초 실습
### 변수 다루기

```python
num = 1030
string = 'hello, '
num = num + 204
string = string + 'elice!'
print(num)
print(string)
```

### 음식 가격 계산하기

```python
korean = 7000
chinese = 6000
western = 8500
discount_korean = korean*0.9
total_price = discount_korean*55 + chinese*43 + western*52

print("한식 : " + str(korean))
print("중식 : " + str(chinese))
print("양식 : " + str(western))
print("할인된 한식 : " + str(discount_korean))
print("전체 예산 : " + str(total_price))
```

### 몫과 나머지 구하기

```python
num1 = 23781367
num2 = 1754

print(num1//num2)
print(num1%num2)
```

### [미션] 계단 별자리

```python
print('*')
print('**')
print('***')
print('****')
print('*****')
```

### [미션] 섭씨와 화씨

```python
c = 18
f = c * (9/5) + 32
today_temp = [c, f]

print(today_temp)
```

---
## 03-1 논리 자료형
### [수업자료] 논리 자료형
input()의 중요한 특징 : 무엇을 입력하든 '문자열'로 입력 받아짐!

float → int 형 변환시 int는 기본적으로 소수점 이하 버림

비교 연산자 : 등호 앞에 느낌표나 부등호를 붙임

and : 모두 True인가?

or : True가 있는가?

not : 논리값 뒤집기

---
## 03-2 논리 자료형 실습
### 센티미터와 인치

```python
n = int(input())
print(n * 2.54)
```

### 정사각형의 넓이 출력하기

```python
n = int(input())
print(n * n)
```

---
## 04-1 조건문 알아보기 (논리 자료형 심화)
### [수업자료] 조건문 알아보기 (논리 자료형 심화)
if : 조건이 True이면 명령 실행 (조건문에서 필수, else & elif는 필요에 따라), 들여쓰기는 tab으로

elif : 아닌 경우에 ~라면

else : 아니면 명령 실행

if-elif-else 구문은 하나의 블럭으로 작동 (필요에 따라 써야함)

---
## 04-2 조건문 알아보기 실습
### if-else문 개념

```python
x = int(input())
y = int(input())

if x >= y:
  print('x가 y보다 크거나 같습니다.')
else:
  print('x가 y보다 작습니다.')
```

### if-elif-else문 개념

```python
x = int(input())
y = int(input())

if x > y:
  print('x가 y보다 큽니다.')
elif x < y:
  print('x가 y보다 작습니다.')
else:
  print('x와 y가 같습니다.')
```

### 자리수 판별기

```python
num = int(input())

if num >= 1 and num <= 9:
  print('한 자리 숫자입니다.')
elif num >= 10 and num <= 99:
  print('두 자리 숫자입니다.')
else:
  print('세 자리 숫자입니다.')
```

### 놀이공원 입장료 계산하기

```python
age = int(input())

if age >= 1 and age <= 7:
  print('고객님, 입장료는 0원입니다.')
elif age >= 8 and age <= 13:
  print('고객님, 입장료는 5000원입니다.')
elif age >= 14 and age <= 19:
  print('고객님, 입장료는 10000원입니다.')
else:
  print('고객님, 입장료는 20000원입니다.')
```

### 집에 가는길

```python
money = int(input())

if money >= 1000:
  print('택시')
elif money < 1000 and money >= 500:
  print('버스')
elif money < 500 and money >= 300:
  print('지하철')
else:
  print('도보')
```

---
