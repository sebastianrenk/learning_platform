import sys
import database as db
from datetime import datetime
from tracker import ActivityTracker


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

        try:
            choice = int(input("\nWhat do you want to do? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:

            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = int(input("Duration (min): "))
            date = input("Date (YYYY-MM-DD): ") 
            tracker.add_activity(subject, topic, duration, date)
            

        elif choice == 2:

            id = int(input("Id: "))
            subject = input("Subject: ")
            topic = input("Topic: ")
            duration = int(input("Duration (min): "))
            date = input("Date: ")
            if tracker.update_activity(id, subject, topic, duration, date) == 0:
                print("\nNo match found.")

        elif choice == 3:

            id = int(input("Id: "))
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
            print("Total learning time: ", tracker.display_time(tracker.calculate_total_time()), "\n")

            print("Time by subject: \n")
            subjects = tracker.get_subjects()
            for subject in subjects:
                print(subject, tracker.display_time(tracker.calculate_time_by_subject(subject)))
            print("\n")

            print("This week:\n")
            print(tracker.show_weekly_statistics(), "\n")

        elif choice == 7:

            sys.exit()

        else:

            print("Please choose an option.\n")