from ultralytics import YOLOv10
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

if __name__ == '__main__':

    model_s = YOLOv10('yolov10s.pt')

    model_l = YOLOv10("yolov10l.pt")



    model_s.train(data="coco128.yaml", distillation=model_l, Distillation_loss="cwd",amp=False )
