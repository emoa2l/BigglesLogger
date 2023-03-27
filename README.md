## BigglesLogger

BigglesLogger is a simple Python logging utility that makes it easy to log messages to both stdout and a log file. It includes support for rotating log files on a daily basis.

## Installation
To install BigglesLogger, simply copy the BigglesLogger.py file into your project directory.

## Usage
To use BigglesLogger in your project, import the BigglesLogger class and create an instance of it with the desired log level and log directory:

python
Copy code
from BigglesLogger import BigglesLogger

logger = BigglesLogger(log_level=logging.DEBUG, log_directory='./logs')
logger.setup_logging()

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
By default, logs are written to the ./logs directory and rotated daily. You can specify a different log directory by passing it to the BigglesLogger constructor:

python
Copy code
logger = BigglesLogger(log_level=logging.DEBUG, log_directory='/path/to/logs')
You can also customize the log format by modifying the formatter object in the setup_logging() method.

## Contributing
If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.

## License
BigglesLogger is licensed under the MIT License. See the LICENSE file for details.