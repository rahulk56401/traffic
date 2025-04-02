import cv2
import torch
from traffic_system import TrafficSystem, Vehicle


# Initialize the traffic system
traffic_system = TrafficSystem()

# Inside the while loop, after performing inference
vehicle_count = 0
for result in results.xyxy[0]:  # Iterate over detected objects
    if result[5] == 2:  # Assuming class 2 is for vehicles (check your model's class mapping)
        vehicle_count += 1
        # Create a Vehicle object and add it to the traffic system
        vehicle = Vehicle(id=f"Vehicle_{vehicle_count}", type="Car", speed=0, current_route=[])
        traffic_system.add_vehicle(vehicle)

print(f"Total Vehicles Detected: {vehicle_count}")





# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # You can use a different model if needed

# Start video capture (0 for webcam, or replace with your camera URL)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Render results on the frame
    results.render()  # This modifies the frame in place

    # Display the frame
    cv2.imshow('Traffic Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()