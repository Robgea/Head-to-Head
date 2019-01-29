import csv
from judging_info import school_success_dict, counting_dict, ignore_list, school_dict
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




def head_to_head_calc(ignore, schools, success_dict)
    for judge_record in os.listdir('.'):
        if not judge_record.endswith('.csv'):
            print(f'Skipping... {judge_record}')
            continue
        elif judge_record == 'Head_to_Head_Results.csv':
            continue
        else:
            #read the file
            print("Counting judge record for..." + judgeRecord)
            csvFileObj = open(judgeRecord)
            recordReader = csv.reader(csvFileObj)
            recordlist = list(recordReader)

            for row in recordlist:
                aff_team = row[4]
                neg_team = row[5]
                aff_team = aff_team[:-3]
                neg_team = neg_team[:-3]


                if row[2] == 'Event':
                    continue

                else:
                  if (aff_team in ignore) or (neg_team in ignore):
                      ignore_doc.write(f'{recordEntry} has a bad round in {row[0]} with {aff_team}.\n')
                  elif (aff_team in schools) and (neg_team in schools):
                      aff_lookup = schools[aff_team]
                      neg_lookup = schools[neg_team]
                      if row[6].startswith('AFF'):
                          try:
                              success_dict[aff_lookup][neg_lookup + ' Aff Wins'] += 1
                              success_dict[aff_lookup][neg_lookup + ' Aff Total'] += 1
                              success_dict[aff_lookup]['Aff Wins'] += 1
                              success_dict[aff_lookup]['Aff Total'] += 1
                              success_dict[neg_lookup][aff_lookup + ' Neg Total'] += 1
                              success_dict[neg_lookup]['Neg Total'] += 1
                          except:
                              print(f"Something fucky happened. {row[0]} with {aff_team} and {neg_team}.")
                      elif row[6].startswith('NEG'):
                          try:
                              success_dict[aff_lookup][neg_lookup + ' Aff Total'] += 1
                              success_dict[aff_lookup]['Aff Total'] += 1
                              success_dict[neg_lookup][aff_lookup + ' Neg Wins'] += 1
                              success_dict[neg_lookup][aff_lookup + ' Neg Total'] += 1
                              success_dict[neg_lookup]['Neg Wins'] += 1
                              success_dict[neg_lookup]['Neg Total'] += 1
                          except:
                              print(f"Something fucky happened. {row[0]} with {aff_team} and {neg_team}.")
                  else:
                      print('Something really weird happened.')







# for each row of the CSV write out the key and then each of the values