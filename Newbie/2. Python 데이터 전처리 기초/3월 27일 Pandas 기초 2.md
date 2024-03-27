## 01 데이터 추출하기
### [강의자료] 데이터 추출하기
* 데이터 추출

  원하는 구간, 조건에 해당하는 데이터를 추출해야 할 때 사용

  데이터 분석 결과를 얻기 위해, 적절한 데이터를 선택하고 추출하기 위해 필요한 과정

* 참고: pandas 논리연산자

  and → &

  or → |

  not → ~

  소괄호 ()를 사용하여 우선 순위 명시

* 조건에 따른 인덱싱: Boolean indexing

  비교 연산자나 논리 연산자를 사용하여 데이터프레임에서 조건에 맞는 행 추출 가능

* 복잡한 조건을 활용한 Boolean indexing

  pandas 논리연산자를 활용하면 복잡한 조건을 추가할 수 있음

* 라벨을 활용한 데이터 추출: loc

  라벨을 사용하여 데이터프레임에서 데이터를 추출하는 방법
  
  인덱스이름과 컬럼이름을 입력 받아 그에 해당하는 데이터 추출

  **df.loc["인덱스이름", "컬럼이름"]** → 1개인 경우, 컬럼이름만 / 여러개인 경우, 대괄호로 묶어서 입력

* loc과 Boolean indexing을 활용한 데이터 추출

  loc에서 "인덱스이름"에 Boolean indexing을 활용하면 조건에 맞는 데이터 추출 가능

* 순서를 활용한 데이터 추출: iloc

  행과 열의 위치(순서)를 이용해 데이터를 추출할 때 사용

  행이나 열의 위치(순서)를 나타내는 **정수**를 입력 받아 해당 데이터 추출

  **df.iloc[행의 위치, 열의 위치]** → iloc에서 슬라이싱을 할 때는 python과 동일한 logic / 거꾸로 슬라이싱 할 때 (첫번째:마지막:step(-1))

* loc vs iloc

  loc은 index 이름을 활용, iloc은 정수형 위치(순서)를 활용하여 인덱싱

* loc과 iloc을 활용한 값 변환

  loc과 iloc을 활용하여 특정 원소 값 변환 가능

  loc과 iloc을 활용해 바꿀 위치를 지정하고 해당 위치에 넣을 값을 지정

### [실습1] 데이터 추출하기
* 데이터 불러오기
```python
import pandas as pd
df=pd.read_csv("./data/seoul_park03.csv")
mm=pd.read_csv("./data/misemunji.csv")
```
* 조건에 따른 인덱싱: Boolean indexing

  전체 데이터프레임에서 Boolean indexing을 통해 특정 조건에 맞는 데이터를 추출할 수 있습니다.

  예를 들어 어른 입장객 수가 5000보다 큰 날짜들의 데이터를 추출하려면 다음과 같이 코드를 작성할 수 있습니다.

```python
df[df["어른"] > 5000]
```

  Pandas 논리연산자를 활용하면 좀 더 복잡하게 조건을 설정할 수 있습니다.

  두 개 이상의 조건을 and('&')나 or('|')을 활용하여 같이 사용하는데, 이 때 각 조건식은 소괄호로 묶여있어야 합니다.

  어른 입장객의 수가 10000명이 넘는 공휴일의 데이터만을 추출하려면 and('&') 연산자를 활용해 다음과 같이 추출할 수 있습니다.

```python
df[(df["어른"] > 10000) & (df["공휴일"] == "O")]
```

  이번에는 or(|)연산자를 활용해 어른 입장객의 수가 10000명이 넘거나 어린이 입장객 수가 2000명이 넘는 날짜의 데이터를 추출해보도록 하겠습니다.

```python
df[(df["어른"] > 10000) | (df["어린이"] > 2000)]
```

