# Import the necessary dependencies for os.path.join()
import os
import csv

# Intial variables setting
candidate_list = []
unique_candidate_list = []
unique_candidate_list_sorted = []
cumul_votecount = 0
counter = 0
pct_vote = 0.00
winner_num_votes = 0
winner_name = []
outputfile = []

# Open file election_data.csv
csvpoll = os.path.join("Resources", "election_data.csv")

with open(csvpoll, encoding="utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Set the loop to start past the header
    csvheader = next(csvfile)

    # Loop through the file counting the rows
    for row in csvreader:

        # Build list of candidate (one entry per vote)
        candidate_list.append(row[2])

# Take lenght of candidate list (one entry per vote) as vote count
cumul_votecount = int(len(candidate_list))
# Parse candidate list
# Keep unique names only to draw list of candidates
unique_candidate_list = list(set(candidate_list))

# Display results on screen
print("\nElection Results")
print("-----------------------------")
print(f"Total Votes: ", cumul_votecount)
print("-----------------------------")

# Loop list of candidates to count votes,
# Calculate percent votes and display on screen 
for candidate in unique_candidate_list:
    counter =  candidate_list.count(candidate)
    pct_vote = f"{counter / cumul_votecount:.3%}"
    print(f"{candidate} : {pct_vote} ({counter})")

    # Build list with candidates results for writing to output file 
    outputfile.append(candidate)
    outputfile.append(pct_vote)
    outputfile.append(counter)

    # Store name of candidate with most votes: winner
    if counter > winner_num_votes:
        winner_num_votes = counter
        winner_name = candidate

# Display name of winner on screen
print("-----------------------------")
print(f"Winner: ", winner_name)
print("-----------------------------\n")

# Build list to write to output file
output_to_file = [
    "Total Votes", cumul_votecount,
    outputfile,
    "Winner", winner_name,
]

# Create path to output file
outputfile = os.path.join("analysis", "output.csv")

# Write data to file output.csv
with open(outputfile, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(output_to_file)

csvfile.close()