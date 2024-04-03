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
* 데이터 살펴보기

  이번 실습에서는 데이터를 불러오고 확인하는 과정을 수행합니다.

* 라이브러리 불러오기

  데이터 분석에서 널리 사용되는 파이썬 패키지 중 하나인 pandas는 데이터를 처리하고 조작하는 데 필수적인 도구를 제공합니다.

```python
import pandas as pd
```

  실습에 사용할 데이터는 2016년 1월 1일부터 2019년 3월 31일까지의 서울대공원 입장객 데이터입니다. 데이터에는 날짜, 공휴일 여부, 입장객 연령 등 다양한 정보가 저장되어 있습니다.

* 데이터 불러오기: read_csv()

  이제 data폴더에 저장되어 있는 데이터인 seoul_park.csv 파일을 불러와 데이터프레임 df에 저장합니다.

  csv 파일 형태를 가지므로 read_csv()를 활용하여 불러옵니다.

  read_csv()에는 데이터가 저장되어 있는 파일의 경로를 입력받습니다.

```python
df = pd.read_csv("./data/seoul_park.csv")
```

  이제 데이터프레임 df에 서울대공원 입장객 데이터가 저장되어 있습니다.

* 데이터 살펴보기: head(), tail()

  데이터의 갯수는 총 1085개로 데이터가 너무 커 한눈에 들어오지 않습니다.

  pandas 라이브러리에는 데이터를 살펴보기에 유용한 기능들이 있습니다.

  head(), tail()을 사용하면 데이터의 처음과 끝의 일부를 확인할 수 있습니다.

```python
df.head()
df.tail()
df.head(10) #메서드 안에 숫자를 입력하여 출력하는 데이터의 갯수를 지정
```

* 데이터 정보 확인: info()

  데이터가 몇 개의 값을 가지는지, 어떤 자료형으로 저장되어 있는지를 확인하는 데에는 info()를 활용할 수 있습니다.

```python
df.info()
```

* 컬럼 이름을 활용한 특정 컬럼 추출

  데이터프레임은 여러개의 시리즈가 열을 이루고 있는 자료형입니다.

  대괄호를 사용하면 데이터프레임에서 특정 시리즈(열)를 추출할 수 있습니다.

  예를 들어 데이터프레임 df에서 "청소년" 열을 추출하는 코드는 다음과 같습니다.

```python
df["청소년"]
```

  앞으로 특정 메서드에 위의 코드처럼 데이터프레임["컬럼이름"] 형태의 문법이 사용됐다면 해당 열에만 메서드를 적용한다고 이해하시면 됩니다.

  예를 들어 "날씨" 컬럼의 정보만을 알기 위해 info() 메서드를 "날씨" 열에만 적용하려면 다음과 같이 활용할 수 있습니다.

```python
df["날씨"].info()
```

* 데이터 숫자 세기: value_counts()

  value_counts()를 활용하면 컬럼에 어떤 값들이 몇 개씩 존재하는지 확인할 수 있습니다.

  예를 들어 df의 날씨 컬럼에는 날씨가 저장되어 있는데 해당 컬럼에 value_counts()를 활용하면 어떤 종류의 날씨들이 있는지, 각 날씨별로 몇 개의 데이터가 있는지 확인할 수 있습니다.

```python
df["날씨"].value_counts()
```

---
## 03 데이터 변환하고 요약하기
### [강의자료] 데이터 변환하고 요약하기
3. 데이터 변환하기 1

   * 데이터 타입 변환의 필요성
  
     데이터는 항상 원하는 타입으로 되어있지 않다!

     실습에 사용할 데이터에 있는 숫자들이 정수 타입이 아닌 텍스트(object) 타입으로 저장되어 있음

     텍스트(object) 타입일 경우 덧셈이나 뺄셈 등의 연산이 불가능

   * 데이터 타입 변환: astype()
  
     해당 컬럼의 데이터 타입을 원하는 타입으로 변환할 때 사용

