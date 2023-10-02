import sys
sys.path.append("Models")
from EnEnum import EnTipoUsuario
from FrLogin import FrLogin
from MdInicioSesion import MdInicioSesion
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class FrMain():

    # region Propiedades

    root: ttk.Window
    frameHeader: ttk.Frame
    frameInfo: ttk.Frame
    objInicioSesion: MdInicioSesion

    #endregion

    # region Constructores

    def __init__(self) -> None:
        self.root = ttk.Window(themename='flatly')
        self.root.title('UNAL - Control de Asistencia')
        self.root.state('zoomed')
        self.MostrarHeader()
        FrLogin(self)
        self.root.mainloop()

    # endregion

    # region Funciones

    def MostrarHeader(self):
        self.frameHeader = ttk.Frame(self.root)
        self.frameHeader.grid(row=0, column=0)
        logo = ttk.PhotoImage(file="UserInterface\Images\Logo.png")
        labelLogo = ttk.Label(self.frameHeader, image=logo, width=30)
        labelLogo.grid(row=0, column=0)
        title = ttk.Label(self.frameHeader, text="UNAL - Sistema de asistencia",
                        bootstyle='success', font=('Helvetica', 30), width=40)
        title.grid(row=0, column=1)

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

    def ConfigurarMenu(self):
        frameButtons = ttk.Frame(self.root)
        frameButtons.grid(row=2, column=0)
        match self.objInicioSesion.TipoUsuario:
            case EnTipoUsuario.Administrador:
                btnDocentes = ttk.Button(
                    frameButtons, text='Administrar docentes', bootstyle='success')
                btnDocentes.grid(column=0, row=0, padx=5)
                btnEstudiantes = ttk.Button(
                    frameButtons, text='Administrar estudiantes', bootstyle='success')
                btnEstudiantes.grid(column=1, row=0, padx=5)
                btnAsignaturas = ttk.Button(
                    frameButtons, text='Administrar asignaturas', bootstyle='success')
                btnAsignaturas.grid(column=2, row=0, padx=5)
            case EnTipoUsuario.Estudiante:
                btnAsistencia = ttk.Button(
                    frameButtons, text='Consultar asistencia', bootstyle='success')
                btnAsistencia.grid(column=0, row=0, padx=5)
            case EnTipoUsuario.Docente:
                btnClase = ttk.Button(
                    frameButtons, text='Iniciar clase', bootstyle='success')
                btnClase.grid(column=0, row=0, padx=5)
                btnAñadir = ttk.Button(
                    frameButtons, text='Añadir estudiante', bootstyle='success')
                btnAñadir.grid(column=0, row=0, padx=5)

    def onAfterLogin(self, mdInicioSesion: MdInicioSesion):
        self.objInicioSesion = mdInicioSesion
        self.MostrarInfo()
        self.ConfigurarMenu()

    #endregion

    # region Eventos
  
    def onBtnCerrarSesion_onClick(self):
        self.frameInfo.destroy()
        self.objInicioSesion = None
        FrLogin(self)

    # endregion

objInit = FrMain()