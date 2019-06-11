import psycopg2

# Connect to db

con = psycopg2.connect(
				host = "localhost",
				database = "voter_db",
				user = "Angelica",
				password = "password",
				port = 5432)

# Cursor Object

cur = con.cursor()
cur.execute("""COPY Public.voters FROM '/Users/Angelica/Desktop/Projects/voter_dataset.csv' DELIMITER ',' CSV Header""")


con.commit()

# Close cursor
# Close connection

cur.close()
con.close()
# Sucessfully loaded total 9701 rows of data into postgres db table voters 
