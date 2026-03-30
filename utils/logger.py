import logging
import os





class log_maker():
    @staticmethod
    def log_Gen():
        folder = "logs"
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder,"scraper.log")
        logging.basicConfig(filename=file_path,level=logging.INFO,format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger("E-commearce scraping ")
        logger.setLevel(logging.INFO)
        return logger
    