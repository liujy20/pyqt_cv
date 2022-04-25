import argparse
import cv2
i = 0
j = 1

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str)
opt = parser.parse_args()

# ��Ƶ�ļ������ʼ��
filename = opt.filename
camera = cv2.VideoCapture(filename)

# ��Ƶ�ļ������������
out_fps = 24.0  # ����ļ���֡��
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out1 = cv2.VideoWriter('./out1.mp4', fourcc, out_fps, (500, 320))
out2 = cv2.VideoWriter('./out2.mp4', fourcc, out_fps, (500, 320))

# ��ʼ����ǰ֡��ǰ��֡
lastFrame1 = None
lastFrame2 = None

# ������Ƶ��ÿһ֡
while camera.isOpened():

    # ��ȡ��һ֡
    (ret, frame) = camera.read()

    # �������ץȡ��һ֡��˵�����ǵ�����Ƶ�Ľ�β
    if not ret:
        break

    # ������֡�Ĵ�С
    frame = cv2.resize(frame, (500, 400), interpolation=cv2.INTER_CUBIC)

    frame = frame[0:320, 0:500]

    # �����һ��֡��None��������г�ʼ��,�����һ��֡�Ĳ�ͬ
    if lastFrame2 is None:
        if lastFrame1 is None:
            lastFrame1 = frame
        else:
            lastFrame2 = frame
            global frameDelta1  # ȫ�ֱ���
            frameDelta1 = cv2.absdiff(lastFrame1, lastFrame2)  # ֡��һ
        continue

    # ���㵱ǰ֡��ǰ֡�Ĳ�ͬ,������֡���
    frameDelta2 = cv2.absdiff(lastFrame2, frame)  # ֡���
    thresh = cv2.bitwise_and(frameDelta1, frameDelta2)  # ͼ��������
    thresh2 = thresh.copy()

    # ��ǰ֡��Ϊ��һ֡��ǰ֡,ǰ֡��Ϊ��һ֡��ǰǰ֡,֡�����Ϊ֡��һ
    lastFrame1 = lastFrame2
    lastFrame2 = frame.copy()
    frameDelta1 = frameDelta2

    # ���תΪ�Ҷ�ͼ
    thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)

    # ͼ���ֵ��
    thresh = cv2.threshold(thresh, 25, 255, cv2.THRESH_BINARY)[1]

    # ȥ��ͼ������,�ȸ�ʴ������(��̬ѧ������)
    thresh = cv2.dilate(thresh, None, iterations=3)
    thresh = cv2.erode(thresh, None, iterations=1)

    # ��ֵͼ���ϵ�����λ��
    cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    flag = 0

    frameOut = frame.copy()
    cv2.imshow("frame1", frameOut)

    # ��������
    for c in cnts:

        # ����С�������ų����
        if cv2.contourArea(c) < 300:
            continue

        # ���������ı߽���ڵ�ǰ֡�л����ÿ�
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        flag = 1

    # ��ʾ��ǰ֡
    cv2.imshow("frame", frame)
    cv2.imshow("thresh", thresh)
    cv2.imshow("threst2", thresh2)

    # ������Ƶ
    out1.write(frame)
    out2.write(thresh2)

    cv2.imshow("frame2", frameOut)

    # ����ͼƬ
    i += 1
    if i % 3 == 0 and flag == 1:
        cv2.imwrite('./images/frame' + str(j) + '.jpg', frameOut)
        j += 1

    # ���q�������£�����ѭ��
    if cv2.waitKey(200) & 0xFF == ord('q'):
        break

# ������Դ���رմ򿪵Ĵ���
out1.release()
out2.release()
camera.release()
cv2.destroyAllWindows()