import sys
from tkinter.ttk import Entry
sys.path.append("Models")
from MdUsuario import MdUsuario
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdInicioSesion import MdInicioSesion
from EnEnum import EnTipoUsuario

#region Eventos

def btnInicio_onClick():
    mdFormulario = MdInicioSesion()
    mdFormulario.Usuario = txtUsuario.get()
    mdFormulario.Password = txtPassword.get()
    match cbTipoUsuario.get():
        case 'Docente':
            mdFormulario.TipoUsuario = EnTipoUsuario.Docente
        case 'Estudiante':
            mdFormulario.TipoUsuario = EnTipoUsuario.Estudiante
        case 'Administrador':
            mdFormulario.TipoUsuario = EnTipoUsuario.Administrador
    if MdUsuario.ValidarUsuario(mdFormulario):
        print('Usuario Autenticado')
    else:
        print('Usuario o Constraseña invalida!!')

#endregion

#region Formulario

root = ttk.Window(themename='flatly')
root.title('UNAL - Control de Asistencia')
# root.iconbitmap('Images/Icono.png')
root.geometry('500x350')

lbTitulo = ttk.Label(root, text='Inicio de Sesión', font=('Helvetica', 24), bootstyle="success")
lbTitulo.pack(pady=30)

lbTipoCuenta = ttk.Label(root,text='Tipo de cuenta:', bootstyle="success")
lbTipoCuenta.pack(pady=2)

TiposUsuario = ['Administrador','Docente', 'Estudiante']

cbTipoUsuario = ttk.Combobox(root, style=SUCCESS, state="readonly", values=TiposUsuario)
cbTipoUsuario.pack(pady=2)
cbTipoUsuario.current(0)

lbUsuario = ttk.Label(root,text='Usuario:', bootstyle="success")
lbUsuario.pack(pady=3)
txtUsuario = ttk.Entry(root, bootstyle="success")
txtUsuario.pack(pady=2)

lbPassword = ttk.Label(root,text='Password:', bootstyle="success")
lbPassword.pack(pady=2)
txtPassword = ttk.Entry(root, show='*', bootstyle="success")
txtPassword.pack(pady=2)

btnInicio = ttk.Button(root, text='Iniciar sesión', command=btnInicio_onClick,  bootstyle='success')
btnInicio.pack(pady=10)

root.mainloop()

#endregion 
