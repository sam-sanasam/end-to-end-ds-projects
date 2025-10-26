import os
from pathlib import Path, PurePath
import logging
import logging

logger = logging.getLogger(__name__)


project_name="datascience"

## List of file to be created

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.y",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py"
    "resource/resource.ipynb",
    "templates/index.html",
    "app.py"
]


# create all the files and folder
for filepath in list_of_files:
    file_path=Path(filepath)
    file_dir, file_name = os.path.split(file_path)

    # Handling Create Directory
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logger.info(f"Creating directory {file_dir} for files {file_name}")

    # Handling Create Files
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0 ):
        with open(file_path, 'w') as f:
            pass
        logger.info(f"Creating empty file : {file_name}")
    else:
        logger.info(f"The file : {file_name} is already exist")
