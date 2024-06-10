# PYControlAsistencia
Proyecto de control de asistencia UNAL

Este proyecto consiste en la creación de un sistema de registro de asistencia enfocado en el ámbito académico universitario por medio de reconocimiento facial.

Este proyecto permite el registro de maestros y estudiantes, de forma que cada rol pueda revisar la información que le compete.

Los maestros pueden crear clases y añadir estudiantes ya registrados en el sistema a cada una de sus clases. De esta manera, el sistema de reconocimiento facial sabe que rostros de los estudiantes buscar por medio de la cámara.

Los maestros podrán iniciar clases y por medio de una cámara (sea la de un portátil o externa) podrán dar inicio al sistema de reconocimiento facial, en los cuales se registrará como asistidos a los estudiantes reconocidos por el sistema. 

Posteriormente, el maestro podrá dar la clase por finalizada y podrá ver un registro presentado de forma elegante de los estudiantes que asistieron y los que no. Teniendo incluso la opción de importar el registro en un archivo csv, por si se quiere exportar a otro software como excel.

El maestro también puede cambiar que tan exigente es el sistema de reconocimiento facial para reconocer un rostro, mientras más exigente menos probabilidad de falsos positivos, pero también puede que no reconozca un rostro aunque esté en la cámara. Es sistema trae por default la exigencia recomendada que permite su mejor rendimiento y precisión.


Para que el programa funcione, debes tener instalado un compilador de c++ (Como el de Visual Studio). Varias librerías de Python como  face recognition, cv2 y TKInter bootstrap.
Sin mencionar que hay que contar con SQLServer con las distintas tablas y relaciones pertinentes.
Posteriormente decidiré si desplegar un ejecutable para ahorrarles todos estos pasos. Por mientras, aprecien el código :3.
