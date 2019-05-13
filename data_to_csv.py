import csv
import json
import os

welcome_message = '''
This script takes all data from JSON files in the directory user_data, and compiles it into CSV format.

Warning! All data from questionnaire.csv is deleted before recompiling the data. If this is OK, please press Enter.
'''

input(welcome_message)

def write_line(line):
    with open('questionnaire.csv', 'a+') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(line)



title_line = ['id']

users = os.listdir('user_data')

for user in users:
    try:
        assert user != 'current_user.txt'
        with open('user_data/{}'.format(user), 'r') as user_file:
            for key in json.load(user_file).keys():
                title_line.append(key)
        break
    except AssertionError:
        continue


with open('questionnaire.csv'.format(user), 'w') as user_file:
    row_writer = csv.writer(user_file, delimiter=',')
    row_writer.writerow(title_line)
    for user in users:
        data_line = []
        data_line.append(user.split('.')[0])
        with open('user_data/{}'.format(user), 'r') as user_file:
            user_data = json.load(user_file)
        try:
            assert len(user_data.keys()) == 76
            assert user != 'current_user.txt'
        except AssertionError:
            print('Error with user {}. Check the data. Continuing anyway...'.format(user))
            continue
        except AttributeError:
            continue
        for key in user_data:
            data_line.append(user_data[key])

        row_writer.writerow(data_line)
        data_line = []
