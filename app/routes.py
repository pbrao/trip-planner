from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Country, Transportation, Lodging, BucketList
import csv
from pathlib import Path
from datetime import date, time, time as time_type

def parse_date(date_str):
    return date.fromisoformat(date_str) if date_str else None

def parse_time(time_str):
    if time_str:
        return time_type.fromisoformat(time_str)
    return None

def parse_float(float_str):
    return float(float_str) if float_str else None

def load_countries():
    countries_path = Path(__file__).parent / 'data' / 'countries.csv'
    with open(countries_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row['name'] for row in reader]

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/transportation')
def transportation():
    sort_column = request.args.get('sort', 'departure_date')
    sort_direction = request.args.get('direction', 'asc')
    
    # Validate sort column
    valid_columns = ['carrier', 'method', 'departure_date', 'arrival_date', 'total_cost']
    if sort_column not in valid_columns:
        sort_column = 'departure_date'
    
    # Create the order_by clause
    column = getattr(Transportation, sort_column)
    if sort_direction == 'desc':
        column = column.desc()
    
    transport_entries = Transportation.query.order_by(column).all()
    
    return render_template('transportation.html', 
                         transport_entries=transport_entries,
                         sort_column=sort_column,
                         sort_direction=sort_direction)

from datetime import date, time, time as time_type

@main_routes.route('/transportation/<int:id>/edit', methods=['GET', 'POST'])
def edit_transportation(id):
    transport = Transportation.query.get_or_404(id)
    if request.method == 'POST':
        # Convert form data to appropriate types
        def parse_date(date_str):
            return date.fromisoformat(date_str) if date_str else None
            
        def parse_time(time_str):
            if time_str:
                return time_type.fromisoformat(time_str)
            return None
            
        def parse_float(float_str):
            return float(float_str) if float_str else None
            
        def parse_time(time_str):
            if time_str:
                return time_type.fromisoformat(time_str)
            return None
            
        def parse_time(time_str):
            if time_str:
                return time_type.fromisoformat(time_str)
            return None
            
        def parse_time(time_str):
            if time_str:
                return time_type.fromisoformat(time_str)
            return None

        # Update transportation entry with converted data
        transport.carrier = request.form.get('carrier')
        transport.method = request.form.get('method')
        transport.number = request.form.get('number')
        transport.departure_date = parse_date(request.form.get('departure_date'))
        transport.departure_location = request.form.get('departure_location')
        transport.departure_time = parse_time(request.form.get('departure_time'))
        transport.arrival_location = request.form.get('arrival_location')
        transport.arrival_date = parse_date(request.form.get('arrival_date'))
        transport.arrival_time = parse_time(request.form.get('arrival_time'))
        transport.reservation_number = request.form.get('reservation_number')
        transport.booked_date = parse_date(request.form.get('booked_date'))
        transport.booking_info = request.form.get('booking_info')
        transport.luggage_restrictions = request.form.get('luggage_restrictions')
        transport.purchase_price = parse_float(request.form.get('purchase_price'))
        transport.total_cost = parse_float(request.form.get('total_cost'))
        
        db.session.commit()
        flash('Transportation entry updated!', 'success')
        return redirect(url_for('main.transportation'))
    
    return render_template('edit_transportation.html', transport=transport)

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
    sort_column = request.args.get('sort', 'arrival_date')
    sort_direction = request.args.get('direction', 'asc')
    
    # Validate sort column
    valid_columns = ['accommodations', 'city', 'country', 'arrival_date', 'departure_date', 'nights', 'total_cost']
    if sort_column not in valid_columns:
        sort_column = 'arrival_date'
    
    # Create the order_by clause
    column = getattr(Lodging, sort_column)
    if sort_direction == 'desc':
        column = column.desc()
    
    lodgings = Lodging.query.order_by(column).all()
    
    return render_template('lodging.html', 
                         lodgings=lodgings,
                         sort_column=sort_column,
                         sort_direction=sort_direction)

@main_routes.route('/lodging/<int:id>/edit', methods=['GET', 'POST'])
def edit_lodging(id):
    lodging = Lodging.query.get_or_404(id)
    if request.method == 'POST':
        # Update lodging entry with converted data
        lodging.accommodations = request.form.get('accommodations')
        lodging.city = request.form.get('city')
        lodging.country = request.form.get('country')
        lodging.arrival_date = parse_date(request.form.get('arrival_date'))
        lodging.departure_date = parse_date(request.form.get('departure_date'))
        lodging.nights = int(request.form.get('nights'))
        lodging.cost_per_night = parse_float(request.form.get('cost_per_night'))
        lodging.insurance = parse_float(request.form.get('insurance'))
        lodging.vendor = request.form.get('vendor')
        lodging.total_cost = parse_float(request.form.get('total_cost'))
        lodging.date_booked = parse_date(request.form.get('date_booked'))
        lodging.contact = request.form.get('contact')
        lodging.phone_email = request.form.get('phone_email')
        lodging.address = request.form.get('address')
        lodging.confirmation_number = request.form.get('confirmation_number')
        lodging.cancellation_rules = request.form.get('cancellation_rules')
        lodging.check_in = parse_time(request.form.get('check_in'))
        lodging.check_out = parse_time(request.form.get('check_out'))
        lodging.property_link = request.form.get('property_link')
        lodging.notes = request.form.get('notes')
        
        db.session.commit()
        flash('Lodging entry updated!', 'success')
        return redirect(url_for('main.lodging'))
    
    return render_template('edit_lodging.html', lodging=lodging)

@main_routes.route('/lodging/add', methods=['GET', 'POST'])
def add_lodging():
    if request.method == 'POST':
        # Create new lodging entry with converted data
        new_lodging = Lodging(
            accommodations=request.form.get('accommodations'),
            city=request.form.get('city'),
            country=request.form.get('country'),
            arrival_date=parse_date(request.form.get('arrival_date')),
            departure_date=parse_date(request.form.get('departure_date')),
            nights=int(request.form.get('nights')),
            cost_per_night=parse_float(request.form.get('cost_per_night')),
            insurance=parse_float(request.form.get('insurance')),
            vendor=request.form.get('vendor'),
            total_cost=parse_float(request.form.get('total_cost')),
            date_booked=parse_date(request.form.get('date_booked')),
            contact=request.form.get('contact'),
            phone_email=request.form.get('phone_email'),
            address=request.form.get('address'),
            confirmation_number=request.form.get('confirmation_number'),
            cancellation_rules=request.form.get('cancellation_rules'),
            check_in=parse_time(request.form.get('check_in')),
            check_out=parse_time(request.form.get('check_out')),
            property_link=request.form.get('property_link'),
            notes=request.form.get('notes')
        )
        
        db.session.add(new_lodging)
        db.session.commit()
        flash('Lodging entry added!', 'success')
        return redirect(url_for('main.lodging'))
    
    return render_template('add_lodging.html')

@main_routes.route('/bucket-list')
def bucket_list():
    sort_column = request.args.get('sort', 'priority')
    sort_direction = request.args.get('direction', 'asc')
    
    # Validate sort column
    valid_columns = ['country', 'cities', 'region', 'priority', 'cost_level']
    if sort_column not in valid_columns:
        sort_column = 'priority'
    
    # Create the order_by clause
    column = getattr(BucketList, sort_column)
    if sort_direction == 'desc':
        column = column.desc()
    
    items = BucketList.query.order_by(column).all()
    
    return render_template('bucket_list.html', 
                         items=items,
                         sort_column=sort_column,
                         sort_direction=sort_direction)

@main_routes.route('/bucket-list/add', methods=['GET', 'POST'])
def add_bucket_list_item():
    if request.method == 'POST':
        new_item = BucketList(
            country=request.form.get('country'),
            cities=request.form.get('cities'),
            region=request.form.get('region'),
            priority=int(request.form.get('priority', 1)),
            potential_dates=request.form.get('potential_dates'),
            cost_level=request.form.get('cost_level'),
            january='january' in request.form,
            february='february' in request.form,
            march='march' in request.form,
            april='april' in request.form,
            may='may' in request.form,
            june='june' in request.form,
            july='july' in request.form,
            august='august' in request.form,
            september='september' in request.form,
            october='october' in request.form,
            november='november' in request.form,
            december='december' in request.form,
            notes=request.form.get('notes')
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Bucket list item added!', 'success')
        return redirect(url_for('main.bucket_list'))
    
    return render_template('add_bucket_list.html')

@main_routes.route('/bucket-list/<int:id>/edit', methods=['GET', 'POST'])
def edit_bucket_list_item(id):
    item = BucketList.query.get_or_404(id)
    if request.method == 'POST':
        # Update bucket list item with form data
        item.country = request.form.get('country')
        item.cities = request.form.get('cities')
        item.region = request.form.get('region')
        item.priority = int(request.form.get('priority', 1))
        item.potential_dates = request.form.get('potential_dates')
        item.cost_level = request.form.get('cost_level')
        item.january = 'january' in request.form
        item.february = 'february' in request.form
        item.march = 'march' in request.form
        item.april = 'april' in request.form
        item.may = 'may' in request.form
        item.june = 'june' in request.form
        item.july = 'july' in request.form
        item.august = 'august' in request.form
        item.september = 'september' in request.form
        item.october = 'october' in request.form
        item.november = 'november' in request.form
        item.december = 'december' in request.form
        item.notes = request.form.get('notes')
        
        db.session.commit()
        flash('Bucket list item updated!', 'success')
        return redirect(url_for('main.bucket_list'))
    
    return render_template('edit_bucket_list.html', item=item)

@main_routes.route('/bucket-list/<int:id>/delete', methods=['POST'])
def delete_bucket_list_item(id):
    item = BucketList.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Bucket list item deleted!', 'success')
    return redirect(url_for('main.bucket_list'))

@main_routes.route('/countries')
def countries():
    # Get all countries from CSV
    all_countries = load_countries()
    
    # Get existing country records from database
    existing_countries = {c.name: c for c in Country.query.all()}
    
    # Create list of Country objects for all countries
    countries = []
    for country_name in all_countries:
        if country_name in existing_countries:
            # Use existing record
            countries.append(existing_countries[country_name])
        else:
            # Create new Country object and save to database
            new_country = Country(name=country_name)
            db.session.add(new_country)
            countries.append(new_country)
    
    db.session.commit()
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
    
    # Calculate new totals
    husband_total = Country.query.filter_by(husband_visited=True).count()
    wife_total = Country.query.filter_by(wife_visited=True).count()
    
    return {
        'husband_total': husband_total,
        'wife_total': wife_total
    }

