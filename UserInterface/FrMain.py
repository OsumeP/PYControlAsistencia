import sys

sys.path.append("Models")
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from EnEnum import EnTipoUsuario
from FrLogin import FrLogin
from MdInicioSesion import MdInicioSesion
from FrAsignaturas import FrAsignaturas
from FrEstudiantes import FrEstudiantes
from FrDocentes import FrDocentes
from FrClases import FrClases

class FrMain():

    # region Propiedades

    root: ttk.Window
    frameHeader: ttk.Frame
    frameInfo: ttk.Frame
    frameButtons: ttk.Frame
    frameTabs: ttk.Frame
    nbTabControl: ttk.Notebook
    objInicioSesion: MdInicioSesion
    login: FrLogin

    #endregion

    # region Constructores

    def __init__(self) -> None:
        self.root = ttk.Window(themename='flatly')
        self.root.title('UNAL - Control de Asistencia')
        self.root.state('zoomed')
        self.MostrarHeader()
        self.login = FrLogin(self)
        self.root.mainloop()

    # endregion

    # region Funciones

    def MostrarHeader(self):
        self.frameHeader = ttk.Frame(self.root)
        self.frameHeader.grid(row=0, column=0)
        logo = ttk.PhotoImage(file="UserInterface\Images\Logo.png")
        labelLogo = ttk.Label(self.frameHeader, image=logo, width=30)
        labelLogo.grid(row=0, column=0)
        labelLogo.image = logo
        labelLogo.configure(image=logo)
        labelLogo.grid(row=0, column=0)

        title = ttk.Label(self.frameHeader, text="UNAL - Sistema de asistencia",
                        bootstyle='success', font=('Helvetica', 30), width=40)
        title.grid(row=0, column=1)

        self.frameTabs = ttk.Frame(self.root)
        self.frameTabs.grid(row=2, column=0)
        self.nbTabControl = ttk.Notebook(self.frameTabs, width=self.root.winfo_screenwidth())
        self.nbTabControl.pack(expand=1, fill="both")

    def MostrarInfo(self):
        self.frameInfo = ttk.Frame(self.frameHeader, width=50)
        self.frameInfo.grid(row=0, column=2)
        labelUsuario = ttk.Label(
            self.frameInfo, bootstyle='success', text=self.objInicioSesion.Usuario, font=('Helvetica', 12))
        labelUsuario.grid(row=0, column=0)
        labelTipoUsuario = ttk.Label(
            self.frameInfo, bootstyle='success', text=self.objInicioSesion.TipoUsuario.name, font=('Helvetica', 8))
        labelTipoUsuario.grid(row=1, column=0)
        btnCerrarSesion = ttk.Button(
            self.frameInfo, text='Cerrar Sesión', bootstyle='success', command=self.onBtnCerrarSesion_onClick)
        btnCerrarSesion.grid(row=12, column=0)

    def ConfigurarTabs(self):
         match self.objInicioSesion.TipoUsuario:
            case EnTipoUsuario.Administrador:
                self.CrearTabAsignaturas()
                self.CrearTabDocentes()
                self.CrearTabEstudiantes()
                pass
            case EnTipoUsuario.Docente:
                self.CrearTabClases()
            case EnTipoUsuario.Estudiante:
                pass

    def onAfterLogin(self, mdInicioSesion: MdInicioSesion):
        self.objInicioSesion = mdInicioSesion
        self.MostrarInfo()
        self.ConfigurarTabs()

    def CrearTabAsignaturas(self):
        frAsignaturas = FrAsignaturas(self)
    def CrearTabDocentes(self):
        FrDocentes(self)
    def CrearTabEstudiantes(self):
        frEstudiantes = FrEstudiantes(self)

    def CrearTabClases(self):
        FrClases(self, self.objInicioSesion.Id)
    #endregion

    # region Eventos
  
    def onBtnCerrarSesion_onClick(self):
        self.frameInfo.destroy()
        self.objInicioSesion = None
        listKeys = list(self.nbTabControl.children.keys())
        for key in listKeys:
            self.nbTabControl.children[key].destroy()
        self.login.MostrarLogin()

    def onBtnAsignaturas_onClick(self):
        frAsignaturas = FrAsignaturas(self)

    # endregion

objInit = FrMain()