* 라벨을 활용한 데이터 추출: loc

  우리가 일반적으로 데이터프레임에서 원하는 데이터를 추출한다고 가정해봅시다.

  가령 2016년 1월 4일의 어른 입장객 데이터를 알고싶은 경우, 데이터프레임을 쭉 보면서 2016년 1월 4일의 행을 찾고, 그 행에서 "어른" 열을 찾아 그 값을 확인합니다.

  loc은 이러한 데이터 탐색 및 추출과정을 활용한 데이터 추출 메서드입니다.

  입력받은 데이터의 행과 열의 인덱스를 활용하여 그 위치에 해당하는 데이터를 추출합니다.

  여기서 유의할 점은 우리가 사용하고있는 데이터의 행 인덱스는 날짜가 아니라 인덱스 숫자입니다.

  2016년 1월 4일 데이터의 인덱스값은 3이므로, loc을 사용하여 2016년 1월 4일의 어른 데이터를 추출하려면 다음과 같이 사용할 수 있습니다.

```python
df.loc[3, '어른']
```

  연속적인 객체(데이터프레임의 인덱스) 범위를 지정해 가져오는 방법인 슬라이싱을 활용하면 범위를 지정하여 해당 범위에 해당하는 데이터들을 불러올 수도 있습니다.

  이 때 유의할 점은, loc은 라벨 기반 인덱싱을 사용하기 때문에 A:B로 슬라이싱을 하면 A 부터 B까지, 즉 B포함한 범위를 인덱싱 한다는 점입니다.

  예를들어 3:6 의 범위를 지정한다면 인덱스가 3부터 6까지인 데이터, "어른":"외국인" 의 범위를 지정한다면 "어른"부터 "외국인" 까지의 데이터를 지정하게 됩니다.

  또한 이렇게 슬라이싱을 활용해 추출한 데이터들은 복수의 데이터이므로, 시리즈 혹은 데이터프레임 형태라는 사실을 알아두면 좋습니다.

* loc과 Boolean indexing을 활용한 데이터 추출

  앞서 배웠던 Boolean indexing처럼 조건식과 논리연산자를 loc과 같이 활용하면 조건에 맞는 데이터들만을 추출할 수 있습니다.

  예를 들어 다음과 같이 어른과 어린이의 입장객 수가 둘다 1000보다 큰 날짜의 "날짜"부터 "총계" 행을 추출할 수 있습니다.

```python
df.loc[(df['어른'] > 1000) & (df['어린이'] > 1000), "날짜" : "총계"]
```

* 순서를 활용한 데이터 추출: iloc

  다음으로 행과 열의 정수 위치를 이용해 데이터를 추출하는 iloc에 대해 알아보겠습니다.

  앞서 loc이 행과 열의 이름을 좌표로 삼아 해당 위치의 데이터를 추출했다면, iloc은 행과 열의 정수형 위치, 즉 순서를 좌표로 삼아 해당 위치의 데이터를 추출합니다.

  예를 들어 4번 행(2016년 1월 5일)의 7번 열(외국인) 데이터를 추출하면 다음과 같습니다.

```python
df.iloc[4, 7]
```

  iloc 역시 슬라이싱을 활용하여 지정한 범위의 데이터를 추출할 수 있습니다.

  여기서 loc과의 중요한 차이점이 있는데, iloc은 위치 기반 인덱싱을 사용하여 범위를 지정하기 때문에 시작은 포함되고 끝은 포함되지 않습니다.

  즉 iloc에서 A:B로 슬라이싱을 하면 A부터 B-1까지, 즉 B를 포함하지 않는 범위를 인덱싱합니다.

  B를 포함해서 인덱싱하는 loc과는 다르기 때문에 코드를 작성하거나 해석할 때 유의하셔야 합니다.

  iloc을 활용해서 인덱싱을 3~6번 행, 4~6번 열의 값을 추출하면 다음과 같습니다.

