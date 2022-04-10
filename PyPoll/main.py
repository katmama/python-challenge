import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0

candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(csvpath) as csvfile:
    csvpath = csv.reader(csvfile, delimiter=",")
    
    headers = next(csvpath)
    
    for row in csvpath:
        
        total_votes += 1
        
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1


    
    print("Election Results")
    print("-------------------------")
    print("Total Votes: ",total_votes)
    print("-------------------------")
        
        
        
        
   
    
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        
        print(candidate_results)
        
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    
    print("---------------------------")
    print("Winner: ", winning_candidate)
    