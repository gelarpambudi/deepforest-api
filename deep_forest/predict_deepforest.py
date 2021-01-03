import numpy as np
import pandas as pd
import cv2 as cv
import os
from werkzeug.utils import secure_filename
from deepforest import deepforest
from deepforest import get_data
from app import app
from deep_forest import model

def predict(input_image):
    img_path = save_image(input_image)
    bounding_boxes = model.predict_tile(
                        raster_path=img_path, 
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

def save_image(img_file):
    filename = secure_filename(img_file.filename)
    img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return os.path.join(app.config['UPLOAD_FOLDER'], filename)
 