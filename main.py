"""La HMI creada para el Agricobiot busca proporcionar una interfaz intuitiva y fácil de usar para los usuarios finales, 
permitiéndoles controlar y supervisar el funcionamiento del robot, así como visualizar los datos recopilados por 
los sensores y cámaras. La HMI se ha desarrollado con herramientas y tecnologías de última generación para garantizar 
su eficiencia y calidad, y se ha tenido en cuenta la experiencia del usuario en el diseño y la implementación.
"""

from interfaz import *
from Custom_Widgets.Widgets import *
import random
import sys


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        """init(self, parent=None): Constructor de la clase MainWindow que inicializa la ventana principal y carga la interfaz 
        de usuario utilizando el archivo generado por Qt Designer. También carga el estilo de la ventana desde un archivo JSON 
        y define los botones que expanden y colapsan el menú central y el menú derecho. Además, carga una serie de imágenes en 
        una lista y define un temporizador para cambiar la expresión facial de una imagen en un QLabel."""

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        loadJsonStyle(self, self.ui)

        #Expandir menu central
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #Cerrar menu central
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        #Expandir menu derecho
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        #Cerrar menu derecho
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        #Cerrar notificaciones
        self.ui.closeNotificaionBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        #Cargar imagenes con las expresiones (Cambiar ruta si es necesario o agregar mas caras)
        self.frames = [QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_1.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_2.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_3.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_4.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_5.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_6.png"),
                       QPixmap("/home/jonathan/ros2_ws/src/prueba_interfaz/interfaz/caras/cara_7.png")]
        
        self.frame_actual = 0
        self.ui.caras.setPixmap(self.frames[self.frame_actual])

        self.timer = QTimer()
        self.timer.timeout.connect(self.cambiar_expresion)
        self.timer.start(3000)
        

        self.show()

    def cambiar_expresion(self):
        """Método que se ejecuta cuando el temporizador llega a su límite de tiempo. 
        Cambia la expresión facial de la imagen en el QLabel utilizando una imagen """
        self.frame_actual = random.randint(1,7)
        self.frame_actual = (self.frame_actual + 1) % len(self.frames)
        self.ui.caras.setPixmap(self.frames[self.frame_actual])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())