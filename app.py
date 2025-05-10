### File: app.py

from overlay_ui.overlay import OverlayApp
from file_manager.directory_selector import select_directory
from utils.logger import setup_logger

logger = setup_logger()

def main():
    try:
        directory = select_directory()
        logger.info(f"Working directory selected: {directory}")
        
        app = OverlayApp(directory)
        app.run()

    except Exception as e:
        logger.exception("Error launching application")

if __name__ == "__main__":
    main()
