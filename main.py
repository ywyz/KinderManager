import sys
from PyQt6.QtWidgets import QApplication, QWidget
from UI.Login import Ui_Login
from qt_material import apply_stylesheet

if __name__ == "__main__":

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    widget = QWidget()
    widget.setObjectName("MyWidget")
    widget.setStyleSheet("#MyWidget{border-image:url(Background.png);}")
    ui = Ui_Login()
    ui.setupUi(widget)

    widget.show()
    sys.exit(app.exec())