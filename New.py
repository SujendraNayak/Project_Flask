from flask import Flask,jsonify
from flask import request
import mysql.connector

app=Flask(__name__)
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sujendra@27",  
    database="mydatabase"
)
#CURD operations GET,PUT,POST,DELETE

@app.route('/addStudent', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data.get('name')
    mark = data.get('mark')  
    cursor = db.cursor()
    query = "INSERT INTO students(name, mark) VALUES (%s, %s)"
    cursor.execute(query, (name, mark))
    db.commit()
    return jsonify({'message': 'Student Added Successfully'}), 201

#get method
@app.route('/fetchall',methods=['GET'])
def Fetch_all():
    cursor=db.cursor(dictionary=True)
    cursor.execute("select * from students")
    rows=cursor.fetchall()
    cursor.close()
    return jsonify(rows)

@app.route('/fecthbyID/<int:id>',methods=['GET'])
def FetchById(id):
    cursor=db.cursor(dictionary=True  )
    cursor.execute('select * from students where id=%s',(id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

@app.route('/upadte',methods=['PUT'])
def upadte_data():
    id=request.json.get('id')
    name=request.json.get('name')
    mark=request.json.get('mark')
    cursor=db.cursor()
    query="UPDATE students SET name=%s,mark=%s WHERE id=%s"
    cursor.execute(query,(name,mark,id))
    db.commit()
    cursor.close()
    return jsonify({'message':'Data Updated Successfully'}),200

@app.route('/delete/<int:id>',methods=["DELETE"])
def delete_data(id):
    cursor = db.cursor()
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    return jsonify({'message':'Data Deleted Successfully'}),200
    

if __name__=='__main__':
    print("connecting")
    app.run(debug=True)
    
    