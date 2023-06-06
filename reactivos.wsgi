import os
import sys

# Ruta al directorio del proyecto
path = 'C:/Inventario_Reactivos'
if path not in sys.path:
    sys.path.insert(0, path)

# Activa el entorno virtual si lo estás utilizando
activate_this = os.path.join(path, 'venv/bin/activate')
exec(compile(open(activate_this, 'rb').read(), activate_this, 'exec'), dict(__file__=activate_this))

# Importa la aplicación de tu proyecto
from reactivos import app as application
