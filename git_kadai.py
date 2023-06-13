import random as rd

ans=rd.randint(100,999)
ans_checker='flase'
ans_number=0

while ans_checker=='flase':
    ans_input=input("Please enter a three digit number: ")
    ans_number=int(ans_input)
    if ans_number==ans:
        print('Correct!')
        ans_checker='ture'
    elif ans_number < ans:
        print('The answer is a larger number')
    elif ans_number > ans:
        print('The answer is a smaller number')