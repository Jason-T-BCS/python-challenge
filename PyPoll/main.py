# Election Analysis

import os
import csv

file_path = os.path.join("election_data.csv")

keys = ['Candidate', 'Number of Votes', 'Percentage of Votes']
voter_id = []
candidates = []
candidate_number = {}
winner_vote = 0

with open(file_path, newline='') as file_in:
    csvreader = csv.DictReader(file_in, delimiter = ',')
    for row in csvreader:
        candidate = row['Candidate']
        voter_id.append(row['Voter ID'])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_number[candidate] = 1
        else:
            candidate_number[candidate] += 1

# Calculation
total_votes = len(voter_id)
candidate_percentage = {candidate : candidate_number[candidate]/total_votes \
                        for candidate in candidates}
for item in candidate_percentage.items():
    if item[1] > winner_vote:
        winner_vote = item[1]
        winner = item[0]

# Results
results = []
results.append('Election Results')
results.append('-----------------')
results.append(f"Total Votes: {total_votes}")
results.append('-----------------')
for candidate in candidates:
    results.append("{}: ".format(candidate) + \
                    "{:.1%}".format(candidate_percentage[candidate]) + \
                    " ({})".format(candidate_number[candidate]))
results.append('-----------------')
results.append(f"Winner: {winner}")
results.append('-----------------')

for line in results:
    print(line)

# Writing
output_file_path = 'election_out.txt'
with open(output_file_path, 'w') as file_out:
    for line in results:
        file_out.write(line + '\n')
