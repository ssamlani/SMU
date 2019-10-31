
# PART 1 -- DEPENDENCIES AND SETUP
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from flask import Flask, jsonify, request

# PART 2 -- DATABASE SETUP / LINK
# link python to database
engine = create_engine("sqlite:////Users/ssamlani/Documents/SMU_DS_BC /SMU_Homework/10_Advanced Data Storage and Retrieval_Sabir/Resources/hawaii.sqlite", echo = False)

# declare base as automap base
Base = automap_base()

# reflect the database into classes
Base.prepare(engine, reflect=True)

# Save references
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session (link) to database
session = Session(engine)

# PART 3 -- FLASK SETUP AND ROUTE CREATION

# Flask setup
app = Flask(__name__)
# Flask routes
@app.route("/")
# intro/explanation
def welcome():
    return (
        f"Welcome to the weather API!<br/>"
        f"Pick from the following available routes:<br/>"
        f"/api/v1.0/precipitation<br/>Returns a list of JSON representation of dictionary.<br/>"
        f"/api/v1.0/stations<br/>Returns a list of stations from the dataset.<br/>"
        f"/api/v1.0/tobs<br/>Returns a list of dates and temperature observations from dataset. Stations are included to avoid confusion as instructions don't specify a particular station.<br/>"
        f"/api/v1.0/temp/start/end<br/>Returns a list of min, avg, and max temperatures for all dates between the start and end dates.<br/>"
    )
# precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calulate the date 1 year ago from today
    last_date = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date.desc()).first()[0]
    last_year = str(dt.datetime.strptime(last_date,"%Y-%m-%d") - dt.timedelta(days=365))

    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
		filter(Measurement.date >=last_year, Measurement.date <=last_date).\
		order_by(Measurement.date).all()
	# formula for itemizing each item brought in from the query
    precip_dict = {date: prcp for date, prcp in precipitation}
    return jsonify(precip_dict)

# stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Measurement.station).\
    	group_by(Measurement.station).all()
    # formula for itemizing each item brought in from the query
    stations = list(np.ravel(results))
    return jsonify(stations)

# temperature observations route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations for previous year."""
    # last date in the dataset and year from last date calculations
    last_date = session.query(Measurement.date,Measurement.prcp).order_by(Measurement.date.desc()).first()[0]
    last_year = str(dt.datetime.strptime(last_date,"%Y-%m-%d") - dt.timedelta(days=365))

    last_year_tobs = session.query(Measurement.date, Measurement.station,Measurement.tobs).\
		filter(Measurement.date >=last_year, Measurement.date <=last_date).\
		order_by(Measurement.date,Measurement.station).all()

    # formula for itemizing each item brought in from the query
    temps = list(np.ravel(last_year_tobs))
    return jsonify(temps)



if __name__ == '__main__':
    app.run()

