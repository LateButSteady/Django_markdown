# Django_markdown
Example of Django markdown page

# Post in markdown in your Django web application #

## Tutorial ##
1. Pull the repository
    ```
    git clone https://github.com/LateButSteady/Django_markdown
    ```
2. Move to the directory

3. Activate virtualenv
    - Note that repository used python 3.9 (Later version than 3.6 is recommended)

4. Install packages using requirements.txt
    ```
    pip install -r requirements.txt
    ```

5. Run the server locally.
    ```
    python manage.py runserver
    ```
   You will see the log like below if the server is successfully opened.
    ```
    System check identified no issues (0 silenced).
    February 07, 2023 - 03:10:08
    Django version 4.1.6, using settings 'django_md.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
      
6. Enter the url below in browser to open the django page
    ```
    localhost:8000
    ```
   You will see a button "Markdown page". Click it.
   
7. There are two posts. Each post will redirect and show the body.

8. You can add posts in the Django admin page
    ```
    localhost:8000/admin
    ```
9. Login with the info
    - ID: admin
    - Password: admin
    - * You can make your own superuser with the following command.
    
    ```
    python manage.py makesuperuser
    ```

10. Click "Posts".

11. You can modify, add, or delete the posts as you want (in markdown format).

12. To check the posts, go back to the django page and click "markdown" button.

13. Click the post you wrote.
