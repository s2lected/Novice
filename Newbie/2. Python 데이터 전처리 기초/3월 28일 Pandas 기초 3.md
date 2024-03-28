## 01 데이터 정제하고 병합하기
### [강의자료] 데이터 정제하고 병합하기
* 데이터 정제

  원본(Raw) 데이터는 불완전하거나 부정확한 경우가 많음

  데이터가 누락되어 있거나, 잘못된 값이 포함되어 있는 경우 등 다양한 문제가 존재

  데이터를 제거하거나 대체하는 등 다양한 정제과정이 필요

* 데이터 정렬: sort_values()

  데이터프레임의 특정 컬럼의 값을 기준으로 전체 제이터를 정렬할 때 사용

```python
df.sort_values("컬럼이름", ascending = True 또는 False) #ascending이 True면 오름차순, False면 내림차순 (생략되어 있으면 기본값인 True)
```

* 인덱스 재지정: reset_index()

  데이터프레임의 인덱스를 처음부터 다시 지정해줄 때 사용

  데이터프레임을 정렬하는 등의 작업을 하다 보면 index가 뒤섞이게 되는데, 이 때 reset_index()를 활용하여 인덱스 초기화

```python
df.reset_index() #index가 초기화 되면서 기존의 index를 저장한 "index"컬럼이 생김
df.reset_index(drop = True) #기존의 index는 제거되고 새로운 index로 대체
```

* 데이터 삭제: drop()

  데이터프레임에서 특정 행이나 열을 삭제할 때 사용

```python
df.drop("행/열이름", axis = 0 또는 1) #0이면 행 삭제, 1이면 열 삭제
```

* 열 이름 바꾸기: rename()

  데이터프레임의 특정 열 이름을 바꾸는데 사용할 때 사용

```python
df.rename(columns = {"바꿀칼럼이름" : "새컬럼이름"}) #dictionary 형식으로 사용
```

* 결측치 탐색: isnull()

  데이터프레임의 각 원소가 결측치인지 여부를 True/False로 반환할 때 사용

  sum()과 함께 사용하여 각 컬럼별로 결측치가 몇 개 존재하는지 확인하는 용도로 사용

```python
df.isnull().sum() #False는 이상없음, True는 결측치를 의미, 특정 컬럼만 탐색 가능
```

* 결측치 채우기: fillna()

  데이터프레임 내의 결측치를 다른 값으로 대체하기 위해 사용

```python
df["청소년"] = df["청소년"].fillna(int(df["청소년"].mean())) #특정 값이나 수식을 채워서 재할당을 해주어야 
```

* 결측치 데이터 삭제하기: dropna()

  데이터프레임 내의 결측치가 포함된 행을 삭제하는데 사용

```python
df.dropna(subset = "컬럼이름", ignore_index = True 또는 False)
#subset: 특정 컬럼에 결측치를 존재하는지를 검사 (생략 시 전체 컬럼)
#ignore_index: True면 결측치가 존재하는 행이 삭제된 데이터프레임의 인덱스 초기화, False면 그대로(기본값은 False)
```

* 데이터 병합

  데이터가 여러 개로 분산되어 있거나, 추가 데이터를 합치고 싶은 경우

  데이터 병합을 통해 데이터의 일관성을 유지하고 분석 결과의 신뢰도를 높일 수 있음

* 데이터 합치기: concat()

  공통의 컬럼을 가지는 데이터프레임을 합치는데 사용

```python
pd.concat([데이터프레임1, 데이터프레임2], axis = 0 또는 1, join = 'inner' 또는 'outer', ignore_index = True 또는 False)
#axis가 0이면 위아래로, 1이면 좌우로 합침 (기본값은 0)
#join이 'outer'이면 칼럼을 합집합으로, 'inner'이면 교집합으로 처리 (기본값은 outer)
#ignore_index가 False면 원본 데이터프레임의 인덱스를 유지, True면 기존의 인덱스를 무시하고 새로운 인덱스를 부여 (기본값은 False)

df_concat = pd.concat([df, df2], axis = 0, join = 'inner', ignore_index = True)
```

