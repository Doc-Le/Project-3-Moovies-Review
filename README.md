<div align="center">

![logo-header](https://user-images.githubusercontent.com/76841050/161380974-94aa1d41-136a-4cdc-99f6-9000ef4fdff2.png)

</div>

#

Here is a link to the live project.(https://moovies-review-app.herokuapp.com/)
#

This website was created for Milestone 3 - Datacentric Development project, as part of the Code Institutes diploma in Software development.<br>
I love movies and often try to contribute by reviewing them on random websites. This also means I often check a number of reviews or stars before starting to watch any movie<br>
I was inspired by many apps that I have installed on my phone. But one, in particular, called my attention, the IMDB.<br>
Upon exchanging info with family and friends, I came up with a simple and straightforward idea, to develop something similar to a google search bar, but only to search for movies and reviews.  
<b>

![Image showing the website displayed on different screen sizes](static\tests\responsive.png)

#

## User Experience (UX)

   ### Strategy 
   - User goals 
     * As a user I want to be able to find any movie.
     * As a user I want to review any movie. 

   - Site owner/ business goals
     * As the site owner I want my site to be responsive to different screen sizes.
     * As the site owner I want my site to be accessible to my visitors.
     * As the site owner, I want to build up a simple mechanism to help users/visitors to find movies.
     * Ultimately though I want to use the application to find and review movies.

   ### User Stories

   - #### First Time Visitor 

        1. As a first time visitor, I want to easily understand the main purpose of the site. 
        2. As a first time visitor, I want to be able to intuitively use the site.
        3. As a first time visitor, I expect to see an attractive, visually appealing site.
        4. As a first time visitor, I expect an accessible site.
        5. As a first time visitor, I expect the site to look good on my mobile device.
        6. As a first time visitor, I want to easily search the movies.
        7. As a first time visitor, I want to easily register.

   - #### Returning Visitor Goals

        1. As a returning visitor, I want to be able to check previous reviews.
        2. As a returning visitor, I want to follow on social media so I can hear of any new features.
        3. As a returning visitor, I want to be able to add and delete previous reviews.
        4. As a returning visitor, I want to be able to change my password.
        5. As a returning visitor, I want to be able to rate the app.
        6. As a returning visitor, I want to get feedback so I know that something has went through or if i've been redirected, why.

   - #### Frequent Visitor Goals

        1. As a frequent visitor, I want to be able to review movies and delete previous reviews.
        2. As a frequent visitor, I want to be able to contact the owner with suggestions.
        3. As a frequent visitor, I want to be able to update my profile.
        4. As a frequent visitor, I want to be able to change my account information.
        
       

   - #### Admin goals
      
        1. As admin, I want to be able to add, delete or edit a movie review.
        2. As admin, I want to be able to add, delete or edit a genre.
        3. As admin, I want to be able to delete a user.
        4. As admin, I want to be able to make another user an admin.
        5. As admin, I want to be able to reset a users password if they're having trouble logging in.

   ### Scope

   Within project conception, a list of features were compiled, these were the scored 
   between 1 & 5 for importance and feasibility/ viability which then decided which features 
   could be included for initial launch.    

   #### Current features 

-   Responsive on all device sizes

-   Accessible 

-   Easy to navigate (Single use learning)

-   Interactive elements

-   Social Links (build up media presence)

-   Ability to contact owner via contact page.

-   Contact form prefills the personal information for logged in users.

-   Flash messages for feedback

-   registration form to help users complete it correctly

-   Search bar in home can be used to search for genre, title.

-   'Back to top' footer link on each page, saves users from having to scroll up to Nav bar especially on mobile devices.

-   Logged in users can add reviews.

-   Logged in user can delete reviews on home page to their profile.

-   Admin users can add, edit and delete any reviews.

-   Before anything is deleted a confirmation is required preventing accidental deletion.

-   Cancel buttons on edit pages in case user changed their mind or got there accidentally.


   #### Features to implement in the future

-  Movies suggestions based on the users favourite genre, which will crosscheck which movie are in the library of that genre, which movie they have on their profile and display 1 or 2 movies at random so they also aren't seeing the same suggestions everytime they log in.
- Users can add a review to movies they didn't add.
- Users can rate movies they didn't add, the rating displayed will then be the average.
<br/>

<b>

### Structure

- Home page,  all users will be able to use regardless of whether they are logged in or not. The home page will have a search bar and add a dropdown button with login/sign-up options.<br>
- After logging in or sign-up users will be able to check their profile or log out .<br>
- The profile button allows logged-in users to access profiles.<br>
- Logged in users will be able to review movies and edit reviews.<br>
- For logged-in users the dropdown menu will change, sign-up, and login will be replaced with sign-out and profile.<br>
- Profile page has got the users<br>
- The edit-account page allows a user to change everything except their username. They can also delete their account from this page, a confirmation of deletion is requested so that users can't accidentally delete the account.<br>
- Admin users have additional nav links of manage genre and manage users. Manage user allows admin to delete a user, requiring confirmation prior to deletion. <br>

<br>
## Wireframe
<br>


| Page | Desktop | Tablet | Mobile |
| ---- | ------- | ------ | ------ |
|Initial|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/initial.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/initial_tablet.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/initial_mobile_.png)|
|Sign-in|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/signin_form.pngg)|[view](https://doc-le.github.io/Project-Milestone-1/assets/wireframe/tablet/projects.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/signformtablet.png)|
|Logged -in|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/logged-in.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/loggedin.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/loggedin_mobile_1.png)|
|Search Results|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/search.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/search_tablet_.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/search_results_mobile_1_1.png)|
|Results|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/search_result.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/search_resultstablet_1.png)|[view](https://github.com/Doc-Le/Project-3-Moovies-Review/blob/main/wireframe/result_mobile_1_2.png)|


### Surface

 -   #### Colour Scheme
        
        I have loved movies since I remember. Having a chance of creating movie search reviews that would use a simple search bar that could remind us of something that we use regularly, and that would be the google search.
        I used this to style my site, off-white background color to represent the color of the powerful life-changing google search.

-   #### Typography
         
      Used [Google Fonts](https://fonts.google.com/) to import the fonts used for this site.
     

## Technologies 

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries & database

1. [Bootstrap v4.6.0](https://getbootstrap.com/docs/4.6.0/getting-started/introduction/)
    - Bootstrap was used for the initial layout and styling before customising it.
2. [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the Tangerine and Gentium Book Basic. 
3. [Font Awesome](https://fontawesome.com/)
    - The icons used throughout.
4. [Git](https://git-scm.com/)
    - Version control.
5. [GitHub](https://github.com/)
    - For storing project.
6. [Gitpod](https://www.gitpod.io/)
    - Used for editing my code.
7. [Balsamiq](https://balsamiq.com/)
    - Wireframe creation
8. [TinyJPG](https://tinyjpg.com/)
    - TinyJPG was used to optimise the images I used on my site to minimise loading time.
9. [Am I responsive](http://ami.responsivedesign.is/)
    - This was used to generate the image at the top of this README.
10. [Chrome devtools](https://developer.chrome.com/docs/devtools/)
    - This was used massively throughout development to troubleshoot, try out changes before 
   changing code, to test responsiveness and for testing performance of the final site with lighthouse. 
11. [jQuery](https://jquery.com/)
    - Required for some of the bootstrap elements such as collapsibles, modal and tooltips.
12. [Heroku](https://dashboard.heroku.com/apps)
    - For deploying the application
13. [MongoDB](https://www.mongodb.com/)
    - Database used for our data
14. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
    - Micro framework for building applications.
15. [Emailjs](https://www.emailjs.com/)
    - Used to link the contact form to my emails
16. [RandomKeygen](https://randomkeygen.com/)
    - Used to generate secret key
17. [dbdiagram](https://dbdiagram.io/home)
    - Used to create the database schema.
18. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
    - Dependency of Flask and used security helpers.
19. [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
    - Dependency of Flask, templating language used in all my pages.
20. [convertingcolors.com](https://convertingcolors.com/color-bucket.html)
    - For making my colour palette picture



## Deployment

The project was deployed to GitHub Pages using the following steps:

* Log in to GitHub and locate the GitHub Repository
* At the top of the Repository (not top of the page), locate the Settings Button on the menu
* Scroll down the Setting page until you locate the GitHub Pages Section
* Under Source, click the dropdown called “None” and select “Master Branch”
* The Page will automatically refresh
* Scroll back down through the page to locate the now published site Link in the GitHub Pages section

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone, Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Downloading a ZIP file of the code, or Clone this repository using by command:
```#!/bin/sh
$ git clone  https://github.com/Doc-Le/Project-3-Moovies-Review.git
```
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened

*
   *  Clone using command line 
        +  Next to the green Gitpod button is a button that says code, select this. There is a few options as to how you 
        would like to clone, if you choose https, SSH or Github CLI, select the clipboard icon to copy the URL.
        +  In your workspace that you've created, in the terminal , type git clone, paste the URL and enter.
* 
    *  Desktop Github
        + If you choose to clone by selecting open with desktop Github, it will guide you through the clone with prompts.<br>

    * For more information or troubleshooting see the Github documentation 
    [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#about-cloning-a-repository)

- ### Setting up MongoDB 
    - Create account, create cluster, I used the free tier, so chose the region closest to me that had it, gave cluster a name and clicked green 'Create Cluster' button.
    - In menu, choose Database Access then select green 'Add New Database User'. Here choose a username and password(use only numbers and letters) and under priviledges select 'read and write to any database' and then click the green 'Add user' button at bottom.
    - Now back in menu select Network Access and then Add IP address, I selected Allow access from anywhere & then clicked green confirm button.
    - Next choose collections and click 'Create Database'.

    -
- ### Setting Up app
    - Create env.py file containing the following and add to .gitignore. I created my secret key using [RandomKeygen](https://randomkeygen.com/). The mongo URI we get when we connect MongoDB to our app.

    - Install requirements in terminal using pip3 install, see requirements below. 
    
    - Create requirements.txt file and Procfile by typing below into the console. These are required by Heroku so ensure these are pushed to github prior to deployment.
      
- ### Connecting to MongoDB
    - Back in mongoDB on your cluster page select connect button.
      
    - In the window that appears, select 'Connect Your Application and on the next page, select Python and version, you can then copy the connection string it supplies. 
      
    - Go back into the env.py file and paste in the connection string in the space left for the MONGO_URI. As outlined in the connect to cluster page, "password" needs replaced with the password created on the database access page. "myFirstDatabase" in the connection string also needs replaced with the actual database name. Copy this amended URI and paste it into the config vars in heroku.

- ### Heroku deployment
    - Log in to Heroku, click 'New' and select 'Create New App'. In window give the app a name and choose region closest to you and then click 'Create App'.
    
    - In new app page select settings from menu, click reveal config vars and complete the following
      
    - Next select 'Deploy' from menu, three options of deployment are available. If you select Heroku Git, it gives you step by step of what you need to do.
  
    - I chose to use Github, so you have to search and connect to your github repository. 
        
    - Click enable automatic deployment, below that in manual deploy section, you can pick and deploy a branch to ensure everything is et up correctly. 

    - Go to the [the movie database (TMDB) 

## Credits

### Code

-   [Bootstrap4](https://getbootstrap.com/docs/4.1/getting-started/introduction/): Bootstrap Library used for the layout and styling and modals.
-   [Stack Overflow](https://stackoverflow.com/questions/43634440/html-pattern-regex-for-no-spaces): For preventing people from entering spaces in some of the text input boxes.
-   [Iklinac on Stack Overflow](https://stackoverflow.com/questions/62839298/static-files-not-loading-on-one-template-but-loading-on-another): Fix for CSS not loading for profile page when fine on others.
-   [API(TMDB)](https://www.themoviedb.org/documentation/api/sessions): TMBD database and core of this project.
-   [Bootstrap5](maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css):Social media buttons and art.
-   [MongoDb documentation](https://docs.mongodb.com/manual/): Used for push, pull, and addToSet.
-   [Grepper](https://www.codegrepper.com/code-examples/python/how+to+remove+spaces+from+input+in+python): Used to check that book title was not just spaces as user can't edit book title once added, only admin can. 

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

W3C Markup Validator - Results [link](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmoovies-review-app.herokuapp.com%2F)
Testing User Stories from User Experience Section

## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhone X.
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.




## Content

All content was written by the developer


## Media

* Logo custom made by the developer with Adobe Illustrator
* All images found [Image: API] (https://www.themoviedb.org/documentation/api/sessions)

<br></br>
<br></br>
## Author

👤 **Leandro De Araujo**


***
