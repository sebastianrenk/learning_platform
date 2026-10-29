import sys

class ActivityTracker:


    def __init__(self):
        self.activities = []


    def add_activity(self, subject: str, topic: str, duration: float, date: str):
        activity = {"subject": subject,
                    "topic": topic,
                    "duration": duration,
                    "date": date}

        self.activities.append(activity)


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


    def __str__(self):
        ret = "\n==================Activities=================\n"
        
        for activity in self.activities:
            for key in activity:
                ret += f"{key}: {activity[key]}\n"
            ret += "\n"
        return ret


if __name__ == "__main__":
    tracker = ActivityTracker()

    while True:
        print("=====================Menu====================\n")
        print("1. Add activity\n2. Show activities\n3. Calculate total learning time\n4. Calculate time by subject\n5. Quit")
        choice = int(input("What do you want to do? "))

        if choice == 1:
            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = float(input("Duration: "))
            date = input("Date: ")
            tracker.add_activity(subject, topic, duration, date)
        elif choice == 2:
            print(tracker)
        elif choice == 3:
            print(tracker.calculate_total_time(), " min\n")
        elif choice == 4:
            subject = input("Which subject? ")
            print(tracker.calculate_time_by_subject(subject), " min\n")
        elif choice == 5:
            sys.exit()
        else:
            print("Please choose an option.\n")
    