import os
import csv

candidate_list = []
unique_candidate_list = []
unique_candidate_list_sorted = []
cumul_votecount = 0
counter = 0
pct_vote = 0.00
winner_num_votes = 0
winner_name = []

csvpoll = os.path.join("Resources", "election_data.csv")

with open(csvpoll, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Set the loop to start past the header
    csvheader = next(csvfile)

    # Loop through the file counting the rows
    for row in csvreader:

        # Build list
        candidate_list.append(row[2])

cumul_votecount = int(len(candidate_list))
unique_candidate_list = list(set(candidate_list))

print(cumul_votecount)

for candidate in unique_candidate_list:
    counter =  candidate_list.count(candidate)
    pct_vote = counter / cumul_votecount
    print(candidate, counter, pct_vote)
    if counter > winner_num_votes:
        winner_num_votes = counter
        winner_name = candidate

print(winner_name)


