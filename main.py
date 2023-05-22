# An app that gets as input the amount of a bill for a particular period and the days that each of the flatmates stayed in the house for that period and 
# returns how much each flatmate has to pay. It also generates a PDF report stating the names of the flatmates, the period and how much each of them have to pay.

from flat import Bill, Flatmate
from pdfreport import PdfReport


amount = float(input("Hello user, enter the bill amount: "))
period = input("Please enter the period: (Month-Year)")

name1 = input("Enter your name: ")
days_in_the_house1 = int(input(f"How many days did {name1} stay in the house? "))

name2 = input("Enter the name of other flatmate: ")
days_in_the_house2 = int(input(f"How many days did {name2} stay in the house? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_the_house1)
flatmate2 = Flatmate(name2, days_in_the_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)