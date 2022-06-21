# Skye Online English (Shop + LMS)

![Skye Online English - Responsive Views](media/readme_images/responsive_image.jpg)


[Skye Online English](https://www.skyeonlineenglish.com/) is an online English language teaching site.  It is currently focussed on providing face-to-face teaching.  This project intends to provide self-study opportunities for langauge students.  Similarly to sites like Udemy, this project aims to provide lifetime access for single purchases.

## Planning

User Stories - 
- As a User, I want to be able to view a list of available courses so that I can choose which one(s) to buy.
- As a User, I want to be able to sort courses by category so that I can find one more suited to my needs more quickly.
- As a User, I want to be able to view more details about a specific course so that I can make an informed decision before I purchase.
- As a User, I want to view all the items in my bag before purchasing.
- As a User, I want to be able to view the items in my bag at checkout so that I have a final chance to decide if I want to purchase.
- As a User, I want to be able to purchase items securely.
- As a User I want to be able to store my personal data so that I can use it again without having to reinput it.
- As a User, I want to be able to see all of my past purchases in order to ensure that I don't purchase something twice.
- As a User, I want to be able to register for an account to allow for quicker access at a later date.
- As a User, I want to be able to log in to see my personal data and log out when I am finished.
- As a User I want to be able to recover my password if I forget it.
- As a User, I want to be able to email the company with any questions that I may have.
- As a User, I want to be able to access my paid-for course content so that I can study.
- As a User, I would like to see my progress throughout each section of the course.
- As an Admin, I want to be able to add courses to my shop to encourage new business.
- As an Admin, I want to be able to edit/update my courses to keep them current.
- As an Admin, I want to be able to remove courses that I no longer need/want.
- As an Admin, I want to be able to view past orders to ensure there is no discrepancy between what the user bought and expected.


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

Wireframes - LMS

**Desktop**
- [Desktop View - LMS](media/wireframes/desktop_shop/1_lms_desktop_view.jpg)
- [Desktop View - LMS - Content](media/wireframes/desktop_shop/3_lms_content_desktop_view.jpg)

**Mobile**
- [Mobile View - LMS](media/wireframes/desktop_shop/2_lms_mobile_view.jpg)
- [Mobile View - LMS - Content](media/wireframes/desktop_shop/4_lms_content_mobile_view.jpg)

## Features

![Homepage](media/readme_images/home.jpg)

The homepage / base template allows users almost complete navigation throughout the site.  In the navigation bar there are links to:

- the homepage (current)
- all courses - a search with no filters applied
- General English - a search of all published courses with the category 'General English'
- Exam Skills - a search of all published courses with the ctegory 'Exam Skills'
- user's Profile Page - a link to the user's order history, personal details and link to the LMS
- Manage Content (superusers only) - link to content management (lessons, shop content)
- a search bar - for searching all published courses
- a link to a contact form
- a link to the site's privacy policy (footer)
- a link to the site's terms and conditions (footer)
- social links

**Searching / Course Results**

![Search Results](media/readme_images/courses_search_results.jpg)

Here we can see the filtered search results in order of course name.  At present there are only 2 courses for testing/display purposes.

![Search Results empty](media/readme_images/courses_search_results_no_results.jpg)

If the search results come up empty, users will see this message.


**Course Details**

![Course Details](media/readme_images/course_details_67.jpg)

In the course details page the user can see much more infromation about a course than in the search results.  This image has been zoomed out to 67% to show the 'Add to Bag' feature.  Users can only add it to their shopping if it has not been added already, and if it has not been bought before.  

**Shopping Bag**

![Shopping Bag](media/readme_images/shopping_bag.jpg)

In the shopping bag, users can review all the courses they wish to purchase and remove items.

**Checkout**

![Checkout](media/readme_images/checkout.jpg)

Users can purchase their courses here.  The payment system is Stripe.  Users can enter their billing address here and save it to their profile for faster checkout next time.  

**Post Checkout**

![Checkout Success](media/readme_images/post_checkout.jpg)

This page will provide the user with a summary of what has just been purchased.  There will be a copy of this available in the user's profile page.

**Personal Profile**

![Personal Page](media/readme_images/profile_oreder.jpg)

On this page will be a list of all the user's past orders along with their saved address.  This is also where the user will be able to access the LMS.  This was placed in here intentionally as opposed to in the navigation bar as the principle purpose of this site is to make money so the inital links are for business purposes.

**Contact**

![Contact Form](media/readme_images/contact.jpg)

Users can contact the company with questions/comments


### Ongoing Bug discovery and fixes

| Bug No' | Issue | Fix |
|---|---|---|
| 1 | Database isn't connecting and error was displaying in terminal stating 'FATAL:  no pg_hba.conf entry for host "34.76.234.132", user "zfbtmtppxoejuc", database "de76aaatkpqei5", no encryption' | Heroku conducted maintenance on Postgresql database and change the database url and emailed me to inform me.  I have updated the url in my env.py file and it seems to be working fine. |
| 2 | Repeat of bug number 1 - Added new Postgresql DATABASE_URL to env.py, will request further information from mentor/slack community |   |
| 3 | Bag items are not displaying after submitting 'Add to Bag' on course detials page | bag contexts file added to settings.py |
| 4 | Profile page not rendering when function in views.py pulls data from models.py | Created brand new user, seems to work ok after. |
| 5 | embedvideo package ran locally but video wouldn't display as embedded address was changed from 'Https' to 'Http' | Added Content Security Policy to base.html meta |
| 6 | Can access certain pages without logging in | Login_required decorators added to checkout and profiles pages |
| 7 | Summernote fields aren't displaying in the UI, only in the admin| Updated forms.py accordingly |
| 8 | Customers still had access to all courses that weren't paid for | Added for loop to filter course names that match what courses are bought in the user's profile |
| 9 | Customers can purchase the same thing twice but at different times| Added for loop to add_to_bag function tocompare with items already in user's profile |
| 10 | After installation of cloudinary, thumbnail images in LMS were not displaying | Changed model to Charfield and added the urls of the thumbnails in Cloudinary |
|11|Superusers do not have access to courses unless they purchase them|Wrapped view code for LMS content in if statement|

### Testing

#### Manual Testing

There was no automated testing carried out during this project. Each User Story was manually tested as follows:

#### User Stories

**As a User, I want to be able to view a list of available courses so that I can choose which one(s) to buy.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered the site's url|Homepage displays correctly|-|
|Selected 'All courses' from the nav bar|A list of all (2 for development purposes) display in the form of cards|**PASS**|
|Selected 'All courses' from the footer|A list of all (2 for development purposes) display in the form of cards|**PASS**|

**As a User, I want to be able to sort courses by category so that I can find one more suited to my needs more quickly**.

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered the site's url|Homepage displays correctly|-|
|Selected 'General English' from the nav bar|An error displays stating that there are no general English courses available at this time|**PASS**|
|Selected 'General English' from the footer|An error displays that there are no courses that match this search|**PASS**|
|Selected 'Exam Skills' from the nav bar|The two exam skills courses display correctly|**PASS**|
|Selected 'Exam Skills' from the footer|The two exam skills courses display correctly|**PASS**|
|Entered an exam name (IELTS) into the search bar|Only the IELTS course displayed|**PASS**|
|Entered 'English' into the search bar|Both courses displayed|**PASS**|
|Entered 'Cake'|An error displays that there are no courses that match this search|**PASS**|


**As a User, I want to be able to view more details about a specific course so that I can make an informed decision before I purchase.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered the site's url|Homepage displays correctly|-|
|Selected 'All courses' from the nav bar|A list of all (2 for development purposes) display in the form of cards|-|
|Selected 'More Details' fromm the bottom of the course cards|A new page opened up with more information about the specific course I selected.|**PASS**|
|Returned to 'All courses' and selected 'More Details' on a differernt course|A new page opened up with more information about the specific course I selected.|**PASS**|

**As a User, I want to view all the items in my bag before purchasing.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered the site's url|Homepage displays correctly|-|
|Selected 'All courses' from the nav bar|A list of all (2 for development purposes) display in the form of cards|-|
|Selected 'More Details' fromm the bottom of the course cards|A new page opened up with more information about the specific course I selected.|-|
|Selected 'Add to Bag'|Page refreshes and displays message stating that the item was successfully added, link appears at the bottom of the page with bag total|-|
|Returned to 'All courses' and selected 'More Details' on a differernt course|A new page opened up with more information about the specific course I selected.|-|
|Selected 'Add to Bag'|Page refreshes and displays message stating that the item was successfully added, link appears at the bottom of the page with bag total|-|
|Clicked on 'View Bag' at the base of page|Directed to 'Shopping Bag' page where I can see both of the items that I added|**PASS**|

**As I User, I want to be able to view the items in my bag at checkout so that I have a final chance to decide if I want to purchase.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Repeated steps above to add items to bag|Directed to Shopping bag page|-|
|Clicked on 'Secure Checkout' button|Directed to checkout page where user can pay for items||
|Button to return to Shopping Present|||
|Clicked button to return to Shopping Bag|Directed back to shopping bag where I can adjust the items|**PASS**|

**As a User, I want to be able to purchase items securely.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Repeated steps above to add items to bag|Directed to Shopping bag page|-|
|Clicked on 'Secure Checkout' button|Directed to checkout page where user can pay for items||
|Filled in personal details and added Stripe Test number from Stripe documentation.  Clicked on 'Complete Payment|Overlay loads asking user to wait||
|On completion of payment, page directs to 'Order Confirmation' page and displays message confirming purchase has been made||**PASS**|
|Accessed Stripe Dashboard|Accessed webhooks in Stripe's dashboard to confirm if payment was successful. Stripe shows response code 200 for payment intent, charges and balance|**PASS**|

**As a User I want to be able to store my personal data so that I can use it again without having to reinput it.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Repeated above steps to make a purchase but ensure that 'Remember my Details is selected|On successful payment, address is shown in order confirmation page||
|Clicked 'User's Profile Page'in nav bar|Address entered is displayed as it was entered in checkout|**PASS**|
|Accessed User Profile in admin panel|Address is displayed correctly|**PASS**|

**As a User, I want to be able to see all of my past purchases in order to ensure that I don't purchase something twice.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|After making a purchase, I clicked on 'User's Profile Page'|Past order(s) displayed in a table||
|I clicked on the order number of my purchase|Directed to a copy of the order confirmation page for the order in question|**PASS**|
- **NOTE**: the function to add items to the shopping bag has also been modified to compare against past orders.  It is not possible for the user to add a course to the bag if it has already been purchased.  An error will display if the user tries to do so.


**As a User, I want to be able to register for an account to allow for quicker access at a later date.**
&
**As a User, I want to be able to log in to see my personal data and log out when I am finished.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Clicked 'Sign Up' in the nav bar|Directed to sign-up page||
|*Duplicate Email*|||
|Attempted to sign up using an email which already has an account|Page refreshes and error states: A user is already registered with this e-mail address.|**PASS**|
|*Duplicate Username*|||
|Attempted to sign up with a username that already exists|Page refreshes and error states: A user with that username already exists.|**PASS**|
|*New User*|||
|Added unique username and email address|Received email asking to confirm that I have signed up||
|Clicked link in email|Directed to page asking for further confirmation||
|Clicked confirm|Redirected to Log In page with message confirming that an account was set up||
|Entered new username and password|Logged in Succesfully|**PASS**|
|*Log Out*|||
|After signing up and logging in, clicked on logout button in nav bar|Directed to page asking if I want to sign out||
|Clicked sign out|logged out of site, directed to home page with options to sign up and log in present in nav bar|**PASS**|

**As a User I want to be able to recover my password if I forget it.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered site url and clicked 'Log In'|Directed to log in page||
|Clicked 'Forgot Password' below login form|Directed to a screen requesting email address||
|Entered email address and clicked 'Reset my Passord'|An email was sent to the email address I entered||
|Email contains a link to reset passsword, clicked it|Directed to screen asking for new password||
|Entered 2 different passwords to test|Page refreshes telling me that they need to be the same|**PASS**|
|Entered 2 passwords that are the same|Page refreshes confirming that I have changed my password successfully||
|Navigated to log in screen to log in with new password|Logged in successfully|**PASS**|

**As a User, I want to be able to email the company with any questions that I may have.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Entered site url and clicked on 'Get In Touch'|Directed to a contact form||
|Entered data into form correctly and clicked 'Submit'|Page refreshed and a message displayed stating that the email was sent||
|Logged in as an Admin and clicked on 'Admin's Profile'|||
|Clicked on 'Go to Inbox'|The email that was sent has been received and is stored here|**PASS**|
|Returned to contact form and attempted to submit an incomplete form. Clicked 'Submit'|Form will not submit and cursor jumps to where error is|**PASS**|

**As a User, I want to be able to access my paid-for course content so that I can study.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Attempt to access course without purchasing|||
|New User|||
|Logged in a clicked on profile page. |||
|Clicked 'Open LMS'|Directed to a screen stating 'You haven't bought any courses yet.'|**PASS**|
|Via URL - if user not authenicated|||
|Entered URL of course in LMS|Redirected to login page|**PASS**|
|Via URL - if user is authenticated|||
|Entered URL of course that has not been purchased|Directed to LMS page with error stating that course has not been purchased|**PASS**|
|Attempt to access course post-purchase|||
|Logged in a clicked on profile page. |||
|Clicked 'Open LMS'|Directed to a screen with all purchased courses/lessons |**PASS**|
|Clicked on 'Start Studying'| Lesson opens correctly |**PASS**|

**As a User, I would like to see my progress throughout each section of the course.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Logged into the LMS|||
|Chose lesson to study|At the bottom of the content is a blue bar showing my progress|**PASS**|

**As an Admin, I want to be able to add courses to my shop to encourage new business.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Logged into site as superuser|'Profile Link' is now showing as admin's (signed in superuser) page||
|Clicked admin's Page|Directed to 'Manage Content' page||
|Clicked the arrow beside 'Add New Content'|3 options appear: Add a New Course Category, Add A New Lesson, Add New Course to the Shop ||
|*Add a New Course Category*|||
|Clicked button stating 'Add a New Course Category'|Directed to single firled form asking for a unique form category||
|Entered IELTS as form category| Error appears in corner stating that the lesson category cannot be added|**PASS**|
|Entered new category 'cake'|page redirected to 'manage' with confirmation that category has been added.  Logged into django admin to confirm.|**PASS**|
|*Add A New Lesson*|||
|Completed form adding test content in each field|||
|Returned to 'manage' and clicked on the arrow beside 'Edit Lesson Content'|New lesson is displayed on list of lessons||
|Clicked 'View Lesson' next to the added lesson|Lesson opens in LMS content|**PASS**|
|Completed form adding test leaving out required fields|Form will not submit if a required field is not filled and the cursor will jump to the problematic field|**PASS**|
|*Add New Course to the Shop*|||
|Completed form adding test content in each field|||
|Returned to 'manage' and clicked on the arrow beside 'Edit Shop Content'|New shop content is displayed on list of shop courses|**PASS**|
|Clicked on Exam Skills |Can see new course on display in shop|**PASS**|
|Completed form adding test leaving out required fields|Form will not submit if a required field is not filled and the cursor will jump to the problematic field|**PASS**|

- NOTE, it was decided not to give end users the ability to remove lesson categories in the UI as the potential for deleting more content than anticipated is high.  This feeature is to remain in the django admin.

**As an Admin, I want to be able to edit/update my courses to keep them current.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Logged into site as superuser|'Profile Link' is now showing as admin's (signed in superuser) page||
|Clicked admin's Page|Directed to 'Manage Content' page||
|Clicked on the arrow next to 'Edit Lesson Content'|Displays a dropdown list of all lessons and all courses||
|Clicked 'Edit Lesson' next to the lesson I wanted to edit|Directed to a page with a similar form to the 'Add Lesson' form||
|Updated fields and clicked 'update'|Redirects to 'manage' with 'success' message displayed||
|Clicked on the arrow next to 'Edit Lesson Content' and clicked 'Edit Lesson' next to the lesson I just edited|Changes are reflected.  Logged into Django admin to confirm|**PASS**|
|Tried to remove a 'required field|Form wouldn't save and cursor jumped to problematic field|**PASS**|

**As an Admin, I want to be able to remove courses that I no longer need/want.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Logged into site as superuser|'Profile Link' is now showing as admin's (signed in superuser) page||
|Clicked admin's Page|Directed to 'Manage Content' page||
|*Lessons*|||
|Clicked on the arrow next to 'Edit Lesson Content'|Displays a dropdown list of all lessons and all courses||
|Clicked 'Delete Lesson' next to the lesson I don't want|Page refreshes and lesson disappears from list.  Logged into Django admin to confirm.|**PASS**|
|*Shop Content*|||
|Clicked on the arrow next to 'Edit Shop Content'|Displays a dropdown list of all shop content||
|Clicked 'Course in Shop' next to the course I don't want|Page refreshes and course disappears from list.  Logged into Django admin to confirm.|**PASS**|

**As an Admin, I want to be able to view past orders to ensure there is no discrepancy between what the user bought and expected.**

|**Test**|**Result**|**Verdict**|
|---|---|---|
|Logged into Django Admin site|||
|Clicked 'Orders' in 'Checkout Section' on the left|A list of all orders is displayed|**PASS**|

- NOTE, it was decided to keep this in the Django admin site as this has the potential to be a very, very large database.

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
- [Summernote version 0.8.20.0](https://pypi.org/project/django-summernote/)
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