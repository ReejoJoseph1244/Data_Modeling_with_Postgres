import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import dataclean

def process_data(cur,conn,filepath,cleanfun,tableinsertQuery):
    """Driver function to load data from  files into Postgres database.
    :param cur: a database cursor reference
    :param conn: database connection reference
    :param filepath: parent directory where the files exists
    :param cleanfun: function to call for data cleaning
    :param tableinsertQuery: Respective Table insert query
    """
    data=pd.DataFrame(cleanfun())
    print(data)
    
    for i,row in data.iterrows():
        cur.execute(tableinsertQuery,row)
        conn.commit()
    
    print(filepath + " Data inserted Sucessfully!")


def main():
    """
    Driver function for loading files : countries_of_the_world, indsutry, position_of_countries and country_tax  into Postgres database
    """
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname= startupanalysis user=postgres password=Sonu#123")

    except psycopg2.Error as e:
        print(e)
    cur = conn.cursor()

    # process_data(cur,conn,filepath='Data/countries_of_the_world',cleanfun=dataclean.country_clean,tableinsertQuery=countries_table_insert)
    # process_data(cur,conn,filepath='Data/country_tax.csv',cleanfun=dataclean.country_tax_clean,tableinsertQuery=taxdata_table_insert)
   # process_data(cur,conn,filepath='Data/industry.csv',cleanfun=dataclean.industry_clean,tableinsertQuery=industrydata_table_insert)
    process_data(cur,conn,filepath='Data/position_of_countries.csv',cleanfun=dataclean.position_clean,tableinsertQuery=positiondata_table_insert)



    conn.close()


if __name__ == "__main__":
    main()
    print("\n\nFinished processing!!!\n\n")