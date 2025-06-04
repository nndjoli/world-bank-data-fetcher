<h1>worldbankpy</h1> 

- Interacts with the World Bank API to retrieve macroeconomic data.

<h2>Requirements & Installation :</h2>

- Requirements: `datetime`, `requests`, `pandas`.  


<h2>Example:</h2>

```python

import worldbankpy

# Instantiate the World Bank API client:
instance = worldbankpy.Instance()
```

You can filter countries using the `filtered_countries` method. Available filters include region, income level, admin region, lending type. Values for these filters can be obtained using the following attributes:

```python
regions = instance.list_regions  # Display all regions

>>> [
    'Latin America & Caribbean',
    'Aggregates',
    'South Asia',
    'Sub-Saharan Africa',
    'Europe & Central Asia',
    'Middle East & North Africa',
    'East Asia & Pacific',
    'North America'
    ]

countries = instance.list_available_countries  # Display all countries

>>> [
    'Aruba',
    'Africa Eastern and Southern',
    'Afghanistan',
    ...
    'South Africa',
    'Zambia',
    'Zimbabwe'
    ]

income_levels = instance.list_income_levels  # Display all income levels

>>> [
    'High income',
    'Aggregates',
    'Low income',
    'Lower middle income',
    'Upper middle income',
    'Not classified'
    ]

admin_regions = instance.list_admin_regions  # Display all admin regions

>>> [
    'South Asia',
    'Sub-Saharan Africa (excluding high income)',
    'Europe & Central Asia (excluding high income)',
    'Latin America & Caribbean (excluding high income)',
    'East Asia & Pacific (excluding high income)',
    'Middle East & North Africa (excluding high income)'
    ]

lending_types = instance.list_lending_types  # Display all lending types

>>> ['Not classified', 'Aggregates', 'IDA', 'IBRD', 'Blend']
```

For example, you can filter the countries in Europe & Central Asia with high income:

```python
eu_central_asia_high_inc = instance.filtered_countries(region="Europe & Central Asia", income_level="High income")

>>>{
    'Andorra': 'AND',
    'Austria': 'AUT',
    'Belgium': 'BEL',
    ...
    'Slovak Republic': 'SVK',
    'Slovenia': 'SVN',
    'Sweden': 'SWE'
    }

```

You can then filter indicators using the `filtered_indicators` method. Available filters include topics & sources. Values for these filters can be obtained using the following attributes:

```python
topics = instance.list_topics  # Display all topics

>>> [
    'Poverty','Education','Social Protection & Labor','Economy & Growth','Agriculture & Rural Development',
    'Climate Change','Urban Development','External Debt','Public Sector','Financial Sector','Aid Effectiveness',
    'Millenium development goals','Environment','Energy & Mining','Infrastructure','Science & Technology',
    'Private Sector','Trade','Gender','Health'
    ]

sources = instance.list_sources  # Display all sources

>>> [
    'LAC Equity Lab', 'Sustainable Energy for All','Global Partnership for Education',
    'International Comparison Program (ICP) 2005','ICP 2017',
    'Exporter Dynamics Database – Indicators at Country-Year Level','Global Financial Inclusion',
    'G20 Financial Inclusion Indicators','Disability Data Hub (DDH)','Education Statistics',
    ...
    'Indicators of Resilience and Equity','PEFA 2016','PEFA 2011','Joint External Debt Hub',
    'Health Nutrition and Population Statistics','Education Policy',
    'Health Nutrition and Population Statistics by Wealth Quintile','Universal Health Coverage',
    'Jobs','Subnational Malnutrition Database','Subnational Population','Statistical Performance Indicators (SPI)'
    ]


categories = instance.list_available_categories  # Display all categories (similar to topics)
```

You can acces a list of popular indicators using the `list_popular_indicators` attribute:

```python
popular_indicators = instance.list_popular_indicators

>>> [
    {'Population, total': 'SP.POP.TOTL'},
    {'Population growth (annual %)': 'SP.POP.GROW'},
    {'Surface area (sq. km)': 'AG.SRF.TOTL.K2'},
    ...
    {'GDP per capita (current US$)': 'NY.GDP.PCAP.CD'},
    {'Foreign direct investment, net (BoP, current US$)': 'BN.KLT.DINV.CD'},
    {'Inflation, consumer prices (annual %)': 'FP.CPI.TOTL.ZG'}
    ]
```

For example, let's filter the indicators related to Economy & Growth:

```python
gdp_indicators = instance.filtered_indicators(topic="Economy & Growth")
gdp_indicators_v2 = instance.category_indicators('Economy & Growth')

```

Otherwise, you can search for indicators by keywords:

```python
indicators = instance.search_indicator_by_keywords(["GDP", "growth", "annual"])
```

An example use:

```python

countries = instance.filtered_countries(region="Europe & Central Asia", income_level="High income")

>>>{
    'Andorra': 'AND',
    'Austria': 'AUT',
    'Belgium': 'BEL',
    ...
    'Slovak Republic': 'SVK',
    'Slovenia': 'SVN',
    'Sweden': 'SWE'
    }

countries_codes = [v for k, v in countries.items()]

>>> [
    'AND','AUT','BEL','BGR','CHE','CHI','CYP','CZE','DEU','DNK',
    'ESP','EST','FIN','FRA','FRO','GBR','GIB','GRC','GRL','HRV',
    'HUN','IMN','IRL','ISL','ITA','LIE','LTU','LUX','LVA','MCO',
    'NLD','NOR','POL','PRT','ROU','RUS','SMR','SVK','SVN','SWE'
    ]

indicators = instance.search_indicator_by_keywords(["GDP", "growth", "annual"])

>>> [
    {'name': 'GDP growth (annual %)', 'code': 'NY.GDP.MKTP.KN.87.ZG'},
    {'name': 'GDP per capita, PPP annual growth (%)','code': 'NY.GDP.PCAP.PP.KD.ZG'},
    {'name': 'GDP per person employed (annual % growth)','code': 'SL.GDP.PCAP.EM.KD.ZG'},
    {'name': 'GDP growth (annual %)', 'code': 'NY.GDP.MKTP.KD.ZG'},
    {'name': 'GDP per capita growth (annual %)', 'code': 'NY.GDP.PCAP.KD.ZG'}
    ]

indicator_id = indicators[-2]['code']
indicator_name = indicators[-2]['name']


>>> 'NY.GDP.MKTP.KD.ZG'

data = instance.indicator(countries_codes, indicator_id)
 ```

| Date       | AND        | AUT       | BEL       | BGR       | CHE       | CHI       | CYP       | CZE       | DEU       | DNK       | … | NLD       | NOR       | POL       | PRT       | ROU       | RUS       | SMR       | SVK       | SVN       | SWE       |
| ---------- | ---------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | - | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| 1961-01-01 | NaN        | 5.537979  | 4.978423  | NaN       | 8.108672  | NaN       | NaN       | NaN       | 4.298440  | 6.378832  | … | 0.295547  | 6.273336  | NaN       | 5.534903  | NaN       | NaN       | NaN       | NaN       | NaN       | 5.681293  |
| 1962-01-01 | NaN        | 2.648675  | 5.212004  | NaN       | 4.789941  | NaN       | NaN       | NaN       | 4.623471  | 5.666822  | … | 6.843507  | 2.813945  | NaN       | 6.614448  | NaN       | NaN       | NaN       | NaN       | NaN       | 4.259047  |
| 1963-01-01 | NaN        | 4.138268  | 4.351584  | NaN       | 4.879199  | NaN       | NaN       | NaN       | 2.735296  | 0.637021  | … | 3.624622  | 3.785043  | NaN       | 5.873702  | NaN       | NaN       | NaN       | NaN       | NaN       | 5.327934  |
| 1964-01-01 | NaN        | 6.124354  | 6.956685  | NaN       | 5.256351  | NaN       | NaN       | NaN       | 6.639470  | 9.269938  | … | 8.274904  | 5.009651  | NaN       | 6.310747  | NaN       | NaN       | NaN       | NaN       | NaN       | 6.821164  |
| 1965-01-01 | NaN        | 3.480175  | 3.560660  | NaN       | 2.104555  | NaN       | NaN       | NaN       | 5.244164  | 4.555255  | … | 8.643095  | 5.285609  | NaN       | 7.468989  | NaN       | NaN       | NaN       | NaN       | NaN       | 3.821508  |
| …          | …          | …         | …         | …         | …         | …         | …         | …         | …         | …         | … | …         | …         | …         | …         | …         | …         | …         | …         | …         | …         |
| 2019-01-01 | 2.015548   | 1.754976  | 2.442890  | 3.788850  | 1.141982  | 1.573355  | 5.875591  | 3.565777  | 0.987893  | 1.711401  | … | 2.300092  | 1.123778  | 4.580458  | 2.745685  | 3.923264  | 2.198076  | 2.065685  | 2.275899  | 3.505252  | 2.549648  |
| 2020-01-01 | -11.183940 | -6.318255 | -4.792984 | -3.215737 | -2.141737 | -8.896780 | -3.220634 | -5.304880 | -4.095137 | -1.780106 | … | -3.867953 | -1.278172 | -2.035569 | -8.204632 | -3.674384 | -2.653655 | -6.647911 | -2.585513 | -4.084998 | -2.005338 |
| 2021-01-01 | 8.286779   | 4.795329  | 6.202554  | 7.780615  | 5.391888  | 9.936801  | 11.387763 | 4.029018  | 3.670000  | 7.382066  | … | 6.276831  | 3.908687  | 6.927183  | 5.558758  | 5.545710  | 5.614290  | 13.897790 | 5.726989  | 8.389650  | 5.937509  |
| 2022-01-01 | 9.564612   | 5.277894  | 4.233432  | 4.038778  | 2.568328  | 5.341962  | 7.365623  | 2.847171  | 1.369731  | 1.540173  | … | 5.007235  | 3.005635  | 5.255457  | 6.985842  | 3.965308  | -2.069712 | 7.898441  | 0.449674  | 2.699238  | 1.459289  |
| 2023-01-01 | 2.583555   | -0.954962 | 1.251701  | 1.886815  | 0.716067  | 3.715006  | 2.611901  | -0.085330 | -0.266438 | 2.495184  | … | 0.074561  | 0.479647  | 0.138833  | 2.526281  | 2.404272  | 3.600000  | NaN       | 1.378337  | 2.112592  | -0.310670 |

The returned `pandas.DataFrame` has attributes providing relevant informations about the data: 

```python

data.attrs

>>>{
'Country Codes':['AND','AUT','BEL', ..., 'SVK','SVN','SWE'],
'Countries': ['Andorra', 'Austria', 'Belgium', ...,  'Slovak Republic', 'Slovenia', 'Sweden'],
'Indicator': 'GDP growth (annual %)',
'Indicator Code': 'NY.GDP.MKTP.KD.ZG',
'Unit': '',
'Last Updated': '2025-04-15',
'Source': 'World Bank',
'Source URLs': [
  'https://api.worldbank.org/v2/country/AND/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json',
  'https://api.worldbank.org/v2/country/AUT/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json',
  'https://api.worldbank.org/v2/country/BEL/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json',
  ...
  'https://api.worldbank.org/v2/country/SVK/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json',
  'https://api.worldbank.org/v2/country/SVN/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json',
  'https://api.worldbank.org/v2/country/SWE/indicator/NY.GDP.MKTP.KD.ZG?date=1930:2025&per_page=10000&format=json'
  ]
}
```
You can then analyze/ visualize the data:
```python

plt.figure(figsize=(11, 10))
for country in data:
    plt.plot(data.index, data[country], label=country)

plt.title(f"{indicator_name} in Europe & Central Asia (High Income)")
plt.xlabel("Year")
plt.ylabel(indicator_name)
plt.show()
```
<img src="https://github.com/nndjoli/world-bank-data-fetcher/blob/main/Miscellanous/plot.png" />