```python
df["컬럼이름"].astype(변환할타입)
df["어른"] = df["어른"].astype(int) #df의 "어른" 컬럼 데이터의 타입을 int로 변환하여 df의 "어른" 컬럼에 저장(덮어씌우기)
```

   * 데이터프레임 변환 시 유의사항

     Pandas의 메서드는 원본 데이터프레임(시리즈)을 바로 변환하지 않고, 변환된 데이터프레임(시리즈)을 반환

     원본 데이터프레임을 변환하려면 덮어씌워주는 작업이 필요

   * 데이터 타입 변환: to_numeric()

     해당 컬럼의 데이터 타입을 숫자 타입으로 변환할 때 사용

```python
pd.to_numeric(df["컬럼이름"])
df["유료합계"] = pd.to_numeric(df["유료합계"]) #df의 "유료합계" 컬럼의 데이터 타입을 숫자로 변환하여 df의 "유료합계" 컬럼에 저장(덮어씌우기)
```

   * 한꺼번에 타입 변환하기

     변환해야 하는 컬럼들을 리스트로 만들고, for문을 활용해 한꺼번에 타입 변환 가능

```python
columns = ['유료합계', '어른', '청소년', '어린이', '외국인', '단체', '무료합계', '총계']
for i in columns:
  df[i] = pd.to_numeric(df[i])
```

   * 데이터 타입 변환: to_datetime()

     날짜/시간으로 변환 가능한 문자열, 정수, 실수를 시간 타입으로 변환할 때 사용

```python
pd.to_datetime(df["컬럼이름"])
df["날짜"] = pd.to_datetime(df["날짜"]) #df의 "날짜" 컬럼의 텍스트(ex. "2016-01-01")를 시간 타입(ex. 2016년 1월 1일 시간 자료)으로 변환하여 df의 "날짜" 컬럼에 저장(덮어씌우기)
```

   * 시간 타입을 활용한 데이터 변환: dt

     시간 타입은 날짜와 시간에 대한 정보가 담겨있어 다양한 처리가 가능

```python
df['연'] = df['날짜'].dt.year #년도 정보가 저장된 df['연'] 컬럼을 생성
df['월'] = df['날짜'].dt.month #월 정보가 저장된 df['월'] 컬럼을 생성
df['일'] = df['날짜'].dt.day #일 정보가 저장된 df['일'] 컬럼을 생성
df['요일'] = df['날짜'].dt.dayofweek #요일 정보가 저장된 df['요일'] 컬럼을 생성(요일은 숫자로 저장 (월~일:0~6)
```

4. 데이터 변환하기 2

   * 데이터 변환
  
     데이터 분석의 정확성을 높이기 위해 데이터의 값 변환이 필요한 경우가 많음

     알아보기 쉬운 데이터로 바꾸거나, 단위를 통일하는 등 다양한 변환 가능

   * 시리즈 연산을 통한 변환
  
     데이터프레임의 각 열은 시리즈로, 연산이 가능함

     다양한 컬럼의 연산을 활용해 데이터를 변환하거나 새로운 컬럼 생성 가능

```python
df["어른"] = df["어른"] + 200
df["동물원매출"] = df["어른"] * 5000 + df["청소년"] * 3000 + df["어린이"] * 2000
```

   * 열 전체 변환: map()

     데이터프레임의 특정 열 전체를 변환하는데 사용

     딕셔너리 등을 사용하여 변환 방식을 지정하고 해당 컬럼에 적용

```python
df["컬럼이름"].map(딕셔너리 등)
```

   * 데이터프레임에 map() 적용하기

     df의 "요일" 컬럼의 값들을 딕셔너리 week의 Key와 Value를 활용하여 숫자로 표시되어 있는 요일을 글자로 변경

```python
week = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}
df['요일'] = df['요일'].map(week)
```


   * 데이터에 함수 적용: apply()

     데이터프레임에 함수를 적용할 때 사용

     map과 달리 복수의 컬럼에 사용 가능

