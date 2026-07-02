import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:
    """
    MediaPipe-based hand detector with simplified interface.
    """

    def __init__(self,
                 max_hands=1,
                 detection_confidence=0.7,
                 tracking_confidence=0.5):
        """
        Initialize the hand detector.

        Args:
            max_hands: Maximum number of hands to detect
            detection_confidence: Minimum detection confidence (0-1)
            tracking_confidence: Minimum tracking confidence (0-1)
        """
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            min_hand_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
            running_mode=vision.RunningMode.VIDEO
        )
        self.detector = vision.HandLandmarker.create_from_options(options)

    def find_hands(self, frame, draw=True):
        """
        Detect hands in the given frame.

        Args:
            frame: BGR image from OpenCV
            draw: Whether to draw hand landmarks

        Returns:
            List of hand landmarks if hands detected, None otherwise
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Use detect_for_video for VIDEO mode (requires timestamp in ms)
        import time
        timestamp_ms = int(time.time() * 1000)
        results = self.detector.detect_for_video(mp_image, timestamp_ms)

        hands_data = None

        if results.hand_landmarks:
            hands_data = results.hand_landmarks
            if draw:
                self._draw_landmarks(frame, hands_data)

        return hands_data

    def _draw_landmarks(self, frame, hand_landmarks):
        """Draw hand landmarks and connections on the frame."""
        h, w = frame.shape[:2]

        # Landmark indices for hand connections
        connections = [
            (0, 1), (1, 2), (2, 3), (3, 4),  # Thumb
            (0, 5), (5, 6), (6, 7), (7, 8),  # Index
            (0, 9), (9, 10), (10, 11), (11, 12),  # Middle
            (0, 13), (13, 14), (14, 15), (15, 16),  # Ring
            (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky
            (5, 9), (9, 13), (13, 17)  # Palm
        ]

        for landmarks in hand_landmarks:
            # Draw connections
            for connection in connections:
                start = landmarks[connection[0]]
                end = landmarks[connection[1]]
                start_x, start_y = int(start.x * w), int(start.y * h)
                end_x, end_y = int(end.x * w), int(end.y * h)
                cv2.line(frame, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

            # Draw landmark points
            for landmark in landmarks:
                x, y = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

    def get_hand_count(self, frame):
        """
        Get the number of hands detected in the frame.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        import time
        timestamp_ms = int(time.time() * 1000)
        results = self.detector.detect_for_video(mp_image, timestamp_ms)

        if results.hand_landmarks:
            return len(results.hand_landmarks)
        return 0

    def close(self):
        """Release MediaPipe resources."""
        self.detector.close()
