import os
import cv2

#Path to images
path = "C:/Users/haiha/OneDrive/Desktop/python_code"
list_files = os.listdir(path)
images = []

for file in list_files:
    name,ext = os.path.splitext(file)

    if ext == "":
        continue

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+name
        print(file_name)
        images.append(file_name)


count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
#A tuple is used when you dont want the values inside a list to change
size = (width, height)
print(size)

out = cv2.VideoWriter("Project.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
#Adds the images to the video
for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)
out.release()
print("done")