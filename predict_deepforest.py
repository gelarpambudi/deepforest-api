import numpy as np
import pandas as pd
from deepforest import deepforest
from deepforest import get_data
from app import model

def predict(input_image):
    bounding_boxes = model.predict_tile(
                        image_path=input_image, 
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

def 