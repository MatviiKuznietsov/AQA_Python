import json
import os
import logging

logging.basicConfig(
    filename="json_report.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

json_folder = "work_with_json"

for file in os.listdir(json_folder):
    if file.endswith(".json"):
        path = os.path.join(json_folder, file)

        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)

        except json.JSONDecodeError as e:
            logging.error(f"{file} is invalid JSON: {e}")