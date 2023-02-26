from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contact = Blueprint('contact', __name__)

# TODO: select all contacts and the submit to index.html
@contact.route('/')
def home():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


# TODO: add fullname,email,phone to contact response new obect and save in database
@contact.route('/new', methods=['POST'])
def add():
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']

    new_contact = Contact(fullname, email, phone)

    db.session.add(new_contact)
    db.session.commit()

    flash('Contact created succcessfully', 'info')
    return redirect(url_for('contact.home'))


# TODO: list of contacts as parameters, validation method
@contact.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)

    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contact updated succcessfully', 'info')

        return redirect(url_for("contact.home"))

    else:
        return render_template('update.html', contact=contact)

# TODO: recibe el id del contacto como parametro
@contact.route('/delete/<id>')
def delete(id: int):
    contac = Contact.query.get(id)
    db.session.delete(contac)
    db.session.commit()

    flash('Contact delete succcessfully', 'info')
    return redirect(url_for('contact.home'))

@contact.route('/about')
def about():
    return render_template('about.html')
