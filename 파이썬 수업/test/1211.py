# 1번 풀이
# nums = [8, 1, 2, 5, 7, 9, 6]
# ans = []
#
# for num in nums: # for 변수 in 컨테이너:
#     if num % 2: # num % 2    == num % 2 == 1 (홀수 출력)
#         ans.append(num)
# print(ans, len(ans))
# 2번 풀이
# nums = [8, 1, 2, 5, 7, 9, 6]
# cnt = 0 # count
#
# for num in nums:
#     if num % 2 == 1: #홀수
#         cnt += 1
# print(cnt)
# range
# for _ in range(3):
#     print('hi')
# numbers = [1, 2, 3, 4, 5]
#
# # 0부터 (numbers의 길이 - 1)까지 변수 i에 차례로 할당 (즉, i가 numbers의 인덱스 역할 수행 가능)
# for i in range(len(numbers)):
#     print(numbers[i])
#
#while 반복문
# n = 0
# while n < 3:
#     print(n)
#     n += 1
nums = list(range(1,11))
for num in nums:
    if num % 2: #2,4,6,8,10
        continue
    if num % 3: # 3,6,9
        continue

    print(num)

# hash


