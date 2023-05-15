'''
This File contains all the SQl queries to RUN
'''

#DROP Tables
factdata_table_drop = "DROP TABLE  IF EXISTS factdata"
countries_table_drop = "DROP TABLE IF EXISTS  dimcountries"
positiondata_table_drop = "DROP TABLE IF EXISTS  dimpositiondata"
industrydata_table_drop = "DROP TABLE  IF EXISTS dimindustrydata"
taxdata_table_drop = "DROP TABLE  IF EXISTS dimtaxdata"


# CREATE Tables

factdata_table_create = ("""CREATE TABLE IF NOT EXISTS factdata(
	data_id SERIAL  PRIMARY KEY,
    country VARCHAR REFERENCES dimcountries(country),
    position INT REFERENCES dimpositiondata(position),
	industry_key INT REFERENCES dimindustrydata(industry_key),
    tax_id INT REFERENCES dimtaxdata(tax_id)
)""")


countries_table_create = ("""CREATE TABLE IF NOT EXISTS  dimcountries(
	country VARCHAR PRIMARY KEY,
	region  VARCHAR,
	area  VARCHAR,
	netmargin  VARCHAR,
	gdp VARCHAR,
    industries VARCHAR

)""")

positiondata_table_create = ("""CREATE TABLE IF NOT EXISTS  dimpositiondata(
	position INT PRIMARY KEY,
	country  VARCHAR NOT NULL,
	total_score  INT NOT NULL,
	quantity_score  INT,
	quality_score INT ,
    business_score INT NOT NULL

)""")

industrydata_table_create = ("""CREATE TABLE IF NOT EXISTS  dimindustrydata(
    
    industry_key SERIAL PRIMARY KEY,
    company  VARCHAR ,
    valuation  INT,
    industry VARCHAR ,
	country  VARCHAR 
	
	
	

)""")

#taxrate  NUMERIC(4,2) NOT NULL,
taxdata_table_create = ("""CREATE TABLE IF NOT EXISTS  dimtaxdata(
    tax_id SERIAL PRIMARY KEY,
    country VARCHAR ,
	taxrate  VARCHAR NOT NULL

)""")

#INSERT RECORDS
countries_table_insert = ("""INSERT INTO dimcountries VALUES (%s, %s, %s, %s, %s, %s )
""")
positiondata_table_insert = ("""INSERT INTO dimpositiondata VALUES (%s, %s, %s, %s, %s, %s, %s )
""")
industrydata_table_insert = ("""INSERT INTO dimindustrydata(company,valuation,industry,country) VALUES (%s, %s, %s, %s)
""")
taxdata_table_insert = ("""INSERT INTO dimtaxdata(country,taxrate) VALUES ( %s, %s )
""")
factdata_table_insert = ("""INSERT INTO factdata VALUES (%s, %s, %s, %s, %s, %s)
""")




drop_table_queries = [factdata_table_drop,countries_table_drop,positiondata_table_drop,industrydata_table_drop,taxdata_table_drop]
create_table_queries=[countries_table_create, positiondata_table_create, industrydata_table_create, taxdata_table_create, factdata_table_create]