"""Baseball, Guess N digit number.
Strike : Right number, right position. Ball : Right number in input

Exercises
1. How can we make it difficult?
2. How many digits are most difficult?
3. Change it to allow repeated numbers.
"""

import random


def get_num_digit():
    digits = 0
    print("Enter Number of Digits to Play (max 9) : ", end='')
    while True:
        try:
            digits = int(input())
        except ValueError:
            print("You Should Input Only Numbers. Input : ", end='')
        else:
            if digits < 1 or digits > 9:
                print("Invalid Digit. Put a Number Between 1 to 9 : ", end='')
            else:
                break
    return digits


def generate_ran_ans(num_of_digits):
    return random.sample(range(1, 10), num_of_digits)


def get_user_ans(right_ans_):
    user_ans = []
    valid = False
    user_input = input("Please Enter %d-digits : " % len(right_ans_))
    for pos in range(len(user_input)):
        if user_input[pos] < '0' or user_input[pos] > '9':
            valid = True
    while valid:
        user_input = input("Enter Only Numbers. Enter %d-digits : " % len(right_ans_))
        valid = False
        for pos in range(len(user_input)):
            if user_input[pos] < '0' or user_input[pos] > '9':
                valid = True
    for pos in range(len(user_input)):
        user_ans.append(int(user_input[pos]))
    return user_ans


def check_format(user_ans_, right_ans_):
    if len(user_ans_) != len(right_ans_):
        print("Wrong Digit!")
        return False
    for pos in range(len(user_ans_)):
        if user_ans_[pos] < 1 or user_ans_[pos] > 9:
            print("Not a Valid Number! Zero is Not Included")
            return False
    for fix_pos in range(len(user_ans_)):
        for comp_pos in range(fix_pos+1, len(user_ans_)):
            if user_ans_[fix_pos] == user_ans_[comp_pos]:
                print("Repeated Number Included!")
                return False

    return True


def compare_user_ans(right_ans_, user_ans_):
    check_result = {'strike': 0, 'ball': 0}
    for pos in range(len(right_ans_)):
        if user_ans_[pos] == right_ans_[pos]:
            check_result['strike'] += 1
        elif user_ans_[pos] in right_ans_:
            check_result['ball'] += 1
    return check_result


num_of_digits = get_num_digit()
right_ans = generate_ran_ans(num_of_digits)
correct = False
trials = 1

while not correct:
    user_ans = get_user_ans(right_ans)
    if check_format(user_ans, right_ans):
        checked_ans = compare_user_ans(right_ans, user_ans)
        if checked_ans['strike'] == len(right_ans):
            print("You got right answer : ", end='')
            for position in range(len(user_ans)):
                print(user_ans[position], end='')
            print("  with %d trials" % trials)
            correct = True
        else:
            print("Strike : %s\tBall : %s\n%d Trials"
                  % (checked_ans['strike'], checked_ans['ball'], trials))
            trials += 1
