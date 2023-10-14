import sys
sys.path.append("Models")
from ttkbootstrap.dialogs import Messagebox, MessageDialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdUsuario import MdUsuario
from MdInicioSesion import MdInicioSesion
from EnEnum import EnTipoUsuario
from FcUtilidades import CentrarPantalla

class FrLogin():
    objMain: any
    root: ttk.Toplevel
    txtUsuario: ttk.Entry
    txtPassword: ttk.Entry
    cbTipoUsuario: ttk.Combobox

    def __init__(self, objMain) -> None:
        self.objMain = objMain
        self.MostrarLogin()

    def MostrarLogin(self):

        self.root = ttk.Toplevel(self.objMain.root, topmost=True, resizable=(False, False))
        self.root.title('UNAL - Control de Asistencia - Inicio Sesión')
        geometryLogin = CentrarPantalla(self.objMain.root.winfo_screenwidth(), self.objMain.root.winfo_screenheight(), 480, 350)
        self.root.geometry(geometryLogin)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        frContent = ttk.Frame(self.root)
        frContent.grid(column=0, row=0, padx=70, sticky=(N, W, E, S))

        lbTitulo = ttk.Label(frContent, text='Inicio de Sesión',
                            font=('Helvetica', 24), bootstyle="success",)
        lbTitulo.grid(column=0, row=0, pady=50, columnspan=2)

        lbTipoCuenta = ttk.Label(
            frContent, text='Tipo de cuenta:', bootstyle="success", width=20, anchor='e')
        lbTipoCuenta.grid(column=0, row=1, pady=5)

        TiposUsuario = ['Docente', 'Estudiante','Administrador']
        self.cbTipoUsuario = ttk.Combobox(
            frContent, style=SUCCESS, state="readonly", values=TiposUsuario, width=30,)
        self.cbTipoUsuario.grid(column=1, row=1, pady=5)
        self.cbTipoUsuario.current(0)

        lbUsuario = ttk.Label(frContent, text='Usuario:', bootstyle="success", width=20, anchor='e')
        lbUsuario.grid(column=0, row=2, pady=5)
        self.txtUsuario = ttk.Entry(frContent, bootstyle="success", width=32)
        self.txtUsuario.grid(column=1, row=2, pady=5)

        lbPassword = ttk.Label(frContent, text='Password:', bootstyle="success", width=20, anchor='e')
        lbPassword.grid(column=0, row=3, pady=5)
        self.txtPassword = ttk.Entry(frContent, show='*', bootstyle="success", width=32)
        self.txtPassword.grid(column=1, row=3, pady=5)

        btnInicio = ttk.Button(frContent, text='Iniciar sesión',
                            command=self.onBtnInicio_onClick,  bootstyle='success', width=30)
        btnInicio.grid(column=0, row=4, pady=30, columnspan=2)

        self.root.wait_window()
    
    # region Eventos

    def onBtnInicio_onClick(self):
        mdInicioSesion = MdInicioSesion()
        mdInicioSesion.Usuario = self.txtUsuario.get()
        mdInicioSesion.Password = self.txtPassword.get()
        match self.cbTipoUsuario.get():
            case 'Docente':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Docente
            case 'Estudiante':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Estudiante
            case 'Administrador':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Administrador
        if MdUsuario.ValidarUsuario(mdInicioSesion):
            mdInicioSesion.IsLogin = True
            self.root.destroy()
            self.objMain.onAfterLogin(mdInicioSesion)
        else:
            warning = Messagebox.show_warning('Usuario o Constraseña invalida!!', parent=self.root, title='UNAL')
    # endregion
