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

### 별이 빛나는 밤이에요!

```python
print('*')
print('**')
print('***')
print('****')
print('*****')
```

### 섭씨를 화씨로 변환해봅시다!

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

