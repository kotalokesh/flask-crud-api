from flask import Flask, jsonify, render_template,  request, redirect, url_for, flash
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'
app.config['MYSQL_DATABASE_DB'] = 'flaskcrud'
mysql.init_app(app)

@app.route("/")
def index():
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', employees = data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        #flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO employee (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        conn.commit()
        for i in request.form:
            print('in',i)
        print(name,email,phone)
        return redirect(url_for('index'))

@app.route('/delete/<int:id>',methods=['GET'])
def delete(id):
    print(id)
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM  employee WHERE id= %s", (id))
    conn.commit()
    return redirect('/')


@app.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        conn = mysql.connect()
        cur = conn.cursor()
        cur.execute( "UPDATE employee SET name=%s, email=%s, phone=%s WHERE id=%s" , (name, email, phone, id))
        conn.commit()
        return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)