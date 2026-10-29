import sys
import database as db

class ActivityTracker:


    def __init__(self):
        self.activities = []


    def add_activity(self, subject: str, topic: str, duration: float, date: str):
        #activity = {"subject": subject,
        #            "topic": topic,
        #            "duration": duration,
        #            "date": date}

        db.insert_activity(subject, topic, duration, date)
        #self.activities.append(activity)


    def update_activity(self, id: int, subject: str, topic: str, duration: float, date: str):
        db.update_activity(id, subject, topic, duration, date)


    def delete_activity(self, id):
        db.delete_activity(id)


    def calculate_total_time(self):
        total = 0
        for activity in self.activities:
            total += activity["duration"]

        return total


    def calculate_time_by_subject(self, subject: str):
        total = 0
        for activity in self.activities:
            if activity["subject"] == subject:
                total += activity["duration"]

        return total


    def show_activities(self):
        """ ret = "\n==================Activities=================\n"
        
        for activity in self.activities:
            for key in activity:
                ret += f"{key}: {activity[key]}\n"
            ret += "\n"
        return ret """

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
            """ ret = "\n==================Activities=================\n"
            
            for activity in self.activities:
                for key in activity:
                    ret += f"{key}: {activity[key]}\n"
                ret += "\n"
            return ret """
    
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


if __name__ == "__main__":
    db.initialize_database()
    tracker = ActivityTracker()

    while True:
        print("=====================Menu====================\n")
        print("1. Add activity\n"
              "2. Update activity\n"
              "3. Delete activity\n"
              "4. Show activities\n"
              "5. Show activities by subject\n"
              "6. Calculate total learning time\n"
              "7. Calculate time by subject\n"
              "8. Quit")
        
        choice = int(input("\nWhat do you want to do? "))

        if choice == 1:
            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = float(input("Duration: "))
            date = input("Date: ")
            tracker.add_activity(subject, topic, duration, date)
        elif choice == 2:
            id = input("Id: ")
            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = float(input("Duration: "))
            date = input("Date: ")
            tracker.update_activity(id, subject, topic, duration, date)
        elif choice == 3:
            id = input("Id: ")
            tracker.delete_activity(id)
        elif choice == 4:
            print("\n==================Activities=================\n")
            print(tracker.show_activities())
        elif choice == 5:
            subject = input("Which subject? ")
            print("\n==================Activities=================\n")
            print(tracker.show_activities_by_subject(subject))
        elif choice == 6:
            print(tracker.calculate_total_time(), " min\n")
        elif choice == 7:
            subject = input("Which subject? ")
            print(tracker.calculate_time_by_subject(subject), " min\n")
        elif choice == 8:
            sys.exit()
        else:
            print("Please choose an option.\n")