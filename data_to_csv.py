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
        print(user)
        with open('user_data/{}'.format(user), 'r') as user_file:
            for key in json.load(user_file).keys():
                title_line.append(key)
        break
    except AssertionError:
        continue


# Delete previous data
with open('questionnaire.csv'.format(user), 'w') as user_file:
    row_writer = csv.writer(user_file, delimiter=',')
    row_writer.writerow(title_line)
    for user in users:
        data_line = []
        print(user)
        data_line.append(user.split('.')[0])
        with open('user_data/{}'.format(user), 'r') as user_file:
            user_data = json.load(user_file)
        try:
            assert len(user_data.keys()) == 70
            assert user != 'current_user.txt'
        except AssertionError:
            print('Error with user {}. Check the data. Continuing anyway...'.format(user))
            continue
        except AttributeError:
            continue
        for key in user_data:
            if key == 'user_data':
                user_data_section = user_data[key]
                continue
            data_line.append(user_data[key])
            for key in user_data_section:
                data_line.append(user_data_section[key])

        row_writer.writerow(data_line)
        data_line = []






#     with open('program_data/{}.txt'.format(key)) as f:
#         length = len(f.readlines())
#     orig_key = key
#     for i in range(length):
#         i += 14 if orig_key == 'ZMA29_2' else 0
#         item_list.append(orig_key + '_' +  str('{:02d}'.format(i+1)))
#         key = orig_key[:-2] if orig_key[:3] == 'ZMA' else key
#         title_line.append(key + '_' +  str('{:02d}'.format(i+1)))
#         if orig_key[:3] == 'GAD' or orig_key[:3] == 'PHQ':
#             coding_adjust.append(1)
#         else:
#             coding_adjust.append(0)

# write_line(title_line)

# user_files = os.listdir('user_data/')
# users = [user.split('.')[0] for user in user_files]

# for uid in users:

#     print('Processing user {}...'.format(uid))

#     # Retrieve data
#     try:
#         with open('user_data/{}.json'.format(uid), 'r') as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         print('User \'{}\' ignored.'.format(uid))
#         continue

#     line = [uid]

#     # Format data for writing
#     for item in item_list:
#         try:
#             line.append(data[item])
#         except KeyError:
#             line.append('NA')

#     # Coding correction
#     for i in range(len(line)):
#         try:
#             line[i] -= coding_adjust[i]
#         except TypeError:
#             continue

#     write_line(line)