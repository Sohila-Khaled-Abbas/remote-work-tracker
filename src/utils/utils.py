import logging
from datetime import datetime

def setup_logging(log_file="app.log", level=logging.INFO):
    """Sets up basic logging for the application."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging setup complete.")

def get_current_timestamp():
    """Returns the current UTC timestamp in ISO format."""
    return datetime.utcnow().isoformat()

# Example usage (for testing purposes)
if __name__ == "__main__":
    setup_logging("test_app.log", logging.DEBUG)
    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    print(f"Current timestamp: {get_current_timestamp()}")

