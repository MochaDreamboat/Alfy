import json
import csv

'''
Returns Python dictionary containing options key w/ array of options
and each vote with an array of preferences. Accepts either csv or json.
'''
def file_loader(path, file_type):
    if file_type == 'json':
        with open(path) as votes:
            voting_data = json.load(votes)
    
    elif file_type == 'csv':
        with open(path, 'r') as votes:
            voting_reader = csv.reader(votes)

            voting_data = {
                'options': next(voting_reader)
            }

            for vote in voting_reader:
                voting_data[f'vote_{len(voting_data)}'] = vote

    return voting_data


'''
Receives dictionary of options and votes. Tallies votes and returns first, second and third
place winner. Vote determined by first preference of voter.
'''
def plurality(votes):
    preferences = votes['options']
    tally = {option:0 for i, option in enumerate(votes['options'])}
    
    del votes['options']

    for voter in votes.keys():
        tally[preferences[int(votes[voter][0])-1]] += 1

    preferences = sorted(preferences, key=lambda preference: tally[preference], reverse=True)
    
    return {
        f'{i+1}': preferences[i] for i in range(len(preferences))
    }

print(plurality(file_loader('./votes/abc_True.csv', 'csv')))