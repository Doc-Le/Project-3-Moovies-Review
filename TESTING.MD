# Testing

## Contents 
   - [Automated Testing](#automated-testing)
      * [HTML validation](#w3c-markup-validator)
      * [CSS validation](#w3c-css-validator)
      * [Pep8 validation](#pep8-validation)
      * [Lighthouse testing](#lighthouse-testing-in-devtools)
   - [Testing User Stories](#testing-user-stories)
   

## Automated Testing

The W3C Markup Validator and W3C CSS Validator were used to validate every page of the project to ensure there were no syntax errors in the project.

-   ## [W3C Markup Validator](https://validator.w3.org/) 

    ![html test](app\static\tests\htmlvalidator.png)

-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
    
      ![css test](app\static\tests\cssvalidator.png)


-   ## [Pep8 validation](http://pep8online.com/) 
    
    ### Initial/final testing
  
    - app.py 

      ![Initial contact javascript test](app\static\tests\pep8validation.png)

    
-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
       
  
     + Home.html (see report [here](app\static\tests\LHhome.png))

       ![index.html](app\static\tests\LHhome.png)

     + Login.html(see report [here](app\static\tests\Lhlogin.png))

       ![index.html page scores for Login](app\static\tests\Lhlogin.png)
     
     + Logout.html(see report [here](app\static\tests\LHlogout.png)

       ![index.html page scores for Logout](app\static\tests\LHlogout.png)

      
    
## Testing User Stories 

   - #### First Time Visitor 

      1. As a first time visitor, I want to easily understand the main purpose of the site.<br>
        The search bar is located in the center of the page, right below the logo. There is also a dropdown menu located in the top right corner. The dropdown menu with guests has login and signup options. 

         ![app menu](app\static\tests\appmenu.png)
         ![app dropdown](app\static\tests\drodownmenu.png)

         
      2. As a first time visitor, I want to be able to intuitively use the site.<br>
         I have put social links and other useful links in the footer. I also made sure that user understands that this project was base on TMDB, which is a link to their home page.

         ![app footer links](app\static\tests\footermenu.png)


      3. As a first time visitor, I expect to see an objective, visually simple site.<br>
         I have used the white and grey color for the entire<br> Have kept the design fairly simple.<br> Didn't want any gaps in the site or a broken link.

         
      4. As a first time visitor, I expect an accessible site.<br>
         
               
         * Already a member, use the login function.<br>
         ![app login](app\static\tests\login.png)
         * A simple way to  become a member by signing up.<br>
         ![app signup](app\static\tests\signup.png)
         * already logged in, you can logout anytime.<br>
         ![app logged in](app\static\tests\loggedinmsg.png)
         ![app profile](app\static\tests\Profilemsg.png)
         

      6. As a first time visitor, I want to easily search the movies.<br>
         
         
         * The search bar is at the top or center of the home page, the user can use it to search for movie titles, actors, and actresses.<br>
         ![app search bar](app\static\tests\searchmovie.png)
         * After clicking on the review button, user will be able to leave the review.
         ![app search bar](app\static\tests\review.png)

     
## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhone X.
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.