# a부터 b까지 정수의 합 구하기 (for 문)

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요. : '))
b = int(input('정수 b를 입력하세요. : '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b
print(sum)