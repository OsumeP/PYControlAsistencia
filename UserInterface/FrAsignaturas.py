import sys
sys.path.append("Models")
from MdAsignatura import MdAsignatura
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarPantalla
from ttkbootstrap.dialogs import Messagebox

class FrAsignaturas():

    # region Propiedades

    root : ttk.Frame
    txtNombre: ttk.Entry
    ObjMain: any
    tlCrearAsignatura: ttk.Toplevel
    table: Tableview
    btnCrear: ttk.Button
    Asignatura: MdAsignatura

    # endregion

    # region Constructores

    def __init__(self, objMain: any) -> None:
        self.ObjMain = objMain
        self.root = ttk.Frame(self.ObjMain.nbTabControl)
        self.ObjMain.nbTabControl.add(self.root, text='Administración de Asignaturas')
        btnAgregar = ttk.Button(self.root,text="Agregar", bootstyle='success', command=self.onBtnAgregarAsignatura_onClick)
        btnAgregar.grid(row=0, column=0)
        btnEditar = ttk.Button(self.root,text="Editar", bootstyle='success', command=self.onBtnEditar_onClick)
        btnEditar.grid(row=0, column=1)
        btnEliminar = ttk.Button(self.root,text="Eliminar", bootstyle='success', command=self.onBtnEliminar_onClick)
        btnEliminar.grid(row=0, column=2)
        rowdata = self.CargarDatos()
        self.MostrarLista(rowdata)

    # endregion

    # region Funciones

    def MostrarLista(self, rowdata: list[tuple]):
        coldata = [
            {"text": "Id", "stretch": False},
            "Nombre",
        ]

        self.table = Tableview(master=self.root,paginated=True, searchable=True, rowdata=rowdata, bootstyle=PRIMARY,coldata=coldata)
        #table.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        self.table.grid(row=1, column=0, sticky="we", columnspan=3)

    def CargarDatos(self) -> list[list]:
        listaAsignaturas = MdAsignatura.ObtenerTodos()
        rowdata = []
        for i in listaAsignaturas:
            rowdata.append([i.Id, i.Nombre])
        return rowdata

    def ActualizarDatos(self, rowdata: list[tuple]) -> None:
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()

    def MostrarSegundaPantalla(self, id: int, name: str):
        lbId = ttk.Label(self.tlCrearAsignatura, text="Id: ", font=('Helvetica', 16), bootstyle="success")
        lbId.grid(row=0, column=0)

        lbIdInt = ttk.Label(self.tlCrearAsignatura, text=id, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1)

        lbNombre = ttk.Label(self.tlCrearAsignatura, text="Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbNombre.grid(row=1, column=0)

        self.txtNombre = ttk.Entry(self.tlCrearAsignatura, bootstyle="success", width=32)
        self.txtNombre.insert(string=name, index=0)
        self.txtNombre.grid(row=1, column=1)

        self.btnCrear = ttk.Button(self.tlCrearAsignatura, text="Grabar", bootstyle="success")
        self.btnCrear.grid(row=2, column=0)
        btnCancelar = ttk.Button(self.tlCrearAsignatura, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick)
        btnCancelar.grid(row=2, column=1)
    # endregion

    # region Eventos
    def onBtnAgregarAsignatura_onClick(self):
        self.tlCrearAsignatura = ttk.Toplevel(self.root, topmost=True, resizable=(False, False))
        self.tlCrearAsignatura.title = "Creación asignatura"
        self.tlCrearAsignatura.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 500, 400))
        self.MostrarSegundaPantalla(0, "")
        self.btnCrear.configure(command=self.onBtnCrearAsignatura_onClick)
    
    def onBtnCrearAsignatura_onClick(self):
        self.Asignatura = MdAsignatura(self.txtNombre.get())
        if not(self.Asignatura.ValidarAsignatura()):
            self.Asignatura.InsertarRegistro()
            self.ActualizarDatos(self.CargarDatos())
            confirmation = Messagebox.show_warning('Se creó el registro!', parent=self.root, title='UNAL')
        else:
            warning = Messagebox.show_warning('Ya existe una asignatura con este nombre', parent=self.root, title='UNAL')
    
    def onBtnCancelar_onClick(self):
        self.tlCrearAsignatura.destroy()

    def onBtnEliminar_onClick(self):
        confirmacion = Messagebox.show_question(parent=self.ObjMain.root, message="¿Quiere eliminar el registro seleccionado?", title="Confirmacion" ,buttons=["No:danger", "Yes: success"])
        if confirmacion == "Yes":
            row = self.table.get_rows(selected=True)[0]
            id = row.values[0]
            MdAsignatura.EliminarRegistro(id)
            self.ActualizarDatos(self.CargarDatos())

    def onBtnEditar_onClick(self):
        self.tlCrearAsignatura = ttk.Toplevel(self.root, topmost=True, resizable=(False, False))
        self.tlCrearAsignatura.title = "Edición asignatura"
        self.tlCrearAsignatura.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 500, 400))
        row = self.table.get_rows(selected=True)[0]
        id = row.values[0]
        self.Asignatura = MdAsignatura.ObtenerPorId(id)
        self.MostrarSegundaPantalla(self.Asignatura.Id, self.Asignatura.Nombre)
        self.btnCrear.configure(command=self.onBtnGrabarNuevo_onClick)

    def onBtnGrabarNuevo_onClick(self):
        self.Asignatura = MdAsignatura(self.txtNombre.get())
        if not(self.Asignatura.ValidarAsignatura()):
            self.Asignatura.ActualizarRegistro()
            self.ActualizarDatos(self.CargarDatos())
            confirmacion = Messagebox.show_warning("Se editó con exito!")
        else:
            warning = Messagebox.show_warning("Ya existe una asignatura con este nombre")
        self.tlCrearAsignatura.destroy()


    # endregion