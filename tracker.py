import database as db


class ActivityTracker:


    def __init__(self):
        self.activities = []


    def add_activity(self, subject: str, topic: str, duration: int, date: str):
        db.insert_activity(subject, topic, duration, date)


    def update_activity(self, id: int, subject: str, topic: str, duration: int, date: str):
        return db.update_activity(id, subject, topic, duration, date) 


    def delete_activity(self, id):
        return db.delete_activity(id)


    def calculate_total_time(self):
        return db.get_total_learning_time()


    def calculate_time_by_subject(self, subject: str):
        return db.get_learning_time_by_subject(subject)


    def show_activities(self):
        activities = db.get_activities()
        ret = ""

        for activity in activities:
            ret += "ID: " + str(activity[0]) + "\n"
            ret += "Subject: " + str(activity[1]) + "\n"
            ret += "Topic: " + str(activity[2]) + "\n"
            ret += "Duration: " + str(activity[3]) + "\n"
            ret += "Date: " + str(activity[4]) + "\n"
            ret += "\n"

        return ret


    def show_activities_by_subject(self, subject: str):
        activities = db.get_activities_by_subject(subject)
        ret = ""

        for activity in activities:
            ret += "ID: " + str(activity[0]) + "\n"
            ret += "Subject: " + str(activity[1]) + "\n"
            ret += "Topic: " + str(activity[2]) + "\n"
            ret += "Duration: " + str(activity[3]) + "\n"
            ret += "Date: " + str(activity[4]) + "\n"
            ret += "\n"

        return ret


    def get_subjects(self):
        return db.get_subjects()


    def show_weekly_statistics(self):
        result = db.get_weekly_statistics()

        ret = ""
        ret += "Learning time: " + str(self.display_time((result[0]))) + "\n"
        ret += "Number of sessions: " + str(result[1])

        return ret


    def display_time(self, minutes: int):
        hours = int(minutes / 60)
        remaining_minutes = minutes % 60

        ret = ""
        if hours > 0:
            ret += str(hours) + " h "
        ret += str(remaining_minutes) + " min"

        return ret
