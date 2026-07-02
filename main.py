import cv2
from detector import HandDetector
from effects import apply_blur
from gestures import is_peace_gesture

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Initialize hand detector
detector = HandDetector(
    max_hands=2,
    detection_confidence=0.6,
    tracking_confidence=0.5
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame horizontally for selfie view
    frame = cv2.flip(frame, 1)

    # Detect hands (no drawing)
    hands = detector.find_hands(frame, draw=False)

    if hands:
        for hand_landmarks in hands:
            if is_peace_gesture(hand_landmarks):
                frame = apply_blur(frame, hand_landmarks, frame.shape)
                break  # Only need one peace gesture

    # Show frame
    cv2.imshow("Peace Finger Detection", frame)

    # Quit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
detector.close()
