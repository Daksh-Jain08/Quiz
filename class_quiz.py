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
        if(self.q_current==1):
            print("There are no questions before this.")
            return
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
        print("The quiz has been submitted.\nNumber of questions attempted: " ,self.q_attempted, "\nNumber of questions answered correctly: ", self.q_correct, "\nNumber of questions answered incorrectly:", self.q_incorrect)
        print("Total Score: ", self.score)
        exit()
    