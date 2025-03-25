import cv2

# URL of the live stream
url = "http://192.168.222.1:81/stream"


# Open the video stream
cap = cv2.VideoCapture(url)

# Check if the video stream is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the video stream.")
    exit()

# Loop to read frames from the stream
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read frame from the video stream.")
        break

    # Display the frame
    cv2.imshow('Live Stream', frame)

    # Wait for a key press, if 'q' is pressed, exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()