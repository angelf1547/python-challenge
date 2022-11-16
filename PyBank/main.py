#Import os Module
import os, csv

#Import CSV File

budget_path = os.path.join('Resources', 'budget_data.csv')
budget_path = 'PyBank/Resources/budget_data.csv'
budget_outpath = os.path.join('analysis','Results_Analysis.txt')
budget_outpath = '/Users/angelf15/Desktop/GitHub/python-challenge/PyBank/analysis/Results_Analysis.txt'


with open(budget_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    #Declaring Variables
    months = []
    profit = []
    revenue_change = []


    #Seperating Variables Using Append 
    for row in csv_reader:
        months.append(row[0])
        profit.append(int(row[1]))
        
    
    #Calculating Total Months and Total Profit 
    total_months = len(months)
    total_profit = sum(profit)
    
    #Calculate the Change in Revenue 
    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
    #Calculate Average Revenue
    revenue_average = sum(revenue_change) / len(revenue_change)

    #Calculate Greatest Increase and Decrease 
    greatest_increase = max(revenue_change)
    greatest_decrease = min(revenue_change)
  
    # Print Results 
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(revenue_average, 2)))
    print("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")")
    print("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")")


#Export .txt File
with open(budget_outpath, 'w') as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n----------------------------\n")
    txt_file.write("Total Months: " + str(total_months) + "\n")
    txt_file.write("Total: " + "$" + str(total_profit)  + "\n")
    txt_file.write("Average Change: " + "$" + str(round(revenue_average, 2))  + "\n")
    txt_file.write("Greatest Profit Increase: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "(" + "$" + str(greatest_increase) + ")\n")
    txt_file.write("Greatest Profit Decrease: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "(" + "$" + str(greatest_decrease) + ")\n")





