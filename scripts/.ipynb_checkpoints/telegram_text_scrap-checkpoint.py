from telethon.sync import TelegramClient
import pandas as pd
import os

# Step 1: Connect to Telegram
# Replace 'API_ID', 'API_HASH', and 'PHONE_NUMBER' with your credentials.
api_id = 23446573  # Get this from https://my.telegram.org
api_hash = 'd434e5f0dc2e1e7f07a9f61d7f3a72c4'
phone_number = '+251941067467'

# Connect to Telegram
client = TelegramClient('session_one', api_id, api_hash)

def fetch_messages(channel_name, limit=100):
    """
    Fetch messages from a Telegram channel.
    :param channel_name: The name or URL of the Telegram channel.
    :param limit: Number of messages to fetch.
    :return: List of messages.
    """
    try:
        messages = []
        with client:
            for message in client.iter_messages(channel_name, limit=limit):
                if message.text:  # Only fetch text messages
                    messages.append({
                        'sender': message.sender_id,
                        'text': message.text,
                        'timestamp': message.date
                    })
        return messages
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return []

def save_to_csv(data, filename):
    """
    Save messages to a CSV file.
    :param data: List of messages.
    :param filename: File to save the data.
    """
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

if __name__ == "__main__":
    # Step 2: Define the channel to fetch messages from
    channel = 't.me/your_channel_name_here'

    # Step 3: Fetch and save messages
    print("Fetching messages...")
    messages = fetch_messages(channel)
    save_to_csv(messages, 'telegram_messages.csv')

