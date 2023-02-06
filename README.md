# Django_markdown
Example of Django markdown page

# Post in markdown in your Django web application #

## Tutorial ##
1. Pull the repository<br>
    ```
    git clone https://github.com/LateButSteady/Django_markdown
    ```
2. Move to the directory

3. Activate virtualenv you are using<br>
    - Note that repository used python 3.9 (Later than 3.6 is recommended)

4. Install packages using requirements.txt<br>
    ```
    pip install -r requirements.txt
    ```

5. Open the web application locally.
    ```
    python manage.py runserver<br>
    ```
   You will see the log like below if web is successfully opened.
    ```
    System check identified no issues (0 silenced).
    February 07, 2023 - 03:10:08
    Django version 4.1.6, using settings 'django_md.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
      
6. Enter the address below in browser.
    ```
    localhost:8000
    ```
   You will see a button "Markdown page". Click it.
   
7. There are two posts. Each post will redirect and show the body.
   <br>
8. You can add posts in the Django admin page
    ```
    localhost:8000/admin
    ```
9. Login with the info<br>
    - ID: admin
    - Password: admin
    - Note that you can make your own superuser with the following command.
    
    ```
    python manage.py makesuperuser
    ```
   <br>
10. Click "Posts".

11. You can modify, add, or delete the posts as you want.
