# E-Commerce website

## Table of Content

- Demo
- Overview
- Technical Aspect
- Deployement on Heroku
- Technologies Used


## Demo


## Overview
This is a content based Recommendation System Django app. I have used product title and images are the contents for this system. I have created seperate pages for Recommendations using title and images. 
Recommendations using title is based on the TF-IDF vectorisation and using images based on Resnet.

I have added two search buttons, one is for image input and other is for text input. A user can get recommendations, by uploading an image or searching for specific text



## Technical Aspect

This project is divided into two parts:
- Building a recommendation system
- Deploying in heroku.

## Building a recommendation system
Recommendation systems are mainly of two types
### Collaborative filtering
### content based filtering
## Collaborative filtering:
Collaborative recommender systems aggregate ratings or recommendations of objects, recognize commonalities between the users on the basis of their ratings, and generate new recommendations based on inter-user comparisons.
## content based filtering:
A content based recommender works with data that the user provides, either explicitly (rating) or implicitly (clicking on a link). Based on that data, a user profile is generated, which is then used to make suggestions to the user. 

I dont have user data to do colloberative filtering, so im just using content based filtering for my web app.

You can find the more technical details of the model in ipython notebook.

## Deployement
### Django app Creation
I have created a Django app for this system and used postgresql as database. Intially model randomly take inputs from database and show them on the homepge. 
I have created 3 different pages, image based, title based and comnined. Each page gives respective results.
Image Based: for this type of system i have used transfer learning concept and resenet architecture to obtain features. Features for all the images in the database are generated in ipython notebook and save in this django app.
Whenever user clicks the perticular image, model finds the Similar images from the database and return them on the detail page.
Title Based: In this model, all titles are used to fit a TFIDF vectorizer. By using this vectoroizer features for sll titles obtained and saved as a pickle file. When user clicks the perticular product,model grab the title of the product and give recommendations based on that title.



There are two search boxes.

***Image input:***
It takes inut from user an send the resenet architecture to get the features, later model will find our which ever the product from database is similar to this and retuen top results to the user.

***text input:***
It takes some keywords from the user and return products whose title is similar to the entered keywords.
### Deploying in heroku
After finishing the Django app, i have created a repository in github. Heroku uses this repo to deploy.
I have used amazon S3 to store files uploaded from user. To access this files from amazon s3 we need to modify some config var in heroku

Technologies used:

![Alt text](/pics/logos/python.JPG?raw=true "Optional Title")
![Alt text](/pics/logos/keras.JPG?raw=true "Optional Title")

![Alt text](/pics/logos/django.JPG?raw=true "Optional Title")
![Alt text](/pics/logos/amazons3.JPG?raw=true "Optional Title")

![Alt text](/pics/logos/heroku.JPG?raw=true "Optional Title")


