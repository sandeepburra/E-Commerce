# E-Commerce website

## Table of Content


- [Overview](#overview)
- [Technical Aspect](#Technical-Aspect)
- [Deployement](#Deployement)
- [Technologies Used](#Technologies-used)


## Overview
This is a content based Recommendation System Django app. The product title and images are the contents for this system. I have created seperate pages for Recommendations using title and images.

![Alt text](/pics/logos/overview.JPG?raw=true "Optional Title")

Recommendations using title is based on the TF-IDF vectorization and recommendations using images based on Resnet.

I have added two search buttons, one is for image input and other is for text input. A user can get recommendations, by uploading an image or searching for specific text



## Technical Aspect

This project is divided into two parts:
- Building a recommendation system
- Deploying in heroku.

## Building a recommendation system
Recommendation systems are mainly of two types
***Collaborative filtering***
***content based filtering***
## Collaborative filtering:
Collaborative recommender systems aggregate ratings or recommendations of objects, recognize commonalities between the users on the basis of their ratings, and generate new recommendations based on inter-user comparisons.
## content based filtering:
As its name suggests, we do content based recommendation, means its based on tittle text,Description text, images. 

I dont have user data to do colloberative filtering, so im just using content based filtering for my web app.

You can find the more technical details of the model in my ipython notebook.

## Deployement
### Django app Creation
I have created a Django app for this system and used postgresql as a database. Intially model randomly take inputs from database and show them on the homepge. 
I have created 2 different pages, image based, title based, each page gives respective results.
Image Based: for this type of system i have used transfer learning concept and resenet architecture to obtain the features. Features for all the images in the database are generated in ipython notebook and saved in this django app.
Whenever user clicks the perticular image, model finds the Similar images from the database and return them on the detail page.
Title Based: In this model, all titles are used to fit a TFIDF vectorizer. By using this vectoroizer features for all titles obtained and saved as a pickle file. When user clicks the perticular product,model grab the title of the product and give recommendations based on that title.


There are two search boxes.

***Image input:***
It takes input from the user and send the image to resenet architecture to get the features, later model will find our which ever the product from database is similar to this and retuen top results to the user.

![Alt text](/pics/logos/Image_search.JPG?raw=true "Optional Title")

***text input:***
It takes some keywords from the user and return products whose title is similar to the entered keywords.

![Alt text](/pics/logos/title_search.JPG?raw=true "Optional Title")

### Deploying in heroku
After finishing the Django app, a github repository is created. Heroku uses this repo to deploy.
I have used amazon S3 to store files uploaded from user, to access these files from amazon s3 we need to add some config var in heroku

![Alt text](/pics/logos/herokuConfig.JPG?raw=true "Optional Title")

## Technologies used:

![Alt text](/pics/logos/python.JPG?raw=true "Optional Title")
![Alt text](/pics/logos/keras.JPG?raw=true "Optional Title")

![Alt text](/pics/logos/django.JPG?raw=true "Optional Title")
![Alt text](/pics/logos/amazons3.JPG?raw=true "Optional Title")

![Alt text](/pics/logos/heroku.JPG?raw=true "Optional Title")


