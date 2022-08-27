### Data analysis

Data analysis is a method in which data is first collected, and then various operations like normalizing, transforming, cleaning, etc. are applied to that data to extract useful or relevant information. It enables us to make educated decisions instead of just assumptions about data.

#### Why learn data analysis?

Did you know that 90% of the world’s data was created in the last 2 to 3 years? It was predicted that by 2020 we’ll have 40 zettabytes of data, which is close to 400 billion gigabytes! That’s a huge number.

To tackle this exponential increase in data, tech giants such as Facebook, Google, Amazon, and LinkedIn have started hiring data scientists to leverage this huge amount of data to their maximum advantage. Data analysis skills are so in demand that companies pay a huge sum of money to hire the best analyst available.


#### Data analysis tools

There are a lot of purchasable data analysis and visualization tools out there such as Google Analytics, IBM Cognos Analytics, Tableau, but for the scope of our course we focus on tools used in Python programming language, which are:

* Numpy

* Pandas

* Matplotlib

* Seaborn


# Project 1 Stock Markeet Analysis

### Some stock market jargon

* Closing price: The price of the stock when the market closes that day

* Daily returns: The increase or decrease in the percentage amount from the previous day

* Risk: The amount that can be lost

* Stock behavior: Whether the stock price would go up or down

### Let’s dive in

The stock data of the following four technology companies in Pakistan will be analyzed.

* Systems Ltd
* NETSOL
* PTCL
* Avanceon

First and foremost, we need the historical data of these companies. The data is available [here](https://dps.psx.com.pk/historical) and can be viewed by placing the relevant time period and company names in the search fields. A scraper will be used to pull all the data and put it into CSV files.

<strong>Section 1. Price Trends</strong>

For this analysis. the column <code>Close</code> will be of great importance. As mentioned aboce. this column contains the closing price of the stock of each day. So. let's visualize this using a line graph how the closing price of Sysstems Ltd stock has varied throughout the year of 2018.

<strong>Section 2. Daily Returns</strong>

The price of stock changes on a daily basis. Daily return calculations tell us how much the current day stock value is different from the previous day stock value. A positive change indicates a rise in the value of the stock while a negative change indicates a fall in the value of the stock. A stock with minimal positive or negative change is considered to be a stable and good stock.

<strong>Section 3. Correlation in Stocks</strong>

The stock behavior of companies dealing in similar services is usually related, and this relation can be measured using correlation.

Correlation is a statistical technique that determines how strongly two variables are related to each other and how a change in one would affect the other. It can also be defined as a measure of dependence between two or more quantities.

The two types of correlation, in terms of stock behavior, can be described as follows:

* <b>Positive correlation:</b> The stock value of one company goes up, and in correlation with it, the stock values of other companies also go up.

* <b>Negative correlation:</b> The stock value of one company goes up, and in correlation with it, the stock values of other companies go down.

<strong>Section 4. Risk Estimation</strong>

The daily risk for the companies stock prices can be calculated by taking the standard deviation of the daily returns. The daily returns and risks can be visualized using a scatter plot, which can give us a better understanding of the return vs. risk ratio of each company’s stock.

<strong>Section 5. [Predicting Future Stock Behavior](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)</strong>

There are two main techniques used to analyze stock behavior.

* Fundamental analysis: This mostly deals with the intrinsic value of companies based on the various changes in their financials on a regular basis.

* Technical analysis: This provides results based on the historical data of a company’s stock.

Fundamental analysis is beyond the scope of this course, and the information required for it is also not easily accessible.

# Project 2 [Customer Behavior Analysis](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

The decisions and instincts that make a customer buy a certain product or service can be described as customer behavior.

With the advent of targeted marketing, traditional marketing techniques are getting obsolete with every new day. The rise of digital marketing, where every customer is shown advertisements particular to their interests and habits, has taken over the world.

This insight into customer’s interests and habits is obtained through an extensive customer behavior analysis approach. We will try to implement a very basic level of this approach that will include finding the products that are selling more and at which time of the day. Then we will group the customers according to their buying habits.

<strong>Section 1. Brand Analysis </strong>

A brand is a term that differentiates one product from another. In this analysis, we will review whether people like to purchase products with a popular brand or a product without a brand.

For this analysis, only the products actually bought by the users will be considered. In our dataset, the products which have no brand are given a <code>NaN</code> value.
This will be done in two steps:

1. Separate the original <code>DataFrame</code> into two DataFrames. One with all the products with brands and one with all the products without brands.

2. Fetch all those rows from the two <code>DataFrames</code> where the <code>event_type</code> value is <code>purchase.</code>

<strong>Section 2. Customer Activity Analysis </strong>

* <b>view</b>: The user can view an item.

* <b>cart</b>: The user can add the item to the cart.

* <b>purchase</b>: The user can purchase the item.

Analyzing the view and purchasing actions of the user across the different timelines in a month can provide very important information as to at what time most of the users visit the site. When such times are known, resources can be allocated according to that information to optimize performance.

For example, if we know that a significant amount of users visit the site on Sunday just to view the products, resources from other components can be transferred to viewing components to enhance the user experience. Similarly, the same approach can be used on other components if we know at what times certain, user activity is preferred.

<strong>Section 3. Identifying Famous Brands and Categories</strong>

The most common problem faced by any business is inventory management. Sometimes business owners either have too much of a product that is not being sold or too little of a product whose demand is very high. This can cause a substantial loss to a company’s profits and reputation. For more information on this problem, refer [here](https://www.business2community.com/product-management/6-times-horrific-inventory-control-almost-killed-companies-01659644).

If we somehow know what products from which brands and categories are selling the most in the market, then inventory management can be optimized to some level. Here, products from which brand and category were bought the most will be determined.

<strong>Section 4. RFM analysis </strong>

RFM is a categorizing technique that uses the previous purchasing behavior of the customers to divide customers into groups so that an optimal marketing strategy can be developed for each individual. RFM stands for recency, frequency, and monetary, respectively.

* Recency: How many days have passed since a customer has bought an item

* Frequency: How many orders a customer has placed

* Monetary: How much money a customer has spent

Need for RFM analysis

* This technique efficiently categorizes the customers into specific rank-based groups taking into account their past online behaviors.

* This can help marketers and advertisers target each group of consumers separately, enabling them to cater to the needs of groups instead of each individual.

* This technique also informs us of the most and least profit yielding customers so relevant resources can be deployed to each group according to their needs.

* If the results of this technique are correctly used, then even customers who don’t engage in much activity(view, cart, buy) can be influenced to be high potential customers.

RFM technique and steps to perform

In this process, the customers are separated into four groups under each of the RFM metrics, i.e., recency, frequency, and monetary. This means we’ll have a maximum of (4 x 4 x 4) sixty-four groups to deal with, which is not very large considering that the total number of customers can be in the thousands. Quantiles will be used to divide the customers into groups.
