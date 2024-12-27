from app import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    husband_visited = db.Column(db.Boolean, default=False)
    wife_visited = db.Column(db.Boolean, default=False)

class Transportation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    carrier = db.Column(db.String(100))
    method = db.Column(db.String(50))
    number = db.Column(db.String(50))
    departure_date = db.Column(db.Date)
    departure_location = db.Column(db.String(100))
    departure_time = db.Column(db.Time)
    arrival_location = db.Column(db.String(100))
    arrival_date = db.Column(db.Date)
    arrival_time = db.Column(db.Time)
    reservation_number = db.Column(db.String(50))
    booked_date = db.Column(db.Date)
    booking_info = db.Column(db.Text)
    luggage_restrictions = db.Column(db.Text)
    purchase_price = db.Column(db.Float)
    total_cost = db.Column(db.Float)

class Lodging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    accommodations = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    arrival_date = db.Column(db.Date)
    departure_date = db.Column(db.Date)
    nights = db.Column(db.Integer)
    cost_per_night = db.Column(db.Float)
    insurance = db.Column(db.Float)
    vendor = db.Column(db.String(100))
    total_cost = db.Column(db.Float)
    date_booked = db.Column(db.Date)
    contact = db.Column(db.String(100))
    phone_email = db.Column(db.String(100))
    address = db.Column(db.Text)
    confirmation_number = db.Column(db.String(50))
    cancellation_rules = db.Column(db.Text)
    check_in = db.Column(db.Time)
    check_out = db.Column(db.Time)
    property_link = db.Column(db.String(200))
    notes = db.Column(db.Text)

class BucketList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100))
    cities = db.Column(db.Text)
    region = db.Column(db.String(100))
    priority = db.Column(db.Integer)
    potential_dates = db.Column(db.Text)
    cost_level = db.Column(db.String(50))
    january = db.Column(db.Boolean, default=False)
    february = db.Column(db.Boolean, default=False)
    march = db.Column(db.Boolean, default=False)
    april = db.Column(db.Boolean, default=False)
    may = db.Column(db.Boolean, default=False)
    june = db.Column(db.Boolean, default=False)
    july = db.Column(db.Boolean, default=False)
    august = db.Column(db.Boolean, default=False)
    september = db.Column(db.Boolean, default=False)
    october = db.Column(db.Boolean, default=False)
    november = db.Column(db.Boolean, default=False)
    december = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text)
