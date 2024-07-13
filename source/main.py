from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QApplication, QFrame, QGraphicsDropShadowEffect, QTabWidget)
from db.ConexionSQL import ConexionSQL
from views.view_login import FrameLogin
from views.view_signup import FrameRegister
from views.view_dashboard import FrameDashboard
import sys
import os

class BarrioSeguro(QWidget):

    def __init__(self):
        super().__init__()
        self.initComponents()
        self.RememberLogin()

    def initComponents(self):
        self.WindowConfig()   
        self.setConexionSQL()
        self.TabPrincipal()

    def WindowConfig(self):
        self.resize(366, 666)
        self.setLocationToCenter()
        self.setWindowTitle('Barrio Seguro')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def setConexionSQL(self):
        self.objConexionSQL = ConexionSQL()
        self.connection = self.objConexionSQL.ExecuteConnection()

    def TabPrincipal(self):

        PanelPrincipal = QFrame(self)
        PanelPrincipal.setGeometry(3, 3, 360, 660)

        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(10)
        ShadowWindow.setOffset(0.0, 0.0)
        PanelPrincipal.setGraphicsEffect(ShadowWindow)

        self.TabFrames = QTabWidget(PanelPrincipal)
        self.TabFrames.resize(360, 660)
        self.TabFrames.tabBar().hide()
        self.TabFrames.setObjectName("TabFrames")  
        self.TabFrames.setStyleSheet("#TabFrames::pane{border: 0;}")

        PanelLogin = FrameLogin(self, self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelLogin, 'Login_Account')

        PanelRegister = FrameRegister(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelRegister, 'Register_Account')

    def RememberLogin(self):
        try:
            result = ''
            with self.connection.cursor() as stm:
                stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]")
                result = stm.fetchone()

            if(result is not None):
                PanelDashboard = FrameDashboard(self.TabFrames, self.connection)
                self.TabFrames.addTab(PanelDashboard, 'Dashboard')
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameDashboard')))
            else:
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameLogin')))

        except Exception as e:
            print(e)

    def setLocationToCenter(self):
        screen_size = QApplication.primaryScreen().geometry()
        x = ((screen_size.width() - self.width())//2)
        y = ((screen_size.height() - self.height())//2)
        self.move(x , y)

    # Eventos
    def closeEvent(self, event):
        if os.path.exists("token.json"):
            os.remove("token.json")
        self.connection.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    objFrameLogin = BarrioSeguro()
    objFrameLogin.setVisible(True)
    sys.exit(app.exec())