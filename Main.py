from flask import Flask, render_template, flash, redirect, request, url_for, session, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import mysqlcontroller
import Qrcode
import value_find


mysql = mysqlcontroller.mysqlController(username = "root", password = "", database = "myflaskapp")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start_page')
def start_page():
    return render_template('start_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['n']
        email = request.form['e']
        username = request.form['un']
        password = request.form['p']
        confirm_password = request.form['cp']
        # imp = request.form._value()
        if password == confirm_password:
            mysql.executor(query = "INSERT INTO users(name, email, username, password) VALUES (%s, %s, %s, %s)",
                            args= (name, email, username, password))

            flash('YOU ARE NOW REGISTERED AND CAN LOG IN', 'success')

            return redirect(url_for('index'))

    return render_template('register.html')
def verify(data):
    listed = list(data.values())
    for i in listed:
        return i


@app.route('/loginthird', methods=['GET', 'POST'])
def loginthird():
    if request.method == 'POST':
        # Get Form Fields
        us = request.form['username']
        password_candidate = request.form['password']
        result = mysql.executor(query= "SELECT * FROM users WHERE username = %s", args = [us])

        if result > 0:
             formpassworddict = mysql.fetchOne(query= "SELECT password from users WHERE username = %s", args = [us])
             password = verify(formpassworddict)
             if password == password_candidate:
                 session['logged_in'] = True
                 session['username']  = us
                 return redirect(url_for('thirddashboard'))
             else:
                 flash('Password Invalid')
                 return render_template('loginthird.html')
        else:
            error = 'Username not found'
        return render_template('loginthird.html', error=error)
    return render_template('loginthird.html')

@app.route('/loginlab', methods=['GET', 'POST'])
def loginlab():
    if request.method == 'POST':
        # Get Form Fields
        us = request.form['username']
        password_candidate = request.form['password']
        result = mysql.executor(query= "SELECT * FROM users WHERE username = %s", args = [us])

        if result >0:
             formpassworddict = mysql.fetchOne(query= "SELECT password from users WHERE username = %s", args = [us])
             password = verify(formpassworddict)
             if password == password_candidate:
                 session['logged_in'] = True
                 session['username']  = us
                 return redirect(url_for('labdashboard'))
             else:
                 flash('Password Invalid')
                 return render_template('loginlab.html')
        else:
            error = 'Username not found'
        return render_template('loginlab.html', error=error)
    return render_template('loginlab.html')

@app.route('/loginmine', methods=['GET', 'POST'])
def loginmine():
    if request.method == 'POST':
        # Get Form Fields
        us = request.form['username']
        password_candidate = request.form['password']
        result = mysql.executor(query= "SELECT * FROM users WHERE username = %s", args = [us])

        if result > 0:
             formpassworddict = mysql.fetchOne(query= "SELECT password from users WHERE username = %s", args = [us])
             password = verify(formpassworddict)
             if password == password_candidate:
                 session['logged_in'] = True
                 session['username']  = us
                 return redirect(url_for('minedashboard'))
             else:
                 flash('Password Invalid')
                 return render_template('loginmine.html')
        else:
            error = 'Username not found'
        return render_template('loginmine.html', error=error)
    return render_template('loginmine.html')

@app.route('/loginministry', methods=['GET', 'POST'])
def loginministry():
    if request.method == 'POST':
        # Get Form Fields
        us = request.form['username']
        password_candidate = request.form['password']
        result = mysql.executor(query= "SELECT * FROM users WHERE username = %s", args = [us])

        if result >0:
             formpassworddict = mysql.fetchOne(query= "SELECT password from users WHERE username = %s", args = [us])
             password = verify(formpassworddict)
             if password == password_candidate:
                 session['logged_in'] = True
                 session['username']  = us
                 return redirect(url_for('ministry'))
             else:
                 flash('Password Invalid')
                 return render_template('loginministry.html')
        else:
            error = 'Username not found'
        return render_template('loginministry.html', error=error)
    return render_template('loginministry.html')


@app.route('/minedashboard', methods=['GET', 'POST'])
def minedashboard():
    if request.method == 'POST':
        code  = request.form["code"]
        buyer = request.form["buyer"]
        reck = request.form["reck"]
        grade = request.form["grade"]
        ucode = request.form["ucode"]
        quantity = request.form["quantity"]
        mysql.executor(query="INSERT INTO mine(code, buyer, reck, grade, ucode, quantity) VALUES (%s, %s, %s, %s, %s, %s)", args=(code, buyer, reck, grade, ucode, quantity))


    return render_template("minedashboard.html")

@app.route('/ministry', methods=['GET', 'POST'])
def ministry():
    if request.method == 'POST':
        aa = request.form["sample"]
        bb = request.form['ff']
        mysql.executor(query="INSERT INTO result( sample_serial, pdf) VALUES (%s, %s)", args=(aa, bb))
        gg = mysql.fetchOne(query="SELECT * from barcode_info WHERE barcode_second  = %s", args=[aa])
        print(gg)
    return render_template('ministry.html')

@app.route('/labdashboard', methods=['GET','POST'])
def labdashboard():
    if request.method == 'POST':
        sample_id = request.form['sample_id']
        lab_name = request.form['lab_name']
        email = request.form['email']
        test = request.form['test']
        testresult = request.form['testresult']
        print(sample_id, lab_name, email, testresult, test)

        mysql.executor(query="INSERT INTO lab(lab_name, email, sample_id, testname, testresult) VALUES (%s, %s, %s, %s, %s)", args=(lab_name, email, sample_id, test, testresult))

    return render_template('labdashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('YOu have logged out', 'success')
    return redirect(url_for('loginministry'))

@app.route('/lab_names', methods=['GET', 'POST'])
def lab_names():
    if request.method == 'POST':
          ln = request.form['ln']
          lp = request.form['lp']
          mysql.executor(
                query="INSERT INTO lab_list(l_name, l_place ) VALUES (%s, %s)",
                args=(ln, lp))
    return render_template('lab_names.html')

global res
@app.route('/thirddashboard', methods=['GET','POST'])
def thirddashboard():
  # if request.method == 'POST':
      # num = request.form['snumber']

      mydict = mysql.fetchOne("SELECT * FROM lab ")
      res = list(mydict.values())
      print(res)

      return render_template('thirddashboard.html', result=res)


# @app.route('/hh', methods=['GET', 'POST'])
# def hh():
#     if request.method == 'POST':
#         mydict = mysql.fetchOne("SELECT * FROM lab ")
#         res = list(mydict.values())
#
#         lab_val = mysql.fetchAll(query = "SELECT * from master where lab_id = %s", args = (res))
#         print(lab_val)
#         print(mysql)
#         mine_value = mysql.fetchOne(query = "SELECT * from master where lab_id = %s", args = (res[2]))
#         print(mine_value)
#         g = list(mine_value.values())
#         print(g)
#         return render_template('hh.html', data=g)
#


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
