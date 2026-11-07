from flask import Flask, render_template, request, redirect, url_for
from tracker import ActivityTracker


app = Flask(__name__)


tracker = ActivityTracker()


@app.route("/")
def home():
    total_time = tracker.calculate_total_time()
    weekly_stats = tracker.get_weekly_statistics()
    activities = tracker.get_activities()

    # variables in render_template become accessible in html
    return render_template("index.html", total_time=total_time, weekly_stats=weekly_stats, activities=activities)


@app.route("/add", methods=["POST"])
def add_activity():
    subject = request.form["subject"]
    topic = request.form["topic"]
    duration = int(request.form["duration"])
    date = request.form["date"]

    tracker.add_activity(subject, topic, duration, date)

    return redirect(url_for("home"))


@app.route("/delete", methods=["POST"])
def delete_activity():
    id = int(request.form["id"])

    tracker.delete_activity(id)

    return redirect(url_for("home"))


@app.route("/edit", methods=["POST"])
def edit_activity():
    id = int(request.form["id"])
    subject = request.form["subject"]
    topic = request.form["topic"]
    duration = int(request.form["duration"])
    date = request.form["date"]

    tracker.update_activity(id, subject, topic, duration, date)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)