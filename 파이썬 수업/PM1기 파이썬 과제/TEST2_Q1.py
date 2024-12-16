'''
[Question 1] = (10점)
nums 리스트가 주어질 때, 주어진 리스트의 원소 중
5를 포함한 5의 배수들의 전체 합산을 구하시오.
'''

nums = [5, 1, 4, 10, 2, 15, 7, 5, 30]
answer = 0

for i in nums:
    if i % 5 == 0:
        answer += i

print(answer)  # 65가 출력되어야 합니다.