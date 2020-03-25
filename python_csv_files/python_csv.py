import csv
with open("abc.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # print(csvreader)
    # for column in csvreader:
    #     print(column)
    #
    # for row in csvreader:
    #     print(row[-1])

    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row[-1])

import csv

def x(csv_file_name):
    new_user_data = ['Andy', 'Wakefield', 'asdsad@asdasd.com']

    with open("abc.csv", newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        for user in csvreader:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data

print(x("abc.csv"))



def append_list_as_row(file_name, list_if_elem):
    with open('abc.csv', 'a+', newline='dddddd') as write_obj:
        csv_writer = writer(write_obj)

        csv_writer.writerow(list_of_elem)

def create_new_user_data_csv(old_user_data_file="abc.csv", new_file_name='new_user_data.csv'):
    new_user_data = x(create_new_user_data_csv)
    new_file = open(new_file_name, 'w')

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)

create_new_user_data_csv()






