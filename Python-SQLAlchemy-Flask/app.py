##############################################
# Import SQL Alchemy ORM and Flask
##############################################
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from pprint import pprint
from flask import Flask, jsonify


##############################################
# Data Base and Connection Set-up
##############################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

##############################################
# Date Variable for Flask
##############################################
oneyearago = dt.date(2017,8,23) - dt.timedelta(days = 365)

###############################################
# Flask Set-Up
###############################################
app = Flask(__name__)

# Home Route
@app.route("/")
def home():
    return (f"Available routes below:<br/>"
            f"1) Return precipitation data from one year ago of the latest date.<br/>"
            f"/api/v1.0/precipitation<br/>"
            f"2) Return all station numbers from database."
            f"/api/v1.0/stations<br/>"
            f"3)Returns all temperature observations from one year ago of the latest date.<br/>
            f"/api/v1.0/tobs<br/>"
            f"4) Returns the minimum, average, and maximum values of temperature observations from indicated date."
            f"Put the start date in 'YYYY-MM-DD' format<br/>"
            f"/api/v1.0/<start><br/>"
            f"5) Returns the minimum, average, and maximum values of temperature observations between dates."
            f"Put the dates in 'YYYY-MM-DD/YYYY-MM-DD' format"
            f"/api/v1.0/<start>/<end><br/>")

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    prcpresults = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= oneyearago).all()
    all_prcp = {date: prcp for date,prcp in prcpresults}
    return jsonify(all_prcp)

# Station Route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)    
    stationresults = session.query(Station.station).all()    
    all_stations = list(np.ravel(stationresults))    
    return jsonify(all_stations)

# Temperature Observation Route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    tobsresults = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= oneyearago).all()
    all_tobs = {date: tobs for date,tobs in tobsresults}
    return jsonify(all_tobs)

# Functions with Start Date
@app.route("/api/v1.0/<start>")
def startdate(start = None):
    session = Session(engine)
    selection = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    startdateres = session.query(*selection).\
        filter(Measurement.date >= start).all()
    result = list(np.ravel(startdateres))
    return jsonify(result)

#Functions with Start and End Date
@app.route("/api/v1.0/<start>/<end>")
def dates(start = None, end = None):
    session = Session(engine)
    selection = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    dateres = session.query(*selection).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    # result = list(np.ravel(dateres))
    return jsonify(dateres)

#Debugger
if __name__ == "__main__":
    app.run(debug=True)