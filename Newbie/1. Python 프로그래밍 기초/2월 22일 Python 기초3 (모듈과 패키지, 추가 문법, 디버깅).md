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
## [자율심화] 02 파이썬 심화 문법
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

* 




05 Lambda
