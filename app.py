# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import random
import json
from flask import Flask, request, url_for, redirect, render_template, jsonify

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)


with open('jokes.json', 'r', encoding='utf-8') as file:             #'utf-8' is a common encoding that supports a wide range of characters
    jokes = json.load(file)



# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
# The joke displays here when the user submitted it
@app.route('/success/<Joke>')
def success(Joke):
    return '%s' % Joke

# For posting and getting a URL
@app.route('/jokes', methods=['POST' , 'GET'])
def enter():
    if request.method=='POST':
        jks = request.form['jk']
        return redirect(url_for('success', Joke=jks))
    else:
        jks = request.args.get('jk')
        return redirect(url_for('success', Joke = jks))
        

# For getting a random joke
@app.route('/random_joke', methods=['GET'])     
def get_random_joke():
    jks = random.choice(jokes)                                          #Uses the random.choice() function to select a random joke from the list
    return redirect(url_for('success', Joke = list(jks.values())[1]))                     

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()