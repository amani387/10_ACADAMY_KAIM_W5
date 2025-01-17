from telethon.sync import TelegramClient
import pandas as pd
import nest_asyncio
import asyncio

# Step 1: Apply `nest_asyncio` to handle nested event loops in environments like Jupyter
nest_asyncio.apply()

# Step 2: Connect to Telegram
api_id = 23446573  # Replace with your API ID
api_hash = 'd434e5f0dc2e1e7f07a9f61d7f3a72c4'  # Replace with your API Hash
client = TelegramClient('session_one', api_id, api_hash,timeout=10)

async def fetch_messages_async(channel_name, limit=5):
    """
    Asynchronous function to fetch messages from a Telegram channel.
    :param channel_name: The name or URL of the Telegram channel.
    :param limit: Number of messages to fetch.
    :return: List of messages.
    """
    try:
        messages = []
        async with client:
            async for message in client.iter_messages(channel_name, limit=limit):
                if message.text:
                    messages.append({
                        'sender': message.sender_id,
                        'text': message.text,
                        'timestamp': message.date
                    })
        return messages
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return []

def fetch_messages(channel_name, limit=100):
    """
    Wrapper function to run the asynchronous fetch in any environment.
    :param channel_name: The name or URL of the Telegram channel.
    :param limit: Number of messages to fetch.
    :return: List of messages.
    """
    # Use `asyncio.run_coroutine_threadsafe` for environments with running event loops
    loop = asyncio.get_event_loop()
    if loop.is_running():
        # Schedule the coroutine in the running loop and wait for the result
        future = asyncio.run_coroutine_threadsafe(fetch_messages_async(channel_name, limit), loop)
        return future.result()
    else:
        return asyncio.run(fetch_messages_async(channel_name, limit))

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
    # Define the channel to fetch messages from
    channel = 't.me/your_channel_name_here'  # Replace with the actual channel name

    # Fetch and save messages
    print("Fetching messages...")
    messages = fetch_messages(channel)
    save_to_csv(messages, 'telegram_messages.csv')
