# # 문자열 뒤집기
# word = 'hello'
# ans = ''
# for w in word:
#     ans = w + ans
# print(ans)
#
# # 풀이 2
# for i in range(len(word)-1, -1, -1):
#     ans += word[i]
# print(ans)
#
# #
# word = 'hello'
# rev_word = list(word)
# print(rev_word)
# rev_word = rev_word[::-1]
# print(rev_word)
# print(''.join(rev_word))
# # .split()
# word = '서울시 종로구 2가'
# a = word.split() # 공백 기준
# print(a)
# word = 'hello'
# a = list(word)
# print(a)
#
# # .join()
# # 실제로 스트링 그 자체거나?
# word = 'python'
# print('-'.join(word)) # p-y-t-h-o-n
#
# # 리스트의 원소 자체가 스트링이어야지 됨
# word = ['p', 'y', 't', 'h', 'o', 'n']
# print('-'.join(word)) # p-y-t-h-o-n
# print(' '.join(word)) # 공백 p y t h o n
#
# # 평균값 구하기
# nums = [10, 50, 30, 70, 40]
# A = B = 0
# for num in nums:
#     A += num
#     B += 1
# print(A/B)
#
# users = {
# 	'total_user': 3,
# 	'information': [
# 			{'name': 'alex', 'age':3, 'license':True},
# 			{'name': 'june', 'age':7, 'license':False},
# 			{'name': 'peter', 'age':4, 'license':False}
# 	]
# }
# # 방법 1
# A = B = 0
# for i in users['information']:
# 	A += i['age']
# 	B += 1
# print(A/B)
#
# # 방법 2
# total= 0
# for i in range(users['total_user']):
# 	total += users['information'][i]['age']
# 	# print(s)
# 	answer = total/len(users['information'])
# print(answer)
# # print(users['information'][1]['age'])

# 로또 번호
import random
lotto = {8, 15, 19, 21, 32, 36}

# 집계틀
result = {i:0 for i in range(7)}
# 몇 게임
n = int(input())
#랜덤번호
for _ in range(n):
	my = set(random.sample(range(1,46),6))
	cnt = len(lotto & my)
	result[cnt] += 1

print(result)