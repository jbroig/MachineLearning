#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Persons on the enron dataset
print len(enron_data)

#Features
print len(enron_data.values()[0])

#POI's
count = 0

for i in enron_data.values():
    if i['poi'] == 1:
        count +=1

print count

#Query the dataset 1
a = enron_data['PRENTICE JAMES']['total_stock_value']
print a

#Query the dataset 2
b = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print b 

#Query the dataset 3
c = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print c

#Follow the money

names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
for i in names:
    print enron_data[i]['total_payments']

#Dealing with unfilled features

quantified_salary = 0
email_address = 0
for i in enron_data.values():
    if i['salary'] != 'NaN':
        quantified_salary += 1

    if i['email_address'] != 'NaN':
        email_address += 1
    
print quantified_salary
print email_address