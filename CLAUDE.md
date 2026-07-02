# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Real-time hand gesture detection project using MediaPipe. When "peace" finger gesture is detected, the hand area is blurred; otherwise, the video feed displays normally.

## Tech Stack

- **Language**: Python 3.9+
- **Detection**: MediaPipe Hands
- **Computer Vision**: OpenCV
- **Real-time**: Webcam capture with threading

## Quick Start

```bash
# Install dependencies
pip install opencv-python mediapipe numpy

# Run the application
python main.py
```

## Architecture

```
├── main.py          # Entry point, webcam capture loop
├── detector.py      # MediaPipe hand detection logic
├── gestures.py      # Peace finger gesture recognition
├── effects.py       # Blur effect implementation
└── CLAUDE.md        # This file
```

## Gesture Detection

Peace gesture = index and middle fingers extended up, other fingers closed.

## Running

Press `q` to quit the application.
