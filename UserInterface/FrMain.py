import sys
sys.path.append("Models")

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from MdInicioSesion import MdInicioSesion
from FrLogin import FrLogin
from EnEnum import EnTipoUsuario

#region Eventos

def onAfterLogin(mdInicioSesion: MdInicioSesion):
    global objInicioSesion
    objInicioSesion = mdInicioSesion
    ConfigurarMenu()

def ConfigurarMenu():
    match objInicioSesion.TipoUsuario:
        case EnTipoUsuario.Administrador:
            btnDocentes = ttk.Button(root, text='Administrar docentes', bootstyle='success').grid(row=0, column=0, sticky="ew")
            ttk.Frame.columnconfigure(0, weight=1)
            btnEstudiantes = ttk.Button(root, text='Administrar estudiantes', bootstyle='success').grid(row=0, column=1)
            btnAsignaturas = ttk.Button(root, text='Administrar asignaturas', bootstyle='success').grid(row=1, column=0)
        case EnTipoUsuario.Estudiante:
            btnAsistencia = ttk.Button(root, text='Consultar asistencia', bootstyle='success').grid(row=5)
        case EnTipoUsuario.Docente:
            btnClase = ttk.Button(root, text='Iniciar clase', bootstyle='success').grid(row=0, column=0)
            btnAñadir = ttk.Button(root, text='Añadir estudiante', bootstyle='success').grid(row=0, column=4)
#endregion

#region Formulario

root = ttk.Window(themename='flatly')
root.title('UNAL - Control de Asistencia')
root.state('zoomed')
FrLogin(root, onAfterLogin)

root.mainloop()

#endregion 
