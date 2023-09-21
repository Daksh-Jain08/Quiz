import random
import question_bank


class quiz_flow:
    l=[]
    
    def __init__(self):
        self.q_num=0
        self.q_attempted=0
        self.q_remaining=self.q_num
        self.q_current=1
        self.q_id=0
        self.score=0
        self.q_correct=0
        self.q_incorrect=0
        self.q_marked_for_review=[]

    def set_responce(self,response):
        self.l[self.q_current-1][1]=response
        self.q_attempted+=1

    def mark_for_review(self):
        self.l[self.q_current-1][3]=1
        self.q_marked_for_review.append(self.q_marked_for_review)
        print("This question has been marked for review.")

    def show_marked_for_review(self):
        print(self.q_marked_for_review)

    def next_question(self):
        if(self.q_current==self.q_num):
            self.submit()
        else:
            self.q_current+=1

    def previous_question(self):
        if(self.q_current==0):
            print("There are no questions before this.")
        self.q_current-=1

    def move_to_question_num(self,num):
        self.q_current=num

    def is_attempted(self,que):
        if(self.l[que][1]!=0):
            return True
        else:
            return False

    def get_num_attempted(self):
        print(self.q_attempted)

    def get_num_remaining(self):
        self.q_remaining= self.q_num - self.q_attempted

    def clear_response(self):
        self.l[self.q_current-1][0]=0
        self.q_attempted-=1

    def clear_all_response(self):
        for i in range(self.q_num):
            self.l[i][1]=0
        self.q_attempted=0
    
    def unmark_for_review(self):
        self.l[self.q_current-1][3]=0
        print("The question has been marked for review.")

    def submit(self):
        for i in range(self.q_num):
            if(self.l[i][1]==0):
                pass
            elif(self.l[i][1]==self.l[i][2]):
                self.score+=2
                self.q_correct+=1
            else:
                self.score-=1
                self.q_incorrect+=1
        print("The quiz has been submitted.\nNumber of questions attempted: " ,wiz.q_attempted, "\nNumber of questions answered correctly: ", wiz.q_correct, "\nNumber of questions answered incorrectly:", wiz.q_incorrect)
        print("Total Score: ", self.score)
        exit()
    
#interface-----------------------------------------

choice=input("1. Press any key to start quiz \n2. press e to exit\n")
if(choice=='e'):
    print("You should have tried, i worked really hard on this quiz :(")
    exit()
else:
    pass

wiz=quiz_flow()

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
print(wiz.l)
while(True):
    print("\npress:\n1. Give Response \n2. Mark For Review\n3. Unmark for review \n4. Next Question \n5. Previous question \n6. Move to Question Number \n7. Clear Response \n8. Clear all Response\n9. Submit")
    print("\n\t\tQuestion Number: ",wiz.q_current)
    print("\n",question_bank.question_list[wiz.l[wiz.q_current-1][0]]["text"],"\n")
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
            x=input()
            wiz.move_to_question_num(x)
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
            wiz.submit()