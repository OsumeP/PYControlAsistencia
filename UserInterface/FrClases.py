import sys

sys.path.append("Models")
sys.path.append("FaceRecognition")
from ttkbootstrap.constants import *
from MdDocente import MdDocente
import ttkbootstrap as ttk
from datetime import datetime
from ttkbootstrap.tableview import Tableview
from MdAsignatura import MdAsignatura
from MdFaceRecognition import MdFaceRecognition
from MdClase import MdClase
from MdAsistencia import MdAsistencia

class FrClases():

    root: ttk.Frame
    objMain: any
    Docente: MdDocente
    lbFecha: ttk.Label
    table: Tableview
    cbClases: ttk.Combobox
    raw_TS: datetime
    objAsignatura: MdAsignatura
    objReconocedor: MdFaceRecognition
    ids = []
    objClase = MdClase
    lsAsistencias: list[MdAsistencia]
    # region Constructores

    def __init__(self, objMain: any, IdUsuario) -> None:
        self.ObjMain = objMain
        self.Docente = MdDocente.ObtenerPorId(IdUsuario)
        self.CrearToolBar()

    # endregion

    # region Funciones

    def CrearToolBar(self)->None:
        self.root = ttk.Frame(self.ObjMain.nbTabControl)
        self.ObjMain.nbTabControl.add(self.root, text='Administración de Clases')
        lbTitulo = ttk.Label(self.root, text="Administración de Clases",font=('Helvetica', 18), bootstyle="success")
        lbTitulo.grid(row=0, column=0, columnspan=3, pady=5)
        wdButton = int((self.root.winfo_screenwidth() - 120) / 6 /4)
        self.cbClases = ttk.Combobox(self.root, values=self.Docente.ObtenerNombresAsignaturas(), bootstyle="success", width=wdButton,  state="readonly")
        self.cbClases.current(0)
        self.cbClases.grid(row=1, column=0, padx=15, pady=5)
        self.lbFecha = ttk.Label(self.root, text="", font=('Helvetica', 15), bootstyle="success", width=wdButton, anchor="center")
        self.lbFecha.grid(row=1, column=1, padx=15, pady=5)
        btnIniciarClase = ttk.Button(self.root, text="Iniciar Clase", bootstyle="success", width=wdButton, command=self.onBtnIniciar_onClick)
        btnIniciarClase.grid(row=1, column=2, padx=15, pady=5)
        self.ActualizarHora()
        self.DibujarTabla([])

    def CargarDatos(self) -> None:
        self.ids = []
        vectores = []
        nombres= []
        for i in self.objAsignatura.Estudiantes:
            estudiante = i.Estudiante
            nombres.append(estudiante.PrimerNombre + " " + estudiante.PrimerApellido)
            estudiante.CargarVector()
            vectores.append(estudiante.Vector)
            self.ids.append(estudiante.Id)
        self.objReconocedor = MdFaceRecognition(Vectores=vectores, Nombres=nombres)
    
    def LlenarTabla(self) -> list[list]:
        nwAsistencia = MdAsistencia.ObtenerPorClase(self.objClase.Id)
        rowdata = []
        for i in nwAsistencia:
            estudiante = i.Estudiante
            if i.Asistencia == 0:
                i.Asistencia = False
            else:
                i.Asistencia = True
            rowdata.append([estudiante.Id, estudiante.Documento, estudiante.PrimerNombre, estudiante.SegundoNombre, estudiante.PrimerApellido, estudiante.SegundoApellido, i.Asistencia])
        return rowdata

    def DibujarTabla(self, rowdata: list):
        wdButton = int((self.root.winfo_screenwidth() - 20) / 7)
        coldata = [
            {"text": "Id", "stretch": False, "width":wdButton},
            {"text": "Documento", "stretch": False, "width":wdButton},
            {"text": "PrimerNombre", "stretch": False, "width":wdButton},
            {"text": "SegundoNombre", "stretch": False, "width":wdButton},
            {"text": "PrimerApellido", "stretch": False, "width":wdButton},
            {"text": "SegundoApellido", "stretch": False, "width":wdButton},
            {"text": "Asistencia", "stretch": False, "width":wdButton}
        ]
        self.table = Tableview(self.root, paginated=True, searchable=True, rowdata=rowdata, pagesize=40, height=30, bootstyle=PRIMARY,coldata=coldata)
        self.table.grid(row=2, column=0, columnspan=3, sticky="we")

    def ActualizarDatos(self) -> None:
        rowdata = self.LlenarTabla()
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()

    def GenerarRegistros(self):
        self.CargarDatos()
        self.objClase = MdClase(self.Docente, self.objAsignatura, self.raw_TS)
        self.objClase.InsertarRegistro()
        self.objClase.RefrescarId()
        asistencia = MdAsistencia(self.objClase)
        asistencia.GenerarRegistrosClase(self.ids)
        self.listaAsistencia = MdAsistencia.ObtenerPorClase(self.objClase.Id)
        self.objReconocedor.lsAsistencia = self.listaAsistencia
        self.objReconocedor.ReconocimientoFacial()
        self.objClase.FechaFinal = self.raw_TS.strftime('%Y-%m-%d %H:%M:%S')
        self.objClase.ActualizarRegistro()
        self.ActualizarDatos()

    def ActualizarHora(self):
        self.raw_TS = datetime.now()
        date_now = self.raw_TS.strftime("%d/%m/%Y, %H:%M:%S")
        self.lbFecha.config(text=date_now)
        self.lbFecha.after(1000, self.ActualizarHora)

    #endregion

    #region Eventos
    def onBtnIniciar_onClick(self):
        self.objAsignatura = MdAsignatura.ObtenerPorNombre(self.cbClases.get())
        self.objAsignatura.CargarEstudiantes()
        self.GenerarRegistros()


    #endregion