# Online-Web-Forum (Project Assignment)

## Introduction

We're going to ask you to create an a very basic online web forum where users can read posts, create new posts, and comment on existing posts. This will give us practice with using forms and dealing with creating new data. Since we've not yet introduced databases, we'll be stuck with CSV files to persist our data.

## 1. Create Django Project

By now, you should be pretty familiar with all the steps required to create a new Django project, so we're not going to list all of the steps out for you (refer back to your notes if needed). A couple helpful reminders:
- Make sure you create a .gitignore file and ignore your virtual environment folder
- Make sure you create a requirements.txt file to store all the library versions that your project is using

## 2. Relocate Files

We already have implemented all of the data and class logic for you:
- `models.py` - Contains all of the data classes we need, as well as all of the CSV reading and writing logic. Move this file to replace your Django app's models.py with this one. (Note that we are only simulating what our `models.py` would sort of look like, but we'll see how to properly use Django Models later on.)
- `data` folder - Contains all of the csv files (`posts.csv` and `comments.csv`) that we need. Move this entire folder into your Django app folder. 

Make sure you read the contents of `models.py` to understand what we'e provided. We read in our file data into two `all_posts` and `all_comments`, and addtionally created a nested structure for `all_posts` (a post can have comments associated with it) for convenience. You should not have to add or modify anything in `models.py` to solve this challenge (but you can if you desire to). 

## 3. Create View Handlers / Templates / Routing

Your goal for this challenge is to implement the following webpages/functionality:

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

If you haven't already done so, create a base layout template for our template pages. Then, apply some nice CSS styling to make our pages look a little more visually appealing!

## 4. Bonus: Bootstrap Form Controls

Bootstrap provides some nice form controls that can help make our form UIs look better. Check out the the documentation on [Form Controls](https://getbootstrap.com/docs/4.1/components/forms/) and see if you can try to implement them for our project here.

