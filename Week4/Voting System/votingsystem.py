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
        voting_data = {}
        with open(path, 'r') as votes:
            voting_reader = csv.reader(votes)
            voting_data['options'] = next(voting_reader)

            for vote in voting_reader:
                voting_data[f'vote_{len(voting_data)}'] = vote
            
    return voting_data


def plurality(votes):
    pass