# Import  Import modules os and csv
import os
import csv


# Set the path for the CSV file in PyBankcsv and the Output text  file 

mypathinput =r"C:\Users\ssamlani\OneDrive\VSC_Doc\03_Python_Sabir\election_data.csv"
mypathoutput =r"C:\Users\ssamlani\OneDrive\VSC_Doc\03_Python_Sabir\PyPoll_FinAnlz_Output_Sabir.txt"

PyPollcsv = os.path.join(mypathinput)
Output_txt = os.path.join(mypathoutput)

#Create dictionary to use for  candidate name and vote count.
poll = {}

#initiliaze var
total_votes = 0

#gets data file
with open(mypathinput, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #skips header line
    next(csvread, None)

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create empty list for candidates  vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 2))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

    print('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        print(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    print('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints to file

with open(mypathoutput, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(mypathoutput, 'r') as readfile:
    print(readfile.read())