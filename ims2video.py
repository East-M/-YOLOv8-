import os
import cv2

# 路径位置定义
im_path = os.path.join("datasets\\CamouflagedTarget\\predict")
video_path = os.path.join("datasets\\CamouflagedTarget","video_predict.mp4")

# 获取图片文件夹
imDir = os.listdir(im_path)

# 视频的相关参数
fps = 30
fourcc = cv2.VideoWriter.fourcc('m','p','4','v')
height, width = (325, 850)

# 创建视频写入器对象
Video = cv2.VideoWriter(video_path, fourcc, fps, (width,height))

for im in imDir:
    path = os.path.join(im_path, im)
    frame =  cv2.imread(path)
    Video.write(frame)
    
Video.release()

print("done!")