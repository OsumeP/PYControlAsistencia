import sys
sys.path.append("Models")
import cv2
import face_recognition
from MdEstudiante import MdEstudiante
class MdFaceRecognition():
    rostro: any
    vector: any
    objEstudiante: MdEstudiante
    listaVector: list
    listaNombre: list
    lsAsistencia: list[any]

    def __init__(self, estudiante: MdEstudiante = None, Vectores: list = None, Nombres: list = None) -> None:
        if estudiante != None:
            self.objEstudiante = estudiante
        else:
            self.listaVector = Vectores
            self.listaNombre = Nombres
            pass

    def CapturarRostro(self):
        capture = cv2.VideoCapture(0)
        clasificadorFace = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        while capture.isOpened():
            confirm, frame = capture.read()
            if confirm == False: break
            grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = clasificadorFace.detectMultiScale(grayImg, 1.1, 8)
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
                    capture.release()
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
    
    def ReconocimientoFacial(self):
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, frame = cap.read()
            if ret == False: break
            orig = frame.copy()
            faces = faceClassif.detectMultiScale(frame, 1.1, 8)

            for (x, y, w, h) in faces:
                face = orig[y: y+h, x:x+w]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                actualFaceEncoding = face_recognition.face_encodings(face, known_face_locations=[(0,w,h,0)])[0]
                result = face_recognition.compare_faces(self.listaVector, actualFaceEncoding, 0.4)
                if True in result:
                    index = result.index(True)
                    name = self.listaNombre[index]
                    self.lsAsistencia[index].ActualizarRegistro()
                    self.lsAsistencia.pop(index)
                    self.listaVector.pop(index)
                    self.listaNombre.pop(index)
                    color = (125, 220, 0)
                else:
                    name = "Desconocido"
                    color = (50, 50, 255)

                cv2.rectangle(frame, (x,y+h), (x + w, y + h + 30), color, 2)
                cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2)
                cv2.putText(frame,name,(x, y + h + 25), 2, 1, (255, 255, 255), 2, lineType=cv2.LINE_AA)
            cv2.imshow("Frame", frame)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()
