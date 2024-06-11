from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QFrame, QLabel, QGraphicsDropShadowEffect, QLineEdit, QCheckBox, QPushButton, QScrollArea, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QPixmap

class FrameRegister(QFrame):
    
    ValorPass, valorshowPassword = True, True
    ValorPass1, valorshowPassword1 = True, True

    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames=TabFrames
        self.conexionSQL=conexionSQL

        self.setObjectName("MainPanel")
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

        self.Input_User = QLineEdit(PanelUser)
        self.Input_User.setObjectName("InputText")
        self.Input_User.setGeometry(38, 10, 224, 20)
        self.Input_User.setPlaceholderText("Ingrese un usuario")

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
        self.Input_Password.keyReleaseEvent = self.Input_PasswordKeyReleased
        
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
        self.Input_Password1.keyReleaseEvent = self.Input_Password1KeyReleased
        
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
        LabelSuggestion.setText("Si estas registrado. Inicie sesión")
        LabelSuggestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LabelSuggestion.setObjectName("LabelSuggestion")
        self.setShadowWidget(LabelSuggestion)

        LabelSuggestion.mouseReleaseEvent = self.LabelSuggestionMouseClicked

    def verifyPassword(self):
        valor = True if(self.Input_Password.text() == self.Input_Password1.text()) else False
        return valor
     
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

    def Input_Password1KeyReleased(self, event):
        if(event.key() == Qt.Key.Key_Return):
            #self.SaveUser = self.Input_User.text()
            #self.ExecuteLogin()
            if not self.verifyPassword():
                
                pass

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
        if(self.verifyPassword()):
            self.TabFrames.setCurrentIndex(2)

    def LabelSuggestionMouseClicked(self, event):
        self.TabFrames.setCurrentIndex(0)

class FrameEnterData_Register(QFrame):

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

        self.Input_FullName = QLineEdit(PanelFullName)
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
        self.Input_DNI.setObjectName("InputText")
        self.Input_DNI.setPlaceholderText("Ingrese su DNI")

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

    # Eventos
    def ButtonClearMouseClicked(self):
        pass

    def ButtonNextMouseClicked(self):
        if(self.Input_FullName.text() != '' and self.Input_NumberPhone.text() != '' and self.Input_Address.text() != '' and self.Input_DNI.text() != ''):
            self.TabFrames.setCurrentIndex(3)

    def Imput_Email(self,text):
        self.text_input_email=self.Input_Address
        self.text_2='@gmail.com'
        if self.text_2.text() is not self.text_input_email.text():
         self.ValorPass=False
        elif():
            self.ValorPass=True

    def Verify_DNI(self):
        if (len(self.Input_DNI)==8):
            self.ValorPass=True

    def Verify_Number(self):
        if (len(self.Input_NumberPhone)==9):
            self.ValorPass=True

class FrameEnterEmergency_Contact(QFrame):

    a, CurrentState_CantPanelContact = 20, 0
    
    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames=TabFrames
        self.conexionSQL=conexionSQL

        self.setObjectName("MainPanel")
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

        PanelScroll = QFrame()
        PanelScroll.setObjectName("PanelScroll")

        self.layoutV = QVBoxLayout(PanelScroll)
        self.ScrollArea.setWidget(PanelScroll)

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

        IconNext = QLabel(self)
        IconNext.setGeometry(278, 580, 50, 50)
        IconNext.setStyleSheet("background-color: transparent;")
        IconNext.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconNext, 'img/next.png')
        self.setShadowWidget(IconNext)

        IconNext.mouseReleaseEvent = self.IconNextMouseClicked

        self.ButtonAddMouseClicked()

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

    # Eventos
    def ButtonAddMouseClicked(self):

        if(self.CurrentState_CantPanelContact < 8):
            self.ScrollArea.setFixedHeight(self.ScrollArea.height() + 44)
            self.ButtonAdd.move(self.ButtonAdd.x(), self.ButtonAdd.y() + 46)

        contact_widget = QWidget()
        contact_widget.setFixedHeight(40)

        Panel = QFrame(contact_widget)
        Panel.setObjectName("PanelContact")
        Panel.setStyleSheet("#PanelContact {background-color: white; border-radius: 8px;}")
        Panel.resize(238, 40)

        Icon = QLabel(Panel)
        Icon.setGeometry(10, 10, 20, 20)
        self.ResizeImage(Icon, 'img/contacto.png')

        Input = QLineEdit(Panel)
        Input.setObjectName("InputText")
        Input.setGeometry(38, 10, 188, 20)
        Input.setPlaceholderText("Número de teléfono")
        Input.setMaxLength(9)

        ButtonDelete = QPushButton(contact_widget)
        ButtonDelete.setGeometry(248, 8, 24, 24)
        ButtonDelete.setStyleSheet("background-color: transparent; border: none;")

        IconQuitar = QLabel(ButtonDelete)
        IconQuitar.resize(24, 24)
        IconQuitar.setStyleSheet("background-color: transparent;")
        IconQuitar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconQuitar, 'img/less.png')

        ButtonDelete.clicked.connect(lambda: self.ButtonDeleteMouseClicked(contact_widget))

        self.layoutV.addWidget(contact_widget)
        self.CurrentState_CantPanelContact += 1
        
    def ButtonDeleteMouseClicked(self, widget):
        self.layoutV.removeWidget(widget)
        widget.deleteLater()
        self.CurrentState_CantPanelContact -= 1
        if(self.CurrentState_CantPanelContact < 8):
            self.ScrollArea.setFixedHeight(self.ScrollArea.height() - 44)
            self.ButtonAdd.move(self.ButtonAdd.x(), self.ButtonAdd.y() - 46)
        
    def IconNextMouseClicked(self, event):
        self.TabFrames.setCurrentIndex(4)