from flask import Flask, render_template
from tracker import ActivityTracker


app = Flask(__name__)


tracker = ActivityTracker()


@app.route("/")
def home():
    total_time = tracker.calculate_total_time()
    weekly_stats = tracker.get_weekly_statistics()

    # variables in render_template become accesible in html
    return render_template("index.html", total_time=total_time, weekly_stats=weekly_stats)


if __name__ == "__main__":
    app.run(debug=True)