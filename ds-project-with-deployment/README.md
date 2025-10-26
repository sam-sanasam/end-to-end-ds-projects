# Project set-up using template.py file
This approach will make consistency of project structure while working with a team

# Set-Up logging
The logging is very important as a part of developemt process. Specially , working across the team, if we can keep the logging 
the team can tract the error and other development related things using the logging file.

Custom logging logic is written in the file: ds-project-with-deployment/src/datascience/__init__.py

```python
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="<Costum format>",
    handlers=[
        logging.FileHandler("<Logging file where the actual log goes >"),
        logging.StreamHandler(sys.stderr)
    ]
)
```

Here, the logging basicConfig will help to customize our logging formate and where to log the logging message

The "handlers" handle where the logs go. Here logging.FileHandler keeps all the logging messages and
This "logging.StreamHandler(sys.stderr)" tells the logger to send log messages to the console (terminal) — specifically, to the 
standard error stream (stderr) instead of standard output (stdout).


logging attribute ref: https://docs.python.org/3/library/logging.html



logging.getLogger(name) checks if a logger with that name already exists.

- If yes → it returns the same logger (so logs stay consistent).

- If not → it creates a new logger instance with that name.

Each logger has its own:

Logging level (INFO, ERROR, etc.)

Handlers (file, stream, etc.)

Formatters

This allows you to organize logs by component — e.g.:
```python
import logging

logger_data = logging.getLogger("DataProcessing")
logger_model = logging.getLogger("ModelTraining")
logger_api = logging.getLogger("APIDeployment")

```

Calling the logger
logger.info("This is the custom logging")


Output
```commandline
[2025-10-26 23:00:03,810: INFO: main: This is the custom logging]

```
-------------------------------------------------------------------------------------------

