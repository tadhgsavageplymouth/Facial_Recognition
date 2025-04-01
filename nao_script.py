import sys
import time

# Ensure naoqi is installed
try:
    from naoqi import ALProxy
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "naoqi"])
    from naoqi import ALProxy

# NAO connection info
NAO_IP = "192.168.1.100"  # Replace with your robot's IP
NAO_PORT = 9559

# Connect to text-to-speech
try:
    tts = ALProxy("ALTextToSpeech", NAO_IP, NAO_PORT)
except Exception as e:
    sys.exit(f"Could not connect to NAO: {e}")

# Configure and speak
tts.setLanguage("English")
tts.setVolume(0.8)

for phrase in [
    "Hello, I am Nao.",
    "Ready to help with your interview.",
    "Ask me anything!"
]:
    tts.say(phrase)
    time.sleep(1)
