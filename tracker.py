from datetime import datetime
import database as db


class ActivityTracker:


    def add_activity(self, subject: str, topic: str, duration: int, date: str):

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if not subject.strip():
            raise ValueError("Subject cannot be empty.")
        
        if not isinstance(topic, str):
            raise TypeError("Topic must be a string.")
        if not topic.strip():
            raise ValueError("Topic cannot be empty.")

        if isinstance(duration, bool) or not isinstance(duration, int):
            raise TypeError("Duration must be an integer.")
        if duration <= 0:
            raise ValueError("Duration must be > 0.")

        if not isinstance(date, str):
            raise TypeError("Date must be a string.")
        try:
            datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date. Use YYYY-MM-DD.")
        
        return db.insert_activity(subject, topic, duration, date)


    def update_activity(self, id: int, subject: str, topic: str, duration: int, date: str):

        if isinstance(id, bool) or not isinstance(id, int):
            raise TypeError("ID must be an integer.")
        if id <= 0:
            raise ValueError("ID must be >= 1.")

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if not subject.strip():
            raise ValueError("Subject cannot be empty.")

        if not isinstance(topic, str):
            raise TypeError("Topic must be a string.")
        if not topic.strip():
            raise ValueError("Topic cannot be empty.")

        if isinstance(duration, bool) or not isinstance(duration, int):
            raise TypeError("Duration must be an integer.")
        if duration <= 0:
            raise ValueError("Duration must be > 0.")

        if not isinstance(date, str):
            raise TypeError("Date must be a string.")
        try:
            datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date. Use YYYY-MM-DD.")
        
        return db.update_activity(id, subject, topic, duration, date) 


    def delete_activity(self, id):

        if isinstance(id, bool) or not isinstance(id, int):
            raise TypeError("ID must be an integer.")
        if id <= 0:
            raise ValueError("Id must be >= 1.")
        
        return db.delete_activity(id)


    def calculate_total_time(self):
        return db.get_total_learning_time()


    def calculate_time_by_subject(self, subject: str):

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if not subject.strip():
            raise ValueError("Subject cannot be empty.")
        
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

        if not activities:
            return "No activities found."
        return ret
        #return db.get_activities()


    def show_activities_by_subject(self, subject: str):

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if not subject.strip():
            raise ValueError("Subject cannot be empty.")

        #return db.get_activities_by_subject(subject)
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
        #return db.get_weekly_statistics()


    def display_time(self, minutes: int):

        if isinstance(minutes, bool) or not isinstance(minutes, int):
            raise TypeError("Minutes must be an integer.")
        if minutes < 0:
            raise ValueError("Minutes cannot be < 0.")
        
        hours = int(minutes / 60)
        remaining_minutes = minutes % 60

        ret = ""
        if hours > 0:
            ret += str(hours) + " h "
        ret += str(remaining_minutes) + " min"

        return ret
