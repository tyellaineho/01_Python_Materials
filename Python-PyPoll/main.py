import os
import csv
import sys

csv_path = os.path.join("Resources", "election_data.csv")

# `Voter ID`, `County`, and `Candidate`
with open(csv_path, newline='') as polldata:
    pollreader = csv.reader(polldata)
    next(pollreader)
    poll_list = [row for row in pollreader]

    # * The total number of votes cast
    total_votes = len(poll_list)

    # * A complete list of candidates who received votes
    candidate_list = list(set([cand[2] for cand in poll_list]))

    # * The total number of votes each candidate won
    vote_dict = {}
    for candidate in candidate_list:
        candidate_votes = len(
            [row for row in poll_list if row[2] == candidate])
        vote_dict.update({candidate: candidate_votes})

    # * The percentage of votes each candidate won
    pct_dict = {}
    for candidate in candidate_list:
        candidate_pct = round((vote_dict.get(candidate)/total_votes)*100, 2)
        pct_dict.update({candidate: candidate_pct})

    # * The winner of the election based on popular vote.
    for key, value in pct_dict.items():
        if value == max(pct_dict.values()):
            winner = key
            
# #print result to terminal and .txt
def print_results():
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {total_votes} ')
    print("----------------------------")
    for candidate in candidate_list:
        print(f"{candidate} : {vote_dict.get(candidate)} votes ({pct_dict.get(candidate)}%)")
    print("----------------------------")
    print(f'Winner: {winner}')

print_results()

sys.stdout = open('electionresults.txt', 'w')
print_results()
sys.stdout.close()
