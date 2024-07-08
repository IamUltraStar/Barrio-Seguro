from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import (QWidget, QApplication, QFrame, QLabel, QGraphicsDropShadowEffect, QLineEdit, QCheckBox, QPushButton)
from PyQt6.QtGui import QPixmap
from views.view_dashboard import FrameDashboard
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2 import id_token
import os

class FrameLogin(QFrame):

    objFrameLoginAlert = None
    ValorPass, valorshowPassword = True, True

    def __init__(self, MainWindow, TabFrames, conexionSQL):
        super().__init__()
        self.MainWindow = MainWindow
        self.TabFrames = TabFrames
        self.conexionSQL = conexionSQL
        self.installEventFilter(self)

        self.setObjectName("FrameLogin")
        self.BackgroundImage = QLabel(self)
        self.BackgroundImage.resize(360, 660)
        self.ResizeImage(self.BackgroundImage, 'img/fondo1-blur.png')

        LabelTitle = QLabel(self)
        LabelTitle.setText('BIENVENIDO')
        LabelTitle.setObjectName("LabelTitle")
        LabelTitle.setGeometry(100, 160, 160, 40)
        LabelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelTitle)

        self.userComponents()
        self.passwordComponents()
        self.buttonsComponents()
        self.initStyle()

    def userComponents(self):

        PanelUser = QFrame(self)
        PanelUser.setObjectName("InputPanel")
        PanelUser.setGeometry(45, 240, 270, 40)
        self.setShadowWidget(PanelUser)

        IconUser = QLabel(PanelUser)
        IconUser.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconUser, 'img/3.png')

        self.Input_User = QLineEdit(PanelUser)
        self.Input_User.setObjectName("InputText")
        self.Input_User.setGeometry(38, 10, 224, 20)
        self.Input_User.setPlaceholderText("Ingrese su usuario")
        
    def passwordComponents(self):

        PanelPassword = QFrame(self)
        PanelPassword.setObjectName("InputPanel")
        PanelPassword.setGeometry(45, 290, 270, 40)
        self.setShadowWidget(PanelPassword)

        IconPassword = QLabel(PanelPassword)
        IconPassword.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconPassword, 'img/candado.png')

        self.Input_Password = QLineEdit(PanelPassword)
        self.Input_Password.setText("") # Esto evita el lag al ingresar la contraseña
        self.Input_Password.setGeometry(38, 10, 195, 20)
        self.Input_Password.setObjectName("InputText")
        self.Input_Password.setPlaceholderText("Ingrese su contraseña")
        self.Input_Password.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.Input_Password.textChanged.connect(self.Input_PasswordKeyTyped)
        self.Input_Password.keyReleaseEvent = self.Input_PasswordKeyReleased
        
        self.IconShowPassword = QLabel(PanelPassword)
        self.IconShowPassword.setGeometry(234, 10, 20, 20)
        self.IconShowPassword.setCursor(Qt.CursorShape.PointingHandCursor)
        self.IconShowPassword.setEnabled(False)

        self.IconShowPassword.mouseReleaseEvent = self.IconShowPasswordMouseClicked

    def buttonsComponents(self):

        ButtonEntrar = QPushButton(self)
        ButtonEntrar.setText("Iniciar sesión")
        ButtonEntrar.setGeometry(45, 340, 270, 40)
        ButtonEntrar.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ButtonEntrar.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonEntrar.setObjectName("ButtonIn")
        self.setShadowWidget(ButtonEntrar)

        ButtonEntrar.clicked.connect(self.ButtonEntrarMouseClicked)

        Separator = QFrame(self)
        Separator.setGeometry(53, 401, 117, 2)
        Separator.setStyleSheet("background-color: white;")
        self.setShadowWidget(Separator)

        label = QLabel(self)
        label.setGeometry(170, 390, 20, 20)
        label.setObjectName("LabelSuggestion")
        label.setText("o")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(label)

        Separator_1 = QFrame(self)
        Separator_1.setGeometry(190, 401, 117, 2)
        Separator_1.setStyleSheet("background-color: white;")
        self.setShadowWidget(Separator_1)

        ButtonGoogle = QPushButton(self)
        ButtonGoogle.setText("Iniciar sesión con Google")
        ButtonGoogle.setGeometry(45, 420, 270, 40)
        ButtonGoogle.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ButtonGoogle.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonGoogle.setObjectName("ButtonGoogle")
        self.setShadowWidget(ButtonGoogle)

        ButtonGoogle.clicked.connect(self.ButtonGoogleMouseClicked)

        IconGoogle = QLabel(ButtonGoogle)
        IconGoogle.setGeometry(47, 10, 20, 20)
        IconGoogle.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconGoogle, 'img/google_logo.png')
        self.setShadowWidget(IconGoogle)

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setGeometry(70, 500, 220, 20)
        LabelSuggestion.setText("No está registrado? Regístrese ahora")
        LabelSuggestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LabelSuggestion.setObjectName("LabelSuggestion")
        self.setShadowWidget(LabelSuggestion)

        LabelSuggestion.mouseReleaseEvent = self.LabelSuggestionMouseClicked

    def get_credentials(self):
        scopes = ["openid", "https://www.googleapis.com/auth/userinfo.email"]
        cred_file = 'credentials.json'

        try:
            if os.path.exists('token.json'):
                with open('token.json', 'r') as token:
                    creds = Credentials.from_authorized_user_file('token.json', scopes)
            else:
                flow = InstalledAppFlow.from_client_secrets_file(cred_file, scopes)
                creds = flow.run_local_server(port=0)

                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
        except Exception as e:
            print(f"Error al obtener las credenciales: {e}")
            creds = None

        return creds

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(20)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    def initStyle(self):
        with open('source/css/styleLogin.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    def ExecuteLogin(self):
        self.valorLogin = False
        try:
            self.statement = self.conexionSQL.cursor()
            self.statement.execute("SELECT U_User,U_Password FROM [BarrioSeguro].[dbo].[Usuario]")
            result = self.statement.fetchall()

            for row in result:
                if((row[0] == self.Input_User.text()) and (row[1] == self.Input_Password.text())):
                    self.valorLogin = True

            if(self.valorLogin):
                with self.conexionSQL.cursor() as stm:
                    stm.execute("INSERT INTO [BarrioSeguro].[dbo].[RememberLogin] (R_Usuario) VALUES (?)", (self.SaveUser))
                self.ResetStylePassword()
                PanelDashboard = FrameDashboard(self.TabFrames, self.conexionSQL)
                self.TabFrames.addTab(PanelDashboard, 'Dashboard')
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameDashboard')))
            else:
                self.setEnabled(False)
                self.objFrameLoginAlert = FrameLoginAlert(self)
                self.objFrameLoginAlert.setVisible(True)
        except Exception as e:
            print(e)

    def ResetStylePassword(self):
        self.Input_Password.setText('')
        if(self.Input_User.text() != ''):
            self.Input_Password.setFocus()

    def setNone_FrameLoginAlert(self):
        self.objFrameLoginAlert = None

    # Eventos
    def Input_PasswordKeyReleased(self, event):
        if(event.key() == Qt.Key.Key_Return):
            self.SaveUser = self.Input_User.text()
            self.ExecuteLogin()

    def Input_PasswordKeyTyped(self, text):
        isEmptyPassword = len(text) == 0

        if(isEmptyPassword):
            self.IconShowPassword.setPixmap(QPixmap())
            self.IconShowPassword.setEnabled(False)
            self.Input_Password.setEchoMode(QLineEdit.EchoMode.Password)
            self.ValorPass, self.valorshowPassword = True, True
        elif(self.ValorPass):
            self.ResizeImage(self.IconShowPassword, 'img/show.png')
            self.IconShowPassword.setEnabled(True)
            self.ValorPass = False

    def IconShowPasswordMouseClicked(self, event):
        if(self.IconShowPassword.isEnabled()):
            if(self.valorshowPassword):
                self.ResizeImage(self.IconShowPassword, 'img/hide.png')
                self.Input_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.ResizeImage(self.IconShowPassword, 'img/show.png')
                self.Input_Password.setEchoMode(QLineEdit.EchoMode.Password)

            self.valorshowPassword = not self.valorshowPassword

    def ButtonEntrarMouseClicked(self):
        self.SaveUser = self.Input_User.text()
        self.ExecuteLogin()

    def ButtonGoogleMouseClicked(self):
        creds = self.get_credentials()
        if creds:
            try:
                request = Request()
                id_info = id_token.verify_oauth2_token(creds.id_token, request)
            except ValueError as e:
                print(f"Invalid token: {e}")
            try:
                print(id_info.get('email'))
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameDashboard')))
            except Exception as e:
                print(f"Failed to get user info: {e}")
        else:
            print("Authentication failed")

    def LabelSuggestionMouseClicked(self, event):
        self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameRegister')))
        self.Input_User.setText('')
        self.ResetStylePassword()

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameLoginAlert != None):
            self.objFrameLoginAlert.raise_()
            self.objFrameLoginAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameLoginAlert(QWidget):

    def __init__(self, FrameLogin):
        super().__init__()
        self.objFrameLogin = FrameLogin
        self.initcomponents()

    def initcomponents(self):
        self.WindowConfig()   
        self.FrameComponents()
        self.initStyle()

    def WindowConfig(self):
        self.resize(276, 96)
        self.setLocationToCenter()
        self.installEventFilter(self)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Tool)

    def FrameComponents(self):
        PanelPrincipal = QFrame(self)
        PanelPrincipal.setGeometry(3, 3, 270, 90)
        PanelPrincipal.setObjectName("MainPanel")
        self.setShadowWidget(PanelPrincipal)

        self.LabelMessage = QLabel(PanelPrincipal)
        self.LabelMessage.setGeometry(45, 20, 180, 20)
        self.LabelMessage.setObjectName("LabelMessage")
        self.LabelMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelMessage.setText("Usuario o Contraseña incorrecto.")
        
        ButtonOk = QPushButton(PanelPrincipal)
        ButtonOk.setGeometry(110, 50, 50, 25)
        ButtonOk.setText('OK')
        ButtonOk.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(ButtonOk)
        
        ButtonOk.clicked.connect(self.ButtonOkMouseClicked)

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def setLocationToCenter(self):
        screen_size = QApplication.primaryScreen().geometry()
        x = ((screen_size.width() - self.width())//2)
        y = ((screen_size.height() - self.height())//2)
        self.move(x , y)

    def initStyle(self):
        with open('source/css/styleLoginAlert.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    # Eventos
    def ButtonOkMouseClicked(self, event):
        self.objFrameLogin.setEnabled(True)
        self.objFrameLogin.ResetStylePassword()
        self.close()
        self.objFrameLogin.setNone_FrameLoginAlert()

    def showEvent(self, event):
        self.activateWindow()
        return super().showEvent(event)

    def keyReleaseEvent(self, event):
        if(event.key() == Qt.Key.Key_Return):
            self.objFrameLogin.setEnabled(True)
            self.objFrameLogin.ResetStylePassword()
            self.close()
            self.objFrameLogin.setNone_FrameLoginAlert()
        return super().keyReleaseEvent(event)
