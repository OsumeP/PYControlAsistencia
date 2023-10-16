import sys
sys.path.append("Models")
from MdAsignatura import MdAsignatura
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from FcUtilidades import CentrarMensaje, CentrarPantalla
from ttkbootstrap.dialogs import Messagebox

class FrAsignaturasEditor():

    # region Propiedades

    root : ttk.Toplevel
    txtNombre: ttk.Entry
    ObjMain: any
    ObjId: int
    Asignatura: MdAsignatura

    # endregion

    # region Constructores

    def __init__(self, objMain: any, id: int) -> None:
        self.ObjMain = objMain
        self.ObjId = id
        self.InstanciarAsignatura()
        self.MostrarEditor()
    # endregion

    # region Funciones

    def MostrarEditor(self):
        self.root = ttk.Toplevel(self.ObjMain.root, topmost=True, resizable=(False, False))
        self.root.title = "Creación asignatura"
        self.root.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 500, 400))

        lbId = ttk.Label(self.root, text="Id: ", font=('Helvetica', 16), bootstyle="success")
        lbId.grid(row=0, column=0)

        lbIdInt = ttk.Label(self.root, text=self.ObjId, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1)

        lbNombre = ttk.Label(self.root, text="Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbNombre.grid(row=1, column=0)

        self.txtNombre = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtNombre.insert(string=self.Asignatura.Nombre, index=0)
        self.txtNombre.grid(row=1, column=1)

        self.btnCrear = ttk.Button(self.root, text="Grabar", bootstyle="success", command=self.onBtnGrabarAsignatura_onClick)
        self.btnCrear.grid(row=2, column=0)
        btnCancelar = ttk.Button(self.root, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick)
        btnCancelar.grid(row=2, column=1)

    def InstanciarAsignatura(self):
        if self.ObjId <= 0:
            self.Asignatura = MdAsignatura("")
            self.Asignatura.EstablecerId(0)
        else:
            self.Asignatura = MdAsignatura.ObtenerPorId(self.ObjId)
    
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
            Messagebox.show_warning("Ya existe una asignatura con este nombre.s", parent=self.root, title='UNAL', **keywords)
    
    def onBtnCancelar_onClick(self):
        self.root.destroy()

    # endregion