* 데이터 합치기: merge()

  특정 컬럼을 기준으로 합치는데 사용

  on은 데이터프레임을 합칠 때 기준(key)이 되는 컬럼의 이름

  how는 데이터프레임의 데이터(행)를 합치는 방법으로 4가지 방법이 존재

```python
pd.merge(데이터프레임1, 데이터프레임2, on = "컬럼이름", how = 'inner' 또는 'outer' 또는 'left' 또는 'right')
#inner: 두 데이터프레임에 모두 존재하는 데이터만 (교집합)
#outer: 두 데이터프레임의 모든 데이터 사용 (합집합)
#left: 데이터프레임1에 있는 모든 데이터
#right: 데이터프레임2에 있는 모든 데이터
```

* 참고: 판다스 docs 확인

  https://pandas.pydata.org/docs/

### [실습1] 데이터 정제하기
결측치(Missing Value): 값이 없는 것

1. NaN (Not a Number): 숫자가 아님
2. Null: 아무것도 존재하지 않음
3. Na (Not Available): 유효하지 않음

* 데이터 불러오기

```python
import pandas as pd
df=pd.read_csv("./data/seoul_park03.csv")
mm=pd.read_csv("./data/misemunji.csv")
```

* 데이터 정렬: sort_values

  먼저 데이터를 정렬해서 사용하는 방법에 대해 알아보겠습니다.

  현재의 데이터는 시간의 순서대로 기록되어 있는데, 특정 상황에서는 입장객 수에 따라서 정렬을 하면 사용이 용이한 경우가 많습니다.

  이럴 때 우리는 sort_values()를 사용할 수 있습니다.

  sort_values()는 특정 컬럼의 값을 기준으로 전체 데이터를 오름차순 혹은 내림차순으로 정렬합니다.

  입장객 수가 많은 순서를 알아보기 위해 "총계" 컬럼을 기준으로 내림차순으로 정렬해보도록 하겠습니다.

```python
df_sorted=df.sort_values("총계", ascending=False) #데이터를 확인하기 위해 정렬한 데이터프레임을 df_sorted에 저장
df_sorted.head(10) #입장객수가 많았던 날짜의 데이터 상위 10개 출력
```

  입장객 수가 많았던 순서대로 정렬해보니 데이터가 집계된 기간의 어린이날들이 모두 최상위권에 위치해 있어 어린이날의 위엄을 알 수 있습니다.
  
  이는 단순히 어린이날이라는 이유 뿐 만 아니라, 서울대공원의 경우 어린이날 당일에는 13세 미만 어린이들에게 무료 개방을 하고 있기 때문입니다.
  
  이러한 정보를 통해 어린이날의 "어린이" 컬럼의 값이 비정상적으로 낮고 "무료합계" 컬럼이 높은 이유 또한 알 수 있습니다.

  또한 전부 공휴일인 것은 모두가 예상하신대로 일 것이고, 어린이날을 제외한 상위권을 살펴보면 2016년 6월 5일은 다음날이 공휴일인 일요일, 2017년 4월 8일과 9일은 서울대공원 벚꽃축제, 2017년 4월 23일은 서울대공원 겹벚꽃 원더풀 데이 축제 날짜였습니다.
  
  이렇게 특정 이벤트가 있는 날짜의 입장객 수가 평범한 날들에 비해 월등히 높은 것을 알 수 있습니다.
  
  이번에는 입장객 수 하위 10개 데이터를 살펴보겠습니다.

```python
df_sorted.tail(10)
```

  하위 2개 데이터는 폐쇄 후 재개장을 위한 테스트로 추정되기 때문에 제외하고, 나머지 데이터를 살펴보면 일단 전부 공휴일이 아니라는 것을 알 수 있습니다.
  
  최하위권에 2018년 1월 24일부터 25일까지가 위치해있는데, 날씨가 맑음임에도 불구하고 아무리 평일이라도 입장객 수가 지나치게 낮은 것을 확인할 수 있습니다.
  
  이유를 알아보면 해당 일차의 날씨 자체는 맑음이 맞지만 강렬한 한파로 인해 서울의 최저기온이 영하 18도까지 내려갔던 기간이었습니다.
  
  이렇게 데이터를 정렬하면 추가 정보를 얻을 수 있고, 데이터 분석의 방향을 결정할 수도 있습니다.

