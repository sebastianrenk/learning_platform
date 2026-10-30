import sys
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
        ret += "Learning time: " + str(display_time((result[0]))) + "\n"
        ret += "Number of sessions: " + str(result[1])

        return ret


def display_time(minutes: int):
    hours = int(minutes / 60)
    remaining_minutes = minutes % 60

    ret = ""
    if hours > 0:
        ret += str(hours) + " h "
    ret += str(remaining_minutes) + " min"

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
              "6. Show statistics\n"
              "7. Quit")
        
        choice = int(input("\nWhat do you want to do? "))

        if choice == 1:

            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = int(input("Duration (min): "))
            date = input("Date: ")
            tracker.add_activity(subject, topic, duration, date)

        elif choice == 2:

            id = input("Id: ")
            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = int(input("Duration (min): "))
            date = input("Date: ")
            if tracker.update_activity(id, subject, topic, duration, date) == 0:
                print("\nNo match found.")

        elif choice == 3:

            id = input("Id: ")
            if tracker.delete_activity(id) == 0:
                print("\nNo match found.")

        elif choice == 4:

            print("\n==================Activities=================\n")
            print(tracker.show_activities())

        elif choice == 5:

            subject = input("Which subject? ")
            print("\n==================Activities=================\n")
            print(tracker.show_activities_by_subject(subject))

        elif choice == 6:

            print("\n=================Learning Stats================\n")
            print("Total learning time: ", display_time(tracker.calculate_total_time()), "\n")

            print("Time by subject: \n")
            subjects = tracker.get_subjects()
            for subject in subjects:
                print(subject, display_time(tracker.calculate_time_by_subject(subject)))
            print("\n")

            print("This week:\n")
            print(tracker.show_weekly_statistics(), "\n")

        elif choice == 7:

            sys.exit()

        else:

            print("Please choose an option.\n")