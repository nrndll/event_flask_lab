from flask import render_template, request              #redirect
from app import app
from models.event_list import events
from models.event import Event

@app.route("/events")
def index():
    return render_template("events.html", events=events)