* 인덱스 재지정: reset_index

  이런식으로 데이터를 정렬하여 데이터를 사용하다보면 한 가지 문제가 발생합니다.

  다시 df_sorted를 살펴보시면 데이터는 "총계"컬럼에 맞춰서 정렬되었지만 이 과정에서 기존의 인덱스를 그대로 가지고 정렬된 사실을 확인할 수 있습니다.

  이렇게 될 경우 앞서 배웠던 loc 등을 활용하기가 어렵기 때문에, 이 데이터를 가지고 계속 데이터 분석을 할 예정이라면 인덱스를 재정렬해줄 필요가 있습니다.

  이 때 우리는 reset_index()를 활용합니다.

```python
df_sorted.reset_index(drop = True) #drop을 True로 지정해주어 "index"컬럼 생성 안함
```

  df_sorted의 인덱스가 깔끔하게 재정렬된 것을 확인할 수 있습니다.

  이렇게 인덱스 재지정은 지금처럼 데이터를 정렬하거나, 일부 데이터를 삭제하는 등의 작업을 통해 인덱스가 흐트러졌을 때 수행해주면 유용한 작업입니다.

* 데이터 삭제: drop

  데이터에는 다양한 정보가 저장되어 있지만, 데이터분석 목적에 따라 크게 중요하지 않은 정보들이 있을 수 있습니다.

  가령 서울대공원 데이터를 다시 살펴보면 "유료합계" 컬럼과 "무료합계" 컬럼은 입장객 수를 분석하는 데에 있어서 크게 중요하지 않습니다.

  이런 경우 해당 컬럼을 drop()을 활용하여 삭제하여 좀 더 깔끔하고 명확한 데이터를 분석하는데 활용할 수 있습니다.

  "유료합계"와 "무료합계" 컬럼을 삭제하여 df에 덮어씌우는 과정은 다음과 같습니다.

```python
df = df.drop(["유료합계", "무료합계"], axis = 1) #axis = 1로 설정하여 컬럼을 삭제
df.drop(df[df["날씨"] == "구름 많음"].index, axis = 0) #'.index'를 사용하면 해당 행의 인덱스 이름을 받아올 수 있음
df[df["날씨"] != "구름 많음"] #'구름 많음'이 아닌 행만 선택을 하기 때문에 해당 행이 없어지는 효과
```

  필요 없는 컬럼이 삭제되어 좀더 깔끔한 데이터가 된 것을 확인할 수 있습니다.

* 열 이름 바꾸기: rename

  떄로는 데이터의 컬럼이름이 잘못 설정되어있거나, 알아보기 어렵게 설정되어있는 경우가 있습니다.

  이런 경우 rename()을 활용해 컬럼의 이름을 바꿀 수 있습니다.

  서울대공원 데이터에서 "총계" 컬럼의 경우 총 관람객 수를 의미한다는 것을 유추할 수 있지만, 좀 더 명확하게 "총계" 컬럼의 이름을 "총입장객수" 로 바꿔보도록 하겠습니다.

```python
df = df.rename(columns = {"총계": "총입장객수"})
a = df.columns.tolist() #a라는 변수에 컬럼명을 리스트로 저장
```

  컬럼의 이름이 "총입장객수" 로 바뀐것을 확인할 수 있습니다.

