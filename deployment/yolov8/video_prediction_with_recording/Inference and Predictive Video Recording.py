# Import necessary libraries
import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
# NOTE: Replace the path below with the path to your YOLOv8 weights file
model = YOLO('<PATH_TO_YOUR_YOLOV8_WEIGHTS_FILE>')

# Open the video file for processing
# NOTE: Replace the path below with the path to your video file
video_path = '<PATH_TO_YOUR_VIDEO_FILE>'
cap = cv2.VideoCapture(video_path)

# Create a VideoWriter object to save the annotated video
# NOTE: Replace the path below with the desired path for your output video file
output_path = '<PATH_TO_YOUR_OUTPUT_VIDEO_FILE>'
video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), int(cap.get(5)), (int(cap.get(3)), int(cap.get(4))))

# Initialize a variable to count the number of processed frames
frame_count = 0

# Loop through each frame of the video
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    frame_count += 1  # Increment the frame count

    if success:
        # Perform object detection on the frame using the YOLOv8 model
        results = model(frame)

        # Visualize the detection results on the frame
        annotated_frame = results[0].plot()

        # Write the annotated frame to the output video
        video_writer.write(annotated_frame)

        # Display the annotated frame in a window
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Exit the loop if there are no more frames to read from the video
        break

# Close the video file and the output video file
cap.release()
video_writer.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
