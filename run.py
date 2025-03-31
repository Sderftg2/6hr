import subprocess
import time

def run_dashwave():
    while True:
        print("Starting Dashwave terminal...")
        
        try:
            # Open a persistent shell session to Dashwave
            process = subprocess.Popen(["bash", "-c", "console.dashwave.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            stdout, stderr = process.communicate()
            print(f"Dashwave stopped. Restarting in 5 seconds...\nError: {stderr.decode('utf-8')}")

        except Exception as e:
            print(f"Unexpected error: {e}")

        time.sleep(5)  # Wait before restarting

if name == "main":
    run_dashwave()