* 결측치 처리

  우리가 실습에서 사용하고 있는 데이터는 실제 서울대공원의 입장객 수를 기록한 데이터입니다.

  그런데 실제로 데이터를 수집하다보면 다양한 문제가 야기됩니다. 앞서 처리했던 표기의 문제도 있었고, 데이터 자료형의 문제도 있었습니다.

  그리고 또 다른 문제로는 데이터의 누락이 있습니다. 오랜 기간 데이터를 수집하다보면 데이터가 수집되지 않는 경우들이 발생할 수 있습니다.

  데이터의 갯수를 보면 대부분의 컬럼이 1086개의 데이터를 가지고 있지만 "날씨" 컬럼과 "청소년" 컬럼의 데이터가 부족한것을 확인할 수 있습니다.

  잘보면 데이터의 갯수가 Non-Null Count라고 되어있는데, 즉 "날씨" 컬럼과 "청소년" 컬럼에는 Null이 존재한다는 뜻입니다.

  이 Null이 어떻게 생겼는지는 데이터프레임에서 확인할 수 있습니다.

  **entries (전체 행의 개수) - Non-Null Count (값이 있는 행의 개수) = Null**

  2016년 1월 4일의 데이터의 "청소년" 컬럼을 확인하면 NaN(Not a Number)라고 되어있습니다.

  이는 0이 아니라 아예 공백, 즉 수집되지 않아서 어떤 값인지 알 수 없는 데이터입니다. 이런 값들을 결측치 라고 합니다.

  당연한 얘기지만, 이런 결측치들은 데이터 분석이나 인공지능 적용 과정에서 걸림돌로 작용합니다. 이제부터 이 결측치를 처리하는 방법을 배워보겠습니다.

* 결측치 탐색: isnull()

  먼저 결측치가 얼마나 존재하는지 알아보기 위해 isnull()을 활용합니다.

  물론 앞서 봤듯이 info()를 활용해서도 알 수 있지만, isnull()을 활용하면 추가적인 계산 필요 없이 직관적으로 어떤 컬럼에 몇 개의 결측치가 존재하는지 확인할 수 있습니다.

  먼저 데이터프레임에 isnull()을 적용해보겠습니다.

  isnull()은 데이터프레임의 각 원소가 결측치인지 아닌지를 검사합니다. 결측치가 아닌 제대로된 값은 False, 결측치는 True로 채워진것을 확인할 수 있습니다.

  하지만 저 표를 가지고는 결측치가 컬럼별로 몇개인지 확인할 수가 없습니다.

  이 때 True는 1로, False는 0으로 계산되어 sum()을 활용해서 각 컬럼별로 전체값의 합을 구하면 결과값은 컬럼에 존재하는 True의 갯수, 즉 결측치의 갯수가 됩니다.

```python
df.isnull().sum()
```

  "날씨" 컬럼에 140개, "청소년" 컬럼에 5개의 결측치가 있는 것을 알 수 있습니다.
  
  이렇게 결측치의 갯수를 파악하는 것은 결측치를 어떻게 처리할지 방법을 결정하는데에 중요합니다.
  
  결측치를 처리하는 방법은 대표적으로 2가지가 있습니다. 하나는 결측치를 특정 값으로 채워넣는 것이고, 하나는 결측치가 존재하는 데이터를 삭제하는 것입니다.

* 결측치 채우기: fillna()

  먼저 결측치를 채워넣는 방법에 대해 알아보겠습니다.

  fillna()는 결측치를 특정 값으로 채워넣는데 활용하는 메서드로, 어떤 값으로 채워넣는지는 다양한 방법을 사용합니다.

  이번 실습에서는 "청소년" 컬럼의 결측치를 전체 데이터의 청소년 입장객의 평균값으로 채워보도록 하겠습니다.

```python
df["청소년"].fillna(int(df["청소년"].mean()))
#결측치를 평균이나 중앙값으로 하면 통계값이 크게 튀지 않는 효과
#mean 함수는 결측치가 제외된 데이터로 계산
```

  원래는 결측치였던 2016년 1월 4일의 청소년 데이터가 463명이라는 펑균값으로 채워진것을 확인할 수 있습니다.
  
  물론 이 값이 정확한 값이라고는 할 수 없지만, 최대한 확률이 높은 값으로 채워넣었다고 생각하면 됩니다.