```python
df.iloc[3:7, 4:7]
```

  iloc은 정수 위치를 사용하기 때문에 단순한 작업보다는, for문 등을 활용한 반복작업시에 매우 유용하게 활용할 수 있습니다.

  loc과 iloc을 활용하면 특정 위치에 해당하는 데이터 값을 추출할 수도 있고, 그 값을 다른 값으로 바꿔넣을 수도 있습니다.

  예를 들어 2016년 1월 5일의 "청소년" 컬럼 값을 확인해보겠습니다.

```python
df.loc[4, "청소년"]
```

  만약 이 값을 다른 값으로 바꿔주고 싶다면 loc이나 iloc을 활용해 값을 불러온 다음, 바꿔줄 값을 =을 활용해 저장해주면 됩니다.

```python
df.loc[4, "청소년"] = 100
```

---
## 02 Pandas 기초 2 실습
### 조건에 맞는 데이터 조회

```python
print(df[df['국어'] >= 70])
```

### 여러 조건에 맞는 데이터 조회

```python
print(df[(df['국어'] >= 70) & (df['수학'] < 80)])
```

### 데이터 프레임 슬라이싱 (loc)

```python
print(country.loc["japan":"usa"])
```

### 데이터 프레임 슬라이싱 (iloc)

```python
print(country.iloc[0:2])
```

### 다이어트 실험 조건 분석

```python
print(ex[ex[col] == con].head(20))
```

### 독버섯일 확률 알아보기

```python
import pandas as pd
df = pd.read_csv("mushrooms.csv")

def ratio(df, shape, color):
	total = df[(df['cap-shape'] == shape) & (df['cap-color'] == color)]
	poison = total[total['class'] == 'poisonous']
	return int(100 * len(poison) / len(total))

print(ratio(df, "convex", "red"))
```

### 수면에 관한 설문 데이터 복사하기

```python
import pandas as pd
df = pd.read_csv("sleep.csv", index_col=0)

def sleep(df, name):
	person = df.loc[name, :]
	p = person['PhoneTime'] == df['PhoneTime']
	t = person['Tired'] == df['Tired']
	b = person['Breakfast'] == df['Breakfast']
	people = df[ p & t & b]
	yes = people[people['Enough'] == 'Yes']['Hours'].mean()
	no = people[people['Enough'] == 'No']['Hours'].mean()
	result = yes - no
	return abs(result)

print(sleep(df, "Wendy"))
```

### 수컷 펭귄 분석하기

```python
import pandas as pd
df = pd.read_csv("penguins.csv")

def total(df, s):
	answer = []
  df1 = df.dropna()
  df1 = df[(df['sex'] == 'MALE') & (df['bill_length_mm'] > s)]
  answer.append(len(df1))
  avg = df1['bill_depth_mm'].mean()
  answer.append(avg)
  return answer

print(total(df, 30))
```

### 펭귄 종이 서식하고 있는 섬의 개수

```python
import pandas as pd
df = pd.read_csv("penguins.csv")

def total(df, s):
	df1 = df[df['species'] == s]
	df1 = set(df1['island'])
	return len(df1)

print(total(df, "Adelie"))
```

### 맨해튼 내에서만 일어난 운행

```python
import pandas as pd
import numpy as np

info = pd.read_csv("taxis.csv")
new_info = info.dropna()
new_info = new_info[(new_info['pickup_borough'] == 'Manhattan') & (new_info['dropoff_borough'] == 'Manhattan')]
cal = pd.Series(new_info.groupby('payment')['distance'].mean())

print(new_info)
print(cal)
```

### (자율실습)데이터프레임 생성하고 데이터 수정하기

```python
import pandas as pd

df = pd.DataFrame({'메뉴명' : ['돌솥비빔밥', '제육볶음', '고등어구이', '낙지볶음', '김치찌개&달걀말이'], '가격(원)' : [13000, 15000, 16000, 16000, 21000], '주문횟수' : [14, 55, 21, 48, 30], '평균별점' : [3.3, 4.5, 4.7, 1.2, 4.9]})
avg_star = float(input())

if avg_star <= 5:
	df.loc[3, '평균별점'] = avg_star
  print(df[df['메뉴명'] == '낙지볶음'])
else:
  print('별점은 5점까지 입니다!')
```

