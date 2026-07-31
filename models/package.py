from database import db

class Package(db.Model):
    __tablename__ ="packages"

    id = db.Column (db.Integer,primary_key=True)
    supplier_id = db.Column(db.Integer,db.ForeignKey("suppliers.id"))
    claim_number = db.Column(db.Integer,nullable=False,unique=True)
    status = db.Column(db.String)
    description = db.Column(db.String)
    weight = db.Column(db.Float)