* 결측치 데이터 삭제하기: dropna()

  결측치가 많지 않을 경우, 결측치가 있는 데이터를 삭제해버리는 것도 좋은 방법입니다.

  가령 청소년 컬럼에서 결측치가 있는 데이터를 삭제하면 5일치의 데이터가 사라지는 것입니다.

  이는 전체 기간 1086일의 데이터에서 비중이 크지 않기 때문에 괜찮은 방법이 될 수도 있습니다.

  이럴 때 dropna()를 활용하면 알아서 기준 컬럼에서 결측치를 탐사하고 해당하는 데이터를 삭제합니다.

```python
df.dropna(subset = "청소년")
```

  이번에는 "청소년" 컬럼에 결측치가 있었던 2016년 1월 4일의 데이터가 아예 삭제된 것을 확인할 수 있습니다.
  
  이렇게 결측치를 처리하는 방법은 다양하지만, 이번 강의에서는 이후 강의진행의 편의성을 위해 결측치를 채워넣는 방식으로 df를 변형하도록 하겠습니다.

```python
df["청소년"] = df["청소년"].fillna(int(df["청소년"].mean())) #원하는 컬럼의 결측치만 채워넣어야 함, 전체 데이터프레임에 적용하면 잘못된 데이터가 채워짐
df[df["청소년"].isna()] #청소년 컬럼에서 null 값이 있는 데이터를 검색
df[df.isna().any(acix = 1)] #전체 컬럼 중에 null 값이 있는 모든 데이터를 검색
```

### [실습2] 데이터 정제하기
데이터 병합은 여러 개의 데이터셋을 하나로 합치는 과정을 말합니다.

여러 개의 데이터셋이 각각 다른 정보를 담고 있을 때 이 데이터들을 합치면 데이터의 크기를 늘리거나 종합적인 정보를 얻을 수 있습니다.

* 데이터 불러오기

```python
import pandas as pd
df = pd.read_csv("./data/seoul_park04.csv")
df.head()
```

* 데이터 병함: concat()

  먼저 데이터 확장을 위해 기존의 서울대공원 입장객 데이터에 이후 기간 데이터를 병합하는 과정을 알아보도록 하겠습니다.

  실습에 활용하고있는 서울대공원 입장객 데이터는 2019년 3월 31일까지의 데이터가 담겨 있습니다.

  이 데이터의 뒤에 2019년 4월 한달간의 데이터를 불러와서 합치면 2016년 1월 1일부터 2019년 4월 30일까지의 데이터를 만들 수 있습니다.

```python
df2 = pd.read_csv("./data/seoul_park_april.csv")
df2.head()
```

  concat()을 활용하면 두 개 이상의 데이터프레임을 행 또는 열 방향으로 단순히 이어붙이는데 활용합니다.
  
  지금의 경우 2019년 3월 31일까지의 데이터인 df의 아래방향으로 2019년 4월의 데이터 df2를 이어붙이면 되기 때문에 concat()을 활용합니다.
  
  아래 방향으로 붙이기 때문에 axis를 0으로, 두 데이터프레임에 모두 존재하는 컬럼만을 남기기 위해 join을 inner로, 인덱스를 전체 초기화하기 위해 ignore_index를 True로 설정합니다.

```python
pd.concat([df, df2], axis = 0, join = 'inner', ignore_index = True)
```

  concat()을 활용하여 2016년 1월 1일부터 2019년 4월 30일까지의 데이터를 만들었습니다.
  
  이런식으로 데이터를 늘리면 더 긴 기간동안의 데이터를 분석할 수 있고 데이터 분석 결과의 정확도를 높일 수 있습니다.

* 데이터 병합: merge()

  데이터 병합은 정보의 종류를 늘리는데도 활용할 수 있습니다.

  서울대공원 데이터셋과 미세먼지 데이터셋을 합치면, 날씨 뿐 만 아니라 미세먼지 농도에 따른 입장객 수의 정보를 확인할 수도 있습니다.

  서울대공원 데이터셋과 같은 기간동안 수집된 미세먼지 데이터를 불러오도록 하겠습니다.

