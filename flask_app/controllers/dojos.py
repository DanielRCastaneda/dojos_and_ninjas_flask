from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('index.html', all_dojos = dojos)


@app.route('/create/dojo', methods =['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show(id):
    data = {
        'id':id
    }
    dojos = Dojo.dojo_to_ninja(data)
    print(dojos)
    return render_template('dojo.html', all_dojos = dojos)
