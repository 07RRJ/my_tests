import msvcrt
import time
import threading

def wait_for_input():
    print("Press any key to continue...")
    msvcrt.getch()  # Wait for a key press

# Start the input thread
input_thread = threading.Thread(target=wait_for_input)
input_thread.start()

# Sleep for a specific duration
time.sleep(5)  # Sleep for 5 seconds

# Check if the input thread is still alive
if input_thread.is_alive():
    print("Time's up! No key pressed.")
else:
    print("Key was pressed!")
