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

기존의 리스트를 생성할 때, 


