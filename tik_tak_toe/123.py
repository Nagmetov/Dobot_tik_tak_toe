import cv2
image_path = '20240820_093751.png'
image = cv2.imread(image_path)

from ultralytics import YOLO
model = YOLO('best).pt')
import cv2
import matplotlib.pyplot as plt
results = model.predict(image)
# Convert the image from BGR to RGB format
annotated_img = results[0].plot()

# Convert BGR to RGB for matplotlib display
annotated_img_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)

# Display the image
plt.figure(figsize=(10, 10))
plt.imshow(annotated_img_rgb)
plt.axis('off')  # Hide the axis
plt.show()
