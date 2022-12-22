import matplotlib.pyplot as plt

# rubbles
# start_sum = 1_500_000
# percent = 0.3
# salary_inflation = 0.10
# salary = 200_000
# years = 2
# ress = []
# yearss = []
#
# res = start_sum
#
# for i in range(years):
#     res = res * (1 + percent)
#     res = res + salary * 12
#     salary = salary * (1 + salary_inflation)
#     yearss.append(i)
#     ress.append(res)
# print('₽{:,.2f}'.format(res))
#
# plt.plot(yearss, ress)
# plt.show()


start_sum = 40_000
percent = 0.5
salary_inflation = 0.05
salary = 2_800
years = 20
ress = []
yearss = []

res = start_sum

for i in range(years):
    if i % 5 == 0:
        print('Год: ' + str(i))
        print('Зарплата: ${:,.2f}'.format(salary * 12 * (1 + salary_inflation)))
        print('Прирост инвестиций ${:,.2f}'.format(res * (1 + percent)))
    res = res * (1 + percent)
    res = res + salary * 12
    salary = salary * (1 + salary_inflation)
    yearss.append(i)
    ress.append(res)
print('${:,.2f}'.format(res))

plt.plot(yearss, ress)
plt.show()
