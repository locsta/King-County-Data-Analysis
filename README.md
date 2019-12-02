# Project King County Data Analysis


## Our objectives are defined as follow:
We are consultants hired by realtor company to analyse the house data in King County and provide recommendations on their next investment strategy and the kind of prices that they can command.

Here are the questions we'll try to answer:
1. Can we predict the price of a house based on its location?
2. What are the most impactful factors (features) on the price?

## Data Cleaning Process
Our data are located in the **"kc_house_data.csv"** file.
In order to prepare our dataset to be used for machine learning we are using python libraries such as **pandas**, **numpy**, **matplotlib** and **seaborn** to format and normalize our data.
This is done in our **Jupyter file "index.ipynb"** file.

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
<br><br>

<div><a href="https://scikit-learn.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="Scikit Learn" width="30%" align="left"/></a>
<a href="https://www.statsmodels.org/"><img src="https://www.statsmodels.org/stable/_static/statsmodels_hybi_banner.png" alt="StatsModels" width="60%" align="right"/></a></div>

<br><br><br><br><br><br><br><br><br><br><br><br>
In order to use those libraries we transform *bedrooms*, *bathrooms*, *floors*, *waterfront*, *view*, *condition* and *grade* columns into categorical columns.</br>

We observe that the _price_ doesn't follow a normal distribution. It is right skewed.<br>
We create a column *log_price* using the numpy function log() to transform prices to a log scale that will be better fitted for machine learning.<br>
Then we use the **LabelEncoder** method from **sklearn.preprocessing** to normalize the values for those columns and dropped *price*,*zipcode*,*lat* and *long* columns.<br>
Finally we can run the Ordinary Least Squares (OLS) method from statsmodels.api with the target **y** being the **log_price** column and **X** being our **features** columns.<br>
All our predictors have a P value < 0.05, they rejected the null hypothesis and are therefore meaningful predictors.<br>

## Answering our initial questions
1. Can we predict the price of a house based on its location?<br/>
  > We can show a heat maps to the realtor company in order to help them chose the best location for their project.<br/>
  > Here are the 3 different heat maps we created:
    * Price as per location
    * Price per sqft lot as per location
    * Price per sqft living as per location
  > <br/>_You will find the heat maps in the Jupyter notebook and also in the slides folder._

2. Can we predict the price of a house based on its location and features?<br/>
  > Our model scores a r2 of 0.816, meaning that 81,6% of the variation in price is predicted by features.<br/>
  > Ranking from highest to lowest impact on the prices are the following features:
  * 1. grade
  * 2. sqft_living
  * 3. zip_mean_price
  * 4. sqft_living15 
  * 5. sqft_above 
  * 6. bathrooms

## Presenting our findings to the Realtor company
In the **"Slides"** folder you can find the presentation of our findings to the realtor company