---
## 03 다양한 데이터 연결하기 (JSON)
### [강의자료] 다양한 데이터 연결하기 (JSON)
1. 데이터 포맷과 데이터 파싱

   * 데이터 포맷

     "어플리케이션에서 서버" 또는 "시스템에서 다른 시스템으로" **데이터를 교환하거나 저장하기 위해서는 데이터를 구조화하고 표현하기 위한 규칙과 형식이 필요**

     데이터 포맷은 데이터를 쉽게 이해하고 해석할 수 있도록 정의된 규칙을 가지고 있으며 일반적으로 텍스트 기반으로 표현

     가장 자주 사용되는 포맷은 **JSON(JavaScript Object Notaion)**과 **XML(eXtensible Markup Language)**을 사용하고 있음

   * JSON (JavaScript Object Notation)

     키-값 쌍으로 이루어진 데이터를 전달 또는 저장하기 위해 사람이 사용할 수 있는 텍스트를 사용한 개방형 표준 포맷

     주로 웹 애플리케이션과 다양한 소프트웨어 간에 데이터를 전송하거나 저장하는 용도로 사용

     현재 프로그래밍 언어 대부분은 JSON 호환성을 지원하고 있음

     **JSON은 데이터 포맷일 뿐**이며 어떠한 통신 방법도 아니고 프로그래밍 문법도 아님 → 단순히 데이터를 표시하는 표현 방식

   * JSON 구조

     JSON은 키(Key)-값(Value) 쌍으로 이루어짐

     각 키는 문자열로 표현되며 키와 값은 콜론(:)으로 구분됨

     JSON은 다양한 데이터 타입을 지원 → 문자열(""), 숫자, 불리언, 객체({}), 배열([]), null

   * 데이터 파싱 (Data Parsing)

     데이터를 분석하고 원하는 정보를 추출하는 과정

     데이터 파싱은 데이터 분석, 데이터 마이닝 등 다양한 분야에서 사용됨

     정확한 데이터 파싱을 위해서는 데이터의 형식과 구조를 이해하고 그에 맞는 파싱 방법을 선택해야 함

3. Python으로 JSON 데이터 파싱하기

   * json 라이브러리
  
     Python 에는 json 라이브러리가 내장되어 있어 JSON 데이터를 처리할 수 있음

     내장 라이브러리이기 때문에 별도의 설치 과정이 필요 없음 → import json

     JSON 형식으로 된 문자열 또는 파일을 읽고 Python 객체(Dictionary or List type)로 만들어서 분석함

   * json.load

     JSON 파일 객체를 Python에서 사용할 수 있는 객체로 변환하는 함수

     JSON 파일을 읽기 때문에 with와 open을 함께 사용함

     파일 경로를 인자로 받음

```python
import json
with open('target.json', 'r') as json_file:
    parsed_data = json.load(json_file)
```

   * json.dump

     Python 객체를 JSON 파일 객체로 변환하는 함수

     JSON 파일을 생성하기 때문에 with와 open을 함께 사용함

     데이터 이름과 파일 경로를 인자로 받음

```python
import json
data = {'name' : 'elice', 'age' : 25}
with open('./create_file.json', 'w') as f:
  json.dump(data, f)
```

   * json.loads

     문자열로 표현된 JSON 데이터를 Python 객체로 변환하는 함수

```python
json_str = '{"employee" : {"id" : 123, "name" : "Queen", "department" : "HR", "skilles" : ["communication", "teamwork"]}}'
data = json.loads(josn_str)
```

   * json.dumps

     Python 객체를 문자열로 표현된 JSON 데이터로 변환하는 함수

