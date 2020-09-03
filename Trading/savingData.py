import csv


with open('trade_database.csv','a',newline='')as csvfile:
    fieldnames = ['Exchange', 'Token', 'Ltp', 'Change', 'Exchange Timestamp', 'Volume']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    thewriter.writerow({'Exchange': 4, 'Token': 4, 'Ltp': 567, 'Change': 333,'Exchange Timestamp': 56, 'Volume':666})
