#!/usr/bin/env python
# encoding: utf-8
'''
Stuff here:
'''
import json
from flask import Flask, request, render_template, abort, redirect, url_for
#
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def people():
    '''
    get people information from file and create a python list of lists
    '''
    # Create an empty list
    data = []
    # open file for reading
    f = open('people.txt', "r")

    # read contents of file
    people = f.readlines()

    for p in people:
        # remove carrige return and line feed
        person = p.rstrip('\r\n')
        # Turn python sting into a list
        person = list(person.split(","))
        # Append the person to the data list
        data.append(person)

    message = "Generated with python lists"
    # Pass message and data to the jinj2 template
    return render_template('home.html', message=message, data=data)


@app.route('/p2', methods=['POST','GET'])
def people2():
    '''
    get people information from file and create a python list of lists
    '''
    # Create an empty list
    data = []
    # open file for reading
    f = open('people2.txt', "r")

    # read contents of file
    people = f.readlines()

    for p in people:
        # remove carrige return and line feed
        person = p.rstrip('\r\n')
        # Turn python sting into a dictionary
        person = json.loads(person)
        # Append the person to the data list
        data.append(person)

    message = "Generated with python dictionaries"
    # Pass message and data to the jinj2 template
    return render_template('home1.html', message=message, data=data)


app.run(debug=True)
