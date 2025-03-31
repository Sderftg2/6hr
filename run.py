import subprocess
import time
import logging

# Configure logging
logging.basicConfig(filename="lightning.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def run_lightning():
    """Runs the Lightning AI app continuously with auto-restart."""
    while True:
        try:
            logging.info("Starting Lightning AI App...")
            process = subprocess.Popen(["python", "my_lightning_app.py"])
            process.wait()  # Wait for process to exit

        except Exception as e:
            logging.error(f"Lightning AI App crashed: {e}")

        logging.info("Restarting in 5 seconds...")
        time.sleep(5)  # Delay before restarting

if __name__ == "__main__":
    run_lightning()
