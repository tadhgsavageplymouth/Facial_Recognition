# Facial Recognition for Mock Interviews with NAO Robot 🤖🎓

This project integrates facial recognition and real-time communication with a NAO humanoid robot to support university students in preparing for interviews. Upon recognizing a student's face, the system retrieves their profile and initiates a mock interview using ChatGPT-generated questions tailored to their field of study.

---

## 🧠 Features

- 🔍 **Facial Recognition:** Detect and identify registered users via webcam using OpenCV and face encodings.
- 🤖 **NAO Robot Integration:** Seamless communication with a NAO robot over TCP to trigger behavior based on recognition.
- 🗣️ **ChatGPT Interview Prompts:** Dynamic question generation using OpenAI to simulate a mock interview experience.
- 📁 **User Profiles:** Store and retrieve student data (name, image, course, interests) from a local JSON database.
- 🧪 **Test Mode:** CLI-based test interface for development without the robot.

---

## 📂 Repository Structure

```
Facial_Recognition/
│
├── assets/                # Images and known faces
│   ├── known_faces/       # Subfolder for registered users
│   └── ...
├── nao/                   # NAO robot communication module
│   └── nao_connector.py
├── recognition/           # Core facial recognition logic
│   ├── recognizer.py
│   └── utils.py
├── interviews/            # Question generation logic
│   └── question_generator.py
├── profiles.json          # Student profiles
├── main.py                # Entry point to run the recognition loop
├── test.py                # Command-line test mode
└── requirements.txt       # Dependencies
```

---

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/tadhgsavageplymouth/Facial_Recognition.git
cd Facial_Recognition
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🔴 Run the main application:
```bash
python main.py
```

This will activate the webcam, detect faces, and communicate with the NAO robot.

### 🧪 Run in test mode (no robot):
```bash
python test.py
```

This mode will simulate recognition and output ChatGPT-generated interview questions.

---

## 🧑‍🎓 Adding a New Student

1. Add their photo in `assets/known_faces/` (preferably a clear frontal face shot).
2. Edit `profiles.json` to include their name, course, and other metadata:
```json
{
  "name": "Jane Doe",
  "course": "Computer Science",
  "interests": ["AI", "robotics"],
  "image": "jane_doe.jpg"
}
```

---

## 🔌 NAO Robot Communication

- The NAO robot should be on the same network and listening for TCP messages.
- IP and port can be configured in `nao/nao_connector.py`.

---

## 🛠️ Technologies Used

- Python 3.11+
- OpenCV
- face_recognition
- socket (for NAO communication)
- OpenAI GPT API (optional)
- JSON for data storage

---

## ✅ TODOs / Improvements

- [ ] Add GUI interface for adding new users
- [ ] Enable NAO speech interaction (bi-directional)
- [ ] Encrypt student data for privacy
- [ ] Cloud deployment options

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙋‍♂️ Author

**Tadhg Savage**  
📫 [LinkedIn](https://www.linkedin.com/in/tadhgsavage/) | ✉️ [Email](mailto:tadhgsavagedev@gmail.com)

---

> *"Helping students feel confident, one interview at a time."*
