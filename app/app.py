from flask import Flask
from flask import request
import mysql.connector


app = Flask(__name__)


@app.route('/mini-web-app/main', methods=['GET'])'
def fetch_table():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employees")
    myresult = mycursor.fetchall()
    lines = []
    for record in myresult:
        lines.append(list(record))
    return lines

@app.route('/mini-web-app/add-emp', methods=['POST'])'
def add_employee(first_name, last_name, personal_id, department_name):
    mycursor = mydb.cursor()
    sql = "INSERT INTO employees (first_name, last_name, personal_id, department_id, department_name) VALUES (%s, %s, %s, %s, %s)"
    val = (first_name, last_name, personal_id, department_name)
    mycursor.execute(sql, val)
    mydb.commit()
    return(mycursor.rowcount, "record inserted.")

@app.route('/mini-web-app/main/del', methods=['POST'])'
def delete_employee(key_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM employees WHERE id = %(id)s"
    mycursor.execute(sql, {'id': key_id})
    mydb.commit()
    return(mycursor.rowcount, "record(s) deleted")

@app.route('/mini-web-app/edit-emp', methods=['POST'])'
def edit_employee(key_id, first_name, last_name, personal_id, department):
    mycursor = mydb.cursor()
    sql = "UPDATE employees SET first_name = %s, last_name = %s, personal_id = %s, department=%s WHERE id = %s"
    data = [(first_name, last_name, personal_id, department, key_id)]
    mycursor.executemany(sql, data)
    mydb.commit()
    return(mycursor.rowcount, "record(s) affected")


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
