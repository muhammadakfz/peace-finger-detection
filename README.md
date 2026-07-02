# Peace Finger Detection

Real-time hand gesture detection using MediaPipe. When a **peace** ✌️ gesture (index and middle fingers extended) is detected, the entire screen blurs.

![Demo](demo.gif)

## Features

- Real-time webcam hand tracking
- Peace finger gesture detection
- Full-screen blur effect when gesture detected
- Supports up to 2 hands
- Cross-platform (Windows, macOS, Linux)

## Requirements

- Python 3.9+
- Webcam

## Installation

```bash
pip install opencv-python mediapipe numpy
```

## Setup

Download the MediaPipe hand landmarker model:

```bash
curl -L -o hand_landmarker.task "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
```

## Usage

```bash
python main.py
```

Press `q` to quit.

## How It Works

1. Webcam captures video feed
2. MediaPipe detects hands in real-time
3. Gesture recognition identifies "peace" pose
4. Full-screen blur applies when peace gesture detected

## Project Structure

```
├── main.py          # Main application
├── detector.py      # MediaPipe hand detection
├── gestures.py      # Peace gesture recognition
├── effects.py       # Blur effect
└── requirements.txt # Dependencies
```

## License

MIT
