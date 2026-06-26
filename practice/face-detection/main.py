import os
from src.data_io import get_image_files, load_image, save_image
from src.preprocessing import resize_image
from src.detectors import HaarFaceDetector, YoloFaceDetector

DIR_RAW = os.path.join("data", "raw")
DIR_PREPROCESSED = os.path.join("data", "preprocessed")
DIR_RESULTS = os.path.join("data", "results")

PATH_HAAR = os.path.join("models", "haarcascade_frontalface_default.xml")
PATH_YOLO = os.path.join("models", "yolov8-face.pt")

def main():
    ### BEGIN


    ### END

if __name__ == "__main__":
    main()