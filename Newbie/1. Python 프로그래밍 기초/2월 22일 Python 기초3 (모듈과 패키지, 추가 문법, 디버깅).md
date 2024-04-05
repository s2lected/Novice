## 01-1 함수와 메서드
### [수업 자료] 함수와 메서드
프로그래밍의 기본 틀 : 정보 입력 → 작업 → 결과 출력

함수 : 특정 기능을 수행하는 키워드

1. 내장함수
2. 사용자 지정 함수

```python
def 함수이름(매개변수):
  명령1
  명령2
  return 반환값
```

**프로그래머의 역할과 사용자의 역할?**

return vs print : return은 함수의 결과값을 변수에 할당 가능

global variable vs local variable : 함수 내에서만 할당한 변수는 전체 코드에 영향을 주지 않음

메서드 : 특정 자료와 연관 지어 가능 (특화함수)

---
## 01-2 함수와 메서드 실습
### 시퀀스의 합과 길이 구하기

```python
my_list = [1,2,3,4,5]

print(sum(my_list))
print(len(my_list))
print(sum(my_list)/len(my_list))
```

### 나만의 별 찍기 함수

```python
def my_star(x):
  print('*' * x)

star = int(input())
my_star(star)
```

### 코딩 대회

```python
score = [55, 58, 60, 45, 100, 95, 70, 88]
score.append(90)
score.pop(5)

print(score)

print('대상 수상자의 점수는',max(score),'점!')
```

---
## 01-3 모듈과 패키지
### [수업 자료] 모듈과 패키지
0. 함수 : 특정 기능을 수행하는 코드 몇 줄
1. 모듈 : 함수나 자료가 모여있는 파이썬 파일 (특정 목적을 구현하기 위한 복잡한 코드를 묶어둠)
2. 패키지 : 모듈이 모여있는 폴더 (= 라이브러리)

<모듈 사용법>

import 모듈

모듈.함수()

from 모듈 import 함수 : 이렇게 사용하면 함수 이름만 써도 사용 가능

<패키지 사용법>

import 패키지

패키지.모듈.함수()

from 패키지 import 모듈 : 모듈.함수()로 간단하게 사용 가능

form 패키지.모듈 import 함수 : 함수() 단독으로 사용 가능

설치 방법 : !pip install 패키지

<대표적인 패키지>

pandas, numpy, seaborn, matplotlib, scikitlearn, pytorch

<함수를 어떻게 만들었는지 보는 방법>

github에서 검색해서 확인

---
## 01-4 모듈과 패키지 실습
### 지구의 부피

```python
import math

volume = (4/3) * math.pi * pow(6371,3)

print(volume)
```

### 소수 판별기

```python
import prime

num = int(input())

print(prime.prime_number(num))
```

---
## [자율심화]02 파이썬 심화 문법
### [수업자료] 실무에서 자주 사용하는 추가적인 문법 패턴
01 f-string 포맷팅

* f-string 포맷팅이란?

  Python 3.6 이상부터 기존의 print보다 더 상세하게 출력할 수 있는 방법

  Print와 함께 f 그리고 중괄호{}를 이용하여 표현 : f를 먼저 선언, 문자열(" ") 안에 중괄호{}와 변수명 작성

```python
hour = 9
minute = 15
word1 = "오전"

print("현재 시간은", word1, hour, "시", minute, "분 입니다") #기존 방법
print(f"현재 시간은 {word1} {hour}시 {minute}분 입니다") #f-string 포맷팅
```

02 List Comprehension

* List Comprehension 이란?

  Python에서 리스트를 선언하는 방법

  기존의 리스트를 생성할 때, 조건문과 반복문을 사용한 여러 줄로 된 코드를 한 줄로 줄일 수 있음

  리스트를 생성하는 대괄호 안에 조건문과 반복문을 사용하여 리스트를 생성할 수 있음

```python
num_list = [num for num in range(100) if num % 2 == 0] #0부터 99까지의 숫자 중에서 짝수만 저장된 리스트를 생성
```

