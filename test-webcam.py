# Quick smoke test: run YOLO26n on the default webcam and show annotated frames.
from ultralytics import YOLO
import cv2

# Load the pretrained YOLO26n model (auto-downloads ~5 MB on first run).
model = YOLO("yolo26n.pt")

# Open the default webcam (device index 0).
video_cap = cv2.VideoCapture(0)

while True:
    # Grab a frame; ok is False if the camera fails or disconnects.
    ok, frame = video_cap.read()
    if not ok:
        break

    # Run inference on the frame (verbose=False silences per-frame console output).
    results = model(frame, verbose=False)

    # Draw detections on the frame and display it in a window.
    cv2.imshow("YOLO26n test - press q to quit", results[0].plot())

    # Poll the keyboard for 1 ms; exit if the user presses 'q'.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and close the preview window.
video_cap.release()
cv2.destroyAllWindows()