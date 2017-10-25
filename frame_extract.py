#extract frames from video
# pre-process equalise histograms for each color channel

import numpy
import imutils
import argparse
import os,sys
import cv2


def main(dir_path, vid_name):

    path = dir_path+"/"+vid_name
    exdir_path = dir_path + "/extracted_frames_test"
    counter = 0;
    cap = cv2.VideoCapture(path)

    if not os.path.exists(exdir_path):
        os.makedirs(exdir_path)
    else:
        print("Overwriting directory for extracted frames...")

    if cap.isOpened():
        print "opened video"
    # loop runs if capturing has been initialized.
    while True:
        # reads frames from a video
        ret, frames = cap.read()
        b,g,r = cv2.split(frames)
        b = cv2.equalizeHist(b)
        g = cv2.equalizeHist(g)
        r = cv2.equalizeHist(r)
        frames = cv2.merge((b,g,r))
        # cv2.imshow("eq",img)
        sizeX,sizeY,sizeD = frames.shape
        print frames.shape
        frames = frames[300:720-120,0:1280]
        sizeX,sizeY,sizeD = frames.shape
        # frameY, frameX, frameD = frames.shape
        # img = cv2.resize(frames, (frameX/2, frameY/2))
        cv2.imwrite(exdir_path + "/frame" + str(counter)+ ".jpg",frames)
        counter += 1
        if counter == 10:
            break
        cv2.imshow("hey",frames)
        if cv2.waitKey(33) == 27:
            break

    # De-allocate any associated memory usage
    cv2.destroyAllWindows()


dir_path = raw_input("Enter directory path : ")
vid_name = raw_input("Enter video name : ")
main(dir_path,vid_name)
# path = '/Users/ishani/Documents/MINI/Dataset_annotation/LabelImg/Chetan_vids/1/1.mp4'
