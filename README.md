# **HMI para Robot**
Este repositorio contiene una versión anterior de la interfaz de usuario (HMI) desarrollada como parte de mi estancia preprofesional en la Universidad de Almería. Esta versión sirve como referencia antes de la entrega final al grupo de investigación de la universidad.

## *Descripción*
La interfaz de usuario fue diseñada y desarrollada utilizando Qt Designer, una herramienta poderosa para la creación rápida de interfaces gráficas de usuario. Durante el proceso, se hicieron uso de varias bibliotecas de Python que facilitaron la implementación y mejora de la interfaz. Las librerías principales utilizadas son:

- [PyQt5](https://pypi.org/project/PyQt5/#:~:text=PyQt5%20is%20a%20comprehensive%20set,platforms%20including%20iOS%20and%20Android.): PyQt5 proporciona enlaces Python para la biblioteca Qt y se utiliza para crear aplicaciones de escritorio con interfaces gráficas.

- [PySide2](https://pypi.org/project/PySide2/#:~:text=PySide2%20is%20the%20official%20Python,and%20an%20open%20design%20process.): PySide2 es otro conjunto de enlaces Python para Qt y se eligió por su compatibilidad con la versión 5 de Qt.

- [QT-PyQt-PySide-Custom-Widgets](https://pypi.org/project/QT-PyQt-PySide-Custom-Widgets/): Este conjunto de widgets personalizados proporciona componentes adicionales que enriquecen la apariencia y funcionalidad de la interfaz.

## **Estructura del Repositorio**
- /caras: Carpeta que contiene imágenes de caras utilizadas en la interfaz.
- /icons: Carpeta que almacena iconos utilizados en la interfaz.
- interfaz.py: Código fuente de la interfaz de usuario desarrollada en Qt Designer.
- interfaz.ui: Archivo de diseño de la interfaz creado en Qt Designer.
- logo1.png: Imagen de logo utilizada en la interfaz.
- main.py: Archivo principal que ejecuta la aplicación.
- resources.qrc: Archivo de recursos utilizado para la interfaz.
- resources_rc.py: Archivo generado a partir del archivo de recursos.
- style.json: Archivo que define las acciones de navegación y animación en la interfaz.

## **Uso**
Para utilizar esta versión de la interfaz de usuario, asegúrate de estar en un entorno virtual y tener instaladas las librerías mencionadas. Puedes instalarlas utilizando pip:
```pip install PyQt5 PySide2 QT-PyQt-PySide-Custom-Widgets```


## Recursos Adicionales
[Documentación de Qt Designer](https://doc.qt.io/qt-5/qtdesigner-manual.html): Referencia oficial para aprender a utilizar Qt Designer.
[Tutorial PyQt5](https://www.pythonguis.com/pyqt5-tutorial/): Recursos para aprender más sobre PyQt5.
[Qt for Python Documentation](https://doc.qt.io/qtforpython-5/contents.html): Documentación oficial de PySide2.
