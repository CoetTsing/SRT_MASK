import paddlehub
import cv2
import os

module = paddlehub.Module(name="pyramidbox_lite_mobile_mask")  # 加载口罩人脸检测模型
capture = cv2.VideoCapture(0)  # 创建摄像头对象

while(True):

    successFlag, image = capture.read()  # 获取画面

    result = module.face_detection(images=[image],
                                   visualization=True,
                                   output_dir='detection_result')  # 是否佩戴口罩检测

    filename = (os.listdir("./detection_result/"))[0]  # 获取检测结果
    cv2.imshow('result', cv2.imread("./detection_result/" + filename))  # 展示结果
    os.remove("./detection_result/" + filename)  # 移除生成的文件

    if cv2.waitKey(3) & 0xff == 27:  # 按ESC键退出
        print("ESC")
        capture.release()  # 释放摄像头
        cv2.destroyAllWindows()  # 删除建立的窗口
        break
