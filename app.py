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
    return render_template('index.html')


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

    conflicts = session.query("SELECT conflict FROM Hazard type")

    disasters = session.query("SELECT natural distease, FROM Hazard type")

    session.close()

    return jsonify(piechart)


@app.route("/api/v1.0/racecar`")
def racecar():
    racecar = session.query(
        "SELECT country, population, new_displacement, year, start_date, FROM merged_data").first()

    session.close()

    return jsonify(racecar)


@app.route("/api/v1.0/barchart")
def barchart():
    Displaced = session.query("SELECT country, new_displacement, year, start_date, FROM merged_data").filter(
        new_displacement).limit(5).all()

    session.close()

    # bardata = list(np.ravel(Displaced))

    return jsonify(Displaced)


@app.route("/api/v1.0/<start>")
def start():
    starting_point = session.query(merged_data.year, merged_data.population).filter(
         merged_data.year > "2014-01-01").all()
    session.close()

    return jsonify(start)

@app.route("/api/v1.0/<end>")
def end():
    ending_point = session.query(merged_data.year, merged_data.population).filter(
         Measure.date == "2019-12-30").all()

    session.close()

    # Convert list of tuples into normal list
    # end = list(np.ravel(ending_point))

    return jsonify(ending_point)



if __name__ == '__main__':
    app.run(debug=True)


