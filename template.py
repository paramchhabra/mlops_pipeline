import os
from pathlib import Path
import logging

#what are the other parameter options, what does this one do
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "mlProject"

file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for i in file_list:
    path = Path(i)
    fdir, fname = os.path.split(path)

    if fdir != "":
        os.makedirs(fdir, exist_ok=True)
        logging.info(f"Creating directory: {fdir} for the file {fname}")

    if (not os.path.exists(path)) or (os.path.getsize(path) == 0):
        with open(path,"w") as f:
            pass
        logging.info(f"Creating empty file :{path}")
    else:
        logging.info(f"{fname} already exists")