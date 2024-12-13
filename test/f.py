# 5개 이상, 1000원 이상 > VIP회원
# 하나만 만족 > 우수회원
n = int(input('물건을 입력하세요: '))
pay = int(input('금액을 입력하세요: '))

if n >= 5 and pay >= 1000:
    print('VIP회원 입니다.')
elif n >= 5 or pay >= 1000:
    print('우수회원 입니다.')
else:
    print('일반회원 입니다.')