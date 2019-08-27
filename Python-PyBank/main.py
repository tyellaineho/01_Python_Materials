import os
import csv

csv_path = os.path.join("..","Resources", "budget_data.csv")

with open(csv_path, newline='') as bankdata:
    bankreader = csv.reader(bankdata)
    next(bankreader) #skip heading

    bank_list= [row for row in bankreader] #accumulate your data into a list

    netprofit = [int(row[1]) for row in bank_list] #accumulate the profit into a list

    total = sum(netprofit) #sum list into variable total

    months = len(netprofit) #calculate months

    profitchange = [int(netprofit[i] - netprofit[i-1]) for i in range(1,months)] #calculate the change in profit and accumulate into list

    changeaverage = sum(profitchange)/len(profitchange) #calculate average

    changemax = max(profitchange) #retrieve maximum change
    changemin = min(profitchange) #retriece minimum change

    maxindex = profitchange.index(changemax) #retrieve index number
    minindex = profitchange.index(changemin) #retrieve index number

    maxmonth = bank_list[int(maxindex + 1)][0] #retrieve month value and increment by 1
    minmonth = bank_list[int(minindex + 1)][0] #retrieve month value and increment by 1

    #print result to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(changeaverage,2)}')
    print(f'Greatest Increase in Profits: {maxmonth} (${changemax})')
    print(f'Greatest Decrease in Profits: {minmonth} (${changemin})')
    #print result to .txt
    financialanalysis = open('financialanalysis.txt', 'w')
    print("Financial Analysis", file = financialanalysis)
    print("----------------------------", file = financialanalysis)
    print(f'Total Months: {months}', file = financialanalysis)
    print(f'Total: ${total}', file = financialanalysis)
    print(f'Average Change: ${round(changeaverage,2)}', file = financialanalysis)
    print(f'Greatest Increase in Profits: {maxmonth} (${changemax})', file = financialanalysis)
    print(f'Greatest Decrease in Profits: {minmonth} (${changemin})', file = financialanalysis)
    financialanalysis.close()