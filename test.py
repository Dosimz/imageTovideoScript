import cv2

img_root = '/home/yuyi/Desktop/study/ObjectDetector/imageSet/'
fps = 10
#size = (1600,900)
size = (1024,1024)
#size = (1600,900)
#size = (800,448)

# fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vW = cv2.VideoWriter('/home/yuyi/Desktop/study/MeUtils/imageTovideo/test_10fps_bird.mp4', fourcc, fps, size)
def video_factory(n):
    for i in range(1, n):
        #frame = cv2.imread(img_root+str(i)+'generic.png')
        frame = cv2.imread(img_root+str(i)+'bird_pred.png')
        #frame = cv2.imread(img_root+str(i)+'bird_pred.png')
        #frame = cv2.imread(img_root+str(i)+'pc_pillar_2d_overlay.jpg')
        vW.write(frame)
    vW.release()

video_factory(485)
