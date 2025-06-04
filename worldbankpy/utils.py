import requests
import pandas


def build_indicators_df():
    world_bank_data_indicators_url = (
        "https://api.worldbank.org/v2/indicators?per_page=30000&format=json"
    )
    world_bank_data_indicators = requests.get(
        world_bank_data_indicators_url
    ).json()
    indicators_dataframe = pandas.DataFrame(world_bank_data_indicators[1])
    return indicators_dataframe


def build_countries_df():
    world_bank_countries_url = (
        "https://api.worldbank.org/v2/country?per_page=350&format=json"
    )
    world_bank_countries = requests.get(world_bank_countries_url).json()
    countries_dataframe = pandas.DataFrame(world_bank_countries[1])
    return countries_dataframe


def build_countries_mapping(countries_data):

    countries_mapping = {}

    for country in countries_data:
        countries_mapping[country["name"]] = country["id"]

    return countries_mapping


def build_indicators_mapping(indicators_data):

    indicators_mapping = {}

    for indicator in indicators_data:
        try:
            topic = indicator["topics"][0]["value"].strip()
            if topic not in indicators_mapping:
                indicators_mapping[topic] = {}
            indicators_mapping[topic][indicator["name"]] = indicator["id"]
        except:
            if "Other" not in indicators_mapping:
                indicators_mapping["Other"] = {}
            indicators_mapping["Other"][indicator["name"]] = indicator["id"]

    return indicators_mapping
