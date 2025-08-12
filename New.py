from flask import Flask
from flask import request
import mysql.connector
app=Flask(__name__)
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sujendra@27",
    database="mydatabase"
)
@app.route('/addStudent',methods=['POST'])
def add_student():
    data=request.