```python
mm = pd.read_csv("./data/misemunji.csv")
mm.head()
```

  2016년 1월 1일부터 2019년 3월 31일까지의 서울대공원 입장객 데이터에 2016년 1월 1일부터 2019년 3월 31일까지의 미세먼지 데이터를 합쳐보도록 하겠습니다.
  
  merge()를 활용해서 데이터를 합칠 때에는 기준이 될 컬럼이 필요합니다.
  
  이번 경우에는 날짜를 기준으로 입장객수와 미세먼지 데이터간의 관계를 확인하기 위해 기준 컬럼인 on을 날짜로 하겠습니다.
  
  how는 데이터를 합치는 방법을 지정합니다. 데이터를 합치는 방법은 데이터 분석의 목적에 따라 달라지므로 각 방법을 선택하는 이유에 대한 이해가 필요합니다.
  
  우리의 관심사는 미세먼지에 따른 입장객의 수이기 때문에, 입장객 수 데이터가 없는 부분은 필요하지 않습니다.
  
  두 데이터의 수집 기간은 같지만, 서울대공원 입장객 데이터의 경우 조류독감으로 인해 폐쇄된 구간의 데이터가 없기 때문에 해당 기간의 미세먼지 데이터는 필요가 없습니다.
  
  따라서 입장객 수의 데이터가 존재하는 구간의 데이터만을 얻기 위해 how를 입장객 수 데이터, left에 맞춘 것입니다.
  
  (이번 실습의 경우 inner를 활용해도 같은 결과를 얻을 수 있습니다)

```python
pd.merge(df, mm, on = '날짜', how = 'left')
```

---
## 02 Pandas 기초 3 실습
### 꽃 종류 정렬

```python
import pandas as pd
flower = pd.read_csv('iris.csv')

row_start = int(input())
row_end = int(input())
column = input()

ans = flower.sort_values(column, ascending = True)

print(ans.iloc[row_start:row_end])
```

### 잭이 심은 콩나무 데이터 정렬하기

```python
import pandas as pd
tree_df = pd.read_csv("./data/tree_data.csv")

tree_df = tree_df.sort_values('height', ascending = False)

print(tree_df.head(5))
```

### 서울시 지역구별 혼인이혼 통계 데이터 병합

```python
import pandas as pd
df1 = pd.read_csv("./data/seoul_population.csv")
df2 = pd.read_csv("./data/seoul_marriage_divorce_data.csv")

df2.loc[10, '혼인'] = 1520
ans_df = pd.merge(df1, df2, on = '지역구', how = 'outer')

print(ans_df)
```

### 허리둘레 변환하기

```python
import numpy as np
import pandas as pd
info = pd.read_csv("waist.csv")

info = info.dropna()
info["허리둘레(inch)"] = np.nan
info["허리둘레(inch)"] = info["허리둘레"] / 2.54
info["허리둘레(inch)"] = info["허리둘레(inch)"].astype(int)
info_column_add = info

print(info_column_add)
```

### 부상자수 구하기

```python
import numpy as np
import pandas as pd
info = pd.read_csv("accident.csv")

info = info.dropna()
info["부상자수"] = np.nan
info["부상자수"] = info["중상자수"] + info["경상자수"] + info["부상신고자수"]
info["부상자수"] = info["부상자수"].astype(int)
info_column_add = info

print(info_column_add)
```

### BMI

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from elice_utils import EliceUtils

info = pd.read_csv("bmi.csv")
info = info.dropna()
info["BMI"] = np.nan
info["BMI"] = info["체중"] / ((info["신장"]/100) ** 2)
info["BMI"] = info["BMI"].astype(int)
info_column_add = info

print(info_column_add)
```

### 장르별 인기 있는 웹툰들 알아보기

```python
import pandas as pd
df = pd.read_csv("webtoon.csv")

def best(df, g):
  df = df[df["Genre"] == g].sort_values("Rating", ascending = False)
  first = df.iloc[0, 4]
  df = df[df["Rating"] == first]
  return df

print(best(df, "Romance"))
```

### 세계인의 축젯날

```python
import pandas as pd
df = pd.read_csv("result.csv")

