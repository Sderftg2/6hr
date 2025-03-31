import subprocess
import time

def run_dashwave():
    while True:
        print("Starting Dashwave...")
        process = subprocess.Popen(["dashwave", "run"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Monitor the process
        stdout, stderr = process.communicate()
        print("Dashwave stopped. Restarting in 5 seconds...")
        print(stderr.decode("utf-8"))
        
        time.sleep(5)  # Wait before restarting

if name == "main":
    run_dashwave()
