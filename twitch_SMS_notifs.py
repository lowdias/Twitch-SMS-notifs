"""
Twitch Live SMS Notifier
Author: Ilias Kamal
Email: ilias.kamal@gmail.com
Date: March 24, 2023

Description: This script checks if a specific Twitch channel is live and sends an SMS notification using Twilio if it is.
"""

import requests
from twilio.rest import Client

# Set up Twilio client with your Account SID and Auth Token
client = Client("YOUR_ACCOUNT_SID", "YOUR_AUTH_TOKEN")

# Set up Twitch API endpoint and headers
endpoint = "https://api.twitch.tv/helix/streams"
headers = {"Client-ID": "YOUR_TWITCH_CLIENT_ID"}

# Set the Twitch channel name to check
channel_name = "YOUR_TWITCH_CHANNEL_NAME"

# Set the phone number to receive SMS alerts
phone_number = "YOUR_PHONE_NUMBER"

# Check if the Twitch channel is live
response = requests.get(endpoint, headers=headers, params={"user_login": channel_name})
data = response.json()
is_live = False
if "data" in data and len(data["data"]) > 0:
    is_live = True

# Send an SMS alert if the channel is live
if is_live:
    message = client.messages.create(
        to=phone_number,
        from_="YOUR_TWILIO_PHONE_NUMBER",
        body=f"{channel_name} is now live on Twitch!"
    )
    print("SMS message sent!")
else:
    print("Channel is not live.")
