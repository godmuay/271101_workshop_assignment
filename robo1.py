#Call hand pipe line module
import cv2
import mediapipe as mp
import numpy as np
import math
mpHands = mp.solutions.hands
hands = mpHands.Hands()
cap = cv2.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils

arr = np.zeros((21, 2))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    Rcount, Lcount = 0, 0
    HRcheck, HLcheck = [], []
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                arr[id] = [cx, -cy]
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            if np.cross(np.subtract(arr[5], arr[0]), np.subtract(arr[17], arr[5])) > 0: 
                x0, y0 = np.subtract(arr[9], arr[5])
                x1, y1 = np.subtract(arr[20], arr[0])                
                x2, y2 = np.subtract(arr[16], arr[0])
                x3, y3 = np.subtract(arr[12], arr[0])
                x4, y4 = np.subtract(arr[8], arr[0])
                x5, y5 = np.subtract(arr[4], arr[17])
                z0, z1, z2, z3, z4, z5 = math.sqrt(pow(x0, 2) + pow(y0, 2)), math.sqrt(pow(x1, 2) + pow(y1, 2)), math.sqrt(pow(x2, 2) + pow(y2, 2)), math.sqrt(pow(x3, 2) + pow(y3, 2)), math.sqrt(pow(x4, 2) + pow(y4, 2)), math.sqrt(pow(x5, 2) + pow(y5, 2))
                HR = [z1, z2, z3, z4,z5]
                HRcheck = [0, 0, 0, 0, 0]
                HRcount = [0, 0, 0, 0, 0]
                for i in range(len(HR)) :
                    if z0 != 0 and HR[i]/z0*10 > 40:
                        HRcheck[i] = 5-i
                        HRcount[i] = 1
                    else :
                        HRcheck[i] = 0
                        HRcount[i] = 0
                
                Rcount = sum(HRcount)
                #print ("Right {} count={}".format(HRcheck,Rcount))
            else : 
                x0, y0 = np.subtract(arr[9], arr[5])
                x1, y1 = np.subtract(arr[20], arr[0])                
                x2, y2 = np.subtract(arr[16], arr[0])
                x3, y3 = np.subtract(arr[12], arr[0])
                x4, y4 = np.subtract(arr[8], arr[0])
                x5, y5 = np.subtract(arr[4], arr[17])
                z0, z1, z2, z3, z4, z5 = math.sqrt(pow(x0, 2) + pow(y0, 2)), math.sqrt(pow(x1, 2) + pow(y1, 2)), math.sqrt(pow(x2, 2) + pow(y2, 2)), math.sqrt(pow(x3, 2) + pow(y3, 2)), math.sqrt(pow(x4, 2) + pow(y4, 2)), math.sqrt(pow(x5, 2) + pow(y5, 2))
                HL = [z1, z2, z3, z4,z5]
                HLcheck = [0, 0, 0, 0, 0]
                HLcount = [0, 0, 0, 0, 0]
                for i in range(len(HL)) :
                    if z0 != 0 and  HL[i]/z0*10 > 40 :
                        HLcheck[i] = 5-i
                        HLcount[i] = 1
                    else :
                        HLcheck[i] = 0
                        HLcount[i] = 0
                
                Lcount = sum(HLcount)
                #print ("Left {} count={}".format(HLcheck,Lcount))
    cv2.putText(img,"Finger : ", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (104, 99, 247), 3)
    cv2.putText(img, str("Right :") , (40, 70), cv2.FONT_HERSHEY_PLAIN, 1.5, (126, 191, 252 ), 2)
    cv2.putText(img, str("Left :") , (40, 100), cv2.FONT_HERSHEY_PLAIN, 1.5, (126, 191, 252), 2)
    if (len(HRcheck) != 0) | (len(HLcheck) != 0):
        cv2.putText(img, str((Rcount + Lcount)), (150, 40), cv2.FONT_HERSHEY_PLAIN, 2, (104, 99, 247), 3)
        cv2.putText(img, str(HLcheck), (120, 100), cv2.FONT_HERSHEY_PLAIN, 1.25, (126, 191, 252 ), 2)
        cv2.putText(img, str(HRcheck), (130, 70), cv2.FONT_HERSHEY_PLAIN, 1.25, (126, 191, 252 ), 2)
    else:
        cv2.putText(img, "None", (130, 92), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
        cv2.putText(img, f"{str((Rcount + Lcount))}", (150, 40), cv2.FONT_HERSHEY_PLAIN, 2, (57, 130, 247), 3)
    #cv2.putText(img, str((Rcount)), (30, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3) #ขนาด ,(B, G, R),ความหนา
    #cv2.putText(img, str((Lcount)), (600, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    #cv2.putText(img,"Finger : ", (10, 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    #cv2.putText(img, str(HLcheck), (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
#Closeing all open windows
#Call hand pipe line module
import cv2
import mediapipe as mp
import numpy as np
import math
mpHands = mp.solutions.hands
hands = mpHands.Hands()
cap = cv2.VideoCapture(0)
mpDraw = mp.solutions.drawing_utils

arr = np.zeros((21, 2))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                arr[id] = [cx, -cy]
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            if np.cross(np.subtract(arr[5], arr[0]), np.subtract(arr[17], arr[5])) > 0: 
                x0, y0 = np.subtract(arr[9], arr[5])
                x1, y1 = np.subtract(arr[20], arr[0])                
                x2, y2 = np.subtract(arr[16], arr[0])
                x3, y3 = np.subtract(arr[12], arr[0])
                x4, y4 = np.subtract(arr[8], arr[0])
                x5, y5 = np.subtract(arr[4], arr[0])
                z0, z1, z2, z3, z4, z5 = math.sqrt(pow(x0, 2) + pow(y0, 2)), math.sqrt(pow(x1, 2) + pow(y1, 2)), math.sqrt(pow(x2, 2) + pow(y2, 2)), math.sqrt(pow(x3, 2) + pow(y3, 2)), math.sqrt(pow(x4, 2) + pow(y4, 2)), math.sqrt(pow(x5, 2) + pow(y5, 2))
                HR = [z1, z2, z3, z4,z5]
                HRcheck = [0, 0, 0, 0, 0]
                HRcount = [0, 0, 0, 0, 0]
                for i in range(len(HR)) :
                    if z0 != 0 and HR[i]/z0*10 > 40:
                        HRcheck[i] = 5-i
                        HRcount[i] = 1
                    else :
                        HRcheck[i] = 0
                        HRcount[i] = 0
                
                Rcount = sum(HRcount)
                print ("Right {} count={}".format(HRcheck,Rcount))
            else : 
                x0, y0 = np.subtract(arr[9], arr[5])
                x1, y1 = np.subtract(arr[20], arr[0])                
                x2, y2 = np.subtract(arr[16], arr[0])
                x3, y3 = np.subtract(arr[12], arr[0])
                x4, y4 = np.subtract(arr[8], arr[0])
                x5, y5 = np.subtract(arr[4], arr[0])
                z0, z1, z2, z3, z4, z5 = math.sqrt(pow(x0, 2) + pow(y0, 2)), math.sqrt(pow(x1, 2) + pow(y1, 2)), math.sqrt(pow(x2, 2) + pow(y2, 2)), math.sqrt(pow(x3, 2) + pow(y3, 2)), math.sqrt(pow(x4, 2) + pow(y4, 2)), math.sqrt(pow(x5, 2) + pow(y5, 2))
                HL = [z1, z2, z3, z4,z5]
                HLcheck = [0, 0, 0, 0, 0]
                HLcount = [0, 0, 0, 0, 0]
                for i in range(len(HL)) :
                    if z0 != 0 and  HL[i]/z0*10 > 40 :
                        HLcheck[i] = 5-i
                        HLcount[i] = 1
                    else :
                        HLcheck[i] = 0
                        HLcount[i] = 0
                
                Lcount = sum(HLcount)
                print ("Left {} count={}".format(HLcheck,Lcount))
    
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()