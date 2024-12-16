'''
[Question 3] = (30점)
뒤집어도 같은 글자가 되는 단어를 '회문(palindrome)'이라고 정의할 때,
주어진 리스트에서 회문이 몇 개 있는지 고르는 함수를 완성하시오.
ex) 'box'를 뒤집으면 'xob'가 되므로 'box' != 'xob' 이다.
그런데, 'pop'을 뒤집으면 여전히 'pop'이 되므로 이것은 회문이다.
'''

words = ['banana', 'level', '역삼역', 'car', '별똥별', '우영우', 'palindrome']

def find_palindrome(words):
    count = 0
    for word in words:
        if word == word[::-1]:  # 단어를 뒤집어서 원래와 같은지 비교
            count += 1
    return count

answer = find_palindrome(words)
print(answer)