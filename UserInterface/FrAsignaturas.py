import sys
from tkinter.ttk import Style
sys.path.append("Models")
from FrAsignaturasEditor import FrAsignaturasEditor
from MdAsignatura import MdAsignatura
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarMensaje, CentrarPantalla
from ttkbootstrap.dialogs import Messagebox

class FrAsignaturas():

    # region Propiedades

    root : ttk.Frame
    txtNombre: ttk.Entry
    ObjMain: any
    tlCrearAsignatura: ttk.Toplevel
    table: Tableview
    Asignatura: MdAsignatura

    # endregion

    # region Constructores

    def __init__(self, objMain: any) -> None:
        self.ObjMain = objMain
        self.CrearToolbar()
        self.MostrarLista( self.CargarDatos())

    # endregion

    # region Funciones

    def CrearToolbar(self):
        self.root = ttk.Frame(self.ObjMain.nbTabControl)
        self.ObjMain.nbTabControl.add(self.root, text='Administración de Asignaturas')
        label = ttk.Label(self.root, text='Administración de Asignaturas', font=('Helvetica', 18), bootstyle="success")
        label.grid(row=0, column=0, columnspan=3, pady=5)
        wdButton = int((self.root.winfo_screenwidth() - 120) / 6 /3)
        btnAgregar = ttk.Button(self.root,text="Agregar", bootstyle='success', width=wdButton, command=self.onBtnAgregarAsignatura_onClick)
        btnAgregar.grid(row=1, column=0,padx=5,pady=5)
        btnEditar = ttk.Button(self.root,text="Editar", bootstyle='info', width=wdButton, command=self.onBtnEditar_onClick)
        btnEditar.grid(row=1, column=1,padx=5,pady=5)
        btnEliminar = ttk.Button(self.root,text="Eliminar", bootstyle='danger', width=wdButton, command=self.onBtnEliminar_onClick)
        btnEliminar.grid(row=1, column=2,padx=5,pady=5)

    def MostrarLista(self, rowdata: list[tuple]):
        wdButton = int((self.root.winfo_screenwidth() - 20) / 2)
        coldata = [
            {"text": "Id", "stretch": False, "width":wdButton},
            {"text": "Nombre", "stretch": False, "width":wdButton},
        ]

        self.table = Tableview(master=self.root,paginated=True, searchable=True, rowdata=rowdata, pagesize=50,
                               bootstyle=PRIMARY, coldata=coldata, height=30)
        self.table.grid(row=2, column=0, sticky="we", columnspan=3)

    def CargarDatos(self) -> list[list]:
        listaAsignaturas = MdAsignatura.ObtenerTodos()
        rowdata = []
        for i in listaAsignaturas:
            rowdata.append([i.Id, i.Nombre])
        return rowdata

    def ActualizarDatos(self) -> None:
        rowdata = self.CargarDatos()
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()
    # endregion

    # region Eventos
    def onBtnAgregarAsignatura_onClick(self):
        FrAsignaturasEditor(self, 0)

    def onBtnEliminar_onClick(self):
        keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
        confirmacion = Messagebox.show_question(parent=self.ObjMain.root, message="¿Quiere eliminar el registro seleccionado?", title="Confirmacion" ,buttons=["No:danger", "Yes: success"],**keywords)
        if confirmacion == "Yes":
            try:
                row = self.table.get_rows(selected=True)[0]
                id = row.values[0]
                MdAsignatura.EliminarRegistro(id)
                self.ActualizarDatos()
            except:
                pass

    def onBtnEditar_onClick(self):
        row = self.table.get_rows(selected=True)[0]
        id = row.values[0]
        FrAsignaturasEditor(self, id)
    # endregion