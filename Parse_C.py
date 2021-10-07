import csv
import json


def Parsing_Covid():
    fileOPEN = open('covid_cases.json')
    getDATA = json.load(fileOPEN) # Get Data DATE_REPORTED, CTRY_TERR, NO_CASES, and DEATHS.

    DATE_REPORTED = []
    CTRY_TERR = []
    NO_CASES = []
    DEATHS = []

    for reported in getDATA['records']:
        DATE_REPORTED.append(reported['dateRep'])

    for country in getDATA['records']:
        CTRY_TERR.append(country['countriesAndTerritories'])

    for cases in getDATA['records']:
        NO_CASES.append(cases['cases'])

    for deaths in getDATA['records']:
        DEATHS.append(deaths['deaths'])

    COLS_NAMES = ["dateRep", "countriesAndTerritories", "cases", "deaths"]

    with open('/home/devasc/labs/devnet-src/PRELIM_SKILLS_EXAM/Covid_Cases.csv', newline = "", mode = "w") as csvGenerator:
        createCSV = csv.writer(csvGenerator)
        createCSV.writerow(COLS_NAMES)

        for cases_csv in range(len(DATE_REPORTED)):
            data = [DATE_REPORTED[cases_csv], CTRY_TERR[cases_csv], NO_CASES[cases_csv], DEATHS[cases_csv]]
            createCSV.writerow(data)

Parsing_Covid()