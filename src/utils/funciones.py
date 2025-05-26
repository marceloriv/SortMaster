def ruta():
    """
    Abre un diálogo para seleccionar un directorio y devuelve la ruta completa del directorio seleccionado.

    Returns:
        str: Ruta completa del directorio seleccionado o una cadena vacía si se cancela.
    """
    import tkinter as tk
    from tkinter import filedialog

    # Crear una ventana raíz oculta
    root = tk.Tk()
    root.withdraw()

    # Mostrar el diálogo para seleccionar directorio
    ruta_directorio = filedialog.askdirectory(
        title="Seleccionar directorio",
    )

    # Destruir la ventana raíz
    root.destroy()

    return ruta_archivo
