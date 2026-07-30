from database import db


class Shipment(db.Model):
    __tablename__ = "shipments"

    id = db.Column(db.Integer, primary_key=True)

    vehicle_id = db.Column(
        db.Integer,
        db.ForeignKey("vehicles.id"),
        nullable=False
    )

    origin_office_id = db.Column(db.Integer)
    destination_office_id = db.Column(db.Integer)

    departure_date = db.Column(db.DateTime, nullable=False)
    shipment_status = db.Column(db.String(50), nullable=False)

    expected_arrival = db.Column(db.DateTime)
    actual_arrival = db.Column(db.DateTime)

    distance_in_km = db.Column(db.Float)

    vehicle = db.relationship(
        "Vehicle",
        back_populates="shipments"
    )

    def __repr__(self):
        return f"<Shipment {self.id}>"