# Financial Analysis

import os
import csv

file_path = os.path.join("budget_data.csv")

date_list = []
revenue_list = []
total_revenue = 0
total_change = 0
change_max = ['',0]
change_min = ['',0]

with open("budget_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        date = row[0]
        revenue = float(row[1])
        date_list.append(date)
        revenue_list.append(revenue)
        total_revenue += revenue
   
    # Calculation    
    total_month = len(date_list)
    for i in range(1,len(date_list)):
        change = revenue_list[i]-revenue_list[i-1]
        total_change += change
        if change > change_max[1]:
            change_max = [date_list[i],change]
        if change < change_min[1]:
            change_min = [date_list[i],change]
        average_change = total_change / total_month
        
        # Results    
        line1 = 'Financial Analysis'
        line2 = '------------------'
        line3 = 'Total Months: ' + str(total_month)
        line4 = 'Total Revenue: $' + str(round(total_revenue))
        line5 = 'Average Revenue Change: $' + str(round(average_change))
        line6 = 'Greatest Increase in Revenue: ' + change_max[0] + '($' + str(round(change_max[1])) + ')'
        line7 = 'Greatest Decrease in Revenue: ' + change_min[0] + '($' + str(round(change_min[1])) + ')'
        summary = []
        summary.extend([line1, line2, line3, line4, line5, line6, line7])
        
        print('')
        print("budget_data.csv")
        for line in summary:
            print(line)
        print('')
        
        # Writing
        output_file_path = 'budget_analysis.txt'
        with open(output_file_path, 'w') as file_out:
            for line in summary:
                file_out.write(line + '\n')