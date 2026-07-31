from database import db
class Supplier(db.Model):
    __tablename__ = "suppliers"
    id = db.Column (db.Integer,primary_key=True)
    name = db.Column(db.String)
    city_id = db.Column(db.Integer,db.ForeignKey("cities.id"))