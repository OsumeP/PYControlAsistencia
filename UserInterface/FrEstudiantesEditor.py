import sys
sys.path.append("Models")
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import io
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
    lbFoto : ttk.Label

    # endregion

    # region Constructores

    def __init__(self, objPadre, id : int) -> None:
        self.objPadre = objPadre
        self.idObjeto = id
        self.InstanciarObjeto()
        self.MostrarEditor()
    
    # endregion

    # region Funciones

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
            self.Estudiante.CargarVector()
            self.Estudiante.CargarFoto()

    def MostrarEditor(self):
        self.root = ttk.Toplevel(self.objPadre.root, resizable=(False, False))
        self.root.title('UNAL - Editor de Estudiante')
        self.root.geometry(CentrarPantalla(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 1200, 400))

        lbTitulo = ttk.Label(self.root, text="EDITOR DE ESTUDIANTE",font=('Helvetica', 15), bootstyle="success")
        lbTitulo.grid(row=0, column=0, columnspan=2, pady=5)

        frData = ttk.Frame(self.root)
        frData.grid(row=1, column=0, pady=5)

        lbId = ttk.Label(frData, text="Id: ", font=('Helvetica', 16), bootstyle="success")
        lbId.grid(row=0, column=0,pady=5)
        lbIdInt = ttk.Label(frData, text=self.Estudiante.Id, font=('Helvetica', 16), bootstyle="success")
        lbIdInt.grid(row=0, column=1)

        lbTipoDocumento = ttk.Label(frData, text="Tipo de Documento:", font=('Helvetica', 16), bootstyle="success")
        lbTipoDocumento.grid(row=1, column=0,padx=20, pady=5)

        tiposDocumento = ["CC", "CE", "TI", "PT"]
        self.cbTipoDocumento = ttk.Combobox(frData, bootstyle="SUCCESS",  state="readonly", values=tiposDocumento)
        self.cbTipoDocumento.grid(row=1,column=1, padx=10, sticky="ew")
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
        
        lbDocumento = ttk.Label(frData, text="Documento:", font=('Helvetica', 16), bootstyle="success")
        lbDocumento.grid(row=1, column=2, padx=20)

        self.txtDocumento = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtDocumento.insert(0, self.Estudiante.Documento)
        self.txtDocumento.grid(row=1, column=3)

        lbPrimerNombre = ttk.Label(frData, text="Primer Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerNombre.grid(row=2, column=0,padx=20, pady=5)

        self.txtPrimerNombre = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtPrimerNombre.insert(0, self.Estudiante.PrimerNombre)
        self.txtPrimerNombre.grid(row=2, column=1, padx=10)

        lbSegundoNombre = ttk.Label(frData, text="Segundo Nombre:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoNombre.grid(row=2, column=2, padx=10)

        self.txtSegundoNombre = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtSegundoNombre.insert(0, self.Estudiante.SegundoNombre)
        self.txtSegundoNombre.grid(row=2, column=3)

        lbPrimerApellido = ttk.Label(frData, text="Primer Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbPrimerApellido.grid(row=3, column=0,padx=20, pady=5)

        self.txtPrimerApellido = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtPrimerApellido.insert(0, self.Estudiante.PrimerApellido)
        self.txtPrimerApellido.grid(row=3, column=1, padx=10)

        lbSegundoApellido = ttk.Label(frData, text="Segundo Apellido:", font=('Helvetica', 16), bootstyle="success")
        lbSegundoApellido.grid(row=3, column=2, padx=10)

        self.txtSegundoApellido = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtSegundoApellido.insert(0, self.Estudiante.SegundoApellido)
        self.txtSegundoApellido.grid(row=3, column=3)

        lbNumeroCarne = ttk.Label(frData, text="Número de Carné:", font=('Helvetica', 16), bootstyle="success")
        lbNumeroCarne.grid(row=4, column=0,padx=20, pady=5)

        self.txtNumeroCarne = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtNumeroCarne.insert(0, self.Estudiante.NumeroCarne)
        self.txtNumeroCarne.grid(row=4, column=1, padx=20)

        lbEmail = ttk.Label(frData, text="Email:", font=('Helvetica', 16), bootstyle="success")
        lbEmail.grid(row=4, column=2, padx=20)

        self.txtEmail = ttk.Entry(frData, bootstyle="success", width=32)
        self.txtEmail.insert(0, self.Estudiante.Email)
        self.txtEmail.grid(row=4, column=3, padx=10)

        btnGrabar = ttk.Button(frData, text="Grabar", bootstyle="success", command=self.onBtnGrabar_onClick)
        btnGrabar.grid(row=6, column=1, padx=20, pady=5, sticky='EW')
        btnCancelar = ttk.Button(frData, text="Cancelar", bootstyle="danger", command=self.onBtnCancelar_onClick)
        btnCancelar.grid(row=6, column=3, padx=20, sticky='EW')

        frFoto = ttk.Frame(self.root)
        frFoto.grid(row=1, column=1, pady=5)

        self.lbFoto = ttk.Label(frFoto, width=50)
        self.lbFoto.grid(row=0, column=0, columnspan=2)
        self.MostrarFoto()

        btnCapturar = ttk.Button(frFoto, text="Tomar Foto", bootstyle="info", command=self.onTomarFoto)
        btnCapturar.grid(row=1, column=0, padx=20, pady=5, sticky='EW')

        btnSubir = ttk.Button(frFoto, text="Subir Foto", bootstyle="info", command=self.onSubirFoto)
        btnSubir.grid(row=1, column=1, padx=20, sticky='EW')

    def MostrarFoto(self)-> None:
        if self.Estudiante.Foto != None:
            img = Image.open(io.BytesIO(self.Estudiante.Foto))
            img = img.resize((200,200))
            img = ImageTk.PhotoImage(img)
            self.image = img
            self.lbFoto.configure(image=img)
            self.lbFoto.grid(row=0, column=0, columnspan=2)
        
    def ValidarFoto(self) -> None:
        keywords = CentrarMensaje(self.root.winfo_screenwidth(), self.root.winfo_screenheight(), 250, 180)
        if self.Estudiante.Vector == None:
            Messagebox.show_info("No se reconoció un rostro en la foto", parent=self.root, title='UNAL', **keywords)


    #endregion

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
    
    def onTomarFoto(self):
        self.Estudiante.AsignarFotoVector()
        self.MostrarFoto()
        self.ValidarFoto()

    def onSubirFoto(self):
        pathName = filedialog.askopenfilename(parent=self.root)
        if not(pathName == ''):
            self.Estudiante.SubirFoto(pathName)
            self.ValidarFoto()
            self.MostrarFoto()

    # endregion
