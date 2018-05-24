# How to Run and Initialize GameWorld:

Python version 2.7.x. is necessary to start.

Install the virtual environment if it is the first time running the database.

1. To install the virtual environment using Terminal please enter:            
$ virtualenv venv

2. Then you must activate the virtual environment by entering:        
$ source venv/bin/activate

3. Next, to install the necessary packages enter:                                    
$ pip install -r requirements.txt

4. To initialize the base information and code for the database enter:
$ python manage.py deploy

5. To run the server:
$ python manage.py runserver -d

6. Access the website with the given IP address from terminal using a web browser.
