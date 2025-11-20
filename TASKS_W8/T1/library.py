import time

def activatePause(duration: float):
    print(f"Pausing for {duration} seconds.")
    time.sleep(duration)
    print("Unpaused.")