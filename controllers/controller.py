from flask import render_template, request, redirect
from app import app
from models.event_list import *
from models.event import Event

@app.route("/events")
def index():
    return render_template("events.html", events=events)


@app.route("/events", methods=["POST"])
def add_event():
    event_date = request.form["date"]
    name_of_event = request.form["name_of_event"]
    number_of_guests = request.form["number_of_guests"]
    room_location = request.form["room_location"]
    description = request.form["description"]
    new_event = Event(date=event_date, name_of_event=name_of_event, number_of_guests=number_of_guests, room_location=room_location, description=description)
    add_new_event(new_event)
    return redirect("/events")

