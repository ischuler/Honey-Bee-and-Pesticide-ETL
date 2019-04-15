# import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify

# Database Setup
#################################################
# create engine
engine = create_engine("mysql://root:ericaDB@localhost/honeybees")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the bee data and pesticide use tables
bees = Base.classes.bees_data
pests = Base.classes.pesticides

# Create our session (link) from Python to the DB
session = Session(engine)


# Flask Setup
#################################################
app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h2>Welcome, honeybees! <br/></h2>"
        f"<h3>Available Routes:</h3>"
        f"<p><a href=""/api/2015/honey-yield"">2015 U.S. Honey Yield Data</a> (/api/2015/honey-yield)<br/>"
        # f"<ul>/api/2015/honey-yield</ul></p>"
        f"<p><a href=""/api/2015/pesticides-colonies"">2015 U.S. Pesticides and Colony Change</a> (/api/2015/pesticides-colonies)<br/>"
        # f"<ul>/api/2015/pesticides-colonies</ul></p>"
    )


@app.route("/api/2015/honey-yield")
def honey():
    """Returns a list of states' honey yield per colony"""
    # Query all states' bee colony & honey production data in descending order
    sel = [bees.state, bees.end_colonies,bees.colony_yield, bees.production]
    results = session.query(*sel).\
        order_by(bees.colony_yield.desc()).\
        all()

    # create dictionary of row data and append to list for production in all states
    all_prod = []
    for state, end_colonies, colony_yield, production in results:
        prod_dict = {}
        prod_dict["state (abbr.)"] = state
        prod_dict["colony count (end of year)"] = end_colonies
        prod_dict["yield per colony"] = colony_yield
        prod_dict["production"] = production
        all_prod.append(prod_dict)

    return jsonify(all_prod)


@app.route("/api/2015/pesticides-colonies")
def change():
    """Return a list of colony change data including the state, colony change, and pesticide use"""
    # Query bees and pesticides tables
    sel = [bees.state, bees.colony_change, pests.compound, pests.high_estimate]
    results = session.query(*sel).filter(bees.state == pests.state).all()

    # Create a dictionary from the row data and append to a list of colony change and pesticide use
    change_pest = []
    for state, colony_change, compound, high_estimate in results:
        chg_p_dict = {}
        chg_p_dict["state"] = state
        chg_p_dict["colony change"] = colony_change
        chg_p_dict["compound"] = compound
        chg_p_dict["high estimate"] = high_estimate
        change_pest.append(chg_p_dict)

    return jsonify(change_pest)


if __name__ == '__main__':
    app.run(debug=True)
