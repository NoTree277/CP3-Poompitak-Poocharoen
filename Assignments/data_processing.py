import csv

# open Cities.csv file with csv.DictReader and read its content into a list of dictionary, cities_data
cities_data = []
with open('Cities.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities_data.append(r)

# open Countries.csv file with csv.DictReader and read its content into a list of dictionary, countries_data
countries_data = []
with open('Countries.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries_data.append(r)


def min_max_temp(cities_data):
    """Returns a list whose first and second elements are the min and the max temperatures of all the
    cities in cities_data.
    """
    temps = []
    for r in cities_data:
        temps.append(float(r['temperature']))
    return [min(temps), max(temps)]


def country_list(cities_data):
    """Returns a list of all the countries represented in cities_data.
    """
    countries = []
    for r in cities_data:
        if r['country'] not in countries:
            countries.append(r['country'])
    return countries


def average_country_temp(cities_data):
    """
    Return a dictionary whose key:value pair is country name:its average temp. The size of the
    returned dictionary must equal the number of countries represented.
    """
    d = dict()
    for country in country_list(cities_data):
        t = []
        for r in cities_data:
            if r['country'] == country:
                t.append(float(r['temperature']))
        d[country] = sum(t) / len(t)
    return d


def country_max_diff_temperature(cities_data):
    d = dict()
    for country in country_list(cities_data):
        tmax = [0]
        tmin = [100]
        for r in cities_data:
            if r['country'] == country:
                if float(r['temperature']) > float(tmax[0]):
                    tmax.clear()
                    tmax.append(float(r['temperature']))
                if float(r['temperature']) < float(tmin[0]):
                    tmin.clear()
                    tmin.append(float(r['temperature']))
        d[country] = f'{tmax[0] - tmin[0]:.2f}'
    return d


def northern_sounthern_most_cities(cities_data):
    global c_lamax, c_lamin
    lamax = [0]
    lamin = [0]
    for country in country_list(cities_data):
        for r in cities_data:
            if r['country'] == country:
                if float(r['latitude']) > float(lamax[0]):
                    lamax.clear()
                    lamax.append(float(r['latitude']))
                    c_lamax = (r['city'], r['country'])
                if float(r['latitude']) < float(lamax[0]):
                    lamin.clear()
                    lamin.append(float(r['latitude']))
                    c_lamin = (r['city'], r['country'])
    c_final = [c_lamax, c_lamin]
    return c_final


def population_countries_no_coastline_in_EU(countries_data):
    d = dict()
    for country in country_list(countries_data):
        for r in countries_data:
            if r['EU'] == 'yes':
                if r['coastline'] == 'no':
                    d[country] = r['EU'], r['coastline']
    return d


def cities_in_EU(cities_data, countries_data):
    d = dict()
    c = []
    eu = []
    for city in cities_data:
        for country in countries_data:
            c = city['city']
            eu = country['EU']
        d[c] = eu
    return d

def average_EU_city_temperature(cities_data, countries_data):
    eu_temp = []
    no_eu_temp = []
    for city in cities_data:
        for country in countries_data:
            if country['EU'] == 'yes':
                eu_temp.append(float(city['temperature']))
            if country['EU'] == 'no':
                no_eu_temp.append(float(city['temperature']))
    eu_temp = sum(eu_temp) / len(eu_temp)
    no_eu_temp = sum(no_eu_temp) / len(no_eu_temp)
    avg = (eu_temp, no_eu_temp)
    return avg


# open Players.csv file with csv.DictReader and read its content into a list of dictionary, players_data
players_data = []
with open('Players.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        players_data.append(r)

# open Teams.csv file with csv.DictReader and read its content into a list of dictionary, teams_data
teams_data = []
with open('Teams.csv', 'r') as f:
    rows = csv.DictReader(f)
    for r in rows:
        teams_data.append(r)


def average_passes(players_data):
    """Returns a tuple with four elements; the first, second, third, and fourth elements show the average number of passes made by defenders, midfielders, forwards, and goalkeepers, respectively
    """


def max_GF_GA_ratio(teams_data):
    """Returns the string name of a team with highest ratio of goalsFor to goalsAgainst
    """


def whose_player_list(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a player who is on a team ranked in the top 20, plays less than 200 minutes and makes more than 100 passes; the format for each tuple is (player's surname, team played for, team ranking, minutes played, number of passes)
    """

    # Reminder: Convert minutes and passes to integers before comparing to values


def team_list_passes_per_minute(players_data, teams_data):
    """Returns a list of tuples; each tuple has information about a team and its passes per minute value generated by its players
    """


# open Titanic.csv file with csv.DictReader and read its content into a list of dictionary, titanic_data
titanic_data = []
with open('Titanic.csv') as f:
    rows = csv.DictReader(f)
    for r in rows:
        titanic_data.append(r)


def number_married_women_embarked(place_embarked, age_threshold, titanic_data):
    """Returns the number of married women over age_threshold embarked at place_embarked

    Your test code must include at least five test cases with different combinations of place_embarked and age_threshold
    """


def class_survival_rate(passenger_class, titanic_data):
    """Returns the survival rate of a given passenger_class

    Your test case must test all the three passenger classes
    """


def gender_survival_number(passenger_gender, titanic_data):
    """Returns the number of survivors for a given gender, M (male) or F (female)

    Your test case must test both genders
    """


def twin_list(titanic_data):
    """Returns a list of tuples of pairs of passengers who are likely to be twin children, i.e., same last name, same age, same place of embarkment, and age is under 18; each tuple has the following format: (person1's "last name" + "first name", person2's "last name" + "first name")
    """
