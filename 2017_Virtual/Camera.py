#coding:UTF-8
import cv2

class Camera:

    #カメラから画像を取得
    def getimage(self,reheight,rewidth):
        #0番目のカメラから画像取得
        capture = cv2.VideoCapture(0)

        #デコード
        ret, image = capture.read()


        if ret == True:
            #画像の保存
            y, x, cannels= image.shape[:3]
            #サイズ変更
            image2 = image[200:y+reheight, 200:x+rewidth]
            cv2.imwrite("outimage.jpg", image)
            cv2.imwrite("outimage2.jpg", image2)
        else:
            print("写真を撮れていません")

        #デコード前の画像を返す
        return capture

cam=Camera()
cam.getimage(500,100)
