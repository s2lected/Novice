## 01-1 리스트와 시퀀스 자료형
### [수업 자료] 리스트 : 모아모아 다모아
엑셀을 파이썬으로 가져오면 데이터프레임 형식으로 가져오기 때문에 리스트 형식이 중요

<리스트 특화함수>

list.append(d) : 맨 마지막에 원소 추가 (덧셈과 다르게 저장하는 기능까지 포함!)

list.insert(i,d) : 위치 지정해서 원소 추가 (오직 한 개만)

list.remove(d) : 원소 제거 (처음 나오는 원소)

list.pop(i) : 인덱스의 원소를 제거 후 그 원소를 출력

list.sort() : 숫자형은 오름차순, 문자열은 사전순

list.sort(reverse = True) : 숫자형은 내림차순, 문자열은 사전역순

<시퀀스 자료형>

문자열, 리스트[], 튜플()

* 순서가 있는 자료형
* 원소로 이루어져있음
* 중복되는 원소 허용
1. 인덱싱/슬라이싱 가능
2. 더하기 연산 가능
3. 곱하기 연산 가능
4. in 연산 가능 (원소 조회) : 문자열만 여러 원소 조회 가능
5. len 함수 사용 가능 (원소 개수)

<인덱싱, 슬라이싱 심화>
1. 음수 인덱스 : 뒤에서부터 -1번 인덱스
2. 공백 슬라이싱 : 처음부터/끝까지 가져올 때 앞/뒤 비워두기
3. 역슬라이싱 : [a:b:c]에서 c값에 -1을 넣어줌

---
## 01-2 리스트와 시퀀스 자료형 실습
### 선착순! 줄을~ 서시오

```python
line_up = []

line_up.append('도마뱀')
line_up.append('홍학')
line_up.append('토끼')

print(line_up)
```

### 도도의 심부름

```python
fruit = ["apple", "blueberry", "kiwi"]

length = len(fruit)
include = 'banana' in fruit
print(length, include)
```

---
## 02-1 반복문
### [수업 자료] 반복문 : 코드의 반복 줄이기
<반복문>
1. 범위를 기준으로 반복 : for문 → 변수가 시퀀스의 원소를 차례대로 방문하며~ (len만큼 반복)
2. 조건을 기준으로 반복 : while문 → 조건이 True이면 명령 반복

---
## 02-2 반복문 실습
### 3,6,9 게임

```python
for i in range(1,31):
  if i % 3 != 0:
    print(i)
  else:
    print('짝!')
```

### 계단 별자리2

```python
num = int(input())

for i in range(1, num + 1):
  print("*" * i)
```

### 1부터 n까지 자연수의 합

```python
n = int(input())
mysum = 0

for i in range(1, n + 1):
  mysum = mysum + i

print(mysum)
```

### 약수 찾기

```python
num = int(input())
i = 1

while num >= i:
  if num % i == 0:
    print(i)
  i = i + 1
```

---
## 03-1 복합 자료형
### [수업 자료] 기초 자료형2
<그 외 특화함수>

seq.count(d) : 자료 d의 개수

str.split(c) : c를 기준으로 문자열 → 리스트

str.join(list) : str을 기준으로 리스트 → 문자열

<Tuple>

1. 리스트와 유사, but 값의 변경 X
2. ()로 정의
3. 시퀀스 자료형
