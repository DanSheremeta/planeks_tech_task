# planeks_tech_task
Tech task for PLANEKS

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [Bootstrap](https://getbootstrap.com/): Framework for building responsive, mobile-first sites, with jsDelivr and a template starter page.
* [JQuery](https://jquery.com/): Fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ https://github.com/DanSheremeta/merp.git
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd planeks_tech_task
        ```
    2. Create and fire up your virtual environment:
        ```bash
            $ python -m venv env
            $ env/Scripts/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the main page of site on your browser by using
    ```
        http://localhost:8000/schemas/
    ```
    
## All end-points:

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/dashboard/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Login: http://127.0.0.1:8000/accounts/login/</li>
    <li>Logout: http://127.0.0.1:8000/accounts/logout/</li>
</ul>
<br>

<b>3. Datasets</b>
<ul>
    <li>Schemas list: http://127.0.0.1:8000/schemas/</li>
    <li>Schema create (Only authenticated user): http://127.0.0.1:8000/schemas/create/</li>
    <li>Schemas update (Only authenticated user): http://127.0.0.1:8000/schemas/update/&lt;int:schema_id&gt;/</li>
    <li>Schema delete (Only authenticated user): http://127.0.0.1:8000/schemas/delete/</li>
    <li>Delete specific column (Only authenticated user): http://127.0.0.1:8000/delete-column/&lt;int:column_id&gt;/</li>
    <li>Datasets list: http://127.0.0.1:8000/schema/&lt;int:schema_id&gt;/datasets/</li>
    <li>Csv file generator: http://127.0.0.1:8000/schema/&lt;int:schema_id&gt;/csv-generate/</li>
    <li>Download specific csv file: http://127.0.0.1:8000/schema/&lt;int:schema_id&gt;/csv-download/</li>
</ul>
<br>
