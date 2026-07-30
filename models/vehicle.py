from database import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"

    id = db.Column(db.Integer, primary_key=True)
    plate_number = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    current_city_id = db.Column(db.Integer)

    shipments = db.relationship(
        "Shipment",
        back_populates="vehicle",
        lazy=True
    )

    def __repr__(self):
        return f"<Vehicle {self.plate_number}>"