```python
data = {'name' : 'Jhon', 'age' : 30}
json_string = json.dumps(data)
```

   * JSON to DataFrame

     Pandas 라이브러리를 사용하면 JSON 파일을 이용하여 데이터를 분석할 수 있음

   * DataFrame to JSON
  
     분석한 DataFrame을 JSON으로 저장할 수 있음

     Series 자료형은 JSON으로 저장할 수 없음

### [퀴즈1] JSON의 특징
* 다음 보기 중에서 JSON의 특징으로 옳지 않은 것을 고르세요.

  키(Key)-값(Value)의 쌍으로 이루어져 있음

  각 키(Key)는 문자열로 표현되며 키와 값은 콤마(,)로 구분됨 → 콜론(:)

  JSON은 다양한 데이터 타입을 지원하고 있음

  현재 프로그래밍 언어 대부분은 JSON 호환성을 지원하고 있음

### [퀴즈2] 데이터 파싱
* 다음 보기 중에서 데이터 파싱(Data Parsing)에 대한 정의에 해당하는 것을 고르세요.

  데이터를 분석하여 원하는 정보를 추출하는 과정

### [실습1] JSON 데이터 다루기
* JSON이란?

  JSON(JavaScript Object Notation)은 키-값 쌍으로 이루어진 데이터를 전달 또는 저장하기 위해 사람이 사용할 수 있는 텍스트를 사용한 개방형 표준 포맷

  주로 웹 애플리케이션과 다양한 소프트웨어 간에 데이터를 전송하거나 저장하는 용도로 사용

  JSON은 단순한 데이터 포맷일 뿐이며 어떠한 통신 방법도 아니고 프로그래밍 문법도 아님

1. JSON 데이터 구성

     JSON의 각 키(KEY)는 문자열로 표현되며 키와 값(VALUE)은 콜론(:)으로 구분

     JSON은 문자열, 숫자, 불리언, 객체, 배열, null 다양한 데이터 타입을 지원

2. JSON 데이터 예시

```python
{"employee": {"id": 123, "name": "Queen", "department": "HR", "skills": ["communication", "teamwork"]}}
```

* JSON 데이터 다루기

  데이터를 분석하고 원하는 데이터를 추출하는 과정을 데이터 파싱(Data Parsing) 이라 함

  예를 들면, 주행 중에 발생하고 json 타입으로 저장된 데이터에서 원하는 데이터를 추출하기 위해서는 데이터 타입에 맞는 파싱 방법이 필요

1. JSON Library

     Python 에는 json 라이브러리가 내장되어 있어 JSON 데이터를 처리할 수 있음

     내장 라이브러리이기 때문에 별도의 설치 과정이 필요 없음

     JSON 형식으로 된 문자열 또는 파일을 읽고 Python 객체(Dictionary or List type)로 만들어서 분석함

```python
import json #json 라이브러리 호출하는 방법
```

  2. json.load

     JSON 파일 객체를 Python에서 사용할 수 있는 객체로 변환하는 함수

     파싱된 데이터가 딕셔너리 형태일 경우, 기존의 딕셔너리 형태를 사용하는 것과 동일하게 사용할 수 있음

```python
with open('data/target.json') as json_file : #파일 주소를 open하면서 as로 이름 지정
  parsed_data = json.load(json_file) #python 변환하며 주소 할당
```

  3. json.dump

     Python 객체를 JSON 파일 객체로 변환하는 함수

```python
json_data_dic = {"name" : "elice", "age" : 25, "email" : "rabbit@elicer.com"} #python에서 dict 선언
with open("create_file1.json", "w") as f : #쓰기(w) 가능한 임의의 빈 파일 생성하고 f에 할당
  json.dump(json_data_dic, f) #python에서 선언한 dict를 f에 덤핑하여 저장

json_data_list = [{"name" : "elice", "age" : 25}, {"name" : "Queen", "age" : 47}, {"name" : "Carrot", "age" : 1}]
with open("create_file2.json", "w") as f :
  json.dump(json_data_list, f)
```

  4. json.loads

     문자열로 표현된 JSON 데이터를 Python 객체로 변환하는 함수

