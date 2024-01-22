
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh

centers = []
colors = []
radii = []

centers_2 = []
colors_2 = []
radii_2 = []


video = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    with mp_face_mesh.FaceMesh(
        max_num_faces=3,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as face:

        while(True):
            ret, frame =  video.read()
            
            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame)
            results_face = face.process(frame)
        
    
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if not results.multi_hand_landmarks:
                pass
            else:
                for hand_landmarks in results.multi_hand_landmarks:
                    for landmark in hand_landmarks.landmark:
                        x = int(landmark.x*frame.shape[1])
                        y = int(landmark.y*frame.shape[0])
                        z = int(landmark.z*frame.shape[0])
                        radius = int(abs(z/2) + 1)
                        center = (x,y)
                        rgb_color = (255-x,255-y, 255+z)
                        centers.append(center)
                        colors.append(rgb_color)
                        radii.append(radius)
                        if len(centers) > 100:
                                centers.pop(0)
                                colors.pop(0)
                                radii.pop(0)
                        for i in range(len(centers)):
                            cv2.circle(frame, centers[i], radii[i] , colors[i], 1)
                            if len(centers) > 2:
                                cv2.line(frame, centers[0], centers[-1], colors[i], 1)
            if not results_face.multi_face_landmarks:
                pass
            else:
                for face_landmarks in results_face.multi_face_landmarks:
                    for landmark in face_landmarks.landmark:
                        x = int(landmark.x*frame.shape[1])
                        y = int(landmark.y*frame.shape[0])
                        z = int(landmark.z*frame.shape[0])
                        radius_1 = int(abs(z/2) + 1)
                        center_1 = (x,y)
                        rgb_color_1 = (255-x,255-y, 255+z)
                        centers_2.append(center_1)
                        colors_2.append(rgb_color_1)
                        radii_2.append(radius_1)
                        if len(centers_2) > 100:
                                centers_2.pop(0)
                                colors_2.pop(0)
                                radii_2.pop(0)
                        for i in range(len(centers_2)):
                            cv2.circle(frame, centers_2[i], int((x+y)/100), colors_2[i], 1)
                scalar = 2    
                win_width = int(frame.shape[0] * scalar)
                win_height = int(frame.shape[1] * scalar)
                cv2.namedWindow('hand_drawing', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('hand_drawing', win_width, win_height)
                cv2.imshow('hand_drawing', (cv2.flip(frame, 1)))

                if cv2.waitKey(5) & 0xFF == ord('q'):
                    break
    
video.release()

cv2.destroyAllWindows()




