import os
import cv2
from ultralytics import YOLO

class HaarFaceDetector:
    def __init__(self, xml_path):
        
        self.detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_and_draw(self, img):
        ### BEGIN


        ### END


class YoloFaceDetector:
    def __init__(self, model_path):
        ### BEGIN


        ### END

    def detect_and_draw(self, img):
        ### BEGIN


        ### END