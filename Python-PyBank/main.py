import os
import csv
import sys

csv_path = os.path.join("Resources", "budget_data.csv")

with open(csv_path, newline='') as bankdata:
    bankreader = csv.reader(bankdata)
    next(bankreader)  # skip heading

    bank_list = [row for row in bankreader]  # accumulate your data into a list

    # accumulate the profit into a list
    netprofit = [int(row[1]) for row in bank_list]

    total = sum(netprofit)  # sum list into variable total

    months = len(netprofit)  # calculate months

    # calculate the change in profit and accumulate into list
    profitchange = [int(netprofit[i] - netprofit[i-1])
                    for i in range(1, months)]

    changeaverage = sum(profitchange)/len(profitchange)  # calculate average

    changemax = max(profitchange)  # retrieve maximum change
    changemin = min(profitchange)  # retriece minimum change

    maxindex = profitchange.index(changemax)  # retrieve index number
    minindex = profitchange.index(changemin)  # retrieve index number

    # retrieve month value and increment by 1
    maxmonth = bank_list[int(maxindex + 1)][0]
    # retrieve month value and increment by 1
    minmonth = bank_list[int(minindex + 1)][0]

# print result to terminal
def print_results():
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(changeaverage,2)}')
    print(f'Greatest Increase in Profits: {maxmonth} (${changemax})')
    print(f'Greatest Decrease in Profits: {minmonth} (${changemin})')

print_results()

sys.stdout = open('financialanalysis.txt', 'w')
print_results()
sys.stdout.close()