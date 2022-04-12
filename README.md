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
An accuracy score of .88 was found however. 





## Analysis, Conclusions, and Recommendations
2 CNNs for particular slice orientations with specific scans were produced (1 T2 model on the tranverse plane and 1 Mprage-T1 model on the sagittal plane). An accuracy score of .8947 for the T2 model with a baseline of .4589 was produced. This model has a sensitivity of .9169 and specificity of .8759. The Mprage model has an accuracy score of .9466 with a baseline of .4979. It has a sensitivity .9504 and specificity of .9428. Notably, these scores compare well with another article's models which scored better in terms of accuracy on the tranverse plane [(Source)](https://www.frontiersin.org/articles/10.3389/fpsyt.2020.00016/full). Fluctuations between scores is likely due to difference in both size, scale and optimization of models; it must be noted that the sagittal plane was not used the other article's model. Both the T2 and Mprage models slightly tended to favor a classification towards schizophrenia. The T2 model tended to misclassify groups at the higher slices (100-120). Upon further investigation, about half of the misclassification of the control group revealed that at higher slices there was white noise i.e scans with no actual brain revealed and no more than 12 misclassified slices per patient was produced. Misclassification of scans for the Mprage model was on the exterior portions of the scan (slices below 40 and above 150). Investigation reveals that CNNs were able to classify based on minute brain differences however head shape was also picked up on in constrast of mean images per group. In order to be usable in the field, entire scans per patient can be fed into model and predicted upon. Mean scores of slices can then be generated along side derived confidence intervals to aid with diagnosis. 

The project had several limitations with regards to scope. First, there was a small patient sample size: N=94 for controls and N=83 for schizophrenia. Moreover, not all patients had scans per each scan type and some patients had more than one session per particular scans. There was also a limitation with regards to data and computational power; dicom images store more information (orignally had 150 gbs of data) and thus would require a more robust platform. Model were also used on specific machines with specific scan intensities on specific scans with specific planes. Finally, the dataset was not segmented by age or severity of condition.

There is a plethora of options for further investigation both within and outside the project. Within the project, the recommendation is to first filter out noise scans with segmentation, then try 3D modeling with derived nii files accompanied with data augmenation and introduction of GANs. Although adding more data is always an option, using ATS to further model on existing data would be useful to check for generalizabiltiy and performance with more RAM intensive pipelines. Explanations of the model could also be implemented via gradien ascent and in field applications could be designed with a streamlit app. Outside the project, it is recommended to use fMRIs & clustering models to study brain neural networks. Usage of meta data (age, genetics, and speech) in future models may improve accuracy. Lastly MRI data could be used on other more established mental illnesses or illnesses that are comorbid with schizophrenia.








