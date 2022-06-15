# Skye Online English (Shop + LMS)

![Skye Online English - Responsive Views](media/readme_images/responsive_image.jpg)


[Skye Online English](https://www.skyeonlineenglish.com/) is an online English language teaching site.  It is currently focussed on providing face-to-face teaching.  This project intends to provide self-study opportunities for langauge students.

## Planning

User Stories - 

Wireframes - Shop

**Desktop**

- [Desktop View - Homepage](media/wireframes/desktop_shop/1_desktop_view_homepage.jpg)
- [Desktop View - All Courses](media/wireframes/desktop_shop/2_desktop_view_all_courses_contents_page.jpg)
- [Desktop View - Course Details](media/wireframes/desktop_shop/3_desktop_view_course_details.jpg)
- [Desktop View - Shopping Bag](media/wireframes/desktop_shop/4_desktop_view_course_shopping_bag.jpg)
- [Desktop View - Checkout](media/wireframes/desktop_shop/5_desktop_view_checkout.jpg)

**Mobile**
- [Mobile View - Homepage](media/wireframes/desktop_shop/1_mobile_view_homepage.jpg)
- [Mobile View - All Courses](media/wireframes/desktop_shop/2_mobile_view_all_courses_contents_page.jpg)
- [Mobile View - Course Details](media/wireframes/desktop_shop/3_mobile_view_course_details.jpg)
- [Mobile View - Shopping Bag](media/wireframes/desktop_shop/4_mobile_view_course_shopping_bag.jpg)
- [Mobile View - Checkout](media/wireframes/desktop_shop/5_mobile_view_checkout.jpg)

### Ongoing Bug discovery and fixes

| Bug No' | Issue | Fix |
|---|---|---|
| 1 | Database isn't connecting and error was displaying in terminal stating 'FATAL:  no pg_hba.conf entry for host "34.76.234.132", user "zfbtmtppxoejuc", database "de76aaatkpqei5", no encryption' | Heroku conducted maintenance on Postgresql database and change the database url and emailed me to inform me.  I have updated the url in my env.py file and it seems to be working fine. |
| 2 | Repeat of bug number 1 - Added new Postgresql DATABASE_URL to env.py, will request further information from mentor/slack community |   |
| 3 | Bag items are not displaying after submitting 'Add to Bag' on course detials page | bag contexts file added to settings.py |
| 4 | Profile page not rendering when function in views.py pulls data from models.py | Created brand new user, seems to work ok after. |
| 5 | embedvideo package ran locally but video wouldn't display as embedded address was changed from 'Https' to 'Http' | Added Content Security Policy to base.html meta |
| 6 | Can access certain pages without logging in | Login_required decorators added to checkout and profiles pages |
| 7 | Summernote fields aren't displaying in the UI, only in the admin| Replaced Summernote with ckeditor|
| 8 | Customers still had access to all courses that weren't paid for | Added for loop to filter course names that match what courses are bought in the user's profile |
| 9 | Customers can purchase the same thing twice but at different times| Added for loop to add_to_bag function tocompare with items already in user's profile |

### Testing

**General**

| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 | Attempted to access pages that are notavailable to the public | Entering the url to 'protected' pages (bag.html, checkout.html, checkout-success.html, lms.html, lms-content.html) should redirect user to a login page | Redirects working correctly - **PASS** |
| 2 | Attempted to access pages that are only available to superusers | Entered the url to content management pages as a logged-in and non-logged-in user | I was unable to access the pages without superuser access - **PASS** |

**Page Specific - Home**
| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 |Banner serves as link to homepage|Clicked on the banner on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 2 |Navbar 'Home' link serves as a link to homepage.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 3 |Navbar 'All Courses' link serves as a link to view all courses currently uploaded onto site.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 4 |Navbar 'General English' link serves as a link to view only courses connected to General English, no Exam courses should be viewable.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display General English courses - **PASS**|
| 5 |Navbar 'Exam Skills' link serves as a link to view only courses connected to Exam Skills, no General English Courses should be viewable.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display Exam Skills courses - **PASS**|
| 6 |Navbar 'login' link serves as a link to the login page|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the login page - **PASS**|
| 7 |Navbar 'signup' link serves as a link to the signup page|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the signup page - **PASS**|
| 8 |Navbar 'Search Bar' should search through title and description for search results. |Entered three search terms - IELTS / English / ability |Searching for IELTS returned only the IELTS courses, searching for English returned all courses as 'English' is in all descriptions and searching for 'ability' only returned the courses with the word 'ability' in the description - **PASS**|
| 9 |Main body Links - Clicking on 'view details' in 'Exam Courses box will view only courses connected to Exam Skills, no General English Courses should be viewable.|Clicked on the link|When hovering over the button, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display Exam Skills courses - **PASS**|
| 10 |Main body Links - Clicking on 'view details' in 'General English box will view only courses connected to General English, no Exam Skills Courses should be viewable.|Clicked on the link|When hovering over the button, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display General English courses - **PASS**|
| 11 |Main Body Links - Clicking 'Get in Touch' in the 'Get in Touch' box will take the user to the contact page.|Clicked on the link|When hovering over the button, the intended address appears in the bottom of the screen.  Clicking takes the user to the all contact page - **PASS**|
| 12 |Footer Link 'Home' serves as link to homepage.|Clicked on the link on all pages|When hovering over the link in the footer, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 13 |Footer Link 'All Courses' serves as a link to the All Courses page.|Clicked on the link on all pages|When hovering over the link in the footer, the intended address appears in the bottom of the screen.  Clicking takes the user to the All Courses page - **PASS**|
| 14 |Footer Link 'General English' serves as link to view only courses connected to General English, no Exam courses should be viewable.  At present, there are no General English Courses available so the link should return  no courses accordingly |Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display General English courses.  As there are none, a message is displayed - **PASS**|
| 15 |Footer Link 'Exam Skills' serves as link to view only courses connected to Exam Skills, no General English Courses should be viewable.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display Exam Skills courses - **PASS**|
| 16 |Footer Link 'Privacy Policy' link serves as a link to the Privacy Policy page.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to the Privacy Policy - **PASS**|
| 17 |Footer Link 'Terms and Conditions' link serves as a link to the Terms and Conditions page.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to the Privacy Policy - **PASS**|
| 18 |Footer Link 'Contact Us' link serves as a link to the Contact Us page.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to the Contact Us page - **PASS**|
| 19 |Footer Link 'Facebook' link serves as a link to Facebook.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to Facebook - **PASS**|
| 20 |Footer Link 'Instagram' link serves as a link to Instagram.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to Instagram - **PASS**|
| 21 |Footer Link 'LinkedIn' link serves as a link to LinkedIn.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to LinkedIn - **PASS**|
| 22 |Footer Link 'Youtube' link serves as a link to Youtube.|Clicked on the link on all pages|When hovering over the link, the intended address appears in the bottom of the screen.  Clicking takes the user to Youtube - **PASS**|

**Page Specific - Courses**
| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 | Each course 'card' should link to a page dedicated to that course |Clicked the links| Hovering over the 'MORE DETAILS' button I can see that the urls are the same with the exception of the final integer.  Clicking the buttons takes me to the expected pages - **PASS** |
| 2 | When returning to this page after adding items tot he shopping bag should display a floating div at the bottom which will link to the bag | After clicking 'MORE DETAILS' to be taken to the course's details page, I clicked 'Add to Bag' which displayed a message confirming that the item was added to the bag.  The floating div appeared at the bottom of the screen.  I navigated back to the courses page. | The floating div remains as expected and clicking the link takes me straight to the shopping bag - **PASS** |

**Page Specific - Course's Details**
| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 | Clicking 'add to bag' should only add the item to the bag. | As the floating div was not present, the bag was empty, however I navigated to the 'bag.html' url to confirm.  Then I returned to the course details page and clicked add to bag.  A success message appeared in the top corner and the floating div at the base | On navigating to the bag, I can see the item that I added - **PASS** |
| 2 | Users should not be able to add the same product twice | After completing the first test, I navigated back to the same course page and clicked 'Add to Bag' again. | An error message appeared in the top corner telling me that the item is already in the bag.  The value in the floating div hasn't changed and on navigation to the bag I can only see the item once - **PASS** |
| 3 | Users should only be able to buy a course once.  They cannot buy it a second time as they already have lifetime access| After simulating payment via stripe, I navigated back to the course page and clicked 'Add to Bag' | An error appeared in the top corner telling me that it has already been purchased.  Test was repeated by setting items to 'bought' in the djjango admin panel - **PASS**|

### Technologies Used

**Languages**

- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python version 3.2.13](https://www.python.org/)


**Libraries**

- [Bootstrap version 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [jQuery Version 3.6](https://jquery.com/)


**Packages**

- [Django version 3.2.13](https://www.djangoproject.com/)
- [Allauth version 0.50.0](https://django-allauth.readthedocs.io/en/latest/index.html)
- [Crispy Forms version 1.14.0](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
- [ckeditor vesion 6.4.2](https://ckeditor.com/)
- [Django Countries version 7.3.2](https://pypi.org/project/django-countries/#installation)
- [Stripe](http://stripe.com/)
- [Embed Video version 1.4.4](https://pypi.org/project/django-embed-video/)
- [Pillow version 9.1.1](https://pypi.org/project/Pillow/)

### Media Used

**Homepage image** - [Pexels](https://www.pexels.com/) - <https://images.pexels.com/photos/3786748/pexels-photo-3786748.jpeg>

**Icons** - [Ionicons](https://ionic.io/ionicons)

**Fonts Used** - [Google Fonts](https://fonts.google.com/)

- Lato - <https://fonts.google.com/specimen/Lato>
- Roboto - <https://fonts.google.com/specimen/Roboto>
- Raleway - <https://fonts.google.com/specimen/Raleway>

**Colors** - As taken from source site <https://www.skyeonlineenglish.com>

- Text - [#0cad95](https://g.co/kgs/DqF28c) & [#b877a9](https://g.co/kgs/yjHqid) & [#000000](https://g.co/kgs/xfSLW2) & [#cacecd](https://g.co/kgs/91ighC)
- Backgrounds - [#ffff](https://g.co/kgs/yDTdox)
- Borders - [#b877a9](https://g.co/kgs/yjHqid)