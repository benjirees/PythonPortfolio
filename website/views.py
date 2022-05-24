from unicodedata import category
from flask import Blueprint, jsonify, redirect, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Password
from . import db
import json
import random

import website

# A blueprint of application (Has roots (Home page etc))
views = Blueprint('views', __name__)

@views.route('/') # represents main page of website
#@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
#@login_required
def notes():

    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)

@views.route('/password', methods=['GET', 'POST'])
def generatePassword():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','#','!','£',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','#','!','£']
    specialChar = ['@','#','!','£']
    password = []
    length = 16

    if request.method == 'POST':
        for i in range(length):
            if i % 3 == 0:
                password.append(random.choice(specialChar))
            else:
                letter = random.choice(alphabet)
                password.append(letter)
                #db.session.add(password)
                #db.session.commit()
        genPassword = ''.join(password)
        new_password = Password(generatedPassword=genPassword, user_id=current_user.id)
        db.session.add(new_password)
        #db.session.commit()
        flash('Password saved!')

    return render_template("password.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/home')
def git():
    return redirect("https://github.com/benjirees")

@views.route('/home')
def linkedIn():
    return redirect("http://linkedin.com/in/ben-rees-59a947234")
