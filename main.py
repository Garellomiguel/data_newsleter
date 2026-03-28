import os
import requests

def main():
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token:
        raise ValueError("Falta TELEGRAM_BOT_TOKEN")

    if not chat_id:
        raise ValueError("Falta TELEGRAM_CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "hello world",
    }

    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()

    print("Mensaje enviado correctamente")


if __name__ == "__main__":
    main()