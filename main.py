import pandas as pd  #import pandas
import random  #import random
import sys  #import sys (system functions)

list2 = [0, 1, 2, 3, 4, 5, 6]
list3 = ['RUN OUT', 'CATCH', 'LBW', 'BOWLED']
runs = 0
balls = 0
wickets = 0
overs = 1

runs_1 = 0
balls_1 = 0
wickets_1 = 0
overs_1 = 1

teams = {'Sri Lanka': ['Dasun Shanaka (c)', 'Kusal Janith Perera (wk)', 'Pathum Nissanka', 'Charith Asalanka',
                       'Avishka Fernando', 'Bhanuka Rajapaksa',
                       'Chamika Karunaratne', 'Wanindu Hasaranga', 'Lahiru Kumara',
                       'Maheesh Theekshana', 'Binura Fernando'],

         'India': ['Virat Kohli (c)', 'Ishan Kishan (wk)', 'Rohit Sharma', 'KL Rahul',
                   'Suryakumar Yadav', 'Hardik Pandya', 'Ravindra Jadeja',
                   'Shardul Thakur', 'Varun Chakravarthy', 'Jasprit Bumrah', 'Bhuvneshwar Kumar'],

         'Australia': ['Aaron Finch (c)', 'Matthew Wade (wk)', 'David Warner', 'Adam Zampa',
                       'Ashton Agar', 'Pat Cummins', 'Glenn Maxwell', 'Kane Richardson',
                       'Steve Smith', 'Mitchell Starc', 'Mitchell Marsh'],

         'West Indies': ['Kieron Pollard (c)', 'Andre Fletcher (wk)', 'Chris Gayle',
                         'Shimron Hetmyer', 'Evin Lewis', 'Ravi Rampaul', 'Andre Russell',
                         'Oshane Thomas', 'Obed McCoy', 'Lendl Simmons', 'Dwayne Bravo'],

         'England': ['Eoin Morgan (c)', 'Jos Buttler (wk)', 'Moeen Ali', 'Jonathan Bairstow',
                     'Sam Billings', 'Tom Curran', 'Chris Jordan', 'Liam Livingstone',
                     'Jason Roy', 'David Willey', 'Mark Wood'],

         'Bangladesh': ['Mahmud Ullah (c)', 'Mushfiqur Rahim (wk)', 'Mohammad Naim Sheikh',
                        'Soumya Sarkar', 'Liton Das', 'Shakib Al Hasan', 'Afif Hossain',
                        'Nurul Hasan Sohan', 'Shak Mahedi Hasan', 'Nasum Ahmed', 'Mustafizur Rahman'],

         'Pakistan': ['Babar Azam (c)', 'Mohammad Rizwan (wk)', 'Asif Ali', 'Shoaib Malik',
                      'Fakhar Zaman', 'Shadab Khan', 'Imad Wasim', 'Mohammad Hafeez',
                      'Mohammad Nawaz', 'Shah Afridi', 'Hasan Ali'],

         'South Africa': ['Temba Bavuma (c)', 'Quinton de Kock (wk)', 'Reeza Hendricks',
                          'Aiden Markram', 'David Miller', 'Rassie van der Dussen',
                          'George Linde', 'Bjorn Fortuin', 'Lungi Ngidi', 'Anrich Nortje', 'Lizaad Williams']}

df1 = pd.DataFrame(teams,
                   columns=['Sri Lanka', 'India', 'Australia', 'West Indies', 'England', 'Bangladesh', 'Pakistan',
                            'South Africa'])
df1.to_csv('teams.csv', index=False)

Groups = {'Group A': ['Sri Lanka', 'England', 'South Africa', 'Pakistan'],
          'Group B': ['India', 'Bangladesh', 'Australia', 'West Indies']}

df2 = pd.DataFrame(Groups, columns=['Group A', 'Group B'])
df2.to_csv('Groups.csv', index=False)

