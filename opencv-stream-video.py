import os, sys, cv2 

print('''
    Python 3.6
    pip install opencv-python

    python opencv-stream-video.py {url}
    Basic認証url例：'http://user:pass@xxx.xxx.xxx.xxx:8080/?action=stream'

    s : 録画開始
    e : 録画終了
    q : 終了
''')

def save_stream_video(URL):
    s_video = cv2.VideoCapture(URL)
    # 幅
    width = int(s_video.get(3))
    # 高さ
    height = int(s_video.get(4))
    # fps
    fps = s_video.get(5)
    print('stream video propeties: {}x{} {}fps'.format(width, height, fps))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output.avi'),fourcc, fps, (width,height))
    savideo=False
    while True:
        ret, img = s_video.read()
        if ret==True:
            cv2.imshow("Stream Video",img)
            if savideo:
                img = cv2.resize(img, (width,height))
                out.write(img)
            key = cv2.waitKey(1) & 0xff
            # start save video
            if key == ord('s'):
                print("start save video...")
                savideo = True
                # write the flipped frame
            # end save video
            if key == ord('e'):
                print("end save video...")
                savideo = False
            # quit
            if key == ord('q'):
                print("end...")
                break
        else:
            print('oh...this break! we has some error')
            break
    out.release()
    s_video.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    # Stream Url設定
    if len(sys.argv) > 1:
        URL = sys.argv[1]
        save_stream_video(URL)
    else:
        print('引数不足.....')
