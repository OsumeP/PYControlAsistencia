import sys

sys.path.append("Models")
from ttkbootstrap.dialogs import Messagebox, MessageDialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdDocente import MdDocente
from FcUtilidades import CentrarMensaje, CentrarPantalla

class FrDocentesEditor():

    # region Propiedades

    objPadre: any
    root: ttk.Toplevel
    idObjeto: int
    Docente: MdDocente
    cbTipoDocumento: ttk.Combobox
    txtDocumento: ttk.Entry
    txtPrimerNombre: ttk.Entry
    txtSegundoNombre: ttk.Entry
    txtPrimerApellido: ttk.Entry
    txtSegundoApellido: ttk.Entry
    txtTarjetaProfesional: ttk.Entry
    txtEmail: ttk.Entry

    # endregion

    # region Constructores

    def __init__(self, objPadre, id : int) -> None:
        self.objPadre = objPadre
        self.idObjeto = id
        self.InstanciarObjeto()
        self.MostrarEditor()
    
    # endregion

    def InstanciarObjeto(self):
        if self.idObjeto <= 0:
            self.Docente = MdDocente(0, "")
            self.Docente.EstablecerId(0)
            self.Docente.Documento = ""
            self.Docente.PrimerNombre = ""
            self.Docente.SegundoNombre = ""
            self.Docente.PrimerApellido = ""
            self.Docente.SegundoApellido = ""
            self.Docente.Email = ""
            self.Docente.TarjetaProfesional = ""
            self.Docente.TipoDocumento = 0

        else:
            self.Docente = MdDocente.ObtenerPorId(self.idObjeto)

    def MostrarEditor(self):
        self.root = ttk.Toplevel(self.objPadre.root, topmost=True, resizable=(False, False))
        self.root.title = "Creación/Edición estudiante"
        self.root.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 950, 500))
        
        lbId = ttk.Label(self.root, text="Id: ", font=('Helvetica', 16), bootstyle="success")
        lbId.grid(row=0, column=0, pady=10)

        lbIdInt = ttk.Label(self.root, text=self.Docente.Id, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1, pady=10)

        lbTipoDocumento = ttk.Label(self.root, text="Tipo de Documento:", font=('Helvetica', 16), bootstyle="success")
        lbTipoDocumento.grid(row=1, column=0, padx=20, pady=20)

        tiposDocumento = ["CC", "CE", "TI", "PT"]
        self.cbTipoDocumento = ttk.Combobox(self.root, bootstyle="SUCCESS", width=12,  state="readonly", values=tiposDocumento)
        self.cbTipoDocumento.grid(row=1,column=1)
        match self.Docente.TipoDocumento:
            case 0:
                self.cbTipoDocumento.current(0)
            case 1:
                self.cbTipoDocumento.current(0)
            case 2:
                self.cbTipoDocumento.current(1)
            case 3:
                self.cbTipoDocumento.current(2)
            case 4:
                self.cbTipoDocumento.current(3)
        
        lbDocumento = ttk.Label(self.root, text="Documento:", font=('Helvetica', 16), bootstyle="success")
        lbDocumento.grid(row=1, column=2, padx=20)

        self.txtDocumento = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtDocumento.insert(0, self.Docente.Documento)
        self.txtDocumento.grid(row=1, column=3)

        lbPrimerNombre = ttk.Label(self.root, text="Primer Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerNombre.grid(row=2, column=0, padx=20, pady=20)

        self.txtPrimerNombre = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtPrimerNombre.insert(0, self.Docente.PrimerNombre)
        self.txtPrimerNombre.grid(row=2, column=1, padx=20)

        lbSegundoNombre = ttk.Label(self.root, text="Segundo Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoNombre.grid(row=2, column=2, padx=20)

        self.txtSegundoNombre = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtSegundoNombre.insert(0, self.Docente.SegundoNombre)
        self.txtSegundoNombre.grid(row=2, column=3)

        lbPrimerApellido = ttk.Label(self.root, text="Primer Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerApellido.grid(row=3, column=0, padx=20, pady=20)

        self.txtPrimerApellido = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtPrimerApellido.insert(0, self.Docente.PrimerApellido)
        self.txtPrimerApellido.grid(row=3, column=1, padx=20)

        lbSegundoApellido = ttk.Label(self.root, text="Segundo Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoApellido.grid(row=3, column=2, padx=20)

        self.txtSegundoApellido = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtSegundoApellido.insert(0, self.Docente.SegundoApellido)
        self.txtSegundoApellido.grid(row=3, column=3)

        lbTarjetaProfesional = ttk.Label(self.root, text="Tarjeta Profesional:", font=('Helvetica', 16), bootstyle="success")
        lbTarjetaProfesional.grid(row=4, column=0, padx=20, pady=20)

        self.txtTarjetaProfesional = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtTarjetaProfesional.insert(0, self.Docente.TarjetaProfesional)
        self.txtTarjetaProfesional.grid(row=4, column=1, padx=20)

        lbEmail = ttk.Label(self.root, text="Email:", font=('Helvetica', 16), bootstyle="success")
        lbEmail.grid(row=4, column=2, padx=20)

        self.txtEmail = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtEmail.insert(0, self.Docente.Email)
        self.txtEmail.grid(row=4, column=3, padx=20)

        btnGrabar = ttk.Button(self.root, text="Grabar", bootstyle="success", command=self.onBtnGrabar_onClick, width=20)
        btnGrabar.grid(row=5, column=1, padx=20, pady=20)
        btnCancelar = ttk.Button(self.root, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick, width=20)
        btnCancelar.grid(row=5, column=3)
    
    # region Eventos

    def onBtnGrabar_onClick(self):
        numTipoDocumento = 0
        match self.cbTipoDocumento.get():
            case "CC": 
                numTipoDocumento = 1
            case "CE": 
                numTipoDocumento = 2
            case "TI": 
                numTipoDocumento = 3
            case "PT": 
                numTipoDocumento = 4
            
        self.Docente.TipoDocumento = numTipoDocumento
        self.Docente.Documento = self.txtDocumento.get()
        self.Docente.TarjetaProfesional = self.txtTarjetaProfesional.get()
        self.Docente.PrimerNombre = self.txtPrimerNombre.get()
        self.Docente.SegundoNombre = self.txtSegundoNombre.get()
        self.Docente.PrimerApellido = self.txtPrimerApellido.get()
        self.Docente.SegundoApellido = self.txtSegundoApellido.get()
        self.Docente.Email = self.txtEmail.get()

        if not(self.Docente.ValidarRepeticion()):
            if self.idObjeto <= 0:
                self.Docente.InsertarRegistro()
            else:
                self.Docente.ActualizarRegistro()    
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_info("Registro grabado correctamente!", parent=self.root, title='UNAL', **keywords)
            self.objPadre.ActualizarDatos()
            self.root.destroy()
        else:
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_warning('Ya existe un docente con este documento!', parent=self.root, title='UNAL', **keywords)

    def onBtnCancelar_onClick(self):
        self.root.destroy()

    # endregion
