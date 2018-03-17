# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash
from contact_model import Contact
app = Flask(__name__)
app.secret_key="some_secret"
app.debug = True


@app.route(r'/', methods=['GET'])
def contact_book():
    contacts = Contact.query().fetch()
    return render_template('contact_book.html', contacts=contacts)


@app.route(r'/add', methods=['GET', 'POST'])
def add_contact():

    if request.form:
        contact = Contact(name=request.form.get('name'),
                          phone=request.form.get('phone'),
                          email=request.form.get('email'))

        contact.put()
        flash("Se añadió contacto: {}".format(request.form.get('name')))

    return render_template('add_contact.html')

@app.route(r'/contact/<uid>', methods=["GET"])
def contact_details(uid):
  contact = Contact.get_by_id(int(uid))

  return  render_template("contact.html", contact=contact)

if __name__ == '__main__':
    app.run()