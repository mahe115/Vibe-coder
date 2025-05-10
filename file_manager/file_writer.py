### File: file_manager/file_writer.py

import os
import json
from utils.logger import logger
from config import config


def apply_changes(llm_response):
    try:
        # This assumes the response includes filenames and updated code
        # You may need to adjust based on your actual LLM output format
        changes = json.loads(llm_response)
        for item in changes:
            filepath = item['file']
            new_code = item['content']

            if config['backup_original']:
                os.rename(filepath, filepath + ".bak")

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_code)

            logger.info(f"Updated: {filepath}")

    except Exception as e:
        logger.exception("Failed to apply LLM-generated changes")
