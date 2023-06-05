# TRADES
## API FOR TRADE DATA

The Application is a REST API enbaled in Python using the FastAPI framework which helps to store, retrive the trade details.

- Language: Python
- Modules Used: FASTAPI, SQalchemy
- Database: PostgresSQL

## Features

- Can create trade transaction detaisl into Database.
- Query the data on the basis of maxPrice,minPrice,startdata,enddate,asset_class,Traderid, Trader Name.
- Pagination has been included
- ###### sorting not included

##### Why PostgresSql?

#
> Postgres is the most advanced open-source relational database in the world
> More write capable of writing large amounts of data more efficiently, and it handled concurrency better and it support JSON aswell which is usefull in our case.

##### Why SQLalchemy?
#
> It provides a generalized interface for creating and executing database-agnostic code without needing to write SQL statements and ORM is a bonus to Core that automates commonly-required create, read, update and delete operations.
The Database mapping allows SQLAlchemy to handle the underlying database so developers can work with their Python objects instead of writing bridge code to get data in and out of relational tables


## Installation Steps:

##### Pre-req:
-   Python should be there 3.7 and above
-   postgresql should be there latest 12

Install virtualenv using python

    pip install virtualenv

Create virtualenv

    virtualenv mypython
    
Activate virtualenv

    mypython\Scripts\activate

Clone the git code

    git clone <url>

Install the modules from requriements.txt

    pip install -r requirements.txt

Run the app

    uvicorn main:app --reload

> once the app is up and running go to http://127.0.0.1:8000/docs to access the application where you can get the swagger UI to test the API's
> Visit http://127.0.0.1:8000/redoc for documentation 


