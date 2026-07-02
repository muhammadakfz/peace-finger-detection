def is_peace_gesture(hand_landmarks):
    """
    Detect peace finger gesture (index and middle fingers extended, others closed).

    Uses MediaPipe hand landmark positions to determine if the index and middle
    fingers are extended while ring and pinky fingers are closed.

    Landmark indices:
    - Thumb: 4 (tip), 2 (joint)
    - Index: 8 (tip), 6 (joint)
    - Middle: 12 (tip), 10 (joint)
    - Ring: 16 (tip), 14 (joint)
    - Pinky: 20 (tip), 18 (joint)
    """

    # Get landmark positions (hand_landmarks is a list of NormalizedLandmark in new API)
    landmarks = hand_landmarks

    # Index finger - tip should be above middle joint (extended)
    index_tip = landmarks[8].y
    index_pip = landmarks[6].y
    index_extended = index_tip < index_pip

    # Middle finger - tip should be above middle joint (extended)
    middle_tip = landmarks[12].y
    middle_pip = landmarks[10].y
    middle_extended = middle_tip < middle_pip

    # Ring finger - tip should be below or at middle joint (closed)
    ring_tip = landmarks[16].y
    ring_pip = landmarks[14].y
    ring_closed = ring_tip > ring_pip

    # Pinky finger - tip should be below or at middle joint (closed)
    pinky_tip = landmarks[20].y
    pinky_pip = landmarks[18].y
    pinky_closed = pinky_tip > pinky_pip

    # Peace gesture: index and middle extended, ring and pinky closed
    return index_extended and middle_extended and ring_closed and pinky_closed
