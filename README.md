# Airbnb: Classifing Country Destinations

## Problem Statement
Given new user data from Airbnb, which country will a new user choose as their first booking destination?

## Background
Airbnb is a popular online marketplace for lodging, primarily homestays, for vacation rentals, unique experiences, and tourism activities. Given the prevalence of Airbnb with 5.6 million active listings worldwide in at least 100,000 cities, tracking where new users are willing to book can help locate, grow, and optimize renting opportunities. Specifically more personalized content, decrease time to first booking, and better forecast of new user demand. 

### Data Analyzed
* [train_cleaned.csv](./data/train_cleaned.csv)
* [session_cleaned.csv](./data/session_cleaned.csv)
All data was from [Kaggle](https://www.kaggle.com/c/airbnb-recruiting-new-user-bookings)

### Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|user_id|str|train_cleaned|unique user id for each user|
|date_account_created|str|train_cleaned|date account created|
|timestamp_first_active|str|train_cleaned|timestamp user first active|
|date_first_booking|str|train_cleaned|date user first booked|
|gender|str|train_cleaned|user gender|
|age|str|train_cleaned|user age|
|signup_method|str|train_cleaned|where user signed up|
|signup_flow|int|train_cleaned|page user signed up|
|language|str|train_cleaned|international language preference|
|affiliate_channel|str|train_cleaned|what kind of paid marketing|
|affiliate_provider|str|train_cleaned|where marketing originated|
|first_affiliate_tracked|str|train_cleaned|marketing user first interacted with|
|signup_app|str|train_cleaned|what medium user signed up|
|first_device_type|str|train_cleaned|user device type|
|first_browser|str|train_cleaned|user's first browser|
|country_destination|str|train_cleaned|destination user chose|
|action|str|session_cleaned|action performed by user|
|action_type|str|session_cleaned|type of action performed by user|
|action_detail|str|session_cleaned|details of action performed by user|
|device_type|str|session_cleaned|device user used|
|secs_elapsed|int|session_cleaned|time elapsed for user|

#### Analysis, Conclusions, and Recommendations





## Analysis, Conclusions, and Recommendations