```python
str_json = '{"employee": {"id": 123, "name": "Queen", "department": "HR", "skills": ["communication", "teamwork"]}}'
loads_data = json.loads(str_json) #문자로 된 JSON 데이터를 바로 loads_data에 python 방식 할당
```

  5. json.dumps

     Python 객체를 문자열로 표현된 JSON 데이터로 변환하는 함수

```python
dic_data = {"employee": {"id": 123, "name": "Queen", "department": "HR", "skills": ["communication", "teamwork"]}}
dumps_data = json.dumps(dic_data) #dict type의 python 데이터를 문자열로 된 JSON 데이터로 할당
dumps_data2 = json.dumps(dic_data, indent = 4) #indent 인자를 추가하면 가독성이 좋음
```

### [실습2] JSON 데이터와 데이터프레임
* JSON to DataFrame

  Pandas 라이브러리를 사용하면 JSON 파일을 데이터프레임(DataFrame)으로 변환할 수 있음

  변환된 데이터프레임을 이용하면 다양한 데이터 분석 및 시각화 라이브러리가 이용 가능하여 효과적인 데이터 분석 가능

1. json.load로 불러오기

```python
import json
import pandas as pd

with open('data/target.json') as json_file :
  load_data = json.load(json_file)

dumps_data = json.dumps(load_data, indent = 4) #load한 json 데이터 dumps로 확인

load_df1 = pd.DataFrame(load_data)
```

2. pd.read_json 으로 읽기

```python
load_df2 = pd.read_json('data/target.json')
```
 
3. 불러온 데이터프레임으로 데이터 분석하기

```python
df = pd.DataFrame(load_data["employee"]) #employee에서 skill의 빈도수를 도출하는 간단한 데이터 분석을 진행
df_skills = df['skills'].explode() #DataFrame의 'skills' 열을 이용하여 각 기술을 별도의 행으로 분리
skills_frequency_df = df_skills.value_counts().reset_index() #각 기술의 빈도수 계산하고, index를 새로 부여
skills_frequency_df.columns = ['Skill', 'Frequency'] #열 이름을 명확하게 변경

import matplotlib.pyplot as plt #매트플롯 라이브러리
plt.figure(figsize=(10, 6)) #그래프의 사이즈 지정
plt.bar(skills_frequency_df['Skill'], skills_frequency_df['Frequency'], color='skyblue') #plt.bar(x축, y축, 색상)
plt.title('Frequency of Skills') #그래프의 제목
plt.xlabel('Skill') #x축의 라벨
plt.ylabel('Frequency') #y축의 라벨
plt.xticks(rotation=45) #x축에 있는 기술 이름을 회전시켜 가독성 상승
plt.tight_layout() #회전된 x축 라벨을 위해 레이아웃을 조정
plt.show() #그래프를 표시
```

* DataFrame to JSON

  Pandas 라이브러리에서 지원하는 to_json 함수를 사용하면 분석한 데이터프레임을 JSON으로 저장할 수 있음

  단, Series 자료형은 JSON으로 저장할 수 없음

1. 새로운 데이터 추가하기

```python
new_employee = [{"id" : 108, "name" : "King", "department" : "Developer", "skills" : ["leadership", "communication"]}, {"id" : 133, "name" : "KIM", "department" : "Marketer", "skills" : ["teamwork", "decisiveness"]}]
new_df = pd.DataFrame(new_employee)

df_concat = pd.concat([df, new_df], ignore_index=True) #새로운 행을 추가하는 함수
df_concat.to_json('employee_data.json', orient = "records") #to_json('파일명', '인자')

with open('employee_data.json') as employee_data : #employee_data.json 파일 읽어서 확인
  load_data = json.load(employee_data)

print(json.dumps(load_data, indent=4))
```

---
