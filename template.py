import os
from pathlib import Path
import logging

project_name="hate" 
list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcloud_syncer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/predection_pipeline.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "demo.py",
    "setup.py",
    "requirements.txt",
    "Dockerfile"
]

# Create the files
for file_path in list_of_files:
    dir_name = os.path.dirname(file_path)  
    if dir_name:  # Ensure we don't call makedirs on empty strings (for files in root)
        os.makedirs(dir_name, exist_ok=True)
    
    # Create the file
    with open(file_path, "w") as f:
        pass  # Create an empty file

print("All files have been created successfully!")