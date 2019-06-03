
## My Cook Book

The purpose of this project is to give the user access to their own personal list of Recipes with the ability to
Create, Update and Delete recipes as they wish. This is done through a user friendly website which is optomised for a mobile platform.



 
## UX
 
This website will appeal to users who have an interest in home cooking or baking.

***Below are a sample of wireframe mockups that the site was modelled on. The final version may differ to the initial layout.***

- Homepage and Recipe list ***Desktop*** and ***Mobile*** view

![Alt homepage/Recipe list](/static/images/homepage_desktop_mobile.png "Desktop/Mobile")

- Recipe view page ***Desktop*** 

![Alt Recipe page](/static/images/recipe_page_desktop.png "Desktop")

- Recipe view page ***Mobile*** 

![Alt Recipe page](/static/images/recipe_page_mobile.png "Mobile")




## Features
 
### Existing Features
- Feature 1 - allows users Create a custom Recipe of there choice by filling out the form which is located under Add Recipe link. This is located on the far right hand side on the home page. For mobile view(smartphone), the same link can be located in the drop downmenu or by scrolling to the bottom of the screen

![Alt Main Menu](/static/images/edit_menu.png "Homepage")

![Alt Edit Form](/static/images/Add_Recipe_form.png "Add Recipe")

- Feature 2 - allows to add a Recipe to their Favourite list which is achieved by ticking the Add to favourites checkbox under the Add recipe option. 

![Alt Add to  Favourite](/static/images/Add_to_favourites.png "Add to Favourites")

- Feature 3 - allows users to email a recipe to a friend or collegue by clicking on the email option  which is available on the Recipe page

![Alt email link](/static/images/email_link.png "Email Recipe")

- This will open your current email client as seen below. The link for the recipe will be in the body of the email.

![Alt email client](/static/images/email_client.png "Email client")

- Feature 4 - allows users to edit any recipe by clicking on the edit button located on the Recipe page

![Alt email client](/static/images/edit_recipe_link.png "Email client")

- This will open your current the edit form with all the recipe fields populates. The user can then make changes and then resubmit are cancel if required.

![Alt email client](/static/images/edit_recipe_form.png "Email client")


### Features Left to Implement

- Future features may have included a user login option for the purpose of rating or reviewing recipes.
- Pagination as lists may become very long to scroll through.
- Search bar

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
     - I used ***FontAwesome*** in this project to manipulate the DOM. example, drop down menu for mobile devices

- [Fontawesome](https://fontawesome.com/)
    - I used ***FontAwesome*** in this project to style buttons, fonts and buttons.

- [Bootstrap](https://getbootstrap.com/)
    - I used ***Bootstrap*** in this project as the main framework that set the look and feel of the website and helped me to modify it for mobile application.
    


## Testing

The following checks were performed manually to ensure the site was n good working order

1. Homepage:
    1. From the "Home" page
    1. Hover over all Links to confirm that description is displaying
    2. Click on all Links to confirm that they are working and directing you to the correct location

2. Recipes:
    1. Go to the "Recipes" page
    2. From the Recipes page click on the recipe that you wish to view and confirm that it is working
    

3. Favourites:
    1. Favourites has the same functionality as Recipes page
    

4. Categories:
    1. Go to the "Categories" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

5. Add Recipe:
    1. Go to the "Add Recipe" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to enter text into either the number of servings or difficulty and confirm that the keyboard will not allow this.
    4. Try to tick the favourites box and confirm that after submission that It was added to the Favourites List
    5. Leave favourites box unticked and after submission confirm that It was not added to the Favourites List
    6. Try to submit the form with all inputs valid and verify that a success message appears.

6. Email:
    1. Go to the "Recipe" page
    2. Click on the Email link and confirm that it opens your local email client with the Recipe title as the subject and the Link to the Recipe as the body of the email
    
7. Delete:
    1. Go to the "Recipe" page
    2. Click on the Delete link and confirm that the Recipe that you were viewing is now deleted from the the Recipe list
    

8. Edit:
    1. Go to the "Recipe page" page
    2. Clik on the edit link and confirm that the Recipe Form is opened with all of the inputs populates with the Recipe details

- Below are a few samples of how the site displayed on different browsers and devices


- Homepage viewed on Chrome browser
![Alt chrome](/static/images/chrome.png "chrome homepage")


- Homepage viewed on Explorer browser
![Alt expolrer](/static/images/explorer.png "explorer homepage")


- Homepage viewed on Opera browser
![Alt opera](/static/images/opera.png "opera homepage")


- Homepage viewed on Firerox browser
![Alt firefox](/static/images/firefox.png "firefox homepage")


![Alt mobile](/static/images/iphone678.png "iphone homepage") ![Alt mobile](/static/images/iphone678_recipe.png "iphone Recipe page") ![Alt mobile](/static/images/homepage_S5.png "Galaxy S5 homepage") 



![Alt mobile](/static/images/galaxys5.png "Galaxy S5 Recipe page") ![Alt ipad](/static/images/ipad.png "ipad homepage")


## Deployment



For this project I had to deploy code to 2 different hosting platforms

- Github pages for Repositories
- Heroku for Hosting the site

After every new development on the site I would save my work and proceed to upload the changes that I had made to both Platforms

Both platforms have the exact same code deployed to them. The current number of commits stands at 73. Each commit represents a large or small adjustments and is describe with a comment as to what was done.

## Credits

### Content
- The text for Add Recipe description was copied from the [Alldishes submit your recipe](http://dish.allrecipes.com/customer-service/submit-your-recipes/)
- I used sample recipes from  [BBC GoodFood](https://www.bbcgoodfood.com/)

### Media
- The photos used in this site were obtained from ...

- [Unsplash](https://unsplash.com/)

### Acknowledgements

I used [W3SCHOOLS](https://www.w3schools.com/)  for all issues that arrose with javascript issues in particular form validation 


I took influence from the following websites

 In particular the Recipe layout
- [BBC Good Food](https://www.bbcgoodfood.com/)

- [Delish, Recipes, Party, Food](https://www.delish.com/)





