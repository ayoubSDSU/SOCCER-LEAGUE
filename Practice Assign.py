HTW = int(0)
ATW = int(0)

#____________________________________________________
print("Match 1:")

Home_Team1 = input("Enter Home Team Name:")
print (Home_Team1)

Home_Team_Score1 = int(input("Enter Home Team Score:"))
print (Home_Team_Score1)

Away_Team1 = input("Enter Away Team Name:")
print (Away_Team1)

Away_Team_Score1 = int(input("Enter Away Team Score:"))
print (Away_Team_Score1)


if Home_Team_Score1 > Away_Team_Score1:
    print ( "Home Team Wins")
    HTW = HTW + 1
    
    
if Home_Team_Score1 < Away_Team_Score1:
    print ("Away Team Wins")
    ATW = ATW + 1 
    
#____________________________________________________
print ("____________________________________________________")


print("Match 2:")

Home_Team2 = input("Enter Home Team Name:")
print (Home_Team2)

Home_Team_Score2 = int(input("Enter Home Team Score:"))
print (Home_Team_Score2)

Away_Team2 = input("Enter Away Team Name:")
print (Away_Team2)

Away_Team_Score2 = int(input("Enter Away Team Score:"))
print (Away_Team_Score2)


if Home_Team_Score2 > Away_Team_Score2:
    print ( "Home Team Wins")
    HTW = HTW + 1
    
if Home_Team_Score2 < Away_Team_Score2:
    print ("Away Team Wins")
    ATW = ATW + 1

#____________________________________________________
print ("____________________________________________________")
#____________________________________________________

print("Match 3:")

Home_Team3 = input("Enter Home Team Name:")
print (Home_Team3)

Home_Team_Score3 = int(input("Enter Home Team Score:"))
print (Home_Team_Score3)

Away_Team3 = input("Enter Away Team Name:")
print (Away_Team3)

Away_Team_Score3 = int(input("Enter Away Team Score:"))
print (Away_Team_Score3)


if Home_Team_Score3 > Away_Team_Score3:
    print ( "Home Team Wins")
    HTW = HTW + 1
    
if Home_Team_Score3 < Away_Team_Score3:
    print ("Away Team Wins")
    ATW = ATW + 1

#____________________________________________________
print ("____________________________________________________")
#____________________________________________________


print("Match 4:")

Home_Team4 = input("Enter Home Team Name:")
print (Home_Team4)

Home_Team_Score4 = int(input("Enter Home Team Score:"))
print (Home_Team_Score4)

Away_Team4 = input("Enter Away Team Name:")
print (Away_Team4)

Away_Team_Score4 = int(input("Enter Away Team Score:"))
print (Away_Team_Score4)

if Home_Team_Score4 > Away_Team_Score4:
    print ( "Home Team Wins")
    HTW = HTW + 1
if Home_Team_Score4 < Away_Team_Score4:
    print ("Away Team Wins")
    ATW = ATW + 1
        
#____________________________________________________
print ("____________________________________________________")
#____________________________________________________



print("Match 5:")

Home_Team5 = input("Enter Home Team Name:")
print (Home_Team5)

Home_Team_Score5 = int(input("Enter Home Team Score:"))
print (Home_Team_Score5)

Away_Team5 = input("Enter Away Team Name:")
print (Away_Team5)

Away_Team_Score5 = int(input("Enter Away Team Score:"))
print (Away_Team_Score5)


if Home_Team_Score5 > Away_Team_Score5:
    print ( "Home Team Wins")
    HTW = HTW + 1 

if Home_Team_Score5 < Away_Team_Score5:
    print ("Away Team Wins")
    ATW = ATW + 1
        
#____________________________________________________
print ("____________________________________________________")
#____________________________________________________


print("Match 6:")

Home_Team6 = input("Enter Home Team Name:")
print (Home_Team1)

Home_Team_Score6 = int(input("Enter Home Team Score:"))
print (Home_Team_Score6)

Away_Team6 = input("Enter Away Team Name:")
print (Away_Team6)

Away_Team_Score6 = int(input("Enter Away Team Score:"))
print (Away_Team_Score6)


if Home_Team_Score6 > Away_Team_Score6:
    print ( "Home Team Wins")
    HTW = HTW + 1
    
if Home_Team_Score6 < Away_Team_Score6:
    print ("Away Team Wins")
    ATW = ATW + 1 
        
#____________________________________________________
print ("____________________________________________________")
#____________________________________________________


print("Match 7:")

Home_Team7 = input("Enter Home Team Name:")
print (Home_Team7)

Home_Team_Score7 = int(input("Enter Home Team Score:"))
print (Home_Team_Score7)

Away_Team7 = input("Enter Away Team Name:")
print (Away_Team7)

Away_Team_Score7 = int(input("Enter Away Team Score:"))
print (Away_Team_Score7)


if Home_Team_Score7 > Away_Team_Score7:
    print ( "Home Team Wins")
    HTW = HTW + 1 
if Home_Team_Score7 < Away_Team_Score7:
    print ("Away Team Wins")
    ATW = ATW + 1 


#____________________________________________________
print ("____________________________________________________")
#____________________________________________________

while True:
    text = input("Type Done to see Statistics")
    if text == "Done" :
        print ("____________________________________________________")
        print ("Total Games ",(HTW + ATW))
        print ("Home Team Wins",(HTW))
        print ("Away Team Wins",(ATW))
        print ("Home Team Average Score",((Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7)/7))
        print ("Away Team Average Score",((Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7)/7))
        print ("Home Team Total Score",(Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7))
        print ("Away Team Total Score",(Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7))
        print ("Away Team Average Conceded Score",((Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7)/7))
        print ("Home Team Average Conceded Score",((Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7)/7))
        print ("Away Team Total Conceded Score",(Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7))
        print ("Away Team Total Conceded Score",(Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7))
        print ("Home Team Average Differential Score",((Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7)-(Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7)/7))
        print ("Away Team Average Differential Score",((Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7)-(Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7)/7))
        print ("Home Team Total Differential Score",(Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7)-(Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7))
        print ("Away Team Total Differential Score",(Away_Team_Score1 + Away_Team_Score2 + Away_Team_Score3 + Away_Team_Score4 + Away_Team_Score5 + Away_Team_Score6 + Away_Team_Score7)-(Home_Team_Score1 + Home_Team_Score2 + Home_Team_Score3 + Home_Team_Score4 + Home_Team_Score5 + Home_Team_Score6 + Home_Team_Score7))
        print (("The Highest Score Belongs to Team:",(max( (Away_Team1, Away_Team_Score1), (Away_Team2, Away_Team_Score2), (Away_Team3, Away_Team_Score3), (Away_Team4, Away_Team_Score4), (Away_Team5, Away_Team_Score5), (Away_Team6, Away_Team_Score6), (Away_Team7, Away_Team_Score7), (Home_Team1, Home_Team_Score1), ( Home_Team2,Home_Team_Score2), (Home_Team3, Home_Team_Score3), (Home_Team4, Home_Team_Score4), (Home_Team5, Home_Team_Score5), (Home_Team6, Home_Team_Score6), (Home_Team7, Home_Team_Score7)))))
        break
    else:
        print ("Type Done to see Statistics")

#____________________________________________________
print ("____________________________________________________")
#_________________________________________________


