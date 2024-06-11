from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QApplication, QFrame, QGraphicsDropShadowEffect, QTabWidget)
from db.ConexionSQL import ConexionSQL
from views.view_login import FrameLogin
from views.view_signup import FrameRegister, FrameEnterData_Register, FrameEnterEmergency_Contact
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

        PanelLogin = FrameLogin(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelLogin, 'Login_Account')

        PanelRegister = FrameRegister(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelRegister, 'Register_Account')

        PanelEnterData_Register = FrameEnterData_Register(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelEnterData_Register, 'EnterData_Register')

        PanelEnterEmergency_Contact = FrameEnterEmergency_Contact(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelEnterEmergency_Contact, 'EnterEmergency_Contact')

        PanelDashboard = FrameDashboard(self.TabFrames, self.connection)
        self.TabFrames.addTab(PanelDashboard, 'Dashboard')

    def setLocationToCenter(self):
        screen_size = QApplication.primaryScreen().geometry()
        x = ((screen_size.width() - self.width())//2)
        y = ((screen_size.height() - self.height())//2)
        self.move(x , y)

    def RememberLogin(self):
        try:
            self.statement = self.connection.cursor()
            self.statement.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]")
            result = self.statement.fetchone()

            if(result is not None):
                self.TabFrames.setCurrentIndex(4)
            else:
                self.TabFrames.setCurrentIndex(0)

        except Exception as e:
            print(e)

    # Eventos
    def closeEvent(self, event):
        if os.path.exists("token.json"):
            os.remove("token.json")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    objFrameLogin = BarrioSeguro()
    objFrameLogin.setVisible(True)
    sys.exit(app.exec())