Welcome to our group project for Agile Web Dev!!!

Link to Wireframe Prototype Figma: https://www.figma.com/file/A00hdtf2nIDgGXJphqhQ9L/3402Prototype-ames?type=design&node-id=895170%3A448&mode=design&t=JPTUErnpHmY2oEHZ-1

Figma Web App Framework: https://www.figma.com/board/jKrVV0aJy7j8q8jwQmoT2k/Job-Search-Web-App-Framework?node-id=0%3A1&t=GgdI6AOvhRUp7DnI-1

Description:
This project is a low level online job search/application board. Its functionality allows for search of long term career options or short term daily jobs. It provides a place where users can put their skills up and work freelance or small jobs that require those skills. It also creates a space for job recruiters to post full-time job positions and recieve applications. If they dont want to create those job posts, They can also browse through the list of people that have posted their skills and message candidates via the website.

Predicted Agile Sprint Outline:
Planning -> Basics -> Functionality -> Testing -> Cleaning -> Pretty-ing -> done/submit!

Actual Agile Sprint Outline:
Planning -> Basics -> Pretty-ing -> Functionality <---> Testing -> cleaning -> Done/submit!


Dev environment Notes:
* Clone repo
* Update to Python 3.12
* Install venv in repo main dir and activate
* Run "pip install -r requirements.txt"
* flask run to start development server and test app
* Lauren Gees notes provide solid instruction on setting up environment, refer to them if necessary
=======

Project Structure as per Flask Docs:
* UWA_CITS_3402_Project
    * app config files, db and instance creation, requirements.txt
    * app
      * Helper functions, initializers, models, routes and forms
      * static
        * css
            * *contains css files*
        * js
          * *contains external javascript files*
        * img
          * *contains img files*
      * templates
        * *contains base and all other html templates*
    * test
      * *contains unit and functional tests*
    * migrations
      * *contains db migration scripts*

Usage  
* Before anything make sure python and pip are installed
* Inside your virtual env all dependancies need to be installed, to do this run:  
``` pip install -r requirements.txt ```  
* To run tests use:  
``` pytest ```  
  * The following tests are included:
    * All routes defined in routes.py are checked for status 200
    * User account creation and login
    * User applying for a job, poster receiving application
    * Jobs being returned from search
    * User profile page displaying relevant data
    * Multiple db queries
* To launch app use:  
``` flask run ```  
  * The application has been built to automatically create a db for you and perform all migrations in the background before the app launch
  * Once the flask development server is running follow the link provided
  * Initially the db will be empty. In order to simulate user interactions the ``` /populate ``` page has been created. This will allow you to populate the db with dummy data. To use this feature, add ```/populate ``` to the end of your development server ip. Then follow the prompts to create dummy data.
    * Number of users = number of user accounts
    * Number of request posts = number of posts of type 'job request'
    * Number of looking for posts = number of posts of type 'looking for work'  
=======

1. a description of the purpose of the application, explaining the its design and use.

2. a table with with each row containing the i) UWA ID ii) name and iii) Github user name of the group members.

3. a brief summary of the architecture of the application.


