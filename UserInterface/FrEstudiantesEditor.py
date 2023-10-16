import sys
sys.path.append("Models")
from ttkbootstrap.dialogs import Messagebox, MessageDialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdEstudiante import MdEstudiante
from FcUtilidades import CentrarMensaje, CentrarPantalla

class FrEstudiantesEditor():

    # region Propiedades

    objPadre: any
    root: ttk.Toplevel
    idObjeto: int
    Estudiante: MdEstudiante
    cbTipoDocumento: ttk.Combobox
    txtDocumento: ttk.Entry
    txtPrimerNombre: ttk.Entry
    txtSegundoNombre: ttk.Entry
    txtPrimerApellido: ttk.Entry
    txtSegundoApellido: ttk.Entry
    txtNumeroCarne: ttk.Entry
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
            self.Estudiante = MdEstudiante(0, "")
            self.Estudiante.EstablecerId(0)
            self.Estudiante.Documento = ""
            self.Estudiante.PrimerNombre = ""
            self.Estudiante.SegundoNombre = ""
            self.Estudiante.PrimerApellido = ""
            self.Estudiante.SegundoApellido = ""
            self.Estudiante.Email = ""
            self.Estudiante.NumeroCarne = ""
            self.Estudiante.TipoDocumento = 0

        else:
            self.Estudiante = MdEstudiante.ObtenerPorId(self.idObjeto)

    def MostrarEditor(self):
        self.root = ttk.Toplevel(self.objPadre.root, topmost=True, resizable=(False, False))
        self.root.title = "Creación/Edición estudiante"
        self.root.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 950, 500))
        
        lbId = ttk.Label(self.root, text="Id: ", font=('Helvetica', 16), bootstyle="success")
        lbId.grid(row=0, column=0,pady=20)

        lbIdInt = ttk.Label(self.root, text=self.Estudiante.Id, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1)

        lbTipoDocumento = ttk.Label(self.root, text="Tipo de Documento:", font=('Helvetica', 16), bootstyle="success")
        lbTipoDocumento.grid(row=1, column=0,padx=20, pady=20)

        tiposDocumento = ["CC", "CE", "TI", "PT"]
        self.cbTipoDocumento = ttk.Combobox(self.root, bootstyle="SUCCESS", width=12,  state="readonly", values=tiposDocumento)
        self.cbTipoDocumento.grid(row=1,column=1, padx=20)
        match self.Estudiante.TipoDocumento:
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
        self.txtDocumento.insert(0, self.Estudiante.Documento)
        self.txtDocumento.grid(row=1, column=3)

        lbPrimerNombre = ttk.Label(self.root, text="Primer Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerNombre.grid(row=2, column=0,padx=20, pady=20)

        self.txtPrimerNombre = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtPrimerNombre.insert(0, self.Estudiante.PrimerNombre)
        self.txtPrimerNombre.grid(row=2, column=1, padx=20)

        lbSegundoNombre = ttk.Label(self.root, text="Segundo Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoNombre.grid(row=2, column=2, padx=20)

        self.txtSegundoNombre = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtSegundoNombre.insert(0, self.Estudiante.SegundoNombre)
        self.txtSegundoNombre.grid(row=2, column=3)

        lbPrimerApellido = ttk.Label(self.root, text="Primer Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerApellido.grid(row=3, column=0,padx=20, pady=20)

        self.txtPrimerApellido = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtPrimerApellido.insert(0, self.Estudiante.PrimerApellido)
        self.txtPrimerApellido.grid(row=3, column=1, padx=20)

        lbSegundoApellido = ttk.Label(self.root, text="Segundo Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoApellido.grid(row=3, column=2, padx=20)

        self.txtSegundoApellido = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtSegundoApellido.insert(0, self.Estudiante.SegundoApellido)
        self.txtSegundoApellido.grid(row=3, column=3)

        lbNumeroCarne = ttk.Label(self.root, text="Número de Carné:", font=('Helvetica', 16), bootstyle="success")
        lbNumeroCarne.grid(row=4, column=0,padx=20, pady=20)

        self.txtNumeroCarne = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtNumeroCarne.insert(0, self.Estudiante.NumeroCarne)
        self.txtNumeroCarne.grid(row=4, column=1, padx=20)

        lbEmail = ttk.Label(self.root, text="Email:", font=('Helvetica', 16), bootstyle="success")
        lbEmail.grid(row=4, column=2, padx=20)

        self.txtEmail = ttk.Entry(self.root, bootstyle="success", width=32)
        self.txtEmail.insert(0, self.Estudiante.Email)
        self.txtEmail.grid(row=4, column=3, padx=20)

        btnGrabar = ttk.Button(self.root, text="Grabar", bootstyle="success", command=self.onBtnGrabar_onClick)
        btnGrabar.grid(row=5, column=1, padx=20, pady=20)
        btnCancelar = ttk.Button(self.root, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick)
        btnCancelar.grid(row=5, column=3, padx=20)
    
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
            
        self.Estudiante.TipoDocumento = numTipoDocumento
        self.Estudiante.Documento = self.txtDocumento.get()
        self.Estudiante.NumeroCarne = self.txtNumeroCarne.get()
        self.Estudiante.PrimerNombre = self.txtPrimerNombre.get()
        self.Estudiante.SegundoNombre = self.txtSegundoNombre.get()
        self.Estudiante.PrimerApellido = self.txtPrimerApellido.get()
        self.Estudiante.SegundoApellido = self.txtSegundoApellido.get()
        self.Estudiante.Email = self.txtEmail.get()

        if not(self.Estudiante.ValidarRepeticion()):
            if self.idObjeto <= 0:
                self.Estudiante.InsertarRegistro()
            else:
                self.Estudiante.ActualizarRegistro()    
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_info("Registro grabado correctamente!", parent=self.root, title='UNAL', **keywords)
            self.objPadre.ActualizarDatos()
            self.root.destroy()
        else:
            keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
            Messagebox.show_warning('Ya existe un estudiante con este documento!', parent=self.root, title='UNAL', **keywords)

    def onBtnCancelar_onClick(self):
        self.root.destroy()

    # endregion
