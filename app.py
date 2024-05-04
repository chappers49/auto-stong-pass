#Install Flask(pip install flask)
#Import Flask which allows users to automate the imput of passwords 
#and receive feedback if strong enough
from flask import Flask, request, render_template_string
import re 

app = Flask(__name__)

def strong_password(password):
    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False 
    
    #Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password): 
        return False
    
    #Check if password has at least 8 characters 
    if len(password) < 8: 
        return False 
    
    #Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    #Check if the password contains at least one speacial character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    #If all the conditions are met, the password is strong
    return True

#Flask app will have a single route(/) that handles both GET and POST request
#GET it displays a simple form where users can input a password
#POST it checks the password strength and shows the result on the same page

@app.route('/', methods=['GET', 'POST'])

def index(): 
    message = ""
    if request.method == 'POST':
        password = request.form['password']
        if strong_password(password):
            message = "Strong Password."
        else: message = "Password does not meet requirements."

 #render_template_string is used to render HTML directly from a string, 
 #which keeps everythin in a single file for simplicity       
    return render_template_string('''<!doctype html>
                                  <html>
                                  <head><title>Password Strenght Checker</title></head>
                                  <body>
                                  <h1>Check Your Passwword Strength</h1>
                                  <form method="post">
                                  <input 
                                  type="password"
                                  name="password"
                                  placeholder="Enter your password">
                                  <button type="submit">Check</button>
                                  </form>
                                  <p>{{message}}</p>
                                  </body>
                                  </html>
                                  ''', message=message)

if __name__ == '__main__':
#app.run() is a Flask method that starts the Flask development server
#debug=True provides helpful debugging information in case of errors
#host='0.0.0.0' specify the IP address to which the serer should bind
    app.run(debug=True, host='127.0.0.1')
