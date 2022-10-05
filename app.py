"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cup_cakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def index_page():
    
    cake = Cupcake.query.all()

    return render_template('base.html', cakes=cake)
    # return render_template('base.html')


# @app.route('/', methods=["GET", "POST"])
# def index_page():
#     """Renders html template that includes some JS - NOT PART OF JSON API!"""
#     cakes = Cupcake.query.all()
#     flavor = request.form['flavor']
#     size = request.form['size']
#     rating = request.form['rating']
#     image = request.form['image']
#     cake = Cupcake(flvor=flavor, size=size, rating=rating, image=image)
#     db.session.add(cake)
#     db.session.commit()
#     return render_template('index.html', cakes = cakes)


# *****************************
# RESTFUL CUPCAKES JSON API
# *****************************
@app.route('/api/cupcakes')
def list_cakes():
    """Returns JSON w/ all cakess"""
    all_cup_cakes = [cake.serialize() for cake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cup_cakes)


@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cake(cupcake_id):
    """Returns JSON for one cake in particular"""
    cake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def create_cake():
    """Creates a new cake and returns JSON of that created cake"""
    data = request.json
    new_cake = Cupcake(flavor=data["flavor"], 
                       size=data["size"],
                       rating=data["rating"],
                       image=data["image"] or None)

    db.session.add(new_cake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cake(cupcake_id):
    """Updates a particular cake and responds w/ JSON of that updated cake"""
    cake = Cupcake.query.get_or_404(cupcake_id)
    cake.flavor = request.json.get('flavor', cake.flavor)
    cake.size = request.json.get('size',  cake.size)
    cake.rating = request.json.get('rating',  cake.rating)
    cake.image = request.json.get('image',  cake.image)
    db.session.commit()
    return jsonify(cupcake=cake.serialize())



@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes a particular cake"""
    cake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cake)
    db.session.commit()
    return jsonify(message="Deleted")








