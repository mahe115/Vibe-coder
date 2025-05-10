import json
import requests
from file_manager.file_reader import get_all_code
from utils.logger import logger

config = json.load(open("config.json"))

def handle_prompt(prompt, directory):
    file_list, code_content = get_all_code(directory, config['file_extensions'])

    full_prompt = (
        f"You are a code assistant. A developer has this project containing the following files:\n"
        f"{file_list}\n\n"
        f"They want help with the following prompt:\n{prompt}\n\n"
        f"Here is the content of the files:\n{code_content}"
    )

    payload = {
        "model": config["model"],
        "messages": [
            {"role": "system", "content": "You are a helpful code assistant."},
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.3
    }
    print(full_prompt)
    print(payload)

    try:
        res = requests.post(config["llm_api"], headers={
            "Authorization": f"Bearer {config['api_key']}",
            "Content-Type": "application/json"
        }, json=payload)
        res.raise_for_status()
        return res.json()['choices'][0]['message']['content']
    except Exception as e:
        logger.exception("Error calling Groq LLM API")
        return "[Error calling LLM API]"
