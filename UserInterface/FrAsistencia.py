import sys
sys.path.append("Models")
from MdAsistencia import MdAsistencia
from MdEstudiante import MdEstudiante
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarMensaje, CentrarPantalla
from EnEnum import EnTipoDocumento
from MdDocente import MdDocente
from MdAsignatura import MdAsignatura

class FrAsistencia():

    # region Propiedades

    root : ttk.Frame
    ObjMain: any
    table: Tableview
    objEstudiante: MdEstudiante
    # endregion

    # region Constructores

    def __init__(self, idUser: int, objMain: any) -> None:
        self.ObjMain = objMain
        self.objEstudiante = MdEstudiante.ObtenerPorId(idUser)
        self.CrearToolBar()
        self.MostrarLista(self.CargarDatos())

    # endregion

    # region Funciones

    def CrearToolBar(self)->None:
        self.root = ttk.Frame(self.ObjMain.nbTabControl)
        self.ObjMain.nbTabControl.add(self.root, text='Consulta de Asistencias')
        lbTitulo = ttk.Label(self.root, text="Consulta de Asistencias",font=('Helvetica', 18), bootstyle="success")
        lbTitulo.grid(row=0, column=0, pady=5)

    def CargarDatos(self) -> list[list]:
        listaAsistencia = MdAsistencia.ObtenerDatosPorEstudiante(self.objEstudiante.Id)
        rowdata = []
        for i in listaAsistencia:
            if i.Asistencia == 0:
                i.Asistencia = False
            else:
                i.Asistencia = True
            Docente = MdDocente.ObtenerPorId(i.Id_Docente)
            rowdata.append([MdAsignatura.ObtenerPorId(i.Id_Asignatura).Nombre, Docente.PrimerNombre + Docente.SegundoNombre, i.FechaInicio, i.FechaFinal, i.Asistencia])
        return rowdata

    def MostrarLista(self, rowdata: list[tuple]):
        wdButton = int((self.root.winfo_screenwidth() - 20) / 5)
        coldata = [
            {"text": "Asignatura", "stretch": False, "width":wdButton},
            {"text": "Docente", "stretch": False, "width":wdButton},
            {"text": "FechaInicio", "stretch": False, "width":wdButton},
            {"text": "FechaCierre", "stretch": False, "width":wdButton},
            {"text": "Asistencia", "stretch": False, "width":wdButton},
        ]

        self.table = Tableview(master=self.root,paginated=True, searchable=True, rowdata=rowdata,pagesize=50, height=30, bootstyle=PRIMARY,coldata=coldata)
        self.table.grid(row=1, column=0, sticky="we")

    def ActualizarDatos(self) -> None:
        rowdata = self.CargarDatos()
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()
    #endregion