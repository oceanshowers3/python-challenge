# Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

#import everything we need to get started
import csv
import os
import sys

#set up the file path
electionDataCSV = os.path.join("Resources", "election_data.csv")

#variable list
numVotes = 0
candidates = []
candidateVotes = {}
winningCount = 0
winningCandidate = ""
originalStdout = sys.stdout

#open the budget_data CSV file
with open(electionDataCSV) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    #account for header
    next(csvReader, None)

    #for each vote in CSV file:
    for vote in csvReader:
        #calculate the total number of votes
        numVotes = numVotes + 1
        #create a list of unique candidate names
        candidateName = vote[2] 
        if candidateName not in candidates:
            candidates.append(candidateName)
            candidateVotes[candidateName] = 0
        # add vote to candidate’s count
        candidateVotes[candidateName] = candidateVotes[candidateName] + 1
        #calculate the percentage each candidate won
    for name in candidateVotes:
        #calculate the number of votes each candidate won
        votes = candidateVotes.get(name)
        votePercentage = float(votes) / float(numVotes) * 100
        #display the winner of the popular vote
        if (votes > winningCount):
            #checking to see if vote is larger than previous vote
            winningCount = votes
            winningCandidate = name
        # print each candidate’s voter count and percentage 
        voterOutput = f"{name}: {votePercentage:.2f}% ({votes})\n"
        print(voterOutput, end="") 
        with open('output.txt', 'a+') as f:
            sys.stdout = f 
            print(voterOutput, end="")
            sys.stdout = originalStdout
    #print the results
    print("Number of Votes: ", numVotes) 
    print("List of Candidates: ", candidates) 
    print("The winning candidate is: ", winningCandidate)  

    #print the results to txt file
    with open('output.txt', 'a+') as f:
        sys.stdout = f 
        print("Number of Votes: ", numVotes) 
        print("List of Candidates: ", candidates) 
        print("The winning candidate is: ", winningCandidate) 
        sys.stdout = originalStdout 