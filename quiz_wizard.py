import random
import question_bank
import class_quiz

choice=input("1. Press any key to start quiz \n2. press e to exit\n")
if(choice=='e'):
    print("You should have tried, i worked really hard on this quiz :(")
    exit()
else:
    pass

wiz=class_quiz.quiz_flow()

print("Welcome to the quiz!")
wiz.q_num=int(input("Enter the number of questions in the quiz: "))

randomlist = []
i=1
while (i<=wiz.q_num):
    n = random.randint(0,11)
    if n in randomlist:
        i-=1
    else:
        randomlist.append(n)
    i+=1

j=0
for i in randomlist:
    wiz.l.append([i,0,0,0])
    wiz.l[j][2]=question_bank.question_list[i]["answer"]
    j+=1

while(True):
    print("\npress:\n1. Give Response \n2. Mark For Review\n3. Unmark for review \n4. Next Question \n5. Previous question \n6. Move to Question Number \n7. Clear Response \n8. Clear all Response\n9. Show questions marked for review\n10. Submit")
    print("\n\t\tQuestion Number: ",wiz.q_current)
    print("\n",question_bank.question_list[wiz.l[(wiz.q_current)-1][0]]["text"],"\n")
    ch_1=int(input())
    
    match ch_1:
        case 1:
            while(wiz.q_current<=wiz.q_num):
                print("Press 't' for True \nPress 'f' for False")
                res=input().lower()
                if(res=='t'):
                    wiz.set_responce("True")
                    break
                elif(res=='f'):
                    wiz.set_responce("False")
                    break
                else:
                    print("Enter a valid choice.")
            wiz.next_question()

        case 2:
            wiz.mark_for_review()

        case 3:
            wiz.unmark_for_review()
        
        case 4:
            wiz.next_question()

        case 5:
            wiz.previous_question()
        case 6:
            print("Enter the Number You want to move")
            x=int(input())
            wiz.move_to_question_num
        case 7:
            wiz.clear_response()
        case 8:
            while(True):
                print("\n Are you sure you want to Clear all Response\nPress 'y' for Yes\nPress 'n' for No")
                confirm=input().lower()
                if(confirm=='y'):
                    wiz.clear_all_response()
                    break
                elif(confirm=='n'):
                    break
                else:
                    print("Enter a valid input")
        case 9:
            wiz.show_marked_for_review()

        case 10:
            wiz.submit()