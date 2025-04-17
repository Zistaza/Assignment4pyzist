import time
import threading
import os

# Global variables to control the timer state
paused = False
stopped = False

# Function to clear the console (works on Windows and Unix-like systems)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to handle user commands for pause, resume, and stop
def control_timer():
    global paused, stopped
    while not stopped:
        # Print the control options prompt for the user
        command = input("\nEnter command: [P]ause, [R]esume, [S]top ➤ ").lower().strip()
        if command == 'p':
            paused = True
            print("⏸ Timer paused. Press 'r' to resume.")
        elif command == 'r':
            if paused:
                paused = False
                print("▶️ Timer resumed.")
        elif command == 's':
            stopped = True
            print("❌ Timer stopped.")
            break
        else:
            print("🚫 Unknown command. Please use P, R, or S.")

# Main countdown timer function that also shows a running clock
def countdown(total_seconds):
    global paused, stopped
    while total_seconds > 0 and not stopped:
        clear_console()  # Refresh the display for updated information
        
        # Get current time (running clock)
        current_time = time.strftime("%H:%M:%S")
        mins, secs = divmod(total_seconds, 60)
        
        # Display countdown timer and running clock
        print(f"Countdown Timer: {mins:02d}:{secs:02d}")
        print(f"Running Clock  : {current_time}")
        print("\nEnter command: [P]ause, [R]esume, [S]top ➤ ")

        # Only decrement time if not paused
        if not paused:
            time.sleep(1)
            total_seconds -= 1
        else:
            time.sleep(1)  # Wait while paused (the display still updates)

    clear_console()  # Final clear to show the ending message
    if not stopped:
        print("\n⏰ Time’s up!")
    else:
        print("\n❌ Timer stopped by user.")

# Get user input in MM:SS format
user_input = input("⏳ Enter time (MM:SS): ")
try:
    minutes, seconds = map(int, user_input.split(":"))
    total_seconds = minutes * 60 + seconds
except ValueError:
    print("⚠️ Invalid format. Use MM:SS (e.g., 2:30)")
    exit()

# Start the control thread (for handling pause/resume/stop commands)
threading.Thread(target=control_timer, daemon=True).start()

# Start the countdown
countdown(total_seconds)
