import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math
import numpy as np

new_cases = [702, 789, 910, 1127, 1289, 1367, 1536]
total_cases_values = [17967, 18756 , 19666, 20793, 22082, 23449, 24985]
plt.style.use('ggplot')

regression = LinearRegression()
regression.fit([[i] for i in range(0, 7)], new_cases)
prediction0 = regression.predict([[0]])[0]
total_cases = lambda d: 0.5*regression.coef_*(d**2) + 702*d + 17967

cases_change_figure = plt.figure("By Amr Elmowaled")

plt.xlabel("days")
plt.ylabel("number of new cases per day")
plt.xticks(range(0, 7), ['may ' + str(25 + i) for i in range(0, 7)])

plt.scatter(range(0, 7), new_cases, c="r", label="real new cases")
plt.plot([0, 6], regression.predict([[0], [6]]), label="cases predictions", c='b')
plt.title("corona cases per day will reach %d by june 21 "%
          (math.ceil(regression.predict([[27]])[0])))

plt.legend()
cases_change_figure.show()

total_cases_figure = plt.figure("by Amr Elmowaled")

plt.xlabel("days")
plt.ylabel("total cases per day")

plt.plot(np.arange(0, 7, .01), [total_cases(i) for i in np.arange(0, 7, .01)], label="prediction curve", c='g')
plt.scatter(range(0, 7), total_cases_values, c="orange", label="real total cases")
plt.xticks(range(0, 7), ['may ' + str(25 + i) for i in range(0, 7)])
plt.title("total corona cases will approx be %d by june 21"%total_cases(27))

plt.legend()
total_cases_figure.show()
plt.show()

def cases_method(d):
	"""this function gives more accurate results of calculating total cases at day (d) from may 25 but can't be represented as a curve and must take an integer"""
	return 17967 + sum(regression.predict([[i] for i in range(1, d+1)]))

