from __future__ import division
from flask import Flask, render_template
import random
import datetime


app = Flask(__name__)

target_time = datetime.datetime(2017, 1, 1)


times = [
	(datetime.timedelta(hours=10, minutes=42), '{} days on Saturn'),
	(datetime.timedelta(hours=0, minutes=42, seconds=49), '{} plays of The Dark Side of the Moon'),
	(datetime.timedelta(hours=0, minutes=6, seconds=20), '{} watchings of the original Star Wars Trilogy'),
	(datetime.timedelta(hours=0, minutes=40, seconds=0), '{} episodes of Buffy'),
	(datetime.timedelta(hours=0, minutes=22, seconds=52), '{} days in England'),
	(datetime.timedelta(hours=4, minutes=0, seconds=0), 'approximately {} band jobs'),
	(datetime.timedelta(hours=3, minutes=45), '{} drives to Pembrokeshire'),
	(datetime.timedelta(hours=3, minutes=37), '{} trips to lovelylovelylovelylovely Scarborough'),
	(datetime.timedelta(hours=0, minutes=10), '{} games of Space Rocks 3D (okay, made that one up)'),
	(datetime.timedelta(hours=1, minutes=40), '{} watches of Muppet Treasure Island'),
	(datetime.timedelta(hours=2, minutes=15), 'roughly {} walks into Banbury'),
	(datetime.timedelta(days=5 * 365, ), '(very) roughly {} Moris Minor refurbishments'),
	(datetime.timedelta(minutes=57), '{} playings of Muse - Absolution'),
	(datetime.timedelta(minutes=2, seconds=40), '{} rides on Oblivion'),
]


@app.route("/")
def index():
	timedelta = target_time - datetime.datetime.now()
	days = timedelta.days 
	my_time, text = times[random.randint(0, len(times) - 1)]
	diff = timedelta.total_seconds() / my_time.total_seconds()
	text = text.format(round(diff, 3))
	return(render_template('index.html', days=days, text=text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
