import sys

sys.path.append("Models")
from MdAsignaturaEstudiante import MdAsignaturaEstudiante
from MdEstudiante import MdEstudiante
from MdAsignatura import MdAsignatura
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarMensaje, CentrarPantalla
from ttkbootstrap.dialogs import Messagebox

class FrAsignaturasEditor():

    # region Propiedades

    root : ttk.Toplevel
    Documentos: list
    txtNombre: ttk.Entry
    cbEstudiantes: ttk.Combobox
    ObjMain: any
    ObjId: int
    Asignatura: MdAsignatura
    table: Tableview

    # endregion

    # region Constructores

    def __init__(self, objMain: any, id: int) -> None:
        self.ObjMain = objMain
        self.ObjId = id
        self.Documentos = []
        self.InstanciarAsignatura()
        self.MostrarEditor()
    # endregion

    # region Funciones

    def MostrarEditor(self):
        self.root = ttk.Toplevel(self.ObjMain.root, topmost=True, resizable=(False, False))
        self.root.title("Creación/edición asignatura")
        self.root.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 820, 600))

        lbId = ttk.Label(self.root, text="Id: ", font=('Helvetica', 16), bootstyle="success", width=5)
        lbId.grid(row=0, column=0, padx=5, pady=5)

        lbIdInt = ttk.Label(self.root, text=self.ObjId, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1, padx=5)

        lbNombre = ttk.Label(self.root, text="Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbNombre.grid(row=0, column=2, padx=5, pady=5)

        self.txtNombre = ttk.Entry(self.root, bootstyle="success", width=20)
        self.txtNombre.insert(string=self.Asignatura.Nombre, index=0)
        self.txtNombre.grid(row=0, column=3, padx=20)

        self.btnCrear = ttk.Button(self.root, text="Grabar", bootstyle="success", command=self.onBtnGrabarAsignatura_onClick)
        self.btnCrear.grid(row=1, column=1, padx=5, pady=5)
        btnCancelar = ttk.Button(self.root, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick)
        btnCancelar.grid(row=1, column=3, padx=5)

        self.MostrarDetalle(self.CargarDatos())
        
        if self.ObjId != 0:
            self.cbEstudiantes = ttk.Combobox(master=self.root,  bootstyle="SUCCESS",  state="readonly", values=MdAsignaturaEstudiante.ObtenerEstudiantesFaltantes(self.ObjId), width=25)
            self.cbEstudiantes.grid(row=4, column=0)
            btnAgregarEstudiante = ttk.Button(self.root, bootstyle="success", text="Agregar", command=self.onBtnAgregarEstudiante_onClick)
            btnAgregarEstudiante.grid(row=4, column=1)
            btnAgregarEstudiante = ttk.Button(self.root, bootstyle="danger", text="Eliminar", command=self.onBtnEliminar_onClick)
            btnAgregarEstudiante.grid(row=4, column=2)
        
    
    def MostrarDetalle(self, rowdata: list):
        coldata = [
            {"text": "Id", "stretch": False},
            {"text": "Documento", "stretch": False},
            {"text": "PrimerNombre", "stretch": False},
            {"text": "PrimerApellido", "stretch": False}
        ]
        self.table = Tableview(master=self.root,paginated=True, searchable=True, rowdata=rowdata, pagesize=20, height=20,
                        bootstyle=PRIMARY, coldata=coldata)
         
        self.table.grid(row=3, column=0, sticky="we", columnspan=4)

    def InstanciarAsignatura(self):
        if self.ObjId <= 0:
            self.Asignatura = MdAsignatura("")
            self.Asignatura.EstablecerId(0)
        else:
            self.Asignatura = MdAsignatura.ObtenerPorId(self.ObjId)
            self.Asignatura.CargarEstudiantes()

    def CargarDatos(self) -> list:
        rowdata = []
        if self.Asignatura.Estudiantes != None:
            for i in self.Asignatura.Estudiantes:
                rowdata.append([i.Estudiante.Id, i.Estudiante.Documento, i.Estudiante.PrimerNombre, i.Estudiante.PrimerApellido])
        return rowdata
        
    
    def ActualizarDatos(self) -> None:
        listaEstudiantes = MdAsignaturaEstudiante.ObtenerEstudiantesFaltantes(self.ObjId)
        self.cbEstudiantes["value"] = listaEstudiantes
        if len(listaEstudiantes) > 0:
            self.cbEstudiantes.current(0)
        else:
            self.cbEstudiantes["value"] = []
        self.Asignatura.CargarEstudiantes()
        rowdata = self.CargarDatos()
        self.table.delete_rows()
        self.table._build_table_rows(rowdata)
        self.table.goto_first_page()
    
    # endregion

    # region Eventos

    def onBtnGrabarAsignatura_onClick(self):

        self.Asignatura.Nombre = self.txtNombre.get()

        if not(self.Asignatura.ValidarAsignatura()):
            if self.ObjId <= 0:
                self.Asignatura.InsertarRegistro()
            else:
                self.Asignatura.ActualizarRegistro()
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_info("El registro se grabó correctamente!", parent=self.root, title='UNAL', **keywords)
            self.ObjMain.ActualizarDatos()
            self.root.destroy()
        else:
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_warning("Ya existe una asignatura con este nombre", parent=self.root, title='UNAL', **keywords)
    
    def onBtnCancelar_onClick(self):
        self.root.destroy()
    
    def onBtnEliminar_onClick(self):
        keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
        self.Asignatura.CargarEstudiantes()
        confirmacion = Messagebox.show_question(parent=self.root, message="¿Quiere eliminar el estudiante seleccionado de esta asignatura?", title="Confirmacion" ,buttons=["No:danger", "Yes: success"],**keywords)
        if confirmacion == "Yes":
            row = self.table.get_rows(selected=True)[0]
            id = row.values[0]
            MdAsignaturaEstudiante.EliminarRegistroIdEstudiante(id, self.ObjId)
            self.ActualizarDatos()

    def onBtnAgregarEstudiante_onClick(self):
        obj = MdAsignaturaEstudiante(self.Asignatura, MdEstudiante.ObtenerPorDocumento(self.cbEstudiantes.get().split()[0]))
        obj.InsertarRegistro()
        self.ActualizarDatos()

    # endregion