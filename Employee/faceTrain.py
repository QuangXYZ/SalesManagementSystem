import cv2
import os
from PIL import Image
import numpy as np
import pickle


class faceTrain:

    def __init__(self, base_dir) -> None:

        # BASE_DIR =  os.path.dirname(os.path.abspath("E:\Python\SalesManagementSystem - Copy\Images\Face_customer"))
        self.__image_dir = base_dir
        self.__current_id = 0
        self.__label_ids = {}
        self.__x_train = []
        self.__y_label = []
        self.__recognition = cv2.face.LBPHFaceRecognizer_create()
        self.__face_cascade = cv2.CascadeClassifier(
            '.\Employee\cascade\data\haarcascade_frontalface_default.xml')

    def trainning(self):
        for root, dirs, files in os.walk(self.__image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(" ", "-").upper()
                    print(path, label)

                    if not label in self.__label_ids:
                        self.__label_ids[label] = self.__current_id
                        self.__current_id += 1

                    id_ = self.__label_ids[label]
                    print(self.__label_ids)
                    # y_label.append(label)
                    # x_train.append(path)
                    pil_image = Image.open(path).convert("L")
                    print(pil_image)
                    image_array = np.array(pil_image, "uint8")
                    print(image_array)
                    faces = self.__face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi = image_array[y:y + h, x:x + w]
                        self.__x_train.append(roi)
                        self.__y_label.append(id_)

        self.__save()

    def __save(self):
        with open("label.pickle", 'wb') as f:
            pickle.dump(self.__label_ids, f)

        self.__recognition.train(self.__x_train, np.array(self.__y_label))
        self.__recognition.save("trainner.yml")

    # print(y_label)
    # print(x_train)