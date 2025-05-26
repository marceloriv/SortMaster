# 🚀 SortMaster

![Licencia](https://img.shields.io/badge/Licencia-MIT-green)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow)

## 📋 Descripción

SortMaster es una herramienta diseñada para organizar y gestionar archivos automáticamente. Permite seleccionar una carpeta a través de una interfaz gráfica y procesar sus contenidos según criterios configurables.

## ✨ Características

- Selección de carpetas mediante interfaz gráfica intuitiva
- Organización automática de archivos
- Personalización de reglas de clasificación
- Interfaz limpia y fácil de usar

---

## 🗂️ Estructura del Proyecto

```bash
SortMaster
├── src
│   ├── main.py          # Punto de entrada de la aplicación
│   └── utils
│       └── __init__.py  # Paquete de utilidades
├── tests
│   ├── __init__.py      # Paquete de pruebas
│   └── test_main.py     # Pruebas unitarias para main.py
├── requirements.txt      # Dependencias del proyecto
├── .gitignore            # Archivos y directorios a ignorar por Git
├── setup.py              # Información del paquete
└── README.md             # Documentación del proyecto
```

---

## 🔧 Requisitos

- Python 3.6 o superior
- Acceso a interfaz gráfica (para diálogos de selección de archivos)
- Bibliotecas especificadas en `requirements.txt`

## ⚙️ Instalación

1. Clone este repositorio:

   ```bash
   git clone https://github.com/su-usuario/SortMaster.git
   cd SortMaster
   ```

## Instalación

Para instalar las dependencias del proyecto, ejecute el siguiente comando:

```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar la aplicación, utilice el siguiente comando:

```bash
python src/main.py
```

## Pruebas

Para ejecutar las pruebas unitarias, puede utilizar `unittest` o `pytest`. Por ejemplo, para ejecutar las pruebas con `pytest`, ejecute:

```bash
pytest tests/test_main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o envíe un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo LICENSE para más detalles.
