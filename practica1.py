import os
directory = "notas"
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directorio '{directory}' creado.")
else:
    print(f"El directorio '{directory}' ya existe.")
