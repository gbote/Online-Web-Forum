# Online-Web-Forum (Project Assignment)

## Introduction

I created an "online" web forum where users can read posts, create new posts, and comment on existing posts. This gave me practice with using forms and dealing with creating new data. Since I have not yet learned how to manipulate SQL databases, I will stick to modifying CSV files.

## 1. Create Django Project

By now, I was familiar with all the steps required to create a new Django project. A couple helpful reminders for future reference:
- Make sure you create a .gitignore file and ignore your virtual environment folder
- Make sure you create a requirements.txt file to store all the library versions that your project is using

## 2. Relocate Files

My data and class logic previously implemented in a past simple Python program:
- `models.py` - Contains all of the data classes we need, as well as all of the CSV reading and writing logic. I moved this file to replace the default Django app's models.py with this one.
- `data` folder - Contains all of the csv files (`posts.csv` and `comments.csv`) that we need. I moved this entire folder into my Django app folder. 

## 3. Create View Handlers / Templates / Routing

My goals for this challenge were to implement the following webpages/functionality:

1. Home Page
- This page should show a list of all posts that exist already, showing the title as a hyperlink and the author's name next to the title.
- Each link should take the user to the Post Detail Page, for that specific post.
- Include a button that takes the user to the New Post Page. 

2. Post Detail Page
- This page should show all of the detail about the specific post (Title, Author, Body, Time Created).
- This page should also show all of the comments (Body, Author, Time Created) that have been made for this post. 
- This page should allow users to create a new comment right from this page (not from a new page!).

3. New Post Page
- This page should contain a form to create a new post (Title, Author, Body).
- This page should redirect to the Post Detail Page upon creation of a new post. 

## 3. Styling

I created a base layout template for our template pages. Then, I applied some nice CSS styling to make the pages look more visually appealing.

## 4. Bonus: Bootstrap Form Controls (COMPLETED)

Bootstrap provides some nice form controls that can help make form UIs look better. I checked out the the documentation on [Form Controls](https://getbootstrap.com/docs/4.1/components/forms/) and I tried to implement them for the project here.

