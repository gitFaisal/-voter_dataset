# -voter_dataset
Voter_dataset cleaned and loaded into postgres db

-Voter data set initially a excel file with 1000 rows, imported into jupyter notebook via pandas.read_csv<br>
-Added a Age column to data based on birthdays after removing all the '(null)' values in dob coulmn, removed unwanted column, changed column names to more readable names. Ran simple analysis<br>

-Using Postico created a new table 'voters' in Postgres db 'voter_db'<br>
-Using python library psycopg2, wrote script to load our data set of 9701 rows after cleaning out the '(null)' values<br>
into newly created 'voters' table. <br>
-After sucessfully populating the db, ran some simple SQL queries on data.