* List Comprehension의 동작 순서

  Case 1. 반복문만 이용한 사례

  new_list = [<표현식> for <변수> in <시퀀스>]

  new_list = [num * 10 for num in range(10)]

```python
num_list = [num for num in range(100)] #0부터 99까지 숫자를 저장한 리스트 생성 방법
```

  Case 2. 반복문과 조건문(if)을 이용한 사례

  new_list = [<표현식> for <변수> in <시퀀스> if <조건>]

  new_list = [str(num) for num in range(10) if num % 2 == 0]

```python
region_list = ["수원시(경기도)", "군산시(전라북도)", "포항시(경상북도)", "경주시(경상북도)", "익산시(전라북도)", "강릉시(강원도)", "동해시(강원도)", "고양시(경기도)"]

gyeonggi_list = [region for region in region_list if "경기도" in region] #무작위 시(도) 리스트 중에서 경기도만 추출하여 저장하는 방법
```

  Case 3. 반복문과 조건문(if-else)을 이용한 사례

  if와 함께 else가 있어야 함

  Case 2와 순서가 다름

  new_list = [<표현식> if <조건> else <표현식2> for <변수> in <시퀀스>]

  new_list = ["짝수" if num % 2 == 0 else "홀수" for num in range(10)]

```python
original_prices = [800, 1200, 950, 1100, 750, 1300]
discounted_prices = [int(price * 0.9) if price >= 1000 else price for price in original_prices] #물건의 가격이 1000원 이상이면 10% 할인, 그렇지 않으면 원래 가격을 유지
```

03 Sorted

* 리스트를 정렬하는 방법 (1) - sort 메소드

  Python에서 리스트를 정렬하는 방법은 sort 메소드를 사용

  sort 메소드는 원본 리스트를 정렬

  sort 메소드를 사용한 명령어를 저장하면 None이 저장됨

```python
my_list = [5, 2, 3, 1, 4]
my_list.sort()
print(my_list) = [1, 2, 3, 4, 5]
```

* 리스트를 정렬하는 방법 (2) - sorted 함수

  Python에서 리스트를 정렬하는 또다른 방법은 sorted 함수를 사용

  sorted 함수는 복사본 리스트를 정렬

  sorted 함수를 사용한 명령어를 저장하면 정렬된 리스트가 저장됨

```python
my_list = [5, 2, 3, 1, 4]
sort_list = sorted(my_list)
print(sort_list) = [1, 2, 3, 4, 5]
```

sort 메소드

결과 : 원본 리스트를 정렬

사용법 : list.sort()

내림차순 정렬 : list.sort(reverse = True)

장점 : sorted 함수보다 계산 효율이 미세하게 좋음

sorted 함수

결과 : 복사본 리스트를 정렬

사용법 : result = sorted(list)

내림차순 정렬 : result = sorted(list, reverse = True)

장점 : 원본 리스트를 유지할 수 있음

04 Enumerate

* enumerate 이란?

  enumerate은 순서가 있는 자료형을 대상으로 인덱스(순서)와 그 값을 전달하는 기능을 가진 함수

  enumerate 함수를 print하면 내부 값을 알기 어려움

  list로 형변환하면 확인할 수 있음

  시작 번호를 지정할 수 있음 (보통은 0부터 시작)

```python
my_list = ["Spring", "Summer", "Fall", "Winter"]
print(list(enumerate(my_list, start = 2023))) = [(2023, 'Spring'), (2024, 'Summer'), (2025, 'Fall'), (2026, 'Winter')]
```

* enumerate 함수와 for문

  enumerate은 for문과 함께 자주 사용됨

  for문에서는 list 형변환 없이 바로 사용할 수 있음

```python
my_list = ["elice", "rabiit", "clock", "queen"]

for idx, value in enumerate(my_list):
  print(idx)
  print(value)
```

* enumerate 함수 예시

  순서가 있는 자료형(리스트, 딕셔너리, 문자열 등)을 대상으로 다양하게 사용할 수 있음

