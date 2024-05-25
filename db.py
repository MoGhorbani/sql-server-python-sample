import pyodbc

SERVER = 'localhost'
DATABASE = 'python'
USERNAME = 'sa'
PASSWORD = '1qaz!QAZ'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};TrustServerCertificate=yes;SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString) 


def insert_person(fname,lname):
    conn.execute('Insert Into Person([FirstName],[LastName]) Values(?,?) ',fname,lname)
    conn.commit()

def get_person(id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person WHERE id=?", id)
    return cursor.fetchall()
