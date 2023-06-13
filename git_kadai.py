#課題パターン２
import random as rd

ans=rd.randint(100,999)
print(ans)
ans_number=0

for i in range(10):
    ans_input=input("Please enter a three digit number: ")
    #入力の判定：数字かどうか
    if ans_input.isdigit():
        ans_number=int(ans_input)
        #入力の判定：３桁かどうか
        if ans_number>=100 and ans_number<=999:
            #答えの正誤判定
            if ans_number==ans:
                print('Correct! Congratulation!')
                break
            elif ans_number < ans:
                #ヒント
                print('Wrong answer. The answer is a larger number')
            elif ans_number > ans:
                #ヒント
                print('Wrong answer. The answer is a smaller number')

            #最後の特大ヒント
            if i==8:
                print("Last hint: Answer is around",ans-ans%10)

        else:
            #３桁の数字でない場合
            print('It is not a three digit number')
    else :
        #数字でない入力の場合
        print('It is not a number')

if i==9:
    print("Input limit reached. unfortunately you could not enter the correct answer")
    print("Answer is ",ans)
    