def find(df, rank):
  gold = df[df['Medal'] == 'Gold']
  silver = df[df['Medal'] == 'Silver']
  bronze = df[df['Medal'] == 'Bronze']
  g = gold['Team'].value_counts()
  s = silver['Team'].value_counts()
  b = bronze['Team'].value_counts()
  ranks = pd.DataFrame({"Gold": g, "Silver": s, "Bronze": b})
  ranks = ranks.fillna(0).astype(int)
  result = ranks.sort_values(['Gold', 'Silver', 'Bronze'], ascending = False)
  return result.iloc[rank - 1]

print(find(df, 9))
```

### B라도 받자

```python
import pandas as pd
df = pd.read_csv("scores.csv")

def grade_B(df, score, n):
  result = df[df['total'] < score]
  result = result.sort_values('total', ascending = False)
  result = result.head(n)
  result = result.sort_values('name', ascending = True)
  b_student = result['name']
  return list(b_student)

print(grade_B(df, 75, 10))
```

### 사고의 피해에 따른 교통사고 유형 찾기

```python
import pandas as pd
df = pd.read_csv("accident.csv")

def danger(df, n):
  df["전체"] = df["사망자수"] + df["중상자수"] + df["경상자수"] + df["부상신고자수"]
  df["사고당피해"] = df["전체"] / df["사고건수"]
  df = df.sort_values("사고당피해", ascending = False)
  result = df.iloc[n - 1]
  return int(result['사망자수'] + result['중상자수'])

print(danger(df, 1))
```

### [미션] 서울시 아파트 실거래 데이터 분석

```python
import pandas as pd
import numpy as np
df = pd.read_csv("./data/seoul_apart_2022.csv")

df = df.drop(["해제사유발생일", "중개사소재지", "번지", "본번", "부번", "도로명", "거래유형"], axis = 1) #컬럼 삭제
df = df.rename(columns={"전용면적(㎡)":"전용면적"}) #컬럼명 특수문자 제거
df["구"] = df["시군구"].apply(lambda e: e.split()[1]) #구 split
df["동"] = df["시군구"].apply(lambda e: e.split()[2]) #동 split
def category(e):
  if e <= 60:
    return "소형"
  elif e <= 85:
    return "중형"
  elif e <= 102:
    return "중대형"
  else:
    return "대형"
df["유형"] = df["전용면적"].apply(category) #면적에 따라 아파트 유형을 분류
df["계약일"] = df["계약년월"].astype('str') + df["계약일"].astype(str) #계약년월 컬럼과 계약일 컬럼 합침
df["계약일"] = pd.to_datetime(df["계약일"], format='%Y%m%d') #날짜타입으로 변경
df["계약월"] = df["계약일"].dt.month #계약월 컬럼 생성
df["계약요일"] = df["계약일"].dt.dayofweek #계약요일 컬럼 생성
df["계약요일"] = df["계약요일"].map({0:'월', 1:'화', 2:'수', 3:'목', 4:'금', 5:'토', 6:'일'}) #숫자를 요일로 mapping
df.isnull().sum() #결측치 확인
df = df.dropna(subset = '거래금액(만원)', ignore_index = True) #결측치 삭제 후 index 초기화
df["거래금액(만원)"] = df["거래금액(만원)"].str.replace(",","") #천의 자리 콤마 제거
df["거래금액(만원)"] = pd.to_numeric(df["거래금액(만원)"]) #int type 변경
df.sort_values("거래금액(만원)", ascending = False) #내림차순 정렬

print("거래금액 평균값(만원): ", df["거래금액(만원)"].mean())
print("거래금액 중앙값(만원): ", df["거래금액(만원)"].median())

df["전용면적"] = round(df["전용면적"]/3.3, 2) #round(,2)는 소수점 두번째 자리에서 반올림
df = df.rename(columns={"전용면적":"전용면적(평)"})
df["평당금액"] = df["거래금액(만원)"] / df["전용면적(평)"] #평당금액 컬럼 생성
df["평당금액"] = round(df["평당금액"],2)
df.sort_values("평당금액", ascending = False)
df.groupby("구")[["평당금액"]].mean() #구별 평당금액 데이터
df1 = df[df['구'] == '서초구']
df2 = df1.groupby(['동'])['평당금액'].mean()
df2.sort_values(ascending = False)
ans1 = '잠원동'

