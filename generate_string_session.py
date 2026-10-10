"""Generate a Pyrogram session string locally. Keep the output secret."""
import os
from pyrogram import Client

def env_value(key, default=None):
    return os.environ[key] if key in os.environ else default

def main():
    api_id = env_value("API_ID")
    api_hash = env_value("API_HASH")
    if not api_id or not api_hash:
        raise SystemExit("Set API_ID and API_HASH before running this script.")
    with Client(
        "tanmay_session_generator",
        api_id=int(api_id),
        api_hash=api_hash,
        in_memory=True,
    ) as client:
        print("\nYour STRING_SESSION (keep it private):\n")
        print(client.export_session_string())
        print("\nAdd this value as STRING_SESSION in Render/Railway variables.")

if __name__ == "__main__":
    main()
