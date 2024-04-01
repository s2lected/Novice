## 01 Python 복습
### [조건문 복습] 너의 성적은

```python
num = int(input())

if num > 80:
  print('A')
elif num <= 80 and num > 60:
  print('B')
elif num <= 60 and num > 50:
  print('C')
elif num <= 50 and num > 40:
  print('D')
else:
  print('F')
```

### [반복문 복습] 피라미드

```python
num = int(input())

for i in range(1, num+1):
  print('*' * i)
```

### [조건문 & 반복문 복습] 알파벳 야구

```python
answer = input()
guess = input()
N = 0
M = 0

for i,j in zip(answer,guess):
  if i == j:
    N += 1
  elif j in answer:
    M += 1

if N == len(answer):
  print('정답입니다.')
else:
  print(str(N)+'스트라이크', str(M)+'볼')
```

### [함수 복습] 원재료 검사

```python
def check(ingredients):
  for i in ingredients:
    if i == '호두':
      return True
  return False
```

### [모듈 복습] 청기 들어! 백기 들어!

```python
from elice_func import elice_random_string

pattern = elice_random_string()
new_pattern = pattern[0:6] + pattern[20:30]

print(new_pattern)
```

### [python 종합 복습] 평균과 평균보다 큰 수

```python
def solve(values):
  avg = int(sum(values) / len(values))
  bigger = []
  for num in values:
    if num > avg:
      bigger.append(num)
  return (avg, bigger)

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solve(example_list))
```

---
## 02 Pandas 라이브러리 알아보기
### [강의자료] Pandas 라이브러리 알아보기
1. Pandas 라이브러리 소개

   * Pandas
  
     데이터 조작 및 분석을 위한 파이썬 라이브러리

     시리즈와 데이터프레임이라는 데이터분석에 유용한 데이터 구조 제공

     엑셀의 파이썬 버전

   * Pandas를 배워야 하는 이유

     대용량의 데이터를 처리하기 용이

     프로그래밍을 통한 반복적인 작업 및 자동화에 유리

     머신러닝/딥러닝 모델에 필요한 데이터 처리

   * 데이터

     대부분의 데이터는 엑셀과 유사한 표 형태로 저장

   * DataFrame

     Pandas 라이브러리에서 지원하는 자료구조

     2차원의 행렬 데이터를 표 형태로 저장

     가로인 행(row)과 세로인 열(column)으로 이루어짐

     각 행과 열은 인덱스를 가지고 있어 데이터를 쉽게 검색하고 필터링 가능

   * Series
  
     Pandas 라이브러리에서 지원하는 자료구조

     각 원소는 인덱스와 값으로 이루어짐

     인덱스는 숫자 또는 문자열로 지정 가능

   * 시리즈와 데이터프레임
  
     데이터프레임에서 하나의 열 데이터를 추출하면 시리즈

   * Pandas 사용하기

     Pandas 라이브러리를 사용하기 위해서는 불러오는 작업 필요

```python
import pandas as pd
```

  * pandas 라이브러리를 불러와서, pd라는 별명으로 사용한다는 의미

```python
df = pd.read_csv('data/seoul_park.csv') #pd(pandas)에 있는 read_csv() 함수를 사용
```

2. 데이터 살펴보기

   * 데이터 파일
  
     Pandas는 다양한 형식의 데이터 파일을 불러올 수 있음

     우리가 실제로 사용할 데이터 대부분은 .csv 파일 혹은 .xlsx 파일 형식

   * 강의에 활용할 데이터
  
     2016년 1월 1일부터 2019년 3월 31일까지의 서울대공원 입장객 데이터

     조류독감으로 인해 2016년 12월 18일부터 2017년 3월 27일까지 폐쇄되어 기록이 없음

     입장객의 수와 분류, 공휴일 여부와 날씨 등이 기록되어 있음

     data라는 폴더 안에 "seoul_park.csv"파일로 저장되어 있음

   * 데이터 불러오기: read_csv(), read_excel()

     파일로 저장 되어있는 데이터를 불러와서 데이터프레임으로 저장

     .csv 파일로 저장 되어있는 데이터는 read_csv() 사용

     .xlsx 등의 파일로 저장되어 있는 데이터는 read_excel() 사용

   * 데이터 일부 확인: head(), tail()
  
     데이터프레임의 앞 뒤 일부 데이터를 확인하는데 사용

```python
df.head() #0~4번 index 다섯줄
df.tail() #끝 index부터 다섯줄
```
   * 데이터 정보 확인: info()

     데이터의 정보를 확인하는데 사용

     어떤 컬럼이 있는지, 몇 개의 값이 있는지, 어떤 형태로 저장되어 있는지 확인 가능

```python
df.info()
```

   * 데이터프레임에서 특정 컬럼 추출

     데이터프레임에서 컬럼이름을 활용해 특정 컬럼을 시리즈 형태로 추출 가능

```python
df["컬럼이름"]
```

   * 데이터프레임에서 특정 컬럼 추출

     리스트를 활용하면 여러 개의 컬럼을 데이터프레임 형태로 추출 가능

```python
df[["컬럼이름1", "컬럼이름"]]
```

   * 데이터 숫자 세기: value_counts()

     해당 컬럼에 값들이 몇 개씩 저장되어 있는지 알고 싶을 때 사용

```python
df["컬럼이름"].value_counts()
```

### [실습1] 데이터 살펴보기





