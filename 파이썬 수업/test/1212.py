# def add_two(x, y): # 우클릭 이름변경 -> 동일한 이름 동시 변경됨
#     z = x + y
#     return z
#
# print(add_two(2, 5))
# print(add_two(3, 8))
# print(add_two(4, 7))
#
# def my_len(my_list):
#     cnt = 0
#     for _ in my_list:
#         cnt += 1
#     return cnt
#
# a = my_len([1,9,5,2,1,4])
# print(a)
# # print(my_len('hi'))
#
# def my_func():
#     for _ in range(5):
#         print('hi')
#     return '수고하셨습니다.'
# print(my_func())
#
# def my_func(x):
#     y = x + 1
#     return y
#
# x = 1
# print(my_func(x))

# nums = [3, 5, 1, 4, 2]
# sliced_nums = nums[2:4]
# print(nums, sliced_nums)
# print(nums[:2])
# print(nums[1:])
# print(nums[2:100])

# nums2 = nums
# copied_nums = nums[:]
# print(copied_nums)
# reversed_nums = nums[::-1]
# print(reversed_nums)
#
# nums[0] = 100
# print(nums,copied_nums)
# print(nums2)
# nums[1:2] = [9,10,11]
# print(nums)
# nums[2:4] = []
# print(nums)

# sort()는 안정정렬
# 첫번째 코드
# a = [7, 5, 4, 1, 6]
# a.sort(key = lambda x : -x)
# print(a)
# # 두번째 코드
# b = [[70, 50], [70, 30], [30, 50], [40, 90], [30, 100]]
# # b.sort(reverse = True)
# # print(b)
# # b.sort(key = lambda x : (x[0], -x[1])) # 0 낮은 순서 중 1 높은 순서
# # print(b) # [[30, 100], [30, 50], [40, 90], [70, 50], [70, 30]]
# # b.sort(key = lambda x : (x[0] + x[1])) # 합이 작은 순서대로 x : -(x[0] + x[1]) -> 합이 큰 순서대로 정렬
# # print(b)
# # lambda로 지정하면 안정정렬
# b.sort(key = lambda x : x[0])
# print(b)

# 딕셔너리
# names = ['a', 'b', 'b', 'c', 'a', 'b', 'a', 'c', 'c', 'a', 'b', 'b']
# d = {'a': 0, 'b': 0, 'c': 0}
# for name in names:
#     d[name] += 1
#
# print(d)
# ex 집계틀을 미리 만들 수 없는 상황
# names = ['a', 'b', 'b', 'c', 'a', 'b', 'a', 'c', 'c', 'a', 'b', 'b']
# d = {}
# for name in names:
#     if name in d: # 이름이 있다면
#         d[name] += 1
#     else: # 이름이 없다면 (최초 셋팅코드)
#         d[name] = 1
# print(d)
# .get()
# for name in names:
#     d[name] = d.get(name,0) + 1
#     # if d.get(name, 0) == 0: # if d.get(name, -1) == -1:
#     #     d[name] = 1
#     # else:
#     #     d[name] += 1
# print(d)
a = {'갑': 3, '을': 4, '병': 2}
print(sum(a.values()))
# cnt = 0
# for i in a:
#     cnt += a[i]
#
# print(cnt)

for k, v in a.items():
    print(k,v)

# max(), min() 함수
nums = [7, 1, 2, 4, 6, 8, 3]

# 최댓값
max_num = -1  # 작은 수로 초기화
for num in nums:
    if max_num < num:
        max_num = num

print(max_num)

min_num = 9999  # 큰 수로 초기화
for num in nums:
    if min_num > num:
        min_num = num
print(min_num)