'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
from collections import namedtuple

company_number = int(input("Enter a number of companies: "))
companies = []
income_all_companies = []
for x in range(company_number):
    name = input("Please, enter company name: ")
    n1 = float(input("Please, enter income of the first quarter as a non-negative number: "))
    n2 = float(input("Please, enter income of the second quarter as a non-negative number: "))
    n3 = float(input("Please, enter income of the third quarter as a non-negative number: "))
    n4 = float(input("Please, enter income of the forth quarter as a non-negative number: "))
    company = namedtuple('company', 'name income_1 income_2 income_3 income_4')
    company_ = company(name, n1, n2, n3, n4)
    companies.append(list(company_))
    year_income = company_.income_1 + company_.income_2 + company_.income_3 + company_.income_4
    income_all_companies.append(year_income)

all_companies_total_income = 0
min_income = income_all_companies[0]
for x in income_all_companies:
    all_companies_total_income = x + all_companies_total_income
    if x < min_income:
        min_income = x

mean_of_income = all_companies_total_income / company_number
print(f"Average income across all the companies is {mean_of_income}.")
for company in companies:
    if sum(company[1:]) < mean_of_income:
        print(f"Company {company[0]} has a smaller total income than the average income across all the companies ({mean_of_income}).")
    print(f"Average income of company {company[0]} is {(company[1] + company[2] + company[3] + company[4])/4}.")
