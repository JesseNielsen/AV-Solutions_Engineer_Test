# Solutions Engineering Test

Welcome to the AgVend Digital Solutions solutiosn engineering test. Follow the instructions below to set up your development environment using GitHub Codespaces.

## Setup Instructions

# Instructions for Completing and Submitting the Solutions Engineer Test

## Completing the Test

1. **Create Your Repository from the Template:**
   - Go to the [template repository](https://github.com/zolfran/AgVend-Developer-Test).
   - Click on the green `Use this template` button.
   - Select `Create a new repository`.
   - Name your new repository and make it public.

2. **Open the Repository in GitHub Codespaces:**
   - Navigate to your newly created repository on GitHub.
   - Click the `Code` button.
   - Select `Open with Codespaces` from the dropdown menu.
   - If you do not see `Codespaces` as an option, click `New codespace` and select the appropriate branch (usually `main`).

3. **Work on the Tasks:**
   - The Codespace and app should fully work out of the box.
   - The Codespace will automatically set up the environment based on the configuration files provided in the repository.
   - You do not need to create any new directory structures. At a minimum you will only need to work in the /hello_world/core/views.py, the /hello_world/templates/index.html, and the /hello_world/templates/add_book.html file to complete the first few tasks.
   - You do not need to install any dependendencies or run any commands to get the environment and app running. 
   - Complete the tasks outlined in the README.md.
   - Follow along with #TO-DOs to see where you need to write any code.
   - NOTE - Feel free to use any tools to complete this project. If you need to, use Chat-GPT - just be ready to tell us how you used it, 
     why, and what you learned. 

4. **Commit Your Changes:**
   - As you complete each task, commit your changes to your repository.
   - Use meaningful commit messages to describe your changes.
   - ** If you have trouble submitting commits, check your remote origin 
   - *** Run `git remote -v` to see the end branch URL (this should be blank)
   - *** Add your branch URL by running `git remote add origin https://github.com/<your-username>/<your-repository>.git`
   - *** Run `git push -u origin main`
   - *** Run `git fetch origin`
   - *** Run `git rebase origin/main`

5. **Push Your Changes:**
   - Push your commits to your GitHub repository.
     ```sh
     git add .
     git commit -m "Completed task XYZ"
     git push origin main
     ```

## Submitting Your Work

1. **Share the Repository Link:**
   - Once you have completed the tasks and pushed all your changes, share the link to your repository with us.
   - Fill out the Feedback Form saved in this template repo: "Solutions-Engineer-Test-Summary.md"
   - You can send the link via email or through any other communication method provided.

2. **Review:**
   - Our team will review your repository, including your commits, code changes, and any additional documentation you have provided.

Thank you for completing the test. We look forward to reviewing your work!

## Tasks

### Backend Development
- Implement the following API endpoints in the /hello_world/core/views.py file :
  - `POST /add-book` - Add a new book.
  - `GET /books/<isbn>` - Retrieve book details.
  - `PUT /books/<isbn>` - Update stock quantity.
  - `DELETE /books/<isbn>` - Delete a book.

### Frontend Development
- Create a user interface to interact with the above API endpoints. This environment is using Django HTML templates. 
  - Navigate to the hello_world/templates directory. Here is where you will find the "add book" page (add_book.html) and the landing page (the first loaded screen you see) -- index.html. Make an update to the index.html and the environment should auto-save and update.
  - There is currently a "bug" where after you add a book, the page doesn't redirect back to the index page. Add python logic in either the add_book function in /core/views.py to redirect the user to homepage after adding a new book, OR add html in the /templates/add_book.html that is a button that the user can click to get back to the homepage (index.html or url route "/"). 
  - Additional points for any interfaces built that are user-friendly and responsive.
  - Additional points if you add more HTML pages for more functionalities you build in the /core/views.py file. 

### Database Management
- Review the database model in the hello_world/models.py file.
- The model you need for this app has already been built, just review the table. 
- Write SQL queries to:
  - Retrieve books by a specific author.
  - Find the top 5 most expensive books.
  - Update the price of a book by its ISBN.
  - Delete all books with zero stock.
- You can either turn these SQL Queries into functions in the views.py file, or you can just write the queries in pure SQL in a new file and leave the logic unintegrated for now.
- Explain how you would optimize the database for performance.

### Code Review and Debugging
- Review and fix the provided code snippet in `core/views.py`.
- Explain the issues and your fixes in a separate document.

## Environment Details

- **Python Version:** 3.9
- **Django Version:** 5.0.4
- **Database:** SQLite (for simplicity, replace with PostgreSQL if needed)

Feel free to reach out if you have any questions or encounter any issues.
