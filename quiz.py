questions=[]
questions.append("Full form of html :")
questions.append("Full form of css :")
questions.append("which year discoverd c++ :")
questions.append("Which year html discored :")



options=[
("A: hypertext markup language B: hysji tile mart  C: higher map text D: hh tt mm"),
("A: code sale cading  B: casecading style sheet  C: covert style in style D: Cosecade ssheet"),
("A: 1979 B: 1980 C: 1999 D: 1991"),
("A: 1990 B: 1991 C: 1979 D: 1941")
]

answer=["A","B","A","B"]

ans=[]
points=0

print(questions[0])
print(options[0])
ans.append(input("Select the correct option :").upper())
points=points+1 if ans[0]==answer[0] else points



print(questions[1])
print(options[1])
ans.append(input("Select the correct option :").upper())
points=points+1 if ans[1]==answer[1] else points



print(questions[2])
print(options[2])
ans.append(input("Select the correct option :").upper())
points=points+1 if ans[2]==answer[2] else points



print(questions[3])
print(options[3])
ans.append(input("Select the correct option :").upper())
points=points+1 if ans[3]==answer[3] else points

print()
print(f"Total points are :{points}")
print(f"Your selected options are :{ans}")
print(f"The correct answers are :{answer}")