print(".........Welcome to 2021-Men's T20 World Cup Tournament.........")
print()
print('............GAME RULES............')
print()
print("1. You can select a team from either Group A or Group B.")
print("2. After selecting a team, the computer will randomly select a team from the same group as your opponent.")
print("3. You can choose to make edits to the teams according to your liking BEFORE the game start.")
print("3. If you win the toss, you can choose whether to BAT or BALL first.")
print("4. If you loose the toss you will Computer will decide the decision.")
print("5.You can choose to stop the match anytime you wish.")
print("6.Team with the highest marks wins.")
print()

print("~~~~~~~~~~~CHOOSE YOUR GROUP AND TEAM~~~~~~~~~~~~~")
print()
print("What group do you want to choose? :\n 1)Group A \n 2)Group B ")
print()
print('.....THIS IS GROUP A.....')
print(df2['Group A'])
print()
print('.....THIS IS GROUP B.....')
print(df2['Group B'])
print()
choose = (int(input("Enter either '1' or '2' to choose your group:")))
if choose == 1:
    team_1 = input('Choose your Team:')
    team_2 = random.choice(df2['Group A'])
    while True:
        if team_1 == team_2:
            team_2 = random.choice(df2['Group A'])
        else:
            break
    print('This is your opponent:', team_2)
    print()
    if team_1 == 'Sri Lanka':
        print(df1['Sri Lanka'])
    elif team_1 == 'England':
        print(df1['England'])
    elif team_1 == 'Pakistan':
        print(df1['Pakistan'])
    elif team_1 == 'South Africa':
        print(df1['South africa'])

    if team_2 == 'Sri Lanka':
        print(df1['Sri Lanka'])
    elif team_2 == 'England':
        print(df1['England'])
    elif team_2 == 'Pakistan':
        print(df1['Pakistan'])
    elif team_2 == 'South Africa':
        print(df1['South Africa'])

    print('Do you want to make any changes to the team members?')
    change = str(input('Yes/No :'))
    if change == 'Yes':
        amount = int(input('How many changes do you want to make? :'))
        for i in range(amount):
            getting_changed = str(input('Please Enter the name of the player you wish you change:'))
            new_player = str(input('Please Enter the name of the Replacing player:'))
            df1.loc[df1[team_1] == getting_changed, team_1] = new_player
            df1.loc[df1[team_2] == getting_changed, team_2] = new_player
            print(df1[team_1])
            print(df1[team_2])
        print()
        print('THIS WILL BE YOUR FINALIZED TEAMS!')
    else:
        print('THIS WILL BE YOUR FINALIZED TEAMS!')

elif choose == 2:
    team_1 = input('Choose your Team:')
    team_2 = random.choice(df2['Group B'])
    while True:
        if team_1 == team_2:
            team_2 = random.choice(df2['Group B'])
        else:
            break
    print('This is your opponent:', team_2)
    print()
    if team_1 == 'India':
        print(df1['India'])
    elif team_1 == 'Bangladesh':
        print(df1['Bangladesh'])
    elif team_1 == 'Australia':
        print(df1['Australia'])
    elif team_1 == 'West Indies':
        print(df1['West Indies'])

    if team_2 == 'India':
        print(df1['India'])
    elif team_2 == 'Bangladesh':
        print(df1['Bangladesh'])
    elif team_2 == 'Australia':
        print(df1['Australia'])
    elif team_2 == 'West Indies':
        print(df1['West Indies'])

    print()
    print('Do you want to make any changes to the team members?')
    change = str(input('Yes/No :'))
    if change == 'Yes':
        amount = int(input('How many changes do you want to make? :'))
        for i in range(amount):
            getting_changed = str(input('Please Enter the name of the player you wish you change:'))
            new_player = str(input('Please Enter the name of the Replacing player:'))
            df1.loc[df1[team_1] == getting_changed, team_1] = new_player
            df1.loc[df1[team_2] == getting_changed, team_2] = new_player
            print(df1[team_1])
            print(df1[team_2])
        print()
        print('THIS WILL BE YOUR FINALIZED TEAMS!')
    else:
        print('THIS WILL BE YOUR FINALIZED TEAMS!')

