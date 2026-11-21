from github import Github
from dotenv import load_dotenv
from pathlib import Path
import os

# Claude Desktop does not pass .env in, so load it from the project root.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

github_client = Github(os.getenv("GITHUB_TOKEN"))