```python
df["컬럼이름"].apply(함수, axis = 0 또는 1) #0이면 열 단위로, 1이면 행 단위로 함수 적용(생략되어 있으면 기본값은 0)
```

   * 데이터프레임에 apply() 적용하기

     '눈'과 '비'를 '눈/비'로 합치는 weather 함수를 선언

     df의 "날씨" 컬럼의 값들에 weather 함수를 적용하여 변환한 뒤 df의 "날씨" 컬럼에 저장(덮어씌우기)

```python
def weather(e):
  if e == '눈' or e == '비':
    return '눈/비'
  else:
    return e

df['날씨'] = df['날씨'].apply(weather)
```

   * 참고: lambda 함수

     간단하게 함수를 선언하는 문법

     한 줄로 표현되며, 콜론(:) 왼쪽에는 인자를, 오른쪽에는 반환값을 작성

```python
def times2(x):
  return 2 * x

times = lambda x : 2 * x

def add(x,y):
  return x + y

add = lambda x,y : x + y
```

   * lambda 함수를 활용한 apply 활용

```python
def weather(e):
  if e == '눈' or e == '비':
    return '눈/비'
  else:
    return ee

df['날씨'] = df['날씨'].apply(weather)

df['날씨'] = df['날씨'].apply(lambda e : '눈/비' if e == '눈' or e == '비' else e)
```

5. 데이터 요약하기

   * 데이터 요약
  
     데이터의 정보를 요약해서 확인하기 위한 과정

     데이터에 대한 정보를 미리 파악하여 추후 분석 방향 판단 가능

   * 데이터 통계값 확인: mean(), min(), max(), median()
  
```python
df.mean()
df["컬럼이름"].mean()
```

   * 데이터 전체 통계: describe()

     데이터프레임이나 시리즈의 간단한 통계 정보를 요약해서 확인 가능

     평균(mean), 표준편차(std), 최소값(min), 25/50/75% 분위수(25%/50%/75%), 최대값(max) 출력

```python
df.describe()
```

   * 데이터 그룹화: groupby()

     데이터를 그룹으로 묶어 분석할 때 사용

     groupby()를 적용한 결과는 DataFrame 형태가 아닌 DataFrameGroupBy 형태

     2개 이상의 컬럼을 기준으로 집계도 가능

     특정 컬럼을 지정하지 않고 전체 컬럼에 대한 집계도 가능

```python
df.groupby("컬럼이름1")["컬럼이름2"].집계함수
df.groupby("날씨")["총계"].mean() #df의 "날씨" 컬럼을 기준으로 그룹화하여 "총계" 값의 평균을 집계

df.groupby(["컬럼이름1"], ["컬럼이름2"])["컬럼이름3"].mean()
df.groupby(["날씨", "공휴일"])["총입장객수"].mean() #df의 "날씨"와 "공휴일" 컬럼을 기준으로 그룹화하여 "총입장객수" 컬럼의 평균값을 집계

df.groupby("컬럼이름").집계함수
df.groupby("날씨").mean() #df의 "날씨" 컬럼을 기준으로 모든 컬럼의 평균값을 집계
```

### [실습1] 데이터 변환하기 1
* 데이터 불러오기

  실습에 사용할 데이터를 불러오겠습니다.

  데이터를 다시 살펴보겠습니다.

  데이터의 숫자들에는 천 단위로 콤마(,)가 찍혀있습니다.

  또한 데이터의 "단체" 컬럼의 윗부분과 아래부분을 보면 윗쪽의 데이터에는 0명이 0으로 적혀있지만, 아래쪽에는 - 으로 표기되어있습니다.

  이는 년도가 지나면서 기록 방식이 바뀌면서 생긴 문제입니다.

  info()를 사용해 데이터의 타입을 확인해보면 모든 데이터가 수가 아닌 텍스트(Object) 타입으로 저장되어 있습니다.

  이는 즉 데이터에 있는 3,359는 숫자 3359가 아닌 텍스트 "3,359"가 저장되어있는 상태입니다.

  이 상태로는 숫자의 연산, 나아가 평균값과 같은 통계량을 측정할 수 없습니다. 따라서 우리는 이 텍스트(Object)들을 모두 정수형(int) 으로 바꾸어야 합니다.

  정수형으로 바꾸기 위해선 텍스트에서 숫자만을 남기고 모두 제거해야 합니다.

  이를 위해 숫자로 바꾸어야 하는 컬럼들에서 str.replace()를 활용하여 -를 0으로 바꾸고 콤마를 제거합니다.

