print("WRITE DATES IN THE FORMAT -> DD-MM-YYYY")
date_1 = input("Enter first date: ")
date_2 = input("Enter second date: ")

date_1 = date_1.split("-")
date_2 = date_2.split("-")
print(date_1, date_2, sep="//")
days = abs(int(date_1[0]) - int(date_2[0]))
months = abs(int(date_1[1]) - int(date_2[1]))
years = abs(int(date_1[2]) - int(date_2[2]))

months = months * 30
years = years * 365

total_days = days + months + years
print(total_days)
# print(days, months, years, sep="/")