```python
#리스트 - enumerate
grades = [85, 92, 78, 90, 88]

for index, grade in enumerate(grades, start = 1):
  print(f"학생 {index}의 성적: {grade}점"

#딕셔너리 - enumerate
temperatures = {"서울":28, "부산":30, "대구":29, "인천":27, "광주":31}

for place, temp in enumerate(temperatures.items(), start = 1):
  city, temperature = temp
  print(f"{place}. {city}의 온도: {temperature}도")

#문자열 - enumerate
text = "안녕하세요, 파이썬!"

for index, char in enumerate(text, start = 1)
  print(f"{index}번째 글자: {char}")
```

05 Lambda

* Lambda 란?

  Python에서 간단한 함수를 작성할 때 사용되는 익명 함수

  lambda <매개변수>:<표현식>

```python
square = lambda x: x ** 2
result = square(5)

result = (lambda x: x ** 2)(5)
```

* Lambda 특징

  간결하고 한 줄로 표현할 수 있으며 별도의 함수 정의 없어도 간단한 기능을 표현할 수 있음

  복잡한 로직이나 긴 표현식을 사용하기에는 적합하지 않을 수 있음

* 일반 함수와 람다(Lambda) 함수 비교

  상품 가격과 수량을 받아 세금을 포함한 총 주문 가격을 계산하는 함수

```python
#일반 함수 구현
def calculate_total_price(item_price, quantity):
  tax_rate = 0.1
  total_price = item_price * quantity
  total_with_tax = total_price * (1 + tax_rate)
  return total_with_tax

item_price = 100
quantity = 52

total = calculate_total_price(item_price, quantity)

print(total)

#람다 함수 구현
calculate_total_price = lambda item_price, quantity: (item_price * quantity) * 1.1

item_price = 100
quantity = 52

print(total)
```

* lambda 심화 - map

  map 함수는 함수와 시퀀스 자료형을 인자로 받음

  시퀀스 자료형의 자료 하나씩 함수에 적용함

  map함수의 결과를 그대로 print하면 결과 확인이 어려우므로 list로 형변환을 해서 확인함(map과 list가 주로 같이 사용됨)

  map의 함수 자리에 Lambda 함수 사용 가능

  두 예제는 같은 람다 함수를 사용했지만 Lambda 함수 위치와 list 형변환 위치가 다르다는 차이(정해진 규칙은 없음!)

```python
#map함수 바깥에 있는 Lambda 함수
square = lambda x: x ** 2
num_list = [10, 11, 12, 13, 14, 15]
map_function = map(square, num_list)

print(list(map_function))

#map함수 안에 있는 Lambda 함수
num_list = [10, 11, 12, 13, 14, 15]
map_function = list(map(lambda x: x ** 2, num_list))

print(map_function)
```

### [참고자료] if__name__ == "main__"
01 Remind - 모듈

* 모듈(Module)이란?

  코드의 길이가 길어지는 상황에서 모든 함수, 변수를 구현하는 것은 어려움! → 누군가 만들어놓은 함수, 변수 등을 활용하자!

  모듈(Module) = 특정 목적을 가진 함수, 자료의 모임

02 if __name__ == "__main__"

* 파이썬 파일을 실행하면 모든 코드를 실행한다

  특정 프로그래밍 언어(ex. C, JAVA)에서는 해당 파일을 실행하면 main이라는 함수(main 함수)부터 시작 → 시작점이 분명함

  하지만 파이썬은 main이라는 함수가 없어서 모든 코드(특히 들여쓰기가 되지 않은 코드)를 실행함

  → 프로그램을 구성할 때 의도하지 않은 코드가 실행될 수 있음

  → 프로그램 동작 순서를 구성하기 어려움

  if __name__ == "__main__" 을 이용하면 시작점을 지정할 수 있음

* if __name__ == "__main__" 사용 결과

```python
import sys

def sum(a, b): #3번째 실행
  c = a + b
  return c

def main(): #2번째 실행
  print("3 더하기 6은?")

  result = sum(3, 6)
  print(result)

if __name__ == "__main__": #1번째 실행
  sys.exit(main())
```

---
## [자율심화]03-1 디버깅이 필요한 이유
### [수업 자료] 왜 디버깅이 필요할까요?
* 버그와 예외

  <버그(Bug) : 코드가 원하는 대로 동작하지 않는 모든 경우>

  프로그램이 죽는 (크래시가 발생하는) 경우

  예상한 속도보다 훨씬 느리게 동작하는 경우

  잘못된 결과를 출력하는 경우

  코드 설계 상 일어나면 안 되는 상황이 일어난 경우

  <예외(Exception) : 일반적이지 않은 코드의 동작>

  사용자가 프로그램을 강제 종료하는 경우

  분수의 분모에 0이 들어가는 경우

  열고자 하는 파일이 존재하지 않는 경우

  인터넷이 불안정한 경우

  예외 처리(Exception handling) : 인터넷이 끊기거나 휴대폰이 꺼졌다면? 개발자는 사용자의 다양한 상황을 예측할 수 있어야 함

* 디버깅이란?

  사용/테스트 중 찾아낸 버그를 없애 나가는 과정

  버그의 원인을 찾고

  발생한 버그를 해결하고

  비슷한 버그의 재발을 방지하는 것

  <버그의 원인 찾기>

  어떤 상황에서, 어떤 조작을 했을 때 일어나는가?

  얼마나 잦은 빈도로 발생하는가?

  에러 메시지가 뜬다면 내용이 무엇인가?

  <발생한 버그 해결하기>

  버그가 발생한 원인을 해결하려면 어떻게 해야 하는가?

  새로운 코드가 일으킬 새로운 버그는 없는가?

  <버그 재발 방지하기>

  버그를 일으킨 코드가 다른 곳에서 사용되는가?

  비슷한 설계를 이용한 다른 코드는 없는가?

  코친 코드의 약점은 없는가?

  코드를 지속적으로 검증할 방법은 무엇인가?

* 디버깅이 중요한 이유

  사용자 경험과 직결 : 버그로 인한 불쾌한 경험 > 새로운 기능

  처음부터 완벽한 코드는 없다 : 빠르게 문제를 파악/해결하는 것이 능력! (코드가 한 번에 작동할 때 → 어... 왜 벌써 되지?)

  실패는 성공의 어머니 : 많은 버그를 경험할수록, 더 안전한 코드를 설계하는 능력이 생긴다!

### [실습1] 디버깅 문제 예시

```python
n = int(input())
result = []

for i in range(1, n+1) :
  result.append("결과" + str(i) + ".txt");

for r in result :
  print(r)
```

---
## 자율 실습 문항
### [실습4] 사투리 전문가

```python
greeting = '밥 먹었어?'
print("서울 :",greeting)

def busan(greeting):
  greeting = '밥 뭇나?'

  print("부산 :",greeting)

busan(greeting)
print(greeting)
```

### [실습5] 메서드

```python
my_dict = {1:'Apple',2:'Microsoft',3:'nVidia'}

var1 = my_dict.keys()
var2 = my_dict.values()

print(var1)
print(var2)
```

### [미션 1] 타율 구하기

```python
def batting_average(score):
  on = score[0]
  hit = sum(score[1:])

  if hit > on:
    return -1
  else:
    return(round((hit / on),3))

# 이승엽 선수의 한국 야구 통산 타석수, 1루타 개수, 2루타 개수,3루타 개수, 홈런 개수
batting_score = [7132, 1197, 464, 28, 467]
print(batting_average(batting_score))
```

### 청개구리

```python
def tree_frog(boolean):
  if boolean:
    value = False
  else:
    value = True
  return value

print(tree_frog(1==1))
```

### 봉주~르! 안녕하세요!

```python
def greeting():
  print('bonjour!')

print('bonjour!')
```

### 호박 고르기

```python
pumpkin = (1,2,3,4,5)
big = max(pumpkin)
small = min(pumpkin)
```

### 사투리 전문가

```python
greeting = '밥 먹었어?'
print("서울 :",greeting)

def busan(greeting):
  greeting = '밥 뭇나?'

  print("부산 :",greeting)

busan(greeting)
print(greeting)
```

### [실습2] 모듈 활용 : time

```python
import time

clock = time.ctime()
print(clock)
```

---
