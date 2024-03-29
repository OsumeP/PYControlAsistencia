from ttkbootstrap.dialogs import Messagebox, MessageDialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdUsuario import MdUsuario
from MdInicioSesion import MdInicioSesion
from EnEnum import EnTipoUsuario
import sys
from tkinter import StringVar
sys.path.append("Models")


def FrLogin(root: ttk.Window, onCallBack) -> ttk.Toplevel:

    # region Eventos

    def btnInicio_onClick():
        mdInicioSesion = MdInicioSesion()
        mdInicioSesion.Usuario = txtUsuario.get()
        mdInicioSesion.Password = txtPassword.get()
        match cbTipoUsuario.get():
            case 'Docente':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Docente
            case 'Estudiante':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Estudiante
            case 'Administrador':
                mdInicioSesion.TipoUsuario = EnTipoUsuario.Administrador
        if MdUsuario.ValidarUsuario(mdInicioSesion):
            print('Usuario Autenticado')
            mdInicioSesion.IsLogin = True
            frLogin.destroy()
            onCallBack(mdInicioSesion)
        else:
            Messagebox.show_warning(
                'Usuario o Constraseña invalida!!', parent=frLogin)

    # endregion
    frLogin = ttk.Toplevel(root, topmost=True, resizable=(False, False))
    frLogin.title('UNAL - Control de Asistencia - Inicio Sesión')
    frLogin.geometry('480x350')
    frLogin.columnconfigure(0, weight=1)
    frLogin.rowconfigure(0, weight=1)

    frContent = ttk.Frame(frLogin)
    frContent.grid(column=0, row=0, padx=70, sticky=(N, W, E, S))

    lbTitulo = ttk.Label(frContent, text='Inicio de Sesión',
                         font=('Helvetica', 24), bootstyle="success")
    lbTitulo.grid(column=0, row=0, pady=50, columnspan=2)

    lbTipoCuenta = ttk.Label(
        frContent, text='Tipo de cuenta:', bootstyle="success", width=20)
    lbTipoCuenta.grid(column=0, row=1, pady=5)

    TiposUsuario = ['Administrador', 'Docente', 'Estudiante']
    cbTipoUsuario = ttk.Combobox(
        frContent, style=SUCCESS, state="readonly", values=TiposUsuario, width=30)
    cbTipoUsuario.grid(column=1, row=1, pady=5)
    cbTipoUsuario.current(0)

    lbUsuario = ttk.Label(frContent, text='Usuario:', bootstyle="success", width=20)
    lbUsuario.grid(column=0, row=2, pady=5)
    txtUsuario = ttk.Entry(frContent, bootstyle="success", width=32)
    txtUsuario.grid(column=1, row=2, pady=5)

    lbPassword = ttk.Label(frContent, text='Password:', bootstyle="success", width=20)
    lbPassword.grid(column=0, row=3, pady=5)
    txtPassword = ttk.Entry(frContent, show='*', bootstyle="success", width=32)
    txtPassword.grid(column=1, row=3, pady=5)

    btnInicio = ttk.Button(frContent, text='Iniciar sesión',
                           command=btnInicio_onClick,  bootstyle='success', width=30)
    btnInicio.grid(column=0, row=4, pady=30, columnspan=2)

    frLogin.wait_window()
