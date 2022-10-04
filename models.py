"""Models for Cupcake app."""


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFALUT_IMG_URL = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Todo Model"""

    __tablename__ = "cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, default= DEFALUT_IMG_URL)

    def serialize(self):
        """Returns a dict representation of cake which we can turn into JSON"""
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating

        }

    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} rating={self.rating}>"




