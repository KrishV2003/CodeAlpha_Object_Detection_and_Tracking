import cv2
import torch

# Load the YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Change 'yolov5s' to your model type

# Initialize webcam
cap = cv2.VideoCapture(0)

# Define video writer for saving the output
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('project_output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)  # Perform inference on the frame

    # Results contains the bounding boxes and class labels
    labels = results.names  # Object class names
    pred = results.pred[0]  # Bounding boxes and classes

    # Draw bounding boxes and labels
    for *box, conf, cls in pred:
        label = labels[int(cls)]  # Get the label
        conf = round(conf.item(), 2)  # Confidence score
        x1, y1, x2, y2 = [int(i) for i in box]  # Convert to int

        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display the label and confidence score
        cv2.putText(frame, f'{label} {conf}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Object Detection', frame)

    # Write frame to video file
    out.write(frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()  # Save the video output
cv2.destroyAllWindows()
