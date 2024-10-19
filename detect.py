from ultralytics import YOLOv10

from ultralytics import YOLOv10
import cv2


model = YOLOv10(r"F:\yolov10\runs\detect\train13\weights\last.pt")
results = model(r'F:\yolov10\ultralytics\assets\bus.jpg')

# 保存预测结果为图像文件
img = results[0].plot()
cv2.imwrite('predicted_image.jpg', img)
# results = model(r'F:\yolov10\ultralytics\assets\bus.jpg')
# model.predict()