#import os module
import os, csv

#Reading and importing CSV File

election_path = os.path.join('Resources', 'election_data.csv')
election_path = 'PyPoll/Resources/election_data.csv'
election_outpath = os.path.join('Analysis', 'Budget_Analysis.text')
election_outpath = 'PyPoll/analysis/PyPoll_Results.txt'

with open(election_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    #Declaring Variables
    candidate_dict = {}
    ballot = []
    charles_candidate = 0
    diana_candidate = 0
    raymon_candidate = 0


    #Seperating Variables Using Append
    for row in csv_reader:
        ballot.append(row[0])
    
        # Calculating the number of total votes
        total_votes = len(ballot)

        if row[2] == "Charles Casper Stockham":
            charles_candidate += 1

        elif row[2] == "Diana DeGette":
            diana_candidate += 1

        elif row[2] == "Raymon Anthony Doane":
            raymon_candidate += 1


charles_percentage = round((charles_candidate/total_votes)*100,3)
diana_percentage = round((diana_candidate/total_votes)*100,3)
raymon_percentage = round((raymon_candidate/total_votes)*100,3)
    
candidate_dict = {"Charles Casper Stockham": charles_candidate,
                "Diana DeGette": diana_candidate,
                "Raymon Anthony Doane": raymon_candidate}

winner = max(candidate_dict, key=candidate_dict.get)



    



# Print Results
print("\nElection Results\n")
print("----------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("----------------------------\n")
print(f"Charles Casper Stockham: {charles_percentage}% ({charles_candidate})\n")
print(f"Diana DeGette: {diana_percentage}% ({diana_candidate})\n")
print(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_candidate}) \n")
print("----------------------------\n")
print(f"Winner: {winner}\n")


#Export .txt File
with open(election_outpath, 'w') as txt_file:
    txt_file.write("\nElection Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Charles Casper Stockham: {charles_percentage}% ({charles_candidate})\n")
    txt_file.write(f"Diana DeGette: {diana_percentage}% ({diana_candidate})\n")
    txt_file.write(f"Raymon Anthony Doane: {raymon_percentage}% ({raymon_candidate}) \n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Winner: {winner}\n")