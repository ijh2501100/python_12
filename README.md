# python_12
# Python GitHub 과제

## 1. 과제 개요
- 이 프로젝트는 파이썬의 집합(set) 자료형을 활용하는 다양한 문제들로 구성되어 있다.
합집합, 교집합, 차집합, 대칭차집합과 같은 기본적인 집합 연산부터,
집합 메서드(add, remove, issubset, issuperset) 그리고 집합 컴프리헨션까지 다룬다.  
---

## 2. 수행 과정
1. **첫 번째 commit**
   **본인이 좋아하는 숫자 10개를 5개씩 두 개로 나누어 set를 만든 후 합집합과 교집합을 계산 후 출력**
   - commit 메시지: `#32`  
   - 기능:
a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a | b
d = a & b

print(c)
print(d)

2. **두 번째 commit**
   **본인이 좋아하는 숫자 10개를 5개씩 나누어 set를 만든 후 차집합과 대칭차집합을 계산 후 출력**
   - commit 메시지: `#33` 
   - 기능: 
a = {1,2,3,4,5}
b = {3,4,5,6,7}

c = a - b
d = a ^ b

print(c)
print(d)

3. **세 번째 commit**
   **본인이 좋아하는 숫자 5개로 set를 만든 후, update method을 이용하여 숫자 100 할당 후 출력**
   - commit 메시지:`#34`
   - 기능:
a = {1,2,3,4,5}
a  |= {100}
print(a)

4. **네 번째 commit**
**a = {100,200,300,400,500}를 선언 후 {400,500,600,700,800}set과 intersection_update method, difference_update method 및 symmentic_difference_update method을 수행 후 출력**
   - commit 메시지: `#35`  
   - 기능:
a = {100,200,300,400,500}
a &= {400,500,600,700,800}

print(a)

a = {100,200,300,400,500}
a -= {400,500,600,700,800}

print(a)

a = {100,200,300,400,500}
a ^= {400,500,600,700,800}

print(a)

5. **다섯 번째 commit**
   **a = {100,200,300,400,500}와 {400,500,600,700,800}set이 있을 때 a가 상위집합이면 "상위"를 출력하고, a가 부분집합이면 "부분"을 출력하고 상위집합이면서 부분집합일 경우에는 "동시"를 출력**
   - commit 메시지: `#36` 
   - 기능: 
a = {100,200,300,400,500}
b = {100,200,300,400,500}

if a.issuperset(b) and a.issubset(b):
    print('동시')
elif a.issuperset(b):
    print('상위')
elif a.issubset(b):
    print('부분')

3. **여섯 번째 commit**
   **본인이 좋아하는 숫자 5개로 set를 만든 후, 1000 숫자를 add method을 이용하여 추가하고 마지막 값을 삭제 후 출력**
   - commit 메시지:`#37`
   - 기능:
a = {1,2,3,4,5}
a.add(1000)
a.remove(1000)
print(a)

3. **일곱 번째 commit**
   **아래 코드를 완성하여 1부터 100까지 숫자 중 3과 5의 공배수를 set comprehension을 이용하여 세트 형태로 출력**
   - commit 메시지:`#38`
   - 기능:
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)
---

## 3. GitHub Repository URL
- URL: []
---
