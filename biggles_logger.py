import logging
import logging.handlers
import os
import sys
import os

class BigglesLogger:
  def __init__(self, log_level=logging.DEBUG, log_directory=None):
    
    if log_directory is None:
      log_directory = os.path.join(os.getcwd(), '/logs')
      self.log_directory = log_directory

    self.log_directory = log_directory
    self.log_level = log_level

  def setup_logging(self):
    # Ensure the log directory exists
    os.makedirs(self.log_directory, exist_ok=True)

    # Define the logging format
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    # Create a logger for the root module
    root_logger = logging.getLogger()
    root_logger.setLevel(self.log_level)

    # Add a stream handler to log to stdout when running in debug mode
    if self.log_level == logging.DEBUG:
      stream_handler = logging.StreamHandler(sys.stdout)
      stream_handler.setLevel(self.log_level)
      stream_handler.setFormatter(formatter)
      root_logger.addHandler(stream_handler)a

    # Add a rotating file handler to log to a file in the log directory
    file_handler = logging.handlers.TimedRotatingFileHandler(
      os.path.join(self.log_directory, 'app.log'),
      when='midnight',
      backupCount=7,
      encoding='utf-8'
    )
    file_handler.setLevel(self.log_level)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