```python
columns = ['유료합계', '어른', '청소년', '어린이', '외국인', '단체', '무료합계', '총계']
for i in columns:
  df[i] = df[i].str.replace('-', '0')
  df[i] = df[i].str.replace(',', '')
```

  데이터의 숫자들이 깔끔하게 정리된 것을 확인할 수 있습니다.

* 데이터 타입 변환: astype()

  데이터의 숫자들이 깔끔하게 정리되기는 했지만, info를 활용하여 살펴보면 여전히 데이터 타입은 텍스트(Object)인 것을 알 수 있습니다.

  통계적인 분석을 위해 해당 데이터들을 정수(int)형태로 바꿔주어야 합니다.

  astype()을 사용하면 원하는 타입으로 변환할 수 있습니다. astype메서드를 활용해 "어른" 컬럼의 데이터를 정수 형태로 변환하는 코드는 다음과 같습니다.

```python
df["어른"].astype(int)
```

  이제 "어른" 컬럼의 형태가 제대로 변환되었는지 확인해보겠습니다.

  df의 어른 컬럼의 데이터타입은 object로, astype()을 사용했지만 바뀌지 않은 것을 확인할 수 있습니다. 어떻게 된 일일까요.

  astype()을 비롯해 데이터프레임에 뭔가 변형을 가하거나 작업을 하는 메서드들은 데이터프레임 자체를 변환하지 않고, 변환된 새로운 데이터프레임을 반환합니다.

  따라서 df["어른"].astype(int)이라는 코드는 df의 "어른" 컬럼을 정수형으로 변환하기는 하지만, 그냥 정수형으로 바뀐 "어른" 컬럼을 시리즈 형태로 나타낼 뿐 df의 "어른" 컬럼 그 자체가 바뀌는 것이 아닙니다.

  df의 "어른" 컬럼을 바꾸고 싶다면 astype()을 활용해 변환하여 생성한 "어른" 컬럼 시리즈를 df의 "어른" 컬럼에 덮어씌워주는 작업이 필요합니다. 이는 다음과 같이 수행할 수 있습니다.

```python
df["어른"] = df["어른"].astype(int)
```

  덮어씌워주는 과정을 통해 어른 컬럼의 데이터타입이 정수형(int)으로 바뀐 것을 확인할 수 있습니다.
  
  이런 식으로 원본의 데이터프레임을 가공하기 위해선 덮어씌워주는 작업이 필요하다는 사실과 해당 코드를 익혀두시면 앞으로 강의의 코드를 이해하시기 한결 수월할 것입니다.

* 데이터 타입 변환: to_numeric()

  to_numeric()은 astype()과 같이 데이터의 형태를 변환하지만 원하는 타입을 지정할 수 있는 astype()과 달리 숫자로만 변환한다는 차이점이 존재합니다.

  특히나 데이터분석에서는 데이터를 숫자로 변환할 일이 많기 때문에 유용하게 사용할 수 있습니다.

```python
df["유료합계"] = pd.to_numeric(df["유료합계"])
```

  유료합계 컬럼이 정수형(int)으로 바뀐 것을 확인할 수 있습니다.

* 데이터 타입 변환: to_datetime()

  날짜 컬럼에는 데이터가 수집된 날짜가 기록되어있습니다. 하지만 위의 정보를 보면 알 수 있다시피 날짜는 텍스트로 저장되어있습니다.

  다시 말해 날짜 컬럼의 "2016-01-01"는 텍스트일 뿐 컴퓨터가 이것을 날짜로 인식할 수 없습니다.

  이 날짜를 보다 효과적으로 활용하기 위해 to_datetime()을 활용해 날짜컬럼 전체를 datetime형식으로 변환해줍니다.

