import cv2
import os

input_video_path = 'D:\\Produce.mp4'

cap = cv2.VideoCapture(input_video_path)
i = 0
cnt = 1

while(cap.isOpened()):
    ret, frame = cap.read()
    path = 'D:\\img'
    print(frame, ret)

    if ret and cnt%2==0:
        cv2.imshow("frame", frame)
        frame = cv2.resize(frame, (128,64), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(path , f'img{i}.jpg'), frame)
        i = i+1
        cnt += 1
    elif ret == 0:
        break
    else:
        cnt += 1
        

cap.release()
cv2.destroyAllWindows()