from datetime import datetime
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import calendar


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config.from_envvar("BATHROOM_AVAILABILITY_CONF")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# thanks to https://stackoverflow.com/a/14469780
@app.template_filter("date_to_millis")
def date_to_millis(d):
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return calendar.timegm(d.utctimetuple()) * 1000


class AvailabilityRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


@app.route("/")
def index():
    record = AvailabilityRecord.query.order_by(AvailabilityRecord.id.desc()).first()

    return render_template("main.html", record=record)


@app.route("/update", methods=["POST"])
def update():
    data = request.get_json()
    available = data["available"]
    password = data["password"]

    if password != app.config["SUPER_SECRET_AND_SECURE_PASSWORD"]:
        return "Invalid Password", 403

    if isinstance(available, bool):
        record = AvailabilityRecord(available=available)
        db.session.add(record)
        db.session.commit()

    return "OK", 200