```python
df["날짜"] = pd.to_datetime(df["날짜"])
```

  이번엔 날짜 데이터를 사용해보겠습니다.
  
  데이터프레임에서 datetime 형태의 데이터에는 연, 월, 일 정보가 담겨있어 이를 활용하면 날짜정보를 비롯해 요일과 같은 새로운 정보를 생성할 수 있습니다.
  
  이를 위해 dt 속성을 사용하여 datetime 형태의 데이터에서 특정 정보들을 추출하고 연, 월, 일, 요일 컬럼을 새롭게 생성해보겠습니다.

```python
df['연']=df['날짜'].dt.year
df['월']=df['날짜'].dt.month
df['일']=df['날짜'].dt.day
df['요일']=df['날짜'].dt.dayofweek
```

  연, 월, 일, 요일 컬럼이 생성되고 해당하는 정보가 저장된 것을 확인할 수 있습니다. 그런데 요일이 글자가 아닌 숫자로 기록되어 있는 것을 확인할 수 있습니다.

  이대로도 데이터 분석을 진행할 수는 있지만, 조금 알아보기 번거롭습니다.
  
  만약 요일에 있는 숫자들을 한글로 바꾸는 것 처럼 데이터에 일괄적으로 변형을 주고 싶다면 어떻게 해야할까요? 이에 대해서는 다음 실습에서 알아보도록 하겠습니다.

### [실습2] 데이터 변환하기 2
* 데이터 불러오기

  이전 실습에서 우리는 데이터의 형 변환을 통해 숫자와 날짜 데이터들의 형태를 변환해주고, 날짜 데이터를 활용해 연, 월, 일, 요일 컬럼을 생성하였습니다.

  지난 실습을 통해 정제된 데이터를 불러옵니다.

  요일 컬럼이 글자가 아닌 숫자로 기록되어 있는 것을 확인할 수 있습니다. 이대로도 데이터 분석을 진행할 수는 있지만, 알아보기가 조금 어렵습니다.

* 열 전체 변환: map()

  이 숫자들은 0부터 6까지, 월요일부터 일요일까지 숫자가 매칭되어있습니다. 이 정보를 활용하여 "요일" 컬럼 전체 데이터를 변환하고자 map()을 사용합니다.

  먼저 map()에 변환 정보를 입력해주기 위해 숫자를 키로, 그에 대응하는 요일 글자를 값으로 가지는 week 딕셔너리를 생성합니다.

```python
week = {0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토',6:'일'}
```

  이제 map()과 요일 정보가 담긴 week 딕셔너리를 사용해서 df의 "요일" 컬럼을 변환합니다.

```python
df['요일'] = df['요일'].map(week)
```

  요일 컬럼의 데이터들이 딕셔너리에 맞춰 변환된 것을 확인할 수 있습니다.

* 데이터에 함수 적용: apply()

  이번엔 "날씨" 컬럼을 살펴보겠습니다.

```python
df['날씨'].value_counts()
```

  날씨 컬럼 데이터에는 '눈', '비', '눈/비' 가 있습니다.
  
  날씨와 입장객수의 관계는 매우 밀접하지만, 이것은 어디까지나 날씨가 맑은지 흐린지가 중요할 뿐 비인지 눈인지는 크게 중요하지 않습니다.
  
  그렇기 때문에 세 종류의 데이터를 모두 '눈/비'로 통일해서 합치고자 합니다.
  
  먼저 '눈', '비' 를 입력받으면 '눈/비'로 바꿔주는 함수를 선언합니다.

