import sys
sys.path.append("Models")
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdInicioSesion import MdInicioSesion
from MdDocente import MdDocente
from MdEstudiante import MdEstudiante

#region Eventos

def btnInicio_onClick():
    if not(cbTipoCuenta.get() in TipoCuentas):
        print('Tipo de cuenta no válida')
        pass
    mdFormulario = MdInicioSesion()
    mdFormulario.Usuario = txtUsuario.get()
    mdFormulario.Password = txtPassword.get()
    if cbTipoCuenta.get() == TipoCuentas[0]:
        print('Buscando...')
        MdDocente.ValidarUsuario(mdFormulario.Usuario, mdFormulario.Password)
    else:
        MdEstudiante.ValidarUsuario(mdFormulario.Usuario, mdFormulario.Password)
        print('Buscando...')


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

TipoCuentas = ['Docente', 'Estudiante']

cbTipoCuenta = ttk.Combobox(root, style=SUCCESS, values=TipoCuentas)
cbTipoCuenta.pack(pady=2)
cbTipoCuenta.current(0)

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
