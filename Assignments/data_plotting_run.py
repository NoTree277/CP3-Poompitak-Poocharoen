import data_processing as dp
import matplotlib.pyplot as plt

# Scatter plot of cities showing latitudes versus temperatures
x = []
y = []
for city in dp.cities_data:
    x.append(float(city['latitude']))
    y.append(float(city['temperature']))
plt.xlabel('latitude')
plt.ylabel('temperature')
plt.scatter(x, y)
plt.show()

# Bar chart showing average temperatures of all cities in each country
bars = [] # list of countries
temperature = [] # average temperature of each country
dict = dp.average_country_temp(dp.cities_data)
for key, value in dict.items():
    bars.append(key)
    temperature.append(value)

numbars = len(bars)
width = .75
plt.bar(range(numbars), temperature, width, align='center')
plt.xlabel('country')
plt.ylabel('temperature')
plt.xticks(range(numbars), bars, rotation='vertical')
print(bars)
print(temperature)
plt.show()

# Pie chart showing number of EU countries versus non-EU countries
numEU = 0
numNotEU = 0
for country in dp.countries_data:
    if country['EU'] == 'yes':
        numEU += 1
    else:
        numNotEU +=1
plt.pie([numEU, numNotEU], labels=['EU','not EU'], autopct='%1.1f%%')
plt.show()

# Bar chart showing population of countries that are in EU but do not have coastline

# your code here


# Pie chart showing number of EU cities versus non-EU cities

# your code here


# Scatter plot of players showing minutes played versus passes made;
# color each player based on their position (goalkeeper, defender, midfielder, forward)

# your code here


# Bar chart showing average number of passes made by each player postion (defender, midfielder, forward, goalkeeper)

# your code here


# Bar chart showing the survival rate in each passenger class; the three bars should be labeled 'first', 'second', 'third'

# your code here


# Pie chart showing the number of male survivors versus female survivors

# your code here
