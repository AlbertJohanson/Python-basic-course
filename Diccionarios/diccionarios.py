def run():
    my_dictionary = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    # for value in my_dictionary:
    #     print(my_dictionary[value])


    population_countries = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    # for country in population_countries.keys():
    #     print(country)

    # for country in population_countries.values():
    #     print(country)

    for country, population in population_countries.items():
        print(country + ' has ' + str(population) + ' people')

if __name__ == '__main__':
    run()