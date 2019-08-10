import os
import csv

csv_path = os.path.join("..","Resources", "election_data.csv")

#`Voter ID`, `County`, and `Candidate`
with open(csv_path, newline='') as polldata:
    pollreader = csv.reader(polldata)
    next(pollreader)
    poll_list = [row for row in pollreader]
    
    # * The total number of votes cast
    totalvotes = len(poll_list)
    
    # * A complete list of candidates who received votes
    candidates =[row[2] for row in poll_list]
    unique = set(candidates)
    candidate_list = list(unique)
    
    # * The total number of votes each candidate won
    khanct = [row for row in poll_list if row[2] == "Khan"]
    correyct = [row for row in poll_list if row[2] == "Correy"]
    lict = [row for row in poll_list if row[2] == "Li"]
    otooleyct = [row for row in poll_list if row[2] == "O'Tooley"]

    khantot = len(khanct)
    correytot = len(correyct)
    litot = len(lict)
    otooleytot = len(otooleyct)
    
    # * The percentage of votes each candidate won
    khanpct = (len(khanct) / totalvotes)*100
    correypct = (len(correyct) / totalvotes)*100
    lipct = (len(lict) / totalvotes)*100
    otooleypct = (len(otooleyct) / totalvotes)*100
    
    # * The winner of the election based on popular vote.
    
    if khantot >= correytot or litot or otooleytot:
        win = "Khan"
    elif correytot >= khantot or litot or otooleytot:
        win = "Correy"
    elif litot >= khantot or correytot or otooleytot:
        win = "Li"
    elif otooleytot >= khantot or correytot or litot:
        win = "O'Tooley"

#print result to terminal
print("Election Results")
print("----------------------------")
print(f'Total Votes: {totalvotes} ')
print("----------------------------")
print(f'Khan: {round(khanpct,3)}00% ({khantot})')
print(f'Correy: {round(correypct,3)}00% ({correytot})')
print(f'Li: {round(lipct,3)}00% ({litot})')
print(f"O'Tooley: {round(otooleypct,3)}00% ({otooleytot})")
print("----------------------------")
print(f'Winner: {win}')

#printed results to txt
electionfile = open('electionresults.txt', 'w')
print("Election Results", file = electionfile)
print("----------------------------", file = electionfile)
print(f'Total Votes: {totalvotes}', file = electionfile)
print("----------------------------")
print(f'Khan: {round(khanpct,3)}00% ({khantot})', file = electionfile)
print(f'Correy: {round(correypct,3)}00% ({correytot})', file = electionfile)
print(f'Li: {round(lipct,3)}00% ({litot})', file = electionfile)
print(f"O'Tooley: {round(otooleypct,3)}00% ({otooleytot})", file = electionfile)
print("----------------------------", file = electionfile)
print(f'Winner: {win}', file = electionfile)
electionfile.close()
