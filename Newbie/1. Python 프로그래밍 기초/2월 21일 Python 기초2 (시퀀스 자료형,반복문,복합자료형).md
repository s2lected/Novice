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

<Dictionary>

1. {}로 정의
2. key:value의 형태
3. key의 역할 : value를 꺼내는 열쇠
4. key의 성질 : 고유, 주도적
5. key는 변할 수 없는 자료형 : tuple 가능, list 불가능

<정리>

() : 함수 뒤, tuple 정의

[] : 인덱싱, list 정의

{} : dict 정의

---
## 03-2 복합 자료형 실습
### 수도 퀴즈 만들기

```python
country = {'대한민국': '서울', '베트남': '하노이', '브라질': '브라질리아', '프랑스': '파리', '미국': '워싱턴', '칠레': '산티아고',
           '체코': '프라하', '러시아': '모스크바', '중국': '베이징', '스페인': '마드리드', '이집트': '카이로', '영국': '런던'}

country['벨기에'] = '브뤼셀'
del country['중국']
print(country)
```

### 과일 사전 만들기

```python
my_dict = {'사과':'apple','바나나':'banana','당근':'carrot'}

var1 = my_dict['사과']
del my_dict['당근']
my_dict['체리'] = 'cherry'

print(var1)
print(my_dict)
```

---
## 자율 실습 문항
### 한 번에 여러 입력받기 2

```python
my_list = list(map(int, input().split()))
print(my_list)
```

### 충성! 입대를 명 받았습니다!

```python
soldier = [12, 2, 5, 3, 7, 4, 10, 8, 1, 9, 13, 11, 6]
soldier.sort()
print(soldier)
```

### 무기 강화

```python
item1 = '완전 좋고'
item2 = '빛나며'
item3 = '손에 착착 감기는'

print(item1 + ' ' + item2 + ' ' + item3 + ' ' + '무기')
```

### 새치기의 달인

```python
line_up = ["도마뱀", "홍학", "토끼", "고양이"]
line_up.insert(1,'도도새')

print(line_up)
```

### 시퀀스의 인덱싱과 슬라이싱

```python
my_str = 'Impossible'
my_list = ['Apple','Banana','Chamwae','Durian']

var1 = my_list[2]
var2 = my_str[2:]

print(var1)
print(var2)
```

### 수능 금지곡

```python
a = ['ring']
b = ['ding']
c = ['dong']
d = ['diggi']

lyric = a + b + c
print(lyric)

shinee1 = lyric * 2
print(shinee1)

shinee2 = a + d + b + d + b * 3

print(shinee1,shinee2)
```

### [실습9] 반복문 탈출 : break

```python
i = 1

while True:
  print(i)
  if i == 5:
    print('i가 5에요!')
    break
  i += 1
```

### [실습10] 장바구니 프로그램 만들기

```python
shopping_list = []

while True:
  product = input()
  shopping_list.append(product)
  if product == '구매':
    break

print(shopping_list[:-1])
```

### 꼭꼭 숨어라

```python
for count in range(1,101):
  print(count)
```

### 열 마리 코끼리가 거미줄에 걸렸네

```python
nums = [1,2,3,4,5,6,7,8,9,10]

for i in nums:
  print(i, '번째 코끼리가 거미줄에 걸렸네♪')
```

### 노동요

```python
korean = list(input())
for i in korean:
  if i == ' ':
    print('링디기디기')
  elif i == '.':
    print('딩딩딩')
  else:
    print('링딩동')
```

### 약수의 개수 구하기

```python
num = int(input())
answer = []

for i in range(1,num + 1):
  if num % i == 0:
    answer.append(num)

print(len(answer))
```

### [실습6] Dictionary의 Key

```python
my_dict1 = {}

my_dict1[1] = 'Integer'
my_dict1['a'] = 'String'

print(my_dict1)

key_candidate1 = [1, 2, 3]
key_candidate2 = (1, 2, 3)

my_dict2 = {key_candidate2 : "I am Value!"}

print(my_dict2)
```

### 펜 파인애플 애플 펜

```python
words = ['i', 'have', 'a', 'pen', 'i', 'have', 'pineapple', 'i', 'have', 'an', 'apple', 'pen']

words.pop(4)
words.pop(4)
words.pop(5)
words.pop(5)
words.pop(5)

lyrics = ' '.join(words)

print(lyrics)
```

### 여우와 강아지

```python
words = ['the','quick','brown','fox','jumps','over','the','lazy','dog']

sentence = ' '.join(words)
print(sentence.count('o'))
```

### 훈민정음

```python
hangul = ('나', '랏', '말', '싸', '미', '듕', '귁', '에', '달', '아', '문', '자', '와', '로', '서', '르', '사', '맛', '띠', '아', '니', '할',
          '쌔', '이', '런', '젼', '차', '로', '어', '린', '백', '셩', '이', '니', '르', '고', '져', '홀', '빼', '이', '셔', '도', '마', '참',
          '내', '제', '뜨', '들', '시', '러', '펴', '디', '못', '할', '노', '미', '하', '니', '라')

print(hangul[0] + hangul[47] + hangul[23])
```

### 수도 퀴즈 맞추기

```python
country = {'대한민국': '서울', '베트남': '하노이', '브라질': '브라질리아', '프랑스': '파리', '미국': '워싱턴', '칠레': '산티아고',
           '체코': '프라하', '러시아': '모스크바', '중국': '베이징', '스페인': '마드리드', '이집트': '카이로', '영국': '런던'}

country['chile'] = '산티아고'
print(country['chile'])
```

### 튜플 만들기

```python
my_tuple = (1,2,3,4,5)

var1 = my_tuple[3]
var2 = len(my_tuple)

print(var1)
print(var2)
```
---