print(ans1)
```

### (자율실습)데이터 변환

```python
import pandas as pd
import numpy as np


KOR_COL_NAME = {"name": "이름", "age": "나이", "adult": "성인여부"}


def add_adult(df: pd.DataFrame) -> pd.DataFrame:
    """df에서 age값을 기준으로 성인여부를 의미하는 adult칼럼을 추가합니다."""
    def check(x):
        if x >= 18:
            return True
        else:
            return False
    df["adult"] = df["age"].apply(check)
    return df

def rename_kor(df: pd.DataFrame) -> pd.DataFrame:
    """df의 칼럼 이름을 KOR_COL_NAME를 이용해 한국어로 변경합니다."""
    df = df.rename(columns = {df.columns[0]:KOR_COL_NAME["name"], df.columns[1]:KOR_COL_NAME["age"], df.columns[2]:KOR_COL_NAME["adult"]})
    return df


def main():
    data = pd.DataFrame()
    data["name"] = ["James", "John", "Sarah", "Michael"]
    data["age"] = [19, 20, 18, 31]

    # 1. 성인 여부 칼럼을 추가
    df = add_adult(data)
    print(df)

    # 2. 칼럼이름을 한국어로 변환
    df = rename_kor(df)
    print(df)


if __name__ == "__main__":
    main()
```

### (자율실습)데이터 정제

```python
import pandas as pd
import numpy as np


def print_info(df: pd.DataFrame) -> pd.DataFrame:
    "이상치와 결측치의 수를 화면에 표시합니다."
    print("결측치:", df.score.isna().sum())
    print("이상치:", len(df[df["spent_time"] > 3600]))


def replace_spent_time(df: pd.DataFrame) -> pd.DataFrame:
    """df의 spent_time값이 3600보다 크다면 3600으로 치환합니다."""
    df[df['spent_time'] > 3600] = 3600
    return df


def fill_score(df: pd.DataFrame) -> pd.DataFrame:
    "df의 score값이 NaN이면 0으로 치환합니다."
    df["score"] = df["score"].fillna(0)
    return df


def main():
    DATA_PATH = "test_log.csv"

    df_log = pd.read_csv(DATA_PATH)
    print("==수정전==")
    print_info(df_log)

    # 1. 이상치 대체하기
    df_log = replace_spent_time(df_log)

    # 2. 결측치 대체하기
    df_log = fill_score(df_log)

    print("==수정후==")
    print_info(df_log)


if __name__ == "__main__":
    main()
```

### (자율실습)데이터 병합
```python
import pandas as pd


def concat_data(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    "df1, df2를 이어붙여 하나의 데이터 프레임을 만들어 반환합니다."
    df_new = pd.concat([df1, df2], axis = 0, join = 'inner')
    df_new = df_new.reset_index(drop = True)
    return df_new


def merge_data(df_log: pd.DataFrame, df_name: pd.DataFrame) -> pd.DataFrame:
    "df_log와 df_name에 공통으로 존재하는 값인 student_id를 기준으로 병합하고 반환합니다."
    df_new = pd.merge(df_log, df_name, on = 'student_id', how = 'inner' )
    return df_new


def main():
    CLASS1_PATH = "class1.csv"
    CLASS2_PATH = "class2.csv"
    NAME_PATH = "name.csv"

    # 데이터 불러오기
    df_class1 = pd.read_csv(CLASS1_PATH)
    df_class2 = pd.read_csv(CLASS2_PATH)
    df_name = pd.read_csv(NAME_PATH)

    # 1. 모든 반의 데이터 합치기
    df_all = concat_data(df_class1, df_class2)
    print(df_all)

    # 2. 학생의 이름 데이터 병합하기
    df_merged = merge_data(df_all, df_name)
    print(df_merged)


if __name__ == "__main__":
    main()
```

---
