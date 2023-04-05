#!venv/bin/python3
"""
Copyright (c) 2023 - present diskovafrika.com
"""
import os
from dotenv import load_dotenv, find_dotenv
from diskovafrika import create_app

load_dotenv(find_dotenv())

app = create_app()


if __name__ == "__main__":
    PORT = os.getenv("PORT", default=5000)
    app.run(port=PORT)
