import psycopg2
import sql_queries

def create_database():
    """
    Establishes database connection and return's the connection and cursor references.
    :return: return's (cur, conn) a cursor and connection reference
    """
    # connect to default database
    try :
        conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password=Sonu#123")
    except psycopg2.Error as e:
        print(e)

    conn.set_session(autocommit=True)
    cur = conn.cursor()

    ## create StartupAnalysis database
    cur.execute("DROP DATABASE IF EXISTS startupanalysis")
    cur.execute("CREATE DATABASE startupanalysis")
    # close connection to default database
    conn.commit()
    conn.close()    

    
    # connect to StartupAnalysis database
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname= startupanalysis user=postgres password=Sonu#123")

    except psycopg2.Error as e:
        print(e)
    cur = conn.cursor()
    
    #Returning a cursor and connection reference
    return cur, conn


def drop_tables(cur, conn):
    """
    Run's all the drop table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in sql_queries.drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Run's all the create table queries defined in sql_queries.py
    :param cur: cursor to the database
    :param conn: database connection reference
    """
    for query in sql_queries.create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Driver main function.
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    print("Table dropped successfully!!")

    create_tables(cur, conn)
    print("Table created successfully!!")

    conn.close()


if __name__ == "__main__":
    main()