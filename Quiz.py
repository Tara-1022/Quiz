import mysql.connector as mycon
from data import *
from tkinter import *
import random

n = 10#number of questions
a = int()

#the function called when a radiobutton is selected
def sel():
    global v
    global root
    global a
    #stores the user's choice and closes the question
    a = int(v.get())
    root.destroy()
  
#creating radiobuttons
def create_radio(o1,o2,o3,o4,q):
    global v
    global root
    root = Tk()#tkinter window created
    root.geometry('500x300')
    root.title("Quiz")
    root.option_add('*font', ('arial', 16, 'bold'))
    root['bg']= 'white'
    
    #creating variable to store choice
    v= IntVar(root)

    #placing the question
    t=Label(text = q+'\n', bg='white')
    t.place(x = 40, y = 60)
    t.pack()

    # a list to hold the values, text of each radiobutton
    values = {o1:0,
          o2:1,
          o3:2,
          o4:3,
          "Skip":4}
    
    for (txt,val) in values.items():#creating radio buttons
        Radiobutton(root, 
                  text=txt,
                  indicatoron = 0,
                  width = 60,
                  padx = 60, 
                  variable=v, 
                  value=val,bg = '#1ce3cc', fg = "black").pack(anchor = 'center', side = TOP)
        
    btn = Button(root, text = 'Next', command = sel, bg = 'black', fg = "white")#creating button
    btn.pack(side = 'bottom')
    
    root.mainloop()

#show score in tkinter window
def show_score(total):
    score_board = Tk()#tkinter window created
    score_board.geometry('500x300')
    score_board.title("Score")
    score_board.option_add('*font', ('arial', 16, 'bold'))
    score_board['bg']= 'white'

    txt=Label(text = "\n\n\n\nYour score is "+ str(total), bg='white')
    txt.place() 
  
    txt.pack()

    score_board.mainloop()


#main part 

#setting the connection
con=mycon.connect(host="localhost", user="root", password="1234")
if not con.is_connected():
    print("There was a connection error. Try again later")
    quit()
cur=con.cursor(buffered = True)


#start-up message, input
print("\nWelcome! Enter the correct options for the following questions.\n\
\nEach correct answer results in two points while each false one deducts one.")
name = input("Enter your name: ")


#creating database
cur.execute("Create Database If Not Exists Quiz;")
cur.execute("Use Quiz;")


#checking if table exists, creating new user as needed
try:
    cur.execute("Select * from {};".format(name))
except:
    cur.execute("Create table {} (Question_name char(30) Unique, Score int);".format(name))
    for i in questions.values():
        cur.execute("""Insert into {} values("{}",NULL);""".format(name,i[:30]))
con.commit()

#fetching stored scores
cur.execute("Select * from {} Where Score is Not Null Order By Score DESC;".format(name))
scores = cur.fetchall()
try:
    test = scores[0]
    print("\n\n\nYour previous scores are :")
    display_score(scores)
    print("These scores will be updated when you play the quiz")
except:
    print("This will be your first time playing. Your scores will be shown at the end.")
    
#resetting scores
cur.execute("""Update {} set Score = NULL;""".format(name))
con.commit()


            
# a list containing the indices of asked questions to prevent repetition
asked_questions=[]
total = 0

#calls the function to create the tkinter window with radio button
i = 0
while i<n :
    question_number = random.randint(0, len(correct_ans)-1)
    
    if question_number not in asked_questions:
        # making sure that the question is not repeated
         i+=1
         asked_questions.append(question_number)
         
         create_radio(options[question_number][0],options[question_number][1],
                      options[question_number][2],options[question_number][3],
                      questions[question_number])
         choice = a
    
         if choice == 4:# question is skipped
             sc=0
         elif options[question_number][choice] == correct_ans[question_number]:
             #answer matches
             sc = 2
         else:
             sc=-1

         total = total + sc
         
         # storing the scores
         cur.execute('''Update {} Set Score = {} where Question_name = "{}";'''.format(name,sc,questions[question_number][:30]))
         con.commit()
                    
show_score(total)

# displaying scores after the player has completed
cur.execute("Select * from {} Where Score is NOT NULL Order by Score DESC;".format(name))
scores = cur.fetchall()
print("\n\n\nYour scores are :")
display_score(scores)

print("\n\nThank you for playing. Game created by\n\n\t\tSumitha, Harshita, Tara")
