import datetime

class TimeTracker:
    def __init__(self):
        self.employee_name = None  # Stores the name of the employee that is currently being tracked
        self.time_logs = []  # Store a list of dictionaries, each containing clock-in and clock-out logs 

    def set_employee(self, name):
        # Set the name of the employee to start tracking.
        self.employee_name = name.strip()

    def start(self):
        # Record the clock-in time.
        clock_in_time = datetime.datetime.now()
        #self.time_logs.append(clock_in_time)
        self.time_logs.append({
            'type': 'clock_in',
            'time': clock_in_time
        })
        print(f"{self.employee_name} started working at: {clock_in_time}")

    def stop(self):
        # Record the clock-out time.
        clock_out_time = datetime.datetime.now()
        #self.time_logs.append(clock_out_time)
        self.time_logs.append({
            'type': 'clock_out',
            'time': clock_out_time
        })
        print(f"{self.employee_name} stopped working at: {clock_out_time}")

    def worked_hours(self):
        # Calculate total time worked.
        total_work_seconds = 0
        clock_in_time = None  # Initialize as None
    
        #print(f"time in is working --> {self.time_logs[0]['time']}")
        #print(f"time out is working --> {self.time_logs[1]['time']}")
        for log in self.time_logs:
            
            if log['type'] == 'clock_in':
                
                clock_in_time = log['time']  # Set the clock-in time
            elif log['type'] == 'clock_out' and clock_in_time:
                # Ensure clock_in_time is valid before subtraction
                total_work_seconds += (log['time'] - clock_in_time).total_seconds()
                clock_in_time = None  # Reset clock-in time after pairing with clock-out
    
        if total_work_seconds == 0:
            print("No work time recorded. Make sure to clock in and out correctly.")
            return 0
    
        # Convert total work time to hours, minutes, and seconds.
        total_hours = total_work_seconds // 3600
        minutes = (total_work_seconds % 3600) // 60
        seconds = total_work_seconds % 60
    
        print(f"{self.employee_name} worked for a total of: {int(total_hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds.")
        return total_work_seconds

tracker = TimeTracker()

# Set the employee's name.
employee_name = input("Enter the name of the employee: ")
tracker.set_employee(employee_name)

# Start tracking work.
input("Press Enter to start working")
tracker.start()

# Stop tracking work.
input("Press Enter to stop working")
tracker.stop()

# Calculate and display total worked hours.
input("Press Enter to see how much time was worked")
tracker.worked_hours()
