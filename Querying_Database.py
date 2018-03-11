# Import create_engine, MetaData
from sqlalchemy import create_engine,MetaData
from sqlalchemy import Table, Column, String, Integer, Float
# Import and_,_or_,select for query
from sqlalchemy import and_,or_,select
import pandas as pd
#Engine: Common interface to the database from SQLAlchemy which provides a way to interact or talk to it.

# Define an engine to connect to SpaceDB.sqlite: engine
engine = create_engine('sqlite:///Space@DB.sqlite')

#Metadata object is a catalog that stores database info such as tables so that we dont have to keep looking them up

# Initialize MetaData: metadata
metadata =MetaData()

DST=Table('DSTIndex_Table',metadata,autoload=True,autoload_with=engine)

print("\nYou can now Query the Database which has DST Index Data from year 1975 till year 2018\n")
print("\nEnter the starting year:")
startyear=input()
print("\nEnter the Ending year:")
endyear=input()
print("\nEnter the starting Month:")
startmonth=input()
print("\nEnter the ending Month:")
endmonth=input()


# Build a query for the census table: stmt
stmt = select([DST])

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    or_(and_(DST.columns.Year==startyear,DST.columns.Month>=startmonth),
        and_(DST.columns.Year>startyear,DST.columns.Year<endyear),
       and_(DST.columns.Year==endyear,DST.columns.Month<=endmonth))
    )

# Execute the statement and get the results: results
results = engine.execute(stmt).fetchall()


query_output=pd.DataFrame(data=results,index=None,columns=results[0].keys())

query_output.to_csv('query_output.csv')
print("\nThe Queried Result can be found in file named 'query_output.csv' \n")



