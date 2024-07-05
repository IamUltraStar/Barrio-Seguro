from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtWidgets import (QWidget, QFrame, QLabel, QGraphicsDropShadowEffect, QLineEdit, QCheckBox, QPushButton, QScrollArea, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt6.QtGui import QPixmap
from views.view_dashboard import FrameDashboard

class FrameRegister(QFrame):
    
    ValorPass, valorshowPassword = True, True
    ValorPass1, valorshowPassword1 = True, True
    objFrameAlert = None

    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames=TabFrames
        self.conexionSQL=conexionSQL
        self.installEventFilter(self)

        self.setObjectName("FrameRegister")
        BackgroundImage = QLabel(self)
        BackgroundImage.resize(360, 660)
        self.ResizeImage(BackgroundImage, 'img/fondo1-blur.png')

        LabelTitle = QLabel(self)
        LabelTitle.setText('REGISTRARSE')
        LabelTitle.setObjectName("LabelTitle")
        LabelTitle.setGeometry(90, 140, 180, 40)
        LabelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelTitle)

        self.userComponents()
        self.mailComponents()
        self.passwordComponents()
        self.buttonComponents()
        self.initStyle()

    def userComponents(self):
        PanelUser = QFrame(self)
        PanelUser.setObjectName("InputPanel")
        PanelUser.setGeometry(45, 220, 270, 40)
        self.setShadowWidget(PanelUser)

        IconUser = QLabel(PanelUser)
        IconUser.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconUser, 'img/3.png')

        self.Input_User = InputUserLineEdit(PanelUser)
        self.Input_User.setObjectName("InputText")
        self.Input_User.setGeometry(38, 10, 224, 20)
        self.Input_User.setPlaceholderText("Ingrese un usuario")
        self.Input_User.installEventFilter(self)

    def mailComponents(self):
        PanelMail = QFrame(self)
        PanelMail.setObjectName("InputPanel")
        PanelMail.setGeometry(45, 270, 270, 40)
        self.setShadowWidget(PanelMail)

        IconMail = QLabel(PanelMail)
        IconMail.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconMail, 'img/mail.png')

        self.Input_Mail = QLineEdit(PanelMail)
        self.Input_Mail.setObjectName("InputText")
        self.Input_Mail.setGeometry(38, 10, 224, 20)
        self.Input_Mail.setPlaceholderText("Ingrese un correo electronico")

    def passwordComponents(self):
        # Caja de Texto 1
        PanelPassword = QFrame(self)
        PanelPassword.setObjectName("InputPanel")
        PanelPassword.setGeometry(45, 320, 270, 40)
        self.setShadowWidget(PanelPassword)

        IconPassword = QLabel(PanelPassword)
        IconPassword.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconPassword, 'img/candado.png')

        self.Input_Password = QLineEdit(PanelPassword)
        self.Input_Password.setText("") # Esto evita el lag al ingresar la contraseña
        self.Input_Password.setGeometry(38, 10, 195, 20)
        self.Input_Password.setObjectName("InputText")
        self.Input_Password.setPlaceholderText("Ingrese una contraseña")
        self.Input_Password.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.Input_Password.textChanged.connect(self.Input_PasswordKeyTyped)
        
        self.IconShowPassword = QLabel(PanelPassword)
        self.IconShowPassword.setGeometry(234, 10, 20, 20)
        self.IconShowPassword.setCursor(Qt.CursorShape.PointingHandCursor)
        self.IconShowPassword.setEnabled(False)

        self.IconShowPassword.mouseReleaseEvent = self.IconShowPasswordMouseClicked

        # Caja de texto 2
        PanelPassword1 = QFrame(self)
        PanelPassword1.setObjectName("InputPanel")
        PanelPassword1.setGeometry(45, 370, 270, 40)
        self.setShadowWidget(PanelPassword1)

        IconPassword1 = QLabel(PanelPassword1)
        IconPassword1.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconPassword1, 'img/candado.png')

        self.Input_Password1 = QLineEdit(PanelPassword1)
        self.Input_Password1.setText("") # Esto evita el lag al ingresar la contraseña
        self.Input_Password1.setGeometry(38, 10, 195, 20)
        self.Input_Password1.setObjectName("InputText")
        self.Input_Password1.setPlaceholderText("Confirme su contraseña")
        self.Input_Password1.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.Input_Password1.textChanged.connect(self.Input_Password1KeyTyped)
        
        self.IconShowPassword1 = QLabel(PanelPassword1)
        self.IconShowPassword1.setGeometry(234, 10, 20, 20)
        self.IconShowPassword1.setCursor(Qt.CursorShape.PointingHandCursor)
        self.IconShowPassword1.setEnabled(False)

        self.IconShowPassword1.mouseReleaseEvent = self.IconShowPassword1MouseClicked

    def buttonComponents(self):

        self.CheckTerms = QCheckBox(self)
        self.CheckTerms.setText("Acepto los Términos y Condiciones de Uso.")
        self.CheckTerms.setGeometry(59, 424, 234, 14)
        self.CheckTerms.setObjectName("RememberCheck")
        self.CheckTerms.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.CheckTerms.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(self.CheckTerms)

        ButtonRegistrarse = QPushButton(self)
        ButtonRegistrarse.setText("Registrarse")
        ButtonRegistrarse.setGeometry(45, 452, 270, 40)
        ButtonRegistrarse.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ButtonRegistrarse.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonRegistrarse.setObjectName("ButtonIn")
        self.setShadowWidget(ButtonRegistrarse)

        ButtonRegistrarse.clicked.connect(self.ButtonRegistrarseMouseClicked)

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setGeometry(30, 532, 300, 20)
        LabelSuggestion.setText("Está registrado? Inicie sesión ahora")
        LabelSuggestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LabelSuggestion.setObjectName("LabelSuggestion")
        self.setShadowWidget(LabelSuggestion)

        LabelSuggestion.mouseReleaseEvent = self.LabelSuggestionMouseClicked

    def verifyErrors(self):
        domains = ['@gmail.com','@hotmail.com','@outlook.com']
        if(self.Input_User.text() == ''):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Ingrese un usuario")
            self.objFrameAlert.setVisible(True)
            return False

        if not any(self.Input_Mail.text().endswith(domain) for domain in domains):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Ingrese un correo válido")
            self.objFrameAlert.setVisible(True)
            return False

        if(self.Input_Password.text() == '' and self.Input_Password1.text() == ''):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Ingrese una contraseña")
            self.objFrameAlert.setVisible(True)
            return False

        if(self.Input_Password.text() != self.Input_Password1.text()):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Las contraseñas no coinciden")
            self.objFrameAlert.setVisible(True)
            return False
        
        if not self.CheckTerms.isChecked():
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Acepte los Terminos y Condiciones")
            self.objFrameAlert.setVisible(True)
            return False
        return True
     
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

    def setNone_FrameAlert(self):
        self.objFrameAlert = None

    # Eventos
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

    def Input_Password1KeyTyped(self, text):
        isEmptyPassword = len(text) == 0

        if(isEmptyPassword):
            self.IconShowPassword1.setPixmap(QPixmap())
            self.IconShowPassword1.setEnabled(False)
            self.Input_Password1.setEchoMode(QLineEdit.EchoMode.Password)
            self.ValorPass1, self.valorshowPassword1 = True, True
        elif(self.ValorPass1):
            self.ResizeImage(self.IconShowPassword1, 'img/show.png')
            self.IconShowPassword1.setEnabled(True)
            self.ValorPass1 = False

    def IconShowPassword1MouseClicked(self, event):
        if(self.IconShowPassword1.isEnabled()):
            if(self.valorshowPassword1):
                self.ResizeImage(self.IconShowPassword1, 'img/hide.png')
                self.Input_Password1.setEchoMode(QLineEdit.EchoMode.Normal)
            else:
                self.ResizeImage(self.IconShowPassword1, 'img/show.png')
                self.Input_Password1.setEchoMode(QLineEdit.EchoMode.Password)

            self.valorshowPassword1 = not self.valorshowPassword1

    def ButtonRegistrarseMouseClicked(self):
        if(self.verifyErrors()):
            try:
                with self.conexionSQL.cursor() as stm:
                    stm.execute("INSERT INTO [BarrioSeguro].[dbo].[RememberLogin] (R_Usuario) VALUES (?)", (self.Input_User.text()))
                with self.conexionSQL.cursor() as stm:
                    stm.execute("INSERT INTO [BarrioSeguro].[dbo].[Usuario] (U_User, U_Password, CorreoElectronico, DNI, FullName, NTelefono, Direccion) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.Input_User.text(), self.Input_Password.text(), self.Input_Mail.text(), "None", "None", "None", "None"))
                PanelEnterData_Register = FrameEnterData_Register(self.TabFrames, self.conexionSQL)
                self.TabFrames.addTab(PanelEnterData_Register, 'EnterData_Register')
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameEnterData_Register')))
                self.close()
            except Exception as e:
                print(e)
                # Agregar una alerta cuando el usuario a crear ya exista

    def LabelSuggestionMouseClicked(self, event):
        self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameLogin')))
        self.Input_User.setText('')
        self.Input_Mail.setText('')
        self.Input_Password.setText('')
        self.Input_Password1.setText('')
        self.CheckTerms.setChecked(False)
        self.Input_User.setFocus()

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlert != None):
            self.objFrameAlert.raise_()
            self.objFrameAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameEnterData_Register(QFrame):

    objFrameAlert = None

    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames = TabFrames
        self.conexionSQL = conexionSQL

        self.setObjectName("MainPanel")
        BackgroundImage = QLabel(self)
        BackgroundImage.resize(360, 660)
        self.ResizeImage(BackgroundImage, 'img/fondo1-blur.png')

        LabelTitle = QLabel(self)
        LabelTitle.setText('COMPLETE SUS DATOS')
        LabelTitle.setObjectName("LabelTitle")
        LabelTitle.setGeometry(30, 140, 300, 40)
        LabelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelTitle)

        self.fullNameComponents()
        self.numberPhoneComponents()
        self.addressComponents()
        self.dniComponents()
        self.buttonComponents()
        self.initStyle()

    def fullNameComponents(self):
        PanelFullName = QFrame(self)
        PanelFullName.setObjectName("InputPanel")
        PanelFullName.setGeometry(45, 220, 270, 40)
        self.setShadowWidget(PanelFullName)

        IconFullName = QLabel(PanelFullName)
        IconFullName.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconFullName, 'img/usuario.png')

        self.Input_FullName = InputFullNameLineEdit(PanelFullName)
        self.Input_FullName.setObjectName("InputText")
        self.Input_FullName.setGeometry(38, 10, 224, 20)
        self.Input_FullName.setPlaceholderText("Nombres completos")

    def numberPhoneComponents(self):
        PanelNumberPhone = QFrame(self)
        PanelNumberPhone.setObjectName("InputPanel")
        PanelNumberPhone.setGeometry(45, 270, 270, 40)
        self.setShadowWidget(PanelNumberPhone)

        IconNumberPhone = QLabel(PanelNumberPhone)
        IconNumberPhone.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconNumberPhone, 'img/telefono.png')

        self.Input_NumberPhone = QLineEdit(PanelNumberPhone)
        self.Input_NumberPhone.setObjectName("InputText")
        self.Input_NumberPhone.setGeometry(38, 10, 224, 20)
        self.Input_NumberPhone.setMaxLength(9)
        self.Input_NumberPhone.setPlaceholderText("Número de teléfono")

    def addressComponents(self):
        PanelAddress = QFrame(self)
        PanelAddress.setObjectName("InputPanel")
        PanelAddress.setGeometry(45, 320, 270, 40)
        self.setShadowWidget(PanelAddress)

        IconAddress = QLabel(PanelAddress)
        IconAddress.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconAddress, 'img/ubicacion.png')

        self.Input_Address = QLineEdit(PanelAddress)
        self.Input_Address.setGeometry(38, 10, 224, 20)
        self.Input_Address.setObjectName("InputText")
        self.Input_Address.setPlaceholderText("Ingrese su dirección")
    
    def dniComponents(self):
        PanelDNI = QFrame(self)
        PanelDNI.setObjectName("InputPanel")
        PanelDNI.setGeometry(45, 370, 270, 40)
        self.setShadowWidget(PanelDNI)

        IconDNI = QLabel(PanelDNI)
        IconDNI.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconDNI, 'img/nombre.png')

        self.Input_DNI = QLineEdit(PanelDNI)
        self.Input_DNI.setGeometry(38, 10, 195, 20)
        self.Input_DNI.setMaxLength(8)
        self.Input_DNI.setPlaceholderText("Ingrese su DNI")
        self.Input_DNI.setObjectName("InputText")

    def buttonComponents(self):

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setGeometry(30, 424, 300, 20)
        LabelSuggestion.setText("Esta información no será compartida públicamente")
        LabelSuggestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LabelSuggestion.setStyleSheet("""
                                        font-weight: normal;
                                        font-size: 9pt;
                                        font-family: 'Poppins Regular';
                                        font-style: normal;
                                        color: white;
                                      """)
        self.setShadowWidget(LabelSuggestion)

        ButtonNext = QPushButton(self)
        ButtonNext.setText("Siguiente")
        ButtonNext.setGeometry(45, 458, 270, 40)
        ButtonNext.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        ButtonNext.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonNext.setObjectName("ButtonIn")
        self.setShadowWidget(ButtonNext)

        ButtonNext.clicked.connect(self.ButtonNextMouseClicked)

    def verifyErrors(self):
        if(self.Input_FullName.text() == '' or self.Input_NumberPhone.text() == '' or self.Input_Address.text() == '' or self.Input_DNI.text() == ''):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Rellene todos los campos")
            self.objFrameAlert.setVisible(True)
            return False
        
        if(not self.Input_NumberPhone.text().startswith('9') or not self.Input_NumberPhone.text().isdigit()):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Ingrese un número de teléfono válido")
            self.objFrameAlert.setVisible(True)
            return False
        
        if not self.Input_DNI.text().isdigit():
            self.setEnabled(False)
            self.objFrameAlert = FrameAlert(self)
            self.objFrameAlert.LabelMessage.setText("Ingrese un número de DNI válido")
            self.objFrameAlert.setVisible(True)
            return False
        return True

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

    def setNone_FrameAlert(self):
        self.objFrameAlert = None

    # Eventos
    def ButtonNextMouseClicked(self):
        if(self.verifyErrors()):
            result = ''
            try:
                with self.conexionSQL.cursor() as stm:
                    result = stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()
                with self.conexionSQL.cursor() as stm:
                    stm.execute(f"UPDATE [BarrioSeguro].[dbo].[Usuario] SET DNI = '{self.Input_DNI.text()}', FullName = '{self.Input_FullName.text()}', NTelefono = '{self.Input_NumberPhone.text()}', Direccion = '{self.Input_Address.text()}' WHERE U_USER = '{result[0]}'")
                PanelEnterEmergency_Contact = FrameEnterEmergency_Contact(self.TabFrames, self.conexionSQL)
                self.TabFrames.addTab(PanelEnterEmergency_Contact, 'EnterEmergency_Contact')
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameEnterEmergency_Contact')))
                self.close()
            except Exception as e:
                print(e)

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlert != None):
            self.objFrameAlert.raise_()
            self.objFrameAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameEnterEmergency_Contact(QFrame):

    a, CurrentState_CantPanelContact = 20, 0
    list_contacts = []
    objFrameAlert = None
    
    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames=TabFrames
        self.conexionSQL=conexionSQL

        self.installEventFilter(self)
        self.setObjectName("FrameEnterEmergency_Contact")
        BackgroundImage = QLabel(self)
        BackgroundImage.resize(360, 660)
        self.ResizeImage(BackgroundImage, 'img/fondo1-blur.png')

        self.initComponents()
        self.initStyle()

    def initComponents(self):

        LabelTitle = QLabel(self)
        LabelTitle.setText('AGREGAR CONTACTOS DE EMERGENCIA')
        LabelTitle.setWordWrap(True)
        LabelTitle.setObjectName("LabelTitle")
        #LabelTitle.setFixedHeight(60)
        LabelTitle.setGeometry(30, 40, 300, 60)
        LabelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelTitle)

        #self.layoutV.addWidget(LabelTitle)

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setText("Agrega multiples contactos de emergencia.")
        LabelSuggestion.setGeometry(31, 115, 300, 24)
        LabelSuggestion.setStyleSheet("""
                                        font-weight: bold;
                                        font-size: 10pt;
                                        font-family: 'Roboto Black';
                                        font-style: normal;
                                        color: white;
                                        padding-left: 10px;
                                      """)
        self.setShadowWidget(LabelSuggestion)

        self.ScrollArea = QScrollArea(self)
        self.ScrollArea.setGeometry(35, 135, 300, 20) # 300, 374
        self.ScrollArea.setObjectName("ScrollArea")
        self.ScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ScrollArea.setWidgetResizable(True)

        self.PanelScroll = QFrame()
        self.PanelScroll.setObjectName("PanelScroll")

        self.layoutV = QVBoxLayout(self.PanelScroll)
        self.ScrollArea.setWidget(self.PanelScroll)

        self.ButtonAdd = QPushButton(self)
        self.ButtonAdd.setText("Agregar número de contacto")
        self.ButtonAdd.setGeometry(44, 155, 212, 40) # 44, 520
        self.ButtonAdd.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ButtonAdd.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ButtonAdd.setObjectName("ButtonAdd")
        self.setShadowWidget(self.ButtonAdd)

        self.ButtonAdd.clicked.connect(self.ButtonAddMouseClicked)

        IconAdd = QLabel(self.ButtonAdd)
        IconAdd.setGeometry(12, 13, 14, 14)
        IconAdd.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconAdd, 'img/suma_simbolo.png')

        ButtonNext = QPushButton(self)
        ButtonNext.setText("Siguiente")
        ButtonNext.setGeometry(226, 580, 90, 40)
        ButtonNext.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonNext.setObjectName("ButtonNext")
        self.setShadowWidget(ButtonNext)

        ButtonNext.clicked.connect(self.ButtonNextMouseClicked)

        self.ButtonAddMouseClicked()

    def verifyErrors(self):
        list_numbers = []
        for i in range(self.layoutV.count()): # contact_widget
                widget = self.layoutV.itemAt(i).widget()
                for child in widget.children(): # PanelContact
                    if child.objectName() == "PanelNumberPhone":
                        for child_1 in child.children(): # InputText
                            if child_1.objectName() == "InputText" and child_1.text() != '':
                                if(not child_1.text().isdigit() or not child_1.text().startswith('9')):
                                    self.setEnabled(False)
                                    self.objFrameAlert = FrameAlert(self)
                                    self.objFrameAlert.LabelMessage.setText("Número de teléfono inválido")
                                    self.objFrameAlert.setVisible(True)
                                    return False
                                list_numbers.append(child_1.text())
                                
        if len(list_numbers) != len(set(list_numbers)):
            if self.objFrameAlert == None:
                self.setEnabled(False)
                self.objFrameAlert = FrameAlert(self)
                self.objFrameAlert.LabelMessage.setText("Hay números duplicados")
                self.objFrameAlert.setVisible(True)
            return False
        return True

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

    def setNone_FrameAlert(self):
        self.objFrameAlert = None

    # Eventos
    def ButtonAddMouseClicked(self):

        if(self.CurrentState_CantPanelContact < 8):
            self.ScrollArea.setFixedHeight(self.ScrollArea.height() + 44)
            self.ButtonAdd.move(self.ButtonAdd.x(), self.ButtonAdd.y() + 46)

        contact_widget = QWidget()
        contact_widget.setFixedHeight(40)

        PanelName = QFrame(contact_widget)
        PanelName.setObjectName("PanelContact")
        PanelName.setStyleSheet("#PanelContact {background-color: white; border-radius: 8px;}")
        PanelName.resize(117, 40)

        IconName = QLabel(PanelName)
        IconName.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconName, 'img/contacto.png')

        InputName = QLineEdit(PanelName)
        InputName.setObjectName("InputText")
        InputName.setGeometry(38, 10, 76, 20)
        InputName.setPlaceholderText("Nombre")

        PanelNumberPhone = QFrame(contact_widget)
        PanelNumberPhone.setObjectName("PanelNumberPhone")
        PanelNumberPhone.setStyleSheet("#PanelNumberPhone {background-color: white; border-radius: 8px;}")
        PanelNumberPhone.setGeometry(121, 0, 117, 40)

        IconNumberPhone = QLabel(PanelNumberPhone)
        IconNumberPhone.setGeometry(10, 10, 20, 20)
        self.ResizeImage(IconNumberPhone, 'img/telefono.png')

        InputNumberPhone = QLineEdit(PanelNumberPhone)
        InputNumberPhone.setObjectName("InputText")
        InputNumberPhone.setGeometry(38, 10, 76, 20)
        InputNumberPhone.setMaxLength(9)
        InputNumberPhone.setPlaceholderText("Número de teléfono")

        ButtonDelete = QPushButton(contact_widget)
        ButtonDelete.setGeometry(248, 8, 24, 24)
        ButtonDelete.setStyleSheet("background-color: transparent; border: none;")

        IconQuitar = QLabel(ButtonDelete)
        IconQuitar.resize(24, 24)
        IconQuitar.setStyleSheet("background-color: transparent;")
        IconQuitar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconQuitar, 'img/less.png')

        ButtonDelete.clicked.connect((lambda widget=contact_widget, pos = self.CurrentState_CantPanelContact: lambda: self.ButtonDeleteMouseClicked(widget, pos))())
        
        self.layoutV.addWidget(contact_widget)
        self.CurrentState_CantPanelContact += 1
        
    def ButtonDeleteMouseClicked(self, widget, pos):
        self.layoutV.removeWidget(widget)
        widget.deleteLater()
        self.CurrentState_CantPanelContact -= 1
        if(self.CurrentState_CantPanelContact < 8):
            self.ScrollArea.setFixedHeight(self.ScrollArea.height() - 44)
            self.ButtonAdd.move(self.ButtonAdd.x(), self.ButtonAdd.y() - 46)

    def ButtonNextMouseClicked(self):
        if self.verifyErrors():
            result = ''
            try:
                with self.conexionSQL.cursor() as stm:
                    result = stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()
                for i in range(self.layoutV.count()): # contact_widget
                    data = []
                    widget = self.layoutV.itemAt(i).widget()
                    for child in widget.children(): # PanelContact
                        if child.objectName() == "PanelContact" or child.objectName() == "PanelNumberPhone":
                            for child_1 in child.children(): # InputText
                                if child_1.objectName() == "InputText":
                                    data.append(child_1.text())
                    if data[1] != '':
                        with self.conexionSQL.cursor() as stm:
                            stm.execute(f"INSERT INTO [BarrioSeguro].[dbo].[ContactoEmergencia] VALUES ('{result[0]}', '{data[0]}', '{data[1]}')")
                PanelDashboard = FrameDashboard(self.TabFrames, self.conexionSQL)
                self.TabFrames.addTab(PanelDashboard, 'Dashboard')
                self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameDashboard')))
                self.close()
            except Exception as e:
                print(e)
    
    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlert != None):
            self.objFrameAlert.raise_()
            self.objFrameAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameAlert(QFrame):

    def __init__(self, Frame):
        super().__init__()
        self.objFrame = Frame
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
        self.LabelMessage.setGeometry(35, 20, 200, 20)
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
        self.objFrame.setEnabled(True)
        self.close()
        self.objFrame.setNone_FrameAlert()

    def showEvent(self, event):
        self.activateWindow()
        return super().showEvent(event)

    def keyReleaseEvent(self, event):
        if(event.key() == Qt.Key.Key_Return):
            self.objFrame.setEnabled(True)
            self.close()
            self.objFrame.setNone_FrameAlert()
        return super().keyReleaseEvent(event)

class InputUserLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            return event.ignore()
        else:
            return super().keyPressEvent(event)

class InputFullNameLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if self.text().count(" ") == 3:
            if event.key() == Qt.Key.Key_Space:
                return event.ignore()
            else:
                return super().keyPressEvent(event)
        return super().keyPressEvent(event)
        
