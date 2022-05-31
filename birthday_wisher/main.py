##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)


import smtplib, pandas, csv

empty = {}

birthdays = pandas.read_csv('birthdays.csv')
tup = birthdays['month'].tolist()
tup1 = birthdays['day'].tolist()
empty['month'] = tup
empty['day'] = tup1


















# with open("./Input/Names/invited_names.txt", 'r') as names_list:
#     names_list = names_list.readlines()
#     for name in names_list:
#         with open("./Input/Letters/starting_letter.txt", 'r') as letter_content:
#             letter_text = letter_content.read()
#             name = name.replace("\n", '')
#             path = "./Output/ReadyToSend/" + "Letter for " + name + ".txt"
#             with open(path, 'w') as letter:
#                 letter_text = letter_text.replace("[name]", name)
#                 letter.write(letter_text)
#
#

