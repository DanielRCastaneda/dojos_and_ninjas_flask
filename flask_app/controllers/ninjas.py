from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninja')
def ninja():
    return render_template('ninja.html', all_dojos = Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    print(request.form)
    return redirect('/')
@app.route('/return', methods=['POST'])
def return_to_home():
    return redirect('/')