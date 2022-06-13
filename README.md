# Skye Online English

## Planning

User Stories

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

### Ongoing Testing

**General**

| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 | Attempted to access pages that are notavailable to the public | Entering the url to 'protected' pages (bag.html, checkout.html, checkout-success.html, lms.html, lms-content.html) should redirect user to a login page | After applying login-decorators to each of the aforementioned pages, user is redirected accordingly. |

**Page Specific - Home**
| Test No' | Issue | Steps Carried Out | Result |
|---|---|---|---|
| 1 |Banner serves as link to homepage|Clicked on the banner on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 2 |Navbar 'Home' link serves as link to homepage.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 3 |Navbar 'All Courses' link serves as link to view all courses currently uploaded onto site.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the homepage - **PASS**|
| 4 |Navbar 'General English' link serves as link to view only courses connected to General English, no Exam courses should be viewable.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display General English courses - **PASS**|
| 5 |Navbar 'Exam Skills' link serves as link to view only courses connected to Exam Skills, no General English Courses should be viewable.|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the all courses page, but the results are filtered to only display Exam Skills courses - **PASS**|
| 6 |Navbar 'login' link serves as link to the login page|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the login page - **PASS**|
| 7 |Navbar 'signup' link serves as link to the signup page|Clicked on the link on all pages|When hovering over the banner, the intended address appears in the bottom of the screen.  Clicking takes the user to the login page - **PASS**|


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
- [Summernote version 0.8.20.0](https://github.com/summernote/django-summernote)
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