```python
def weather(e):
  if e=='눈' or e=='비':
    return '눈/비'
  else:
    return e
```

  이제 이 함수를 컬럼 전체에 적용하기 위해 apply()를 사용합니다.
  
  apply()는 특정 컬럼 혹은 데이터프레임 전체에 특정 함수를 적용할 때 사용 가능합니다.
  
  df의 "날씨" 컬럼에 weather 함수를 적용하려면 아래와 같이 사용할 수 있습니다.

```python
df["날씨"] = df["날씨"].apply(weather)
df["날씨"].value_counts()
```

  "날짜" 컬럼의 데이터에서 '눈', '비'가 '눈/비'로 통일되어 111개가 되었음을 확인할 수 있습니다.
  
  이렇게 원하는 함수를 정의해서 apply()를 활용해 적용하는 과정은 굉장히 많이 사용되게 됩니다.
  
  하지만 다양한 변환이 필요할수록 매번 함수를 만들고 사용해야하고, 이는 코드를 지저분하게 만듭니다.
  
  파이썬에서는 이러한 문제를 해결하기 위해 일회용으로 사용할 함수를 정의하는데 유용한 람다함수 기능을 지원합니다.
  
  람다함수를 사용하면 위에서 weather() 함수를 정의하는 과정을 생략하고 다음과 같이 사용할 수 있습니다.
  
```python
df["날씨"]=df["날씨"].apply(lambda e : "눈/비" if e=="눈" or e=="비" else e)
```

### [실습3] 데이터 요약하기
* 데이터 불러오기

  지난 실습에서 데이터 변환을 통해 "요일", "날씨" 컬럼을 알아보기 쉽게 변환하였습니다. 지난 실습을 통해 정제된 데이터를 불러옵니다.

* 데이터 통계값 확인: mean(), min(), max(), median()

  데이터의 통계값을 확인하기 위해 각종 집계함수(mean(), min(), max(), median() 등)를 사용할 수 있습니다.

  예를들어 mean()을 활용해 "어른" 컬럼의 평균값을 구하려면 다음과 같이 사용할 수 있습니다.

```python
df["어른"].mean()
```

  전체 일자의 어른 입장객 수의 평균을 구할 수 있습니다. 이번엔 총 입장객 수("총계")가 가장 적은 날의 입장객 수를 알아보도록 하겠습니다.

```python
df["총계"].min()
```

  총 인원이 2명만 입장한 날이 있다는 사실을 알 수 있습니다.
  
  여담이지만 해당 날짜인 2017년 3월 28일은 조류독감으로 인해 폐쇄되었던 서울대공원의 재개장을 알리는 언론보도가 나온 날짜로 재개장을 위한 입장 및 집계 시스템의 내부 테스트 정도로 유추해볼 수 있습니다.

* 데이터 전체 통계: describe()

  위에서 배운 집계함수를 활용하면 내가 원하는 통계값을 확인할 수 있지만, 때로는 전체 통계값을 보고 이를 통해 데이터의 분석 방향을 결정하기도 합니다.

  이를 위해 데이터프레임의 다양한 통계값을 정리해서 보여주는 describe()를 사용합니다.

  describe()는 숫자형 데이터들로 이루어진 컬럼들의 데이터의 갯수(count), 평균(mean), 표준편차(std), 최소값(min), 사분위수(25/50/75%), 최대값(max)를 보여줍니다.

  describe()를 사용해 우리는 입장객의 수가 가장 많았던 날은 58,688명이었다는 것("총계" 컬럼의 max값),

  평균적으로 어른, 청소년, 어린이, 외국인 순으로 입장객의 수가 많았다는 것(각 컬럼의 mean값 비교) 등 다양한 정보를 얻을 수 있습니다.

* 데이터 그룹화: groupby()

  다음은 데이터를 그룹으로 묶어서 확인할 수 있는 groupby()입니다. groupby()를 사용하면 특정 기준에 따라 데이터를 정리해서 분석할 수 있습니다.

  예를 들어 서울대공원 데이터를 통해서 날씨에 따른 입장객의 수가 궁금할 때, 우리는 groupby()를 사용해서 "날씨"를 기준으로 "총계"값의 평균을 구할 수 있습니다.

```python
df.groupby("날씨")["총계"].mean()
```

  예상대로 날씨가 맑음일 때 가장 평균 입장객 수가 많고, 눈/비일 때 가장 적은 것을 확인할 수 있습니다.
  
  더 나아가 날씨가 맑을때와 눈/비가 올 때의 입장객 수가 수치적으로 2배가 넘게 차이가 난다는 것은 물론 구름의 많고적음은 입장객의 수에 큰 영향을 끼치지 않는다는 사실까지 알 수 있습니다.

  이렇게 groupby()를 사용하면 데이터를 그룹별로 분할하고 각 그룹에 대한 통계량을 확인하여 특정 기준에 따른 데이터의 추세를 확인할 수 있습니다.
  
  이 데이터를 분할하는 기준은 한 개 이상이 될 수도 있습니다.
  
  앞서 날씨에 따라 입장객의 총 수를 확인하였는데, 입장객의 수에 큰 영향을 미치는 또 하나의 요인은 바로 공휴일 여부입니다.
  
  groupby()에서 그룹화 기준이 되는 컬럼을 "날씨"와 "공휴일" 2개의 컬럼으로 설정하면 전체 데이터를 날씨에 따라서 그룹으로 한번 묶고, 각 날씨별 그룹 안에서 다시 공휴일 여부에 따라 두 분류로 데이터를 분류합니다.

```python
df.groupby(["날씨","공휴일"])["총계"].mean()
```

  날씨에 따라 묶었던 데이터를 공휴일 여부에 따라서 데이터를 한번 더 분류했더니 좀 더 자세한 정보들을 알 수 있습니다.
  
  공휴일이 아닌 날의 경우 날씨에 따라 입장객의 수 차이가 그리 크지 않다는 사실을 알 수 있습니다.
  
  또한 날씨가 맑음이거나 구름일 때에는 공휴일 여부에 입장객의 수가 따라 월등히 차이가 나지만 눈/비 일때는 오히려 날씨에 따른 입장객 수의 차이가 크지 않음을 알 수 있습니다.
  
  groupby()를 활용해 2개 이상의 컬럼을 확인하는 것 역시 가능합니다. 이 경우 집계 결과가 데이터프레임으로 출력됩니다.

```python
df.groupby(["날씨","공휴일"])[["어른", "어린이"]].mean()
```

---
## 04 Pandas 기초 1 실습
### pandas 패키지 불러오기

```python
import pandas as pd

df = pd.DataFrame()
print(df)
```

### Series 데이터

```python
import pandas as pd

series = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"], name="Title")
print(series, "\n")

my_series = pd.Series([100, 96, 80, 85], index = ["Kor", "Eng", "Mat", "Sci"], name = "Exam")
print(my_series, "\n")
```

### 데이터프레임에서 특정 컬럼 조회

```python
import pandas as pd

total_student  = int(input('총 성적의 개수 : '))
col_names = ['이름', '국어', '수학', '영어']

scores = [[int(col) if col.isdigit() else col for col in input().split()] for _ in range(total_student)]
df = pd.DataFrame(scores, columns=col_names)
print('\n', df, '\n')

print(df['국어'])
```

### 데이터프레임에 새로운 컬럼 추가

```python
import pandas as pd

total_student  = int(input('총 성적의 개수 : '))
col_names = ['이름', '국어', '수학', '영어']

scores = [[int(col) if col.isdigit() else col for col in input().split()] for _ in range(total_student)]
new_score = list(map(int, input().split()))
df = pd.DataFrame(scores, columns=col_names)
print('\n', df, '\n')
print('new_score :', new_score, '\n')

df[('사회')] = pd.Series(new_score)
print(df)
```

### 데이터프레임 숫자 세기

