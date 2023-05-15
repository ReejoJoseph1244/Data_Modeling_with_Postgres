import pandas as pd

# DATA CLEANING

#countries_of_the_world.csv
def country_clean():
    CountryData = pd.read_csv("Data/countries_of_the_world.csv")
    CountryData_clean = CountryData[['Country','Region','Area (sq. mi.)','Net migration','GDP ($ per capita)','Industry']]
    return CountryData_clean

#country_tax.csv
def country_tax_clean():
    Countrytax_clean = pd.read_csv("Data/country_tax.csv")
    return Countrytax_clean

def industry_clean():
    IndustryData_clean = pd.read_csv("Data/industry.csv")
    return IndustryData_clean

#position_of_countries.csv
def position_clean():
    positionData = pd.read_csv("Data/position_of_countries.csv")
    positionData_clean = positionData[['position','country','total_score','quantity_score','quality_score','business_score']]
    return positionData_clean

