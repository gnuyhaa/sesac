# 다음의 리스트에서 소숫점을 제외한 평균값을 구하시오. ex) 3.1724일 경우 3을 출력
nums = [1, 7, 2, 3, 6, 1, 2, 5, 3, 4, 8, 7]
total = sum(nums)/len(nums)
answer = round(total)

print(answer) # 4