print()
print("~~~~~IT'S TIME FOR THE TOSS~~~~~")
user_toss = input("Type either 'HEADS' or 'TAILS' for the toss:")
opponent_toss = ""

random_toss = ['HEADS', 'TAILS']
random_field = ['BAT', 'BALL']
winning_side = ""
user_field = ""
opponent_field = ""

if user_toss == 'HEADS':
    opponent_toss = 'TAILS'
elif user_toss == 'TAILS':
    opponent_toss = 'HEADS'

if random.choice(random_toss) == user_toss:
    winning_side = "User"
    print('Congratulations!!~ You have won the toss!!')
    user_field = input("Do you want to 'BAT' or 'BALL' first? Choose your pick:")
    if user_field == 'BAT':
        opponent_field = 'BALL'
        print(" You are BATTING FIRST!!~")
        print('........1ST INNINGS............')
        while overs != 20 or wickets != 10:
            opponent = random.choice(list2)
            print()
            try:
                User = int(input("Enter a number between 1 to 6:"))
                if User <= 6 and User>= 1:
                    if User == opponent:
                        print("You are OUT!! It's a", random.choice(list3))
                        print('Wicket is taken by', random.choice(df1[team_2]))
                        wickets = wickets + 1
                    else:
                        balls = balls + 1
                        runs = runs + User
                        if balls == 6:
                            overs = overs + 1
                        print()
                        print('Total runs:', runs)
                        print('Total wickets:', wickets)
                        print('Remaining overs:', 20 - overs)

                    your_choice = input("Do you want to resume the game? Type 'YES' or 'NO' :")
                    if your_choice == 'NO':
                        print(".........2ND INNINGS.........")

                        print('Your opponent needs', runs+1, 'RUNS to win!')
                        print("You are BALLING NOW!!~")

                        opponent_field = 'BAT'
                        user_field = 'BALL'

                        while overs_1 != 20 or wickets_1 != 10:
                            while runs_1 < runs + 1:
                                opponent = random.choice(list2)
                                print()
                                User = int(input("Enter a number between 1 to 6:"))
                                if User == opponent:
                                    print("You NAILED IT! It's an OUT!! It's a", random.choice(list3))
                                    print('Wicket is taken by', random.choice(df1[team_1]))
                                    wickets_1 = wickets_1 + 1
                                else:
                                    balls_1 = balls_1 + 1
                                    runs_1 = runs_1 + User
                                    if balls_1 == 6:
                                        overs_1 = overs_1 + 1
                                    print()
                                    print('Total runs:', runs_1)
                                    print('Total wickets:', wickets_1)
                                    print('Remaining overs:', 20 - overs_1)

                            if runs + 1 > runs_1:
                                print('You WON THE MATCH')
                                f = open("matchdata.txt", "a")
                                f.write("1st Innings-User \n")
                                f.write(team_1 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                f.write("Total runs:"+str(runs)+"\n")
                                f.write("Total wickets:"+str(wickets)+"\n")
                                f.write("Remaining overs:"+str(20-overs)+"\n")

                                print()
                                f.write("2nd Innings-Opponent \n")
                                f.write(team_2 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                f.write("Total runs:"+str(runs_1)+"\n")
                                f.write("Total wickets:" + str(wickets_1) + "\n")
                                f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                f.write(team_1 + ' ' + "WON the MATCH!!")
                                f.close()
                                sys.exit()  # PROGRAM EXIT
                            else:
                                print('You LOST THE MATCH!')
                                f = open("matchdata.txt", "a")
                                f.write("1st Innings-User \n")
                                f.write(team_1 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                f.write("Total runs:"+str(runs)+"\n")
                                f.write("Total wickets:"+str(wickets)+"\n")
                                f.write("Remaining overs:" + str(20 - overs) + "\n")
                                print()
                                f.write("2nd Innings-Opponent \n")
                                f.write(team_2 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                f.write("Total runs:"+str(runs_1)+"\n")
                                f.write("Total wickets:" + str(wickets_1) + "\n")
                                f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                f.write(team_2 + ' ' + "WON the MATCH!!")
                                f.close()
                                sys.exit()
                        else:
                            print('')

                    else:
                        print()
                else:
                    print('Please Enter a Number between 1 and 6!!!')
            except ValueError:
                print("Please Enter a Valid number!!")

    elif user_field == 'BALL':
        opponent_field = 'BAT'
        print("You are BALLING FIRST!!~")
        print('........1ST INNINGS............')
        while overs != 20 or wickets != 10:
            try:
                User = int(input("Enter a number between 1 to 6:"))
                if User <= 6 and User >= 1:
                    print()
                    opponent = random.choice(list2)
                    if User == opponent:
                        print("You NAILED IT! It's an OUT!! It's a", random.choice(list3))
                        print('Wicket is taken by', random.choice(df1[team_1]))
                        wickets = wickets + 1
                    else:
                        balls = balls + 1
                        runs = runs + User
                        if balls == 6:
                            overs = overs + 1
                        print()
                        print('Total runs:', runs)
                        print('Total wickets:', wickets)
                        print('Remaining overs:', 20 - overs)

                        your_choice = input("Do you want to resume the game? Type 'YES' or 'NO' :")
                        if your_choice == 'NO':
                            print(".........2ND INNINGS.........")

                            print('You needs', runs + 1, 'RUNS to win!')
                            print("You are BATTING NOW!!~")

                            opponent_field = 'BAll'
                            user_field = 'BAT'
                            while overs_1 != 20 or wickets_1 != 10:
                                while runs_1 < runs + 1:
                                    opponent = random.choice(list2)
                                    print()
                                    User = int(input("Enter a number between 1 to 6:"))
                                    if User == opponent:
                                        print("You are OUT!! It's a", random.choice(list3))
                                        print('Wicket is taken by', random.choice(df1[team_2]))
                                        wickets_1 = wickets_1 + 1
                                    else:
                                        balls_1 = balls_1 + 1
                                        runs_1 = runs_1 + User
                                        if balls_1 == 6:
                                            overs_1 = overs_1 + 1
                                        print()
                                        print('Total runs:', runs_1)
                                        print('Total wickets:', wickets_1)
                                        print('Remaining overs:', 20 - overs_1)

                                if runs + 1 > runs_1:
                                    print('You LOST THE MATCH')
                                    f = open("matchdata.txt", "a")
                                    f.write("1st Innings-Opponent \n")
                                    f.write(team_2 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                    f.write("Total runs:" + str(runs) + "\n")
                                    f.write("Total wickets:" + str(wickets) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs) + "\n")
                                    print()
                                    f.write("2nd Innings-User \n")
                                    f.write(team_1 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                    f.write("Total runs:" + str(runs_1) + "\n")
                                    f.write("Total wickets:" + str(wickets_1) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                    f.write(team_2 + ' ' + "WON the MATCH!!")
                                    f.close()
                                    sys.exit()  # PROGRAM EXIT
                                else:
                                    print('You WON THE MATCH!')
                                    f = open("matchdata.txt", "a")
                                    f.write("1st Innings-Opponent \n")
                                    f.write(team_2 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                    f.write("Total runs:" + str(runs) + "\n")
                                    f.write("Total wickets:" + str(wickets) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs) + "\n")

                                    print()
                                    f.write("2nd Innings-User \n")
                                    f.write(team_1 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                    f.write("Total runs:" + str(runs_1) + "\n")
                                    f.write("Total wickets:" + str(wickets_1) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                    f.write(team_1 + ' ' + "WON the MATCH!!")
                                    f.close()
                                    sys.exit()
                            else:
                                print('')
                        else:
                            print()
                else:
                    print('Please Enter a Number between 1 and 6!!!')
            except ValueError:
                print("Please Enter a Valid number!!")
    else:
        print('It is invalid!!')

else:
    winning_side = 'opponent'
    print('Your Opponent WON THE TOSS~')
    opponent_field = random.choice(random_field)
    if opponent_field == 'BAT':
        user_field = 'BALL'
        print("You are BALLING FIRST!!~")
        print('........1ST INNINGS............')
        while overs != 20 or wickets != 10:
            opponent = random.choice(list2)
            print()
            try:
                User = int(input("Enter a number between 1 to 6:"))
                if User <= 6 and User >= 1:
                    if opponent == User:
                        print("You NAILED IT! It's an OUT!! It's a", random.choice(list3))
                        print('Wicket is taken by', random.choice(df1[team_1]))
                        wickets = wickets + 1
                    else:
                        balls = balls + 1
                        runs = runs + User
                        if balls == 6:
                            overs = overs + 1
                        print()
                        print('Total runs:', runs)
                        print('Total wickets:', wickets)
                        print('Remaining overs:', 20 - overs)

                        your_choice = input("Do you want to resume the game? Type 'YES' or 'NO' :")
                        if your_choice == 'NO':
                            print(".........2ND INNINGS.........")

                            print('You needs', runs + 1, 'RUNS to win!')
                            print("You are BATTING NOW!!~")

                            opponent_field = 'BAll'
                            user_field = 'BAT'
                            while overs_1 != 20 or wickets_1 != 10:
                                while runs_1 < runs + 1:
                                    opponent = random.choice(list2)
                                    print()
                                    User = int(input("Enter a number between 1 to 6:"))
                                    if User == opponent:
                                        print("You are OUT!! It's a", random.choice(list3))
                                        print('Wicket is taken by', random.choice(df1[team_2]))
                                        wickets_1 = wickets_1 + 1
                                    else:
                                        balls_1 = balls_1 + 1
                                        runs_1 = runs_1 + User
                                        if balls_1 == 6:
                                            overs_1 = overs_1 + 1
                                        print()
                                        print('Total runs:', runs_1)
                                        print('Total wickets:', wickets_1)
                                        print('Remaining overs:', 20 - overs_1)

                                if runs + 1 > runs_1:
                                    print('You LOST THE MATCH')
                                    f = open("matchdata.txt", "a")
                                    f.write("1st Innings-Opponent \n")
                                    f.write(team_2 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                    f.write("Total runs:" + str(runs) + "\n")
                                    f.write("Total wickets:" + str(wickets) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs) + "\n")
                                    print()
                                    f.write("2nd Innings-User \n")
                                    f.write(team_1 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                    f.write("Total runs:" + str(runs_1) + "\n")
                                    f.write("Total wickets:" + str(wickets_1) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                    f.write(team_2 + ' ' + "WON the MATCH!!")
                                    f.close()
                                    sys.exit()  # PROGRAM EXIT
                                else:
                                    print('You WON THE MATCH!')
                                    f = open("matchdata.txt", "a")
                                    f.write("1st Innings-Opponent \n")
                                    f.write(team_2 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                    f.write("Total runs:" + str(runs) + "\n")
                                    f.write("Total wickets:" + str(wickets) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs) + "\n")

                                    print()
                                    f.write("2nd Innings-User \n")
                                    f.write(team_1 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                    f.write("Total runs:" + str(runs_1) + "\n")
                                    f.write("Total wickets:" + str(wickets_1) + "\n")
                                    f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                    f.write(team_1 + ' ' + "WON the MATCH!!")
                                    f.close()
                                    sys.exit()
                            else:
                                print('')
                        else:
                            print()
                else:
                    print('Please Enter a Number between 1 and 6!!!')
            except ValueError:
                print("Please Enter a Valid number!!")

    elif opponent_field == 'BALL':
        user_field = 'BAT'
        print("You are BATTING FIRST!!~")
        print('........1ST INNINGS............')
        while overs != 20 or wickets != 10:
            try:
                User = int(input("Enter a number between 1 to 6:"))
                if User <= 6 and User >= 1:
                    print()
                    opponent = random.choice(list2)
                    if User == opponent:
                        print("You are OUT!! It's a", random.choice(list3))
                        print('Wicket is taken by', random.choice(df1[team_2]))
                        wickets = wickets + 1
                    else:
                        if balls == 6:
                            overs = overs + 1
                        print()
                        print('Total runs:', runs)
                        balls = balls + 1
                        runs = runs + User
                        print('Total wickets:', wickets)
                        print('Remaining overs:', 20 - overs)

                        your_choice = input("Do you want to resume the game? Type 'YES' or 'NO' :")
                        if your_choice == 'NO':
                            if your_choice == 'NO':
                                print(".........2ND INNINGS.........")

                                print('Your opponent needs', runs + 1, 'RUNS to win!')
                                print("You are BALLING NOW!!~")

                                opponent_field = 'BAT'
                                user_field = 'BALL'
                                while overs_1 != 20 or wickets_1 != 10:
                                    while runs_1 < runs + 1:
                                        opponent = random.choice(list2)
                                        print()
                                        User = int(input("Enter a number between 1 to 6:"))
                                        if User == opponent:
                                            print("You NAILED IT! It's an OUT!! It's a", random.choice(list3))
                                            print('Wicket is taken by', random.choice(df1[team_1]))
                                            wickets_1 = wickets_1 + 1
                                        else:
                                            balls_1 = balls_1 + 1
                                            runs_1 = runs_1 + User
                                            if balls_1 == 6:
                                                overs_1 = overs_1 + 1
                                            print()
                                            print('Total runs:', runs_1)
                                            print('Total wickets:', wickets_1)
                                            print('Remaining overs:', 20 - overs_1)

                                    if runs + 1 > runs_1:
                                        print('You WON THE MATCH')
                                        f = open("matchdata.txt", "a")
                                        f.write("1st Innings-User \n")
                                        f.write(team_1 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                        f.write("Total runs:" + str(runs) + "\n")
                                        f.write("Total wickets:" + str(wickets) + "\n")
                                        f.write("Remaining overs:" + str(20 - overs) + "\n")

                                        print()
                                        f.write("2nd Innings-Opponent \n")
                                        f.write(team_2 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                        f.write("Total runs:" + str(runs_1) + "\n")
                                        f.write("Total wickets:" + str(wickets_1) + "\n")
                                        f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                        f.write(team_1 + ' ' + "WON the MATCH!!")
                                        f.close()
                                        sys.exit()  # PROGRAM EXIT
                                    else:
                                        print('You LOST THE MATCH!')
                                        f = open("matchdata.txt", "a")
                                        f.write("1st Innings-User \n")
                                        f.write(team_1 + ' ' + "is BATTING IN THE 1ST Innings \n")
                                        f.write("Total runs:" + str(runs) + "\n")
                                        f.write("Total wickets:" + str(wickets) + "\n")
                                        f.write("Remaining overs:" + str(20 - overs) + "\n")
                                        print()
                                        f.write("2nd Innings-Opponent \n")
                                        f.write(team_2 + ' ' + "is BATTING IN THE 2ND Innings \n")
                                        f.write("Total runs:" + str(runs_1) + "\n")
                                        f.write("Total wickets:" + str(wickets_1) + "\n")
                                        f.write("Remaining overs:" + str(20 - overs_1) + "\n")
                                        f.write(team_2 + ' ' + "WON the MATCH!!")
                                        f.close()
                                        sys.exit()
                                else:
                                    print('')
                            else:
                                print()
                else:
                    print('Please Enter a Number between 1 and 6!!!')
            except ValueError:
                print("Please Enter a Valid number!!")
    else:
        print('It is invalid!!')


