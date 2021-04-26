import sys
import os

# Import classes
from Classes.CSVReader import CSVReader
from Classes.Converter import Converter
from Classes.Image import Image
from Classes.Box import Box
from Classes.CSVWriter import CSVWriter

# Import accuracy script for testing
from Scripts.missing_tooth import missing_tooth
from Tests.accuracy import accuracy
from Tests.accuracy3 import getMap
from Tests.metrics import percision_recall_class
from Tests.visualizer import visualizer
from Tests.precision_recall import precision_recall_iou, f1_iou, precision_recall_ious, f1_ious

# Import teeth arrangement script to correct teeth classification
from Scripts.teeth_arrangement import teeth_arrangements
#from Scripts.relabel import relabel
from Scripts.relabel import relabel

# File paths
project_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = project_dir + "/CS410_VideaHealth_sample_data"
img_folder = data_dir + "/images"
# file_gt = data_dir + "/OLD/1_ground_truth_2a.csv"
# file_pred = data_dir + "/OLD/2_input_model_predictions_2.csv"
file_gt = data_dir + "/1_ground_truth.csv"
file_pred = data_dir + "/2_input_model_predictions.csv"
file_bw_pa = data_dir + "/bw_pa.csv"

# Read the input CSV file
input_raw = CSVReader(file_pred, file_bw_pa).output
images_input = Converter(input_raw).result

# Import the ground truth data
gt_raw = CSVReader(file_gt).output
images_gt = Converter(gt_raw).result

# Specifically check if you want only Bitewing (BW) or Periapical ){PA)
images_input, images_gt = Converter.get_bw_pa(images_input, images_gt, want_bw=False)

iou_threshold = 0.70


# #Testing Without Filtering Detection
# print("\nRunning stats without any Filtering")
# #accuracy(images_input, images_gt)
# print('precision, recall = {}'.format(precision_recall_ious(images_input, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_input, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_input ,images_gt)))

############ Test post processing scripts
# print("\nTesting haehn script:")
# from Scripts.haehn import haehn
# images_pred = haehn(images_input)
# #teeth_arrangements(images_pred)
# #relabel(images_pred)
# accuracy(images_pred, images_gt)
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(accuracy3(images_pred,images_gt)))

# visualizer('haehn', images_pred, images_gt)

# print("\nTesting best_box script:")
# from Scripts.best_box import best_box
# images_pred = best_box(images_input)
# # teeth_arrangements(images_pred)
# #relabel(images_pred)
# #accuracy(images_pred, images_gt)
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))
# # visualizer('best_box', images_pred, images_gt)
# #relabel(images_pred)
# #accuracy(images_pred, images_gt)
# print("Best box after Stage 2")
# images_pred = teeth_arrangements(images_pred)
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))
# images_pred = missing_tooth(images_pred)
# print("Best box after Stage 3")
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))



print("\nTesting nms script:")
from Scripts.non_maximum_suppression import nonmaximum_suppression
images_pred = nonmaximum_suppression(images_input, threshold=0.3, iouThreshold=0.55)
metrics = percision_recall_class.calculate_percision_recall_curv(images_pred, images_gt)


accuracy(images_pred, images_gt)
print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
#getMap(images_pred, images_gt)
#print('mAP = {}'.format(getMap(images_pred, images_gt)))
#accuracy2(images_pred, images_gt)
# visualizer('nms', images_pred, images_gt)
images_pred = teeth_arrangements(images_pred)
print("nms after Stage 2")
print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
#getMap(images_pred, images_gt)
#print('mAP = {}'.format(getMap(images_pred, images_gt)))
images_pred = missing_tooth(images_pred)
print("nms after Stage 3")
print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
#getMap(images_pred, images_gt)
#print('mAP = {}'.format(getMap(images_pred, images_gt)))

# print("\nTesting best cluster haehn script:")
# from Scripts.best_cluster_haehn import best_cluster_haehn
# images_pred = best_cluster_haehn(images_input)
# # teeth_arrangements(images_pred)
# #relabel(images_pred)
# accuracy(images_pred, images_gt)
# #accuracy2(images_pred, images_gt)
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))
# #visualizer('nms', images_pred, images_gt)
# images_pred = teeth_arrangements(images_pred)
# print("best cluster haehn after Stage 2")
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))
# images_pred = missing_tooth(images_pred)
# print("best cluster haehn after Stage 3")
# print('precision, recall = {}'.format(precision_recall_ious(images_pred, images_gt, iou_threshold)))
# print('f1 = {}'.format(f1_ious(images_pred, images_gt, iou_threshold)))
# print('mAP = {}'.format(getMap(images_pred, images_gt)))


# Tony's Magic Number Code
# from Scripts.non_maximum_suppression import nonmaximum_suppression
#
# # print("\nTesting nms script:")
# for y in range(1, 101):
#     iouThreshold = y*0.01
#     for x in range(1, 101):
#         images_input = Converter(input_raw).result
#         scoreThreshold = x*0.01
#         print(iouThreshold, scoreThreshold)
#         images_pred = nonmaximum_suppression(images_input, scoreThreshold, iouThreshold)
#         # teeth_arrangements(images_pred)
#         NMSaccuracy(images_pred, images_gt)
#         # visualizer('nms', images_pred, images_gt)


# Looping Based upon

print()
