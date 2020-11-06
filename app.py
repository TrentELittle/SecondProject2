# import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template


#################################################
# Database Setup
#################################################

connection_string = "postgres:@localhost/project2_db"

engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

session = Session(engine)
#################################################
# Flask Routes
#################################################


@app.route("/")
def home():
    return render_template('index.html', name=name)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/racecar<br/>"
        f"/api/v1.0/piechart<br/>"
        f"/api/v1.0/bar<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>`<br/>"

    )


@app.route("/api/v1.0/piechart")
def piechart():

    piechart = session.query("SELECT * FROM piechart")

    session.close()

    return jsonify(piechart)
    return redirect("/")


@app.route("/api/v1.0/racecar`")
def racecar():

    racecar = session.query("Select * FROM racecar")
    

    session.close()

    return jsonify(racecar)

    return redirect("/")


return redirect("/")


@app.route("/api/v1.0/barchart")
def barchart():
    barchart = session.query("SELECT * FROM barchart")

    # "SELECT country, new_displacement, year, start_date, FROM merged_data").filter(new_displacement).limit(5).all()

    session.close()

    return jsonify(barchart)

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
