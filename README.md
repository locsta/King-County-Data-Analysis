# Project King County Data Analysis


## Our objectives are defined as follow:
We are consultants hired by realtor company to analyse the house data in King County and provide recommendations on their next investment strategy and the kind of prices that they can command.

Here are the questions we'll try to answer:
1. Can we predict the price of a house based on its location and features?
2. What are the most impactful factors (features) on the price?

## Data Cleaning Process
Our data are located in the **"kc_house_data.csv"** file.
In order to prepare our dataset to be used for machine learning we will use libraries such as **pandas**, **numpy**, **matplotlib** and **seaborn** to format and normalize our data in our **Jupyter file "index.ipynb"**

Our data has 20 columns with the description as follows:
* id			- unique identified for a house
* dateDate		- house was sold
* pricePrice		- is prediction target
* bedroomsNumber	- of Bedrooms/House
* bathroomsNumber	- of bathrooms/bedrooms
* sqft_livingsquare	- footage of the home
* sqft_lotsquare	- footage of the lot
* floorsTotal		- floors (levels) in house
* waterfront		- House which has a view to a waterfront
* view			- Has been viewed
* condition		- How good the condition is ( Overall )
* grade			- overall grade given to the housing unit, based on King County grading system
* sqft_above		- square footage of house apart from basement
* sqft_basement		- square footage of the basement
* yr_built		- Built Year
* yr_renovated		- Year when house was renovated
* zipcode		- zip
* lat			- Latitude coordinate
* long			- Longitude coordinate
* sqft_living15		- The square footage of interior housing living space for the nearest 15 neighbors
* sqft_lot15		- The square footage of the land lots of the nearest 15 neighbors

## Building our model
To built our machine learning model we chose to use the SciKit Learn library and the StatsModels library

<div><a href="scikit-learn.org"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit Learn" width="250" align="left"/></a>

<a href="www.statsmodels.org"><img src="https://www.statsmodels.org/stable/_static/statsmodels_hybi_banner.png" alt="StatsModels" width="450" align="right"/></a></div>
---

## Answering our initial questions
Finally we'll present our findings in our **"Slides"** folder

