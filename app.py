import os
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, url_for, send_from_directory


#################################################
# Database Setup
#################################################

connection_string = "postgres:TL!ttl310@localhost/project2_db"

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

@app.route("/api/v1.0/2008/2019`")
def datatable():
    return render_template('data.html')

@app.route("/")
def team():
    return render_template('Team.html')

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/racecar<br/>"
        f"/api/v1.0/piechart<br/>"
        f"/api/v1.0/scatter<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>`<br/>"

    )


@app.route("/api/v1.0/piechart")
def piechart():
    piedata = session.execute('SELECT Hazard_type, new_displacement, year, start_date FROM merged_data ').fetchall()
    session.close()
    piechart = list(np.ravel(piedata))

    return render_template('Piechart.html')
    # return redirect("/")

@app.route("/api/v1.0/racecar")
def racecar():
    racedata=session.execute("SELECT country, new_displacement, year, start_date FROM merged_data").fetchall()
    session.close()
    racecar = list(np.ravel(racedata))
    # return jsonify(racecar)

    return render_template("racecar.html")


@app.route("/api/v1.0/scatter")
def scatterplot():
    scatter_data=session.execute("SELECT country, new_displacement, year, start_date FROM merged_data").fetchall()
    session.close()
    scatter = list(np.ravel(scatter_data))
    # return jsonify(scatter)

    return render_template("scatterplot.html")
    # return redirect("/")

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
    
# @ app.errorhandler(404)
# def page_not_found(e):
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == '__main__':

    app.run()