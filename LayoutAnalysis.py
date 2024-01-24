import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO
import torch
from PIL import Image

weight_path = "best.pt"
model = YOLO(weight_path)

def extractParagraphsFromImage(image: np.ndarray):
    # image = np.array(image)
    paragraph_image = np.ones(image.shape)
    # fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # ax[0].imshow(image)
    # ax[0].set_title("OG Image")

    with torch.no_grad():
        predictions = model(image)

    for r in predictions:
        coords, labels = r.boxes.xyxy, r.boxes.cls
        num = len(coords)
        for i in range(num):
            x_min, y_min, x_max, y_max = coords[i]
            x_min, y_min, x_max, y_max = int(x_min.item()), int(y_min.item()), int(x_max.item()), int(y_max.item())
            if labels[i] == 0:
                paragraph_image[y_min:y_max, x_min:x_max] = image[y_min:y_max, x_min:x_max] / 255.0

    paragraph_image = (paragraph_image * 255).astype(np.uint8)
    return paragraph_image

def extractParagraphsFromPath(image_path: str):
    image = np.array(Image.open(image_path).convert('RGB'))
    paragraph_image = np.ones(image.shape)
    # fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # ax[0].imshow(image)
    # ax[0].set_title("OG Image")

    with torch.no_grad():
        predictions = model(image)

    for r in predictions:
        coords, labels = r.boxes.xyxy, r.boxes.cls
        num = len(coords)
        for i in range(num):
            x_min, y_min, x_max, y_max = coords[i]
            x_min, y_min, x_max, y_max = int(x_min.item()), int(y_min.item()), int(x_max.item()), int(y_max.item())
            if labels[i] == 0:
                paragraph_image[y_min:y_max, x_min:x_max] = image[y_min:y_max, x_min:x_max] / 255.0

    return paragraph_image

# clean_image = extractParagraphsFromImage('sample.png')
# plt.imshow(clean_image)
# plt.show()