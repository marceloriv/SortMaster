import unittest
from unittest.mock import patch, MagicMock, Mock
import sys
import os

# Agregar el directorio src al path para las importaciones
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


class TestMain(unittest.TestCase):

    @patch('builtins.print')
    @patch('utils.funciones.ruta')
    def test_main_prints_welcome_message(self, mock_ruta, mock_print):
        """Prueba que main() imprime el mensaje de bienvenida."""
        mock_ruta.return_value = "/test/path"
        
        main()
        
        # Verificar que se llamó a print con el mensaje de bienvenida
        mock_print.assert_any_call("Bienvenido a la aplicación de Python!")
        # Verificar que se llamó a print con la ruta
        mock_print.assert_any_call("Ruta seleccionada:", "/test/path")

    @patch('utils.funciones.ruta')
    def test_main_calls_ruta_function(self, mock_ruta):
        """Prueba que main() llama a la función ruta()."""
        mock_ruta.return_value = "/test/path"
        
        main()
        
        # Verificar que se llamó a la función ruta
        mock_ruta.assert_called_once()


class TestFunciones(unittest.TestCase):

    @patch('utils.funciones.tk.Tk')
    @patch('utils.funciones.filedialog.askdirectory')
    def test_ruta_returns_selected_directory(self, mock_askdirectory, mock_tk):
        """Prueba que ruta() retorna el directorio seleccionado."""
        # Importar aquí para evitar problemas si tkinter no está disponible
        from utils import funciones
        
        mock_askdirectory.return_value = "/selected/directory"
        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        
        result = funciones.ruta()
        
        # Verificar que se retorna el directorio correcto
        self.assertEqual(result, "/selected/directory")
        # Verificar que se llamó withdraw en la ventana
        mock_root.withdraw.assert_called_once()
        # Verificar que se llamó destroy en la ventana
        mock_root.destroy.assert_called_once()

    @patch('utils.funciones.tk.Tk')
    @patch('utils.funciones.filedialog.askdirectory')
    def test_ruta_returns_empty_string_on_cancel(self, mock_askdirectory, mock_tk):
        """Prueba que ruta() retorna cadena vacía cuando se cancela."""
        # Importar aquí para evitar problemas si tkinter no está disponible
        from utils import funciones
        
        mock_askdirectory.return_value = ""
        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        
        result = funciones.ruta()
        
        # Verificar que se retorna cadena vacía
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()