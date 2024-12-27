from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import db, Country

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
app.config['SECRET_KEY'] = 'your-secret-key'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transportation', methods=['GET', 'POST'])
def transportation():
    if request.method == 'POST':
        # Handle form submission
        flash('Transportation details saved!', 'success')
        return redirect(url_for('transportation'))
    return render_template('transportation.html')

@app.route('/lodging')
def lodging():
    return render_template('lodging.html')

@app.route('/bucket-list')
def bucket_list():
    return render_template('bucket_list.html')

@app.route('/countries')
def countries():
    countries = Country.query.all()
    return render_template('countries.html', countries=countries)

@app.route('/country/add', methods=['POST'])
def add_country():
    name = request.form.get('name')
    if name:
        country = Country(name=name)
        db.session.add(country)
        db.session.commit()
        flash('Country added successfully!', 'success')
    return redirect(url_for('countries'))

@app.route('/country/<int:id>/update', methods=['POST'])
def update_country(id):
    country = Country.query.get_or_404(id)
    country.husband_visited = 'husband_visited' in request.form
    country.wife_visited = 'wife_visited' in request.form
    db.session.commit()
    flash('Country updated successfully!', 'success')
    return redirect(url_for('countries'))

@app.route('/country/<int:id>/delete', methods=['POST'])
def delete_country(id):
    country = Country.query.get_or_404(id)
    db.session.delete(country)
    db.session.commit()
    flash('Country deleted successfully!', 'success')
    return redirect(url_for('countries'))