```python
import pandas as pd

df = pd.read_csv('./data/data.csv')

sex = {
        1: '남성', 
        2: '여성'
      }

df['SEX'] = df['SEX'].map(sex)

dis = {
        1: '고혈압/당뇨병 진료내역 있음',
        2: '고혈압 진료내역 있음', 
        3: '당뇨병 진료 내역 있음', 
        4: '고혈압/당뇨병 진료내역 없음'
       }

df['DIS'] = df['DIS'].map(dis)

dis_count = df['DIS'].value_counts()

print(dis_count)
```

### 콤마가 있는 숫자 처리하기

```python
import pandas as pd

df = pd.read_csv("./data/access_data.csv")

print(df.info())
print("===================\n")

print(df.head())

df["접속일자"] = pd.to_datetime(df["접속일자"])

def del_comma(data: str):
  if "," in data:
    data = data.replace(",", "")
  return data

df["PC접속수"] = df["PC접속수"].apply(del_comma)
df["모바일접속수"] = df["모바일접속수"].apply(del_comma)

df["PC접속수"] = df["PC접속수"].astype(int)
df["모바일접속수"] = df["모바일접속수"].astype(int)

df["전체접속수"] = df["PC접속수"] + df["모바일접속수"]

print(df.info())
print("===================\n")

print(df.head())
```

### 서울시 인구수 데이터 기반 고령화 정도 분석

```python
import pandas as pd

df = pd.read_csv("./data/seoul_population.csv")

df["노인인구비율"] = (df["70대"] + df["80대"] + df["90대 이상"]) / df["총인구수"]

def ratio(x):
  if x >= 0.14:
    return "O"
  else:
    return "X"

df["고령여부"] = df["노인인구비율"].apply(ratio)

print(df)
```

### (자율실습)그룹으로 묶기

```python
import pandas as pd

def main():
  df = pd.DataFrame(
    {
      "class": ["A", "B", "C", "A", "B", "C"],
      "Korean": [100, 96, 94, 92, 90, 86],
      "Math": [85, 88, 91, 94, 97, 100],
    }
  )
  print("DataFrame:")
  print(df, "\n")

  group1 = df.groupby("class")

  print(group1.sum())
```

### (자율실습)펭귄 데이터 그룹화하기

```python
import pandas as pd

df = pd.read_csv('penguins.csv')

cols = input().split(',')

if len(cols) == 1:
  result = df.groupby(cols).mean(numeric_only = True)
else:
  result = df.groupby([cols[0], cols[1]]).mean(numeric_only = True)

print(result)
```

### (자율실습)인도 IT 시장 점유율 확인하기

```python
import pandas as pd

df = pd.read_csv('india_shares.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

col = input()

df = df.groupby(col).mean(numeric_only = True)

print(df)
```

### (자율실습)함수로 데이터 처리하기

```python
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5), columns=["Num"])
print(df, "\n")

def square(x):
    return x ** 2

df["Square"] = df["Num"].apply(square)

df["Square"] = df["Num"].apply(lambda x : x ** 2)
```

### (자율실습)타이타닉 데이터 요약

```python
import pandas as pd

DATA_PATH = "train.csv"

def main():
  df = pd.read_csv(DATA_PATH)
  df.info()
  print(df.head())
  print(df.describe())
  print(df['Survived'].value_counts())

if __name__ == "__main__":
    main()
```

### (자율실습)당뇨 데이터 변환

```python
import pandas as pd
import sys

def load_csv(path: str):
  df = pd.read_csv(path)
  return df

def categorize_bmi(bmi: str) -> int:
  if bmi <= 18.5:
    return 0
  elif bmi > 18.5 and bmi <= 23.0:
    return 1
  elif bmi > 23.0 and bmi <= 25.0:
    return 2
  else:
    return 3

def bmi_to_categorical(data: pd.Series) -> pd.Series:
  new_series = data.apply(categorize_bmi)
  return new_series

def main():
  DATA_PATH = "data/diabetes.csv"
  df = load_csv(DATA_PATH)
  df["BMI"] = bmi_to_categorical(df["BMI"])
  print(df["BMI"])
  return 0

if __name__ == "__main__":
  sys.exit(main())
```
