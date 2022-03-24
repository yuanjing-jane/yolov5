# coding=utf-8
import cv2
import os
import threading
from threading import Lock, Thread
from pathlib import Path

video_path = r"/mnt/d/work/project/project_fish/data/video"
pic_path = r"/mnt/d/work/project/project_fish/data/pic"
filelist = os.listdir(video_path)  # 返回指定的文件夹下包含的文件或文件夹名字的列表，这个列表按字母顺序排序。


def video2pic(filename):
    # print(filename)
    cnt = 0
    dnt = 0
    if os.path.exists(pic_path + str(filename)):
        pass
    else:
        os.mkdir(pic_path + str(filename))
    cap = cv2.VideoCapture(str(Path(video_path) / str(filename)))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 读入视频
    while True:
        # get a frame
        ret, image = cap.read()
        if image is None:
            break
        # show a frame

        w = image.shape[1]
        h = image.shape[0]
        cv2.imencode('.jpg', image)[1].tofile(pic_path + str(filename) + '/' + str(dnt) + '222222.jpg')
        print(pic_path + str(filename) + '/' + str(dnt) + '.jpg')
        dnt = dnt + 1
        if (cnt % 20) == 0: # 每隔20帧存储一次
            cv2.imencode('.jpg', image)[1].tofile(pic_path + str(filename) + '/' + str(dnt) + '.jpg')
            # cv2.imwrite('C:/Users/JiangHuiQi/Desktop/pic/' + str(filename) + '/' + str(dnt) + '.jpg', image) #含中文路径，不可行
            print(pic_path + str(filename) + '/' + str(dnt) + '.jpg')
            dnt = dnt + 1
            # cv2.namedWindow('sliding_slice',0)
            # cv2.imshow('image', image)
            # cv2.waitKey(1000)
        cnt = cnt + 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # cnt = cnt + 1
        # # # if cv2.waitKey(1) & 0xFF == ord('q'):
        # # #     break
        # ch = cv2.waitKey(1)
        # if ch == 27 or ch == ord("q") or ch == ord("Q"):
        #     break
    cap.release()


if __name__ == '__main__':
    for filename in filelist:
        threading.Thread(target=video2pic, args=(filename,)).start()