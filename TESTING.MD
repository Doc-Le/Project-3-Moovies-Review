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

      ![htmlvalidator](https://user-images.githubusercontent.com/76841050/163257408-b9813057-2468-40cf-864b-5c216872c7b3.png))

-   ## [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) 
    
    
      ![cssvalidator](https://user-images.githubusercontent.com/76841050/163257648-0c511620-c2d3-4a33-b8fa-cbd44b352730.png)


-   ## [Pep8 validation](http://pep8online.com/) 
    
    ### Initial/final testing
  
    - app.py 

      ![pep8validation](https://user-images.githubusercontent.com/76841050/163257632-5d5906e3-1f21-47bf-9608-daaff230158b.png)

    
-   ## [Lighthouse testing in devtools](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk?hl=en) 
       
  
     + Home.html (see report [here](app\static\tests\LHhome.png))

       ![LHhome](https://user-images.githubusercontent.com/76841050/163257658-7e378204-899a-46e2-ba90-5c2e3616fac8.png)

     + Login.html(see report [here](app\static\tests\Lhlogin.png))

       ![Lhlogin](https://user-images.githubusercontent.com/76841050/163257661-3010e65f-e6bf-4f9e-99f8-20846ac2c8e8.png)
     
     + Logout.html(see report [here](app\static\tests\LHlogout.png)

      ![LHlogout](https://user-images.githubusercontent.com/76841050/163257624-edc81ac2-b956-4a9c-ad18-46cb389382f3.png)

      
    
## Testing User Stories 

   - #### First Time Visitor 

      1. As a first time visitor, I want to easily understand the main purpose of the site.<br>
        The search bar is located in the center of the page, right below the logo. There is also a dropdown menu located in the top right corner. The dropdown menu with guests has login and signup options. 

         ![appmenu](https://user-images.githubusercontent.com/76841050/163257646-a3434974-42a1-4498-b4b0-f8613e89fca3.png)
         ![drodownmenu](https://user-images.githubusercontent.com/76841050/163257650-f7f51d8a-23e4-4e34-82d0-e3374f56e214.png)

         
      2. As a first time visitor, I want to be able to intuitively use the site.<br>
         I have put social links and other useful links in the footer. I also made sure that user understands that this project was base on TMDB, which is a link to their home page.

         ![footermenu](https://user-images.githubusercontent.com/76841050/163257654-47218c2a-d204-4fdf-abfb-282c4b9a9f1c.png)


      3. As a first time visitor, I expect to see an objective, visually simple site.<br>
         I have used the white and grey color for the entire<br> Have kept the design fairly simple.<br> Didn't want any gaps in the site or a broken link.

         
      4. As a first time visitor, I expect an accessible site.<br>
         
               
         * Already a member, use the login function.<br>
         ![login](https://user-images.githubusercontent.com/76841050/163257628-b9a9c2ca-a874-4726-a667-4f293e3e0f97.png)
         * A simple way to  become a member by signing up.<br>
         ![signup](https://user-images.githubusercontent.com/76841050/163257643-dd7ebde0-69f6-48aa-8a4e-57ae05485909.png)
         * Already logged in, you can logout anytime.<br>
         ![loggedinmsg](https://user-images.githubusercontent.com/76841050/163257626-7323a36b-0d02-40b7-968e-f2f416b82649.png)
         * After logged in click on Profile.<br>
         ![Profilemsg](https://user-images.githubusercontent.com/76841050/163257638-82ce3a2e-6714-4745-b529-6c3a51c03137.png)
         * Profile.<br>
         ![profile](https://user-images.githubusercontent.com/76841050/163257635-7cd5a24e-7684-45a5-80f1-b31f03e22ec3.png)
         

      6. As a first time visitor, I want to easily search the movies.<br>
         
         
         * The search bar is at the top or center of the home page, the user can use it to search for movie titles, actors, and actresses.<br>
         ![searchmovie](https://user-images.githubusercontent.com/76841050/163257642-d33d4884-4a39-4c17-aa57-ad7956cfce00.png)
         * After clicking on the review button, user will be able to leave the review.<br>
         ![thanksforreview](https://user-images.githubusercontent.com/76841050/163257644-9d8359a8-daf9-4bae-875e-cf02a2d37547.png)
         * Review function 
         ![updatingreview](https://user-images.githubusercontent.com/76841050/163257645-11337f06-3d76-4f07-9b30-a3314eb9e1e0.png)
         * No delete function needed, update your review.<br>
     
## Further Testing

* The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
* The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhone X.
* A large amount of testing was done to ensure that all pages were linking correctly.
* Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.