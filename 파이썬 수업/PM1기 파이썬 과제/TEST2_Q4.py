'''
[Question 4] = (40점, 부분점수 있음)
천재교육의 밀크티 학생 API 데이터를 활용하여 다음 질문에 답하시오.
(1) 전체 학생들의 수를 구하시오. (5점)
(2) 모든 학생들의 수학 성적의 평균을 구하시오. (단, 소수점은 버린다) (10점)
(3) 학생들 각자의 총점(수학 성적과 과학 성적의 합산)을 기준으로 상위 3명의 이름을 높은 순서대로 출력하시오. (20점)
단, 어떤 학생도 총점이 같은 경우는 존재하지 않음.
'''
students = {
    'response': 'success',
    'results': [
        {'name': 'kyle', 'math': 100, 'science': 100},
        {'name': 'alex', 'math': 17, 'science': 33},
        {'name': 'haley', 'math': 70, 'science': 63},
        {'name': 'july', 'math': 13, 'science': 56},
        {'name': 'yuna', 'math': 44, 'science': 65},
        {'name': 'jun', 'math': 90, 'science': 100},
        {'name': 'ken', 'math': 94, 'science': 38},
        {'name': 'chelsea', 'math': 58, 'science': 99},
        {'name': 'peter', 'math': 5, 'science': 25},
        {'name': 'rachel', 'math': 26, 'science': 81},
        {'name': 'emily', 'math': 79, 'science': 18},
        {'name': 'harry', 'math': 93, 'science': 84},
        {'name': 'peach', 'math': 64, 'science': 42},
        {'name': 'bob', 'math': 3, 'science': 17},
        {'name': 'sophia', 'math': 31, 'science': 4},
        {'name': 'jane', 'math': 81, 'science': 79},
        {'name': 'mia', 'math': 51, 'science': 22},
        {'name': 'kate', 'math': 100, 'science': 99},
    ],
    'total_pages': 7124,
    'current_page': 1
}
# =========================================================
# 1번 답 :
# 18
# 이곳에 로직을 작성합니다.
print(len(students['results']))



# =========================================================


# =========================================================
# 2번 답 :
# 56
# 이곳에 로직을 작성합니다.

total = 0
for student in students['results']:
    total += student['math']
average_total = total // len(students['results'])
print(average_total)



# =========================================================



# =========================================================
# 3번 답 :
# kyle
# kate
# jun
# 이곳에 로직을 작성합니다.
total_score = []
for student in students['results']:
    total = student['math'] + student['science']
    total_score.append((student['name'], total))

# 총점 기준으로 내림차순 정렬
total_score.sort(key=lambda x: x[1], reverse=True) # lambda x : -x[1]

# 상위 3명 출력
for student in total_score[:3]:
    print(student[0])


# =========================================================