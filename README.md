## Distinctiveness and Complexity

The page is not similar to anything we have already created. It's not a social media application or an e-commerce site. It's not similar to other years' projects either. I believe my project satisfies the criteria of distinctiveness and complexity because this project is to help everyone collect data countries, display the data on this website. Anyone can use it for free.

In terms of complexity, I used Javascript and Django with more than one model. Moreover, all of the web applications are responsive to different screen sizes mainly mobile phones.

## Project

My project involves data collection and graph creation. Before generating the graphs, the following information needs to be provided such as country, last release date, next release date, period types, link, file source, and comments. Before uploading the file, it is necessary to adhere the specific file format requirements to prevent the error.

The project used Django as the backend framework. HTML, CSS, JavaScript and Bootstrap are used as a  frontend development. All generated information is stored in a default SQLite database. All project webpages are mobile-responsive.

#### Installation
  - Install project dependencies by running `pip install -r requirements.txt`. The dependencies for this project include Django and the pillow module, which enables Django to work with images.
  - Apply migrations by running the following commands `python manage.py makemigrations` and `python manage.py migrate`.
  - To create a superuser, use the command `python manage.py createsuperuser`.
  - Visit the website and begin adding the data directory.

#### Files and directories
  - `capstone` - The main application directory is an essential component.
    - `static` contains all static content.
        - `css` contains compiled CSS file and its map.
        - `img` contains image file.
    - `templates` contains all application templates.
        - `add.html` - templates for adding new directory.
        - `base.html` - base templates. All other tempalates extend it.
        - `edit.html` - templates for editing a directory.
        - `error.html` - templates are used to present error pages when errors occur.
        - `format.html` - templates are used to specify the required format of a source file before uploading it.
        - `home.html` - the main template displays a new directory feed.
        - `line.html` - the template displays a single topic and graph from each directory.
    - `admin.py` - included some admin classes and re-registered the User model.
    - `models.py` - The model used in the project is represented. The `Directory` model extends the standard User model.
    - `urls.py` - all application URLs.
    - `views.py` contains all application views.
  - `directory` - project directory.
  
The project's video: 
   https://www.youtube.com/watch?v=TBpTYkUT7QI
