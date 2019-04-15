# ETL Project Report

A look at the health of honey bee colonies, honey production, and pesticide usage in the USA.

## Extracting Data Resources 
* [USDA](https://www.nass.usda.gov/Surveys/Guide_to_NASS_Surveys/Bee_and_Honey/) - CSV on honey bee colonies in the United States and CSV on honey production in the United States. 
* [Kaggle](https://www.kaggle.com/usgs/pesticide-use/version/1) - CSV of pesticide use in the United States via the USGS.

## Transforming Data

### Data sources filtered for 2015

Given the limited time available and inconclusive datasets for many years, we will limit the scope of this project to 2015


### From Resources/bee_colonies_2015

Combine and clean CSVs (hcny_p01_t005, p02_t001, p03_t007, p04_t008) and export to one CSV with:
```
State
January 2015 colony count
December 2015 colony count
Change in colony count
Added colonies 2015
Lost colonies 2015
Renovated colonies 2015
```


### From Resources/honey_2015

Clean the CSV (t003) to include:
```
total production(lbs) - 2015
yield/colony(lbs) - 2015
```

### The Honey and Colony dataframes were merged on state.


### From Resources/AgrPesticideUse_2014-2015

Clean the CVS (2015) to include information for:
```
2015 use rates per harvested-crop acre, or an “estimated pesticide use” (EPest) rate, of the following compounds:
-- acetamiprid
-- clothianidin
-- imidacloprid
-- nitenpyram
-- nithiazine
-- thiacloprid
-- thiamethoxam

These compounds are in the neonicotinoid (neonid) class of pesticides, which have been linked to colony 
collapse disorder.
```    


## Loading Data 

* Load cleaned data into a SQL database
* The SQL database was queried to show the following:
```
-- Top 5 states with the highest honey yield per colony
-- Production rates for the 5 states that ended the 2015 year with the most colonies
-- Pesticide usage for the 5 states that saw the highest colony loss
-- Pesticide usage for the 5 states that saw the most colonies added
-- Change in number of colonies for the states with the greatest pesticide use
```

## Flask

* In addition, a flask app was created to set up APIs for the following:
```
-- bee colony & honey production data for all states (in descending order by yield per colony)
-- colony change, compounds, and pesticide rates for all states
```

### Consideration in reading the data:

In reading this data, please be aware that for some states data is not published separately to avoid disclosing data for individual operations.

For the collected data on colonies: 
Alaska, Delaware, Nevada, New Hampshire, and Rhode Island were not individually reported.

For the collected data on honey production:
Alaska, Connecticut, Delaware, Maryland, Massachusetts, Nevada, New Hampshire, New Mexico, Oklahoma, and Rhode Island were not individually reported on.

Also, in 2015, California, Alaska, and Hawaii did not report on their use of the 7 pesticides believed to cause adverse effects on colony health. 


## Authors
* [**Emily Tavik**](https://github.com/emilyt1985/)
* [**Erica Leon**](https://github.com/ericaleon)
* [**Ian Schuler**](https://github.com/ischuler)
