Welcome to our group project for Agile Web Dev!!!

Colaborators:
+----------+---------------------+---------------+
|  UWA ID  | Name                | Github User   |
+----------+---------------------+---------------+
| 24373764 | Hernan Barajas      | hernancx09    | 
| 22253126 | Christopher Sandon  | Sandoncj      |
| 22029591 | Ames Xiao           | UwaProj       |
| 23246938 | Edward Permono      | EP-Wick       |
+----------+---------------------+---------------+

Link to Wireframe Prototype Figma: https://www.figma.com/file/A00hdtf2nIDgGXJphqhQ9L/3402Prototype-ames?type=design&node-id=895170%3A448&mode=design&t=JPTUErnpHmY2oEHZ-1

Figma Web App Framework: https://www.figma.com/board/jKrVV0aJy7j8q8jwQmoT2k/Job-Search-Web-App-Framework?node-id=0%3A1&t=GgdI6AOvhRUp7DnI-1

Description:
  This project is a low level online job search/application board. Its functionality allows for search of long term 
  career options or short term daily jobs. It provides a place where users can put their skills up and work freelance 
  or small jobs that require those skills. It also creates a space for job recruiters to post full-time job positions 
  and recieve applications. If they dont want to create those job posts, they can also browse through the list of 
  people that have posted their skills and message candidates via the web app. The Figma above has the framework for 
  the design of the project depending on whether the user wants to post jobs or apply for them.

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

Usage  
* Before anything make sure python and pip are installed in your system/wsl
* Clone the repo and set up your preferred virtual environment. We have used venv. Refer to https://docs.python.org/3/library/venv.html for detailed instructions. The easiest way is to locate the clone repo in your terminal/wsl, and in the main directory execute:
``` python3 -m venv venv ```  
This will create the target directory for your virtual env. Next you need to activate it. This is done via:  
``` source venv/bin/activate ```  
You'll know it is active when ``` (venv) ``` appears on the command line before your username.
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

Architecture:

  We used a layered architecture to create this web application. It follows clear seperation of responsibility and allows 
  the layers to have controled interations with eachother. This helped with easier maintinence and testing. 
  All our directories can be seen above.

  Presentation Layer- The Frontend Html, CSS, and Javascript files are located in the *static* and *templates* directories. 
  This was in colaboration with Jinja which allowed templating.

  Logic layer- For the backend we used python along with the flask framework. The functionality is defined in the python 
  files like routes.py, models.py, and forms.py found within the *app* directory.

  Data Access- We used SQLAlchemy and Flasks ORM for data gathering and database interaction. Migration scripts found in 
  the *migrations* directory were used for database schema alterations.

  Database- For the Database we used SQLite since its a relational database and the configuration and management could be 
  easily handled with Flask's setup.
