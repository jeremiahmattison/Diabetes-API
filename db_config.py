import pyodbc

def get_db_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-91RK47F;"  
        "DATABASE=diabetesapi_db;"  
        "UID=diabetesapilogin;"  
        "PWD=diabetesapipassword;"  
    )
    return connection


