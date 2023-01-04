import csv
import os
filepath = os.path.join("Resources","election_data.csv") 
output_path = os.path.join("analysis","electionanalysis.txt")

#Defined everything
votes = {}
totalvotes = 0 
candidates = []
percentagewon= 0
winnervotes = 0
Winner = ""

#Read in the Data

with open(filepath) as file:
    reader = csv.reader(file)
    header = next(reader)
    firstrow = next(reader)
    for row in reader:
        totalvotes = totalvotes + 1
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            votes[candidate]= 0
        votes[candidate]=votes[candidate]+1

with open(output_path,"w") as file:
    output=(f"""
    Election Results
    -------------------------
    Total Votes: {totalvotes}
    -------------------------
    """)
    print(output)
    file.write(output)

    for candidate in votes:
        candidatevotes = votes.get(candidate)
        percentagewon = float(candidatevotes)/float(totalvotes) * 100
        if candidatevotes > winnervotes:
            winnervotes = candidatevotes
            Winner = candidate

        voteroutput=(f"""
        {candidate}: {percentagewon}% {candidatevotes}
        """)
        print(voteroutput)
        file.write(voteroutput)

    winneroutput=(f"""
    -------------------------
    Winner: {Winner}
    -------------------------
    """)
    print(winneroutput)

    file.write(winneroutput)
