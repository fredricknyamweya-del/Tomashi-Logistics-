from models import db


class PackageStatusHistory(db.Model):
    __tablename__ = 'package_status_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    package_id = db.Column(db.Integer, db.ForeignKey('packages.id'), nullable=False)
    status = db.Column(db.String(255), nullable=False)
    remarks = db.Column(db.String(255))
    update_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<PackageStatusHistory id={self.id} status={self.status}>'