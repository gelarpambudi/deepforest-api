import numpy as np
import pandas as pd
import cv2 as cv
from deepforest import deepforest
from deepforest import get_data
#from app import model

model = deepforest.deepforest()
model.use_release()

def predict(input_image):
    img = cv.imdecode(np.fromstring(input_image, np.uint8), cv.IMREAD_UNCHANGED)
    bounding_boxes = model.predict_tile(
                        image_path=img, 
                        show=False, 
                        return_plot = False,
                        patch_overlap=0.3, 
                        iou_threshold=0.2, 
                        patch_size=700
                    )
    return bounding_boxes

def get_center_coordinate(xmin, xmax, ymin, ymax):
    xcenter = (xmin + xmax) * 0.5
    y_center = (ymin + ymax) * 0.5
    return x_center, y_center

def add_to_df(x_center, y_center):
    return ...
 