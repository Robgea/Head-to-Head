import csv
from judging_info import school_success_dict, counting_dict, ignore_list
import os



#three outputs. CSV results, Ignore List Rounds, unread rounds.

# start this off
results_csv = open('Head_to_Head_Results.csv', 'w', newline='')
results_write = csv.writer(results_csv)
header_list = ["name",]
for key in counting_dict.keys():
    header_list.append(key)

results_write.writerow(header_list)

ignore_doc = open('ignored_rounds.txt', 'a')
error_doc = open('error_rounds.txt', 'a')


# for each row of the CSV write out the key and then each of the values