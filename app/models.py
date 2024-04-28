from app import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username})>"

class Hotels(db.Model):
    __tablename__ = 'hotels'

    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(100))
    hotel_location = db.Column(db.String(100))
    manager_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    manager = db.relationship('User', backref=db.backref('managed_hotels', lazy=True))
    dest_id = db.Column(db.Integer, db.ForeignKey('tour_destinations.destination_id'), nullable=False)
    destination = db.relationship('TourDestination', backref=db.backref('hotels', lazy=True))

    def __repr__(self):
        return f"<Hotel(hotel_id={self.hotel_id}, hotel_name={self.hotel_name})>"

class Transports(db.Model):
    __tablename__ = 'transports'

    transport_id = db.Column(db.Integer, primary_key=True)
    transport_type = db.Column(db.String(100))
    availability = db.Column(db.Boolean, default=True)
    cost = db.Column(db.Integer, nullable = False)
    dest_id = db.Column(db.Integer, db.ForeignKey('tour_destinations.destination_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    agent = db.relationship('User', backref=db.backref('transport_agents', lazy=True))

    def __repr__(self):
        return f"<TransportAgent(transport_id={self.transport_id}, transport_type={self.transport_type})>"


class TourDestination(db.Model):
    __tablename__ = 'tour_destinations'

    destination_id = db.Column(db.Integer, primary_key=True)
    destination_name = db.Column(db.String(100))
    destination_description = db.Column(db.Text)
    def __repr__(self):
        return f"<TourDestination(destination_id={self.destination_id}, destination_name={self.destination_name})>"

class Rooms(db.Model):
    __tablename__ = 'rooms'
    room_id = db.Column(db.Integer, primary_key=True)
    room_no = db.Column(db.String(20))
    room_type = db.Column(db.String(50))
    cost = db.Column(db.Float)
    availability = db.Column(db.Boolean, default=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.hotel_id'), nullable=False)
    hotel = db.relationship('Hotels', backref=db.backref('rooms', lazy=True))

    def __repr__(self):
        return f"<Room(room_id={self.room_id}, room_no={self.room_no})>"

class Reviews(db.Model):
    __tablename__ = 'reviews'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    dest_id = db.Column(db.Integer, db.ForeignKey('tour_destinations.destination_id'), primary_key=True)
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)

    def __repr__(self):
        return f"<Review(user_id={self.user_id}, dest_id={self.dest_id})>"


class Reservation(db.Model):
    __tablename__ = 'reservations'

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    reservation_id = db.Column(db.Integer, primary_key=True)
    reservation_date = db.Column(db.DateTime)
    transport_id = db.Column(db.Integer, db.ForeignKey('transports.transport_id'))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.room_id'))
    arrival_date = db.Column(db.DateTime)
    departure_date = db.Column(db.DateTime)
    dinner_reservation = db.Column(db.Boolean)
    room = db.relationship('Rooms', backref='reservation')

    def __repr__(self):
        return f"<Reservation(user_id={self.user_id}, reservation_id={self.reservation_id})>"
