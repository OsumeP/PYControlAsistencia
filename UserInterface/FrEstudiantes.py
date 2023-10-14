import sys
sys.path.append("Models")
from MdAsignatura import MdAsignatura
from MdEstudiante import MdEstudiante
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarPantalla
from ttkbootstrap.dialogs import Messagebox
from FrEstudiantesEditor import FrEstudiantesEditor
from EnEnum import EnTipoDocumento

class FrEstudiantes():

    # region Propiedades

    root : ttk.Frame
    ObjMain: any
    table: Tableview

    # endregion

    # region Constructores

    def __init__(self, objMain: any) -> None:
        self.ObjMain = objMain
        self.CrearToolBar()
        self.MostrarLista(self.CargarDatos())

    # endregion

    # region Funciones

    def CrearToolBar(self)->None:
        self.root = ttk.Frame(self.ObjMain.nbTabControl)
        self.ObjMain.nbTabControl.add(self.root, text='Administración de Estudiantes')
        btnAgregar = ttk.Button(self.root,text="Agregar", bootstyle='success', command=self.onBtnAgregarRegistro_onClick)
        btnAgregar.grid(row=0, column=0)
        btnEditar = ttk.Button(self.root,text="Editar", bootstyle='success', command=self.onBtnEditarRegistro_onClick)
        btnEditar.grid(row=0, column=1)
        btnEliminar = ttk.Button(self.root,text="Eliminar", bootstyle='success', command=self.onBtnEliminarRegistro_onClick)
        btnEliminar.grid(row=0, column=2)

    def CargarDatos(self) -> list[list]:
        listaAsignaturas = MdEstudiante.ObtenerTodos()
        rowdata = []
        for i in listaAsignaturas:
            rowdata.append([i.Id, i.ObtenerTipoDocumentoStr(), i.Documento, i.PrimerNombre, i.SegundoNombre, i.PrimerApellido, i.SegundoApellido, i.Email, i.NumeroCarne])
        return rowdata

    def MostrarLista(self, rowdata: list[tuple]):
        coldata = [
            "Id",
            "TipoDocumento",
            "Documento",
            "PrimerNombre",
            "SegundoNombre",
            "PrimerApellido",
            "SegundoApellido",
            "Email",
            "NúmeroCarne",
        ]

        self.table = Tableview(master=self.root,paginated=True, searchable=True, rowdata=rowdata, bootstyle=PRIMARY,coldata=coldata)
        self.table.grid(row=1, column=0, sticky="we", columnspan=3)

    def ActualizarDatos(self) -> None:
        rowdata = self.CargarDatos()
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()

    # endregion

    # region Eventos

    def onBtnAgregarRegistro_onClick(self):
        frEditor = FrEstudiantesEditor(self, 0)

    def onBtnEditarRegistro_onClick(self):
        row = self.table.get_rows(selected=True)[0]
        id = row.values[0]
        rEditor = FrEstudiantesEditor(self, id)

    def onBtnEliminarRegistro_onClick(self):
        confirmacion = Messagebox.show_question(parent=self.ObjMain.root, message="¿Quiere eliminar el registro seleccionado?", title="Confirmacion" ,buttons=["No:danger", "Yes: success"])
        if confirmacion == "Yes":
            row = self.table.get_rows(selected=True)[0]
            id = row.values[0]
            MdEstudiante.EliminarRegistro(id)
            self.ActualizarDatos()

    # endregion