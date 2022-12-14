import matplotlib.pyplot as plt

start_sum = 1_500_000
percent = 0.2
salary_inflation = 0.08
salary = 150_000
years = 1
ress = []
yearss = []

res = start_sum

for i in range(years):
    res = res * (1 + percent)
    res = res + salary * 12 * (1 + salary_inflation)
    yearss.append(i)
    ress.append(res)
print('₽{:,.2f}'.format(res))

plt.plot(yearss, ress)
plt.show()
