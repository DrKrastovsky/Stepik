countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
for country in countries:
    if city in countries[country]:
        print(f'INFO: {city} is a city in {country}')
        exit()
    else:
        continue
print(f'ERROR: Country for {city} not found')


