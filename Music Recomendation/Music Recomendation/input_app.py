import subprocess

def get_user_input():
    language = input("Enter preferred language (e.g., English, Spanish): ")
    singer = input("Enter preferred singer (optional): ")
    return language, singer

def run_emotion_detection(language, singer):
    # Run the emotion detection script with the user input
    subprocess.run(["python", "emotion_detection_app.py", language, singer])

if __name__ == "__main__":
    language, singer = get_user_input()
    run_emotion_detection(language, singer)
