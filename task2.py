import cv2

video1= cv2.VideoCapture("ChainsawMan.mp4")

fps=int(video1.get(cv2.CAP_PROP_FPS))

out=cv2.VideoWriter("CSM.avi",cv2.VideoWriter_fourcc('M','J','P','G'),fps,(int(video1.get(3)),int(video1.get(4))))

frame75=0.75*int(video1.get(cv2.CAP_PROP_FRAME_COUNT))
frameno=0
c=0
while(video1.isOpened()):
    ret,frame=video1.read()
    if ret == True:
        frameno+=1
        if (frameno>=frame75):
            c+=1
            out.write(frame)
    else:
        break

print(c)
video1.release()
out.release()
cv2.destroyAllWindows()