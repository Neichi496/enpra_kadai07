import random as rd

ans=rd.randint(100,999)
print(ans)
ans_number=0

for i in range(10):
    ans_input=input("Please enter a three digit number: ")
    if ans_input.isdigit():
        ans_number=int(ans_input)
        if ans_number>=100 and ans_number<=999:
            if ans_number==ans:
                print('Correct! Congratulation!')
                break
            elif ans_number < ans:
                print('Wrong answer. The answer is a larger number')
            elif ans_number > ans:
                print('Wrong answer. The answer is a smaller number')
        else:
            print('It is not a three digit number')
    else :
        print('It is not a number')
    

