[![Build Status](https://travis-ci.org/LiamD88/secure_plus.svg?branch=master)](https://travis-ci.org/LiamD88/secure_plus)


# Milestone Project 4 - Secure Plus

This website is a full stack project which will allow users to register details, log in and purchase items from the site. It is aimed at commercial entities who wish to purchase cyber security services for a business.

[Secure Plus-access the site here](https://secure-plus.herokuapp.com/)

# Important Note

When making a payment on the site you must use the below details or else the payment will fail.

* Card Number: 4242424242424242
* Expiry Date: Any date in the future
* CVC: Any Three Digits
* ZIP: 00000



# UX

The design of the site isn't overly complicated, most pages are easy to navigate and layed out in a way for any user to find what they are looking for. The colour scheme is mainly black and an off white colour for text. The images on the pages being the brightest thing to see along with some of the submit buttons being a more stand out blue colour.

On the services page the options to purchase have a hover effect when you move the mouse over them to bring more animation to the site.

## User Stories
---
The site is aimed at commercial entities and I wanted to make it as simple as possible to navigate through the site. Below are some user stories.

1. As a multinational corporation with over 1000 staff cyber security is very important to us. I found this website quite easy to navigate, I like that they have a lot of the services offered but I think the main thing that stands out for me is they have an option to click a contact page and contact them about any other services I might need so they can tailor a package to my needs. I will requite this with so many staff.

2. As a small business owner I am not very computer literate and I want somebody to help me with everything about internet security as a lot of business is online these days. I have recently had a huge issue with a virus in the IT infrastructure of my business, I want to be able to go on here and have a complete overhaul. I see they have a package here for a comprehensive check of our systems, this is exactly what  I need.

3. As a graphic designer I do all of my work on my laptop and I want to ensure I am protected against any cyber threats because if somethign happens with this laptop I will be unable to work. Money is tight, a lot of companies don't display prices for this type of thing without contacting them first. I want to be able to see prices before approaching the company, this website has 3 main prices displayed and I think I will go for the monthly option.

4. As a student I want to have some sort of protection against cyber threats on my laptop to protect my work. I want a full list of all benefits and everything completely laid out when I look throuz§gh this site. Upon searching through services I can see they have some of the main benefits noted down but not all as this is more geared towards commercial entities and it looks like they will contact you after to get everything set up. This site is not for me as I am not a commercial business.

5. As a business owner just starting out costs are tight at the moment and it would suit me to havea an option to pay on a short term basis. When searching for costs I see they have a monthly option which suits me and I will go for this.

## Wireframes
---
Below are the links for wireframes, one was created for each device, mobile, tablet and desktop. The search page was initially designed but removed in the end.

* [Home Desktop Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Home%20Page%20Desktop.png)/
  [Home Ipad Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Home%20Page%20Ipad.png)/
  [Home Mobile Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Home%20Page%20Mobile.png)
* [Login Desktop Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Login%20Page%20Home.png)/
  [Login Ipad Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Login%20Page%20Ipad.png)/
  [Login Mobile Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Login%20Page%20Mobile.png)
* [Register Desktop Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Register%20Page%20Home.png)/
  [Register Ipad Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Register%20Page%20Ipad.png)/
  [Register Mobile Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Register%20Page%20Mobile.png)
* [Services Desktop Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Services%20Page%20Desktop.png)/
  [Services Ipad Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Services%20Page%20Ipad.png)/
  [Services Mobile Page](https://raw.githubusercontent.com/LiamD88/secure_plus/master/secure_plus/static/wireframes/Services%20Page%20Mobile.png)

# Features

### Home Page

There are two main features on the home page, the parallax effect images which is noticeable on desktop screens which you can scoll up and down. The second feature is the text in the centre of the page using the company name which has an animation effect.

### About Page

This page is mainly comprised of txt. There is a google map at the bottom of the page with a ficticious address to show the location of the company and there is also a clickable link which will bring you to the contact us page to send a contact request.

### Services Page

This has three main feature, the first is a carousel at the top of the page which will cycle through 3 seperate images. There is some text in the middle of the page to list services but the main feature being the 3 cards at the bottom of the page which have a hover effect when you move across them and have clicable links to purchase a service.

### Register/Login Page

Both these pages have the same feature, on the register page you have a form to fill in to register your details and the log in page is similar in that you fill in a form with your details to log in.

### Cart Page

This page has one main feature in the centre of the page a card with two buttons one to continue to the checkout and one to clear the cart.

### Checkout Page

This has 3 main features, the text at the top of the page will change depending on which option you have selected to purchase. There is a form to fill in your details to purchase. The final feature is the stripe payment form which allows you to enter in your card details.

### Future Features

* Customers having the option to log in and view there details, i.e current package they are on, how many days left etc.
* A new part of the site with a full breakdown on everything that is on offer in each package.
* Review section for customers to leave full reviews of our service.
* Online chat capabilitys for customers to speak to a live agent.

# Technologies Used 

* HTML - This was used to create the structure of the site and each individual page.
* CSS - This was used to style certain aspects of the site.
* Python - This is the main language used to create the backend of the website.
* [Bootstrap](https://getbootstrap.com/) Bootstrap was used to create the structure of the site using its grid system and to make the site responsive on all devices.
* [Django](https://docs.djangoproject.com/en/3.1/) This is a python framework which allowed me to structure all the views of my site into individual apps for each page.
* [Postgres SQL](https://www.postgresql.org/) The is the database I used for my project and linked with heroku to information of the models used.
* [JQuery](https://jquery.com/) This was used with bootstrap to allow you to place certain elements and functionality on your page.
 * [GitHub](https://github.com/) This allowed me to upload my local repository onto a remote server which was linked to Heroku to build which would push the latest changes to the version which was then built on Heroku.
 * [Heroku](https://www.heroku.com/) This is a site which allows you to deploy this type of application.
 * [VSCode](https://code.visualstudio.com) I used this as my ide to build my project. The local repository along with all my code was stored here.
* [Travis](https://travis-ci.org/) Travis was used to ensure project was building succesfully.
* [Stripe](https://stripe.com/ie) Stripe was used to process the payment on my site.
 * [HTML Validator](https://validator.w3.org/) This allowed me to validate my HTML.
 * [CSS Validator](https://jigsaw.w3.org/css-validator/) This allowed me to validate my CSS.
 * [Auto Prefixer](https://autoprefixer.github.io/) This was used to check if my CSS was valid on all browsers.

# Testing

[TESTING.md](https://github.com/LiamD88/secure_plus/blob/master/TESTING.md)This is a link to the testing done on this website.

# Issues/Bugs

* The parallax 1 image doesnt resize correctly on ipads when being scaled down.
* The registration form sometimes will not register details correctly if you just press enter on keyboard as opposed to clicking the submit button.
* On the home page, the two parallax images have an id of img1. I understand you can only have one id per element. In my extra.js file I added in img 1 + img 2 for this function to target both parallax imgas. However when I change the id in parallax2 to img 2 it doesnt work and when I remove the + img 2 from my extra.js file it only targets one image. This is the only way I could get it to work.
* In the contact app in views.py file the contact function I had an issue with send_mail. I had to create a generic email to place in here for emails to be sent to as when I tried to import the original from my env.py file it wouldnt work. Even importing from settings etc this was the only way I could get this to work.

# Deployment

This project was created with [VSCode](https://code.visualstudio.com) an external IDE not used on the course.
In order to deploy the project I have listed the steps I have taken below.

* The code was written in my local repository on VS code.
* A repository was created in Github for the project.
* The project was then linked from my local repository to github to allow the code to be stored remotely.
* An app was then created in heroku and under the deploy tab, you can enter your github repository link into this section to connect both repositories.
* In this section you can enable automatic deploys which allows you to automatically deploy a heroku build each time you update your github repository.
* The app was then available via a clickable link on the heroku site.

If you wish to deploy locally and clone the repository. To do this you would:

* Go to the main page of the github repository and click clone/download, this will be located under the repository name.
* In the section clone with HTTPS copy the clone URL and open the terminal on your IDE.
* Change the working directory to the location you wish your cloned directory to be placed.
* Type git clone and paste in your URL you had copied earlier.
* Now press enter and your clone will be created.

# Credits

## Content

* [Home Page Animation](https://tobiasahlin.com/moving-letters/#14) This is where i got the html/css and javascript for the animation of the company name on the home page. Also referenced in the css and js pages
* [Parallax Responsive design](https://inkplant.com/code/responsive-parallax-images) This is where i got the css and javascript for the responsive design of my parallax images, also referenced in css and js pages
* [Card Hover](https://stackoverflow.com/questions/63174850/how-to-add-animation-to-a-bootstrap-4-card-on-hover. ) This is where i got the css and for the hover effect on my cards on the services pages also referenced in css
* [Stripe Payments](https://stripe.com/docs/payments/accept-a-payment?integration=elements ) This is where i got the stripe html/css and javascript from to set up the card payment option, also referenced in the css and js pages.

* The footer social media links code was taken from a lesson the code institute provided us for the first project, works quite well so used it again.

  
## Media

* All images on the site are taken from google.
