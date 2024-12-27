from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Country, Transportation

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/transportation')
def transportation():
    transport_entries = Transportation.query.order_by(Transportation.departure_date).all()
    return render_template('transportation.html', transport_entries=transport_entries)

from datetime import date, time

@main_routes.route('/transportation/add', methods=['GET', 'POST'])
def add_transportation():
    if request.method == 'POST':
        # Convert form data to appropriate types
        def parse_date(date_str):
            return date.fromisoformat(date_str) if date_str else None
            
        def parse_time(time_str):
            return time.fromisoformat(time_str) if time_str else None
            
        def parse_float(float_str):
            return float(float_str) if float_str else None

        # Create new transportation entry with converted data
        new_transport = Transportation(
            carrier=request.form.get('carrier'),
            method=request.form.get('method'),
            number=request.form.get('number'),
            departure_date=parse_date(request.form.get('departure_date')),
            departure_location=request.form.get('departure_location'),
            departure_time=parse_time(request.form.get('departure_time')),
            arrival_location=request.form.get('arrival_location'),
            arrival_date=parse_date(request.form.get('arrival_date')),
            arrival_time=parse_time(request.form.get('arrival_time')),
            reservation_number=request.form.get('reservation_number'),
            booked_date=parse_date(request.form.get('booked_date')),
            booking_info=request.form.get('booking_info'),
            luggage_restrictions=request.form.get('luggage_restrictions'),
            purchase_price=parse_float(request.form.get('purchase_price')),
            total_cost=parse_float(request.form.get('total_cost'))
        )
        
        db.session.add(new_transport)
        db.session.commit()
        flash('Transportation entry added!', 'success')
        return redirect(url_for('main.transportation'))
    
    return render_template('add_transportation.html')

@main_routes.route('/lodging')
def lodging():
    return render_template('lodging.html')

@main_routes.route('/bucket-list')
def bucket_list():
    return render_template('bucket_list.html')

@main_routes.route('/countries')
def countries():
    countries = Country.query.all()
    return render_template('countries.html', countries=countries)

@main_routes.route('/country/add', methods=['POST'])
def add_country():
    name = request.form.get('name')
    if name:
        country = Country(name=name)
        db.session.add(country)
        db.session.commit()
        flash('Country added successfully!', 'success')
    return redirect(url_for('main.countries'))

@main_routes.route('/country/<int:id>/update', methods=['POST'])
def update_country(id):
    country = Country.query.get_or_404(id)
    country.husband_visited = 'husband_visited' in request.form
    country.wife_visited = 'wife_visited' in request.form
    db.session.commit()
    flash('Country updated successfully!', 'success')
    return redirect(url_for('main.countries'))

@main_routes.route('/country/<int:id>/delete', methods=['POST'])
def delete_country(id):
    country = Country.query.get_or_404(id)
    db.session.delete(country)
    db.session.commit()
    flash('Country deleted successfully!', 'success')
    return redirect(url_for('main.countries'))
