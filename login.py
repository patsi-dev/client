import mysql.connector
import bcrypt
from flask import Flask, request, render_template, redirect, url_for

connection = mysql.connector.connect(
    host="localhost",
    user="Patsi_dev",
    password="patsi06",
    database="MortiCarDealership"
)
def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def login(username, password):
    cursor = connection.cursor()
    query = "SELECT * FROM Customers WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result and check_password(result[4], password):  # Assuming the password is in the 6th column
        if result[5] == 'admin':  # Assuming the role is in the 7th column
            return True
    return False

    
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login(username, password):
            return redirect(url_for('dashboard'))  # Redirect to the dashboard route
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Assuming you have a dashboard.html template


if __name__ == '__main__':
    app.run(debug=True)


