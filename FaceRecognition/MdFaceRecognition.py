import sys
sys.path.append("Models")
import cv2
import face_recognition
from MdEstudiante import MdEstudiante
class MdFaceRecognition():
    rostro: any
    vector: any
    objEstudiante: MdEstudiante

    def __init__(self, estudiante: MdEstudiante) -> None:
        self.objEstudiante = estudiante

    def CapturarRostro(self):
        capture = cv2.VideoCapture(0)
        clasificadorFace = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while capture.isOpened():
            confirm, frame = capture.read()
            if confirm == False: break
            grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = clasificadorFace.detectMultiScale(grayImg, 1.05, 8)
            order = cv2.waitKey(1)
            if order == 27:
                break
            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (128,0,255), 2)
                if order == ord('s'):
                    self.rostro = frame
                    self.GenerarVector()
                    isaa, foto = cv2.imencode(ext='.jpg',img=self.rostro)
                    self.objEstudiante.Foto = foto.tobytes()
                    self.objEstudiante.Vector = self.vector.tobytes()
                    capture.release
                    cv2.destroyAllWindows()
            cv2.rectangle(frame,(10,5),(450,25),(255,255,255),-1)
            cv2.putText(frame,'Presione s para almacenar el rostro encontrado',(10,20),2,0.5,(128,0,0),1)
            cv2.imshow('frame',frame)
        capture.release
        cv2.destroyAllWindows()

    def AnalizarImagen(self, pathName: str):
        image=cv2.imread(pathName)
        with open(pathName, 'rb') as frb:
            data = frb.read()
        face_loc = face_recognition.face_locations(image)
        if not(len(face_loc) <= 0):
            self.rostro = image
            self.GenerarVector()
            self.objEstudiante.Foto = data
            self.objEstudiante.Vector = self.vector.tobytes()
    
    def GenerarVector(self):
        try:
            face_loc = face_recognition.face_locations(self.rostro)[0]
            self.vector = face_recognition.face_encodings(self.rostro, known_face_locations=[face_loc])[0]

        except:
            pass
