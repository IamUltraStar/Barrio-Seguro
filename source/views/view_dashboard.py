from PyQt6.QtCore import Qt, QDate, QTime
from PyQt6.QtWidgets import (QApplication, QFrame, QLabel, QGraphicsDropShadowEffect, QTabWidget, QLineEdit, QComboBox, QTextEdit, QCheckBox, QFileDialog, QDateEdit, QTimeEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget)
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QEvent
import random

class FrameDashboard(QFrame):

    objFrameAlert = None

    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames = TabFrames
        self.conexionSQL = conexionSQL
        self.installEventFilter(self)
        self.setObjectName("FrameDashboard")
        self.initComponents()
        self.initStyle()

    def initComponents(self):
        self.Tab_Dashboard = QTabWidget(self)
        self.Tab_Dashboard.resize(360, 580)
        self.Tab_Dashboard.tabBar().hide()
        self.Tab_Dashboard.setObjectName("Tab_Dashboard")
        self.Tab_Dashboard.setStyleSheet("#Tab_Dashboard::pane{border: 0; background-color: rgb(229, 231, 234); border-top-left-radius: 32px; border-top-right-radius: 32px;}")

        self.PanelHomePage = FrameHomePage(self.conexionSQL)
        self.Tab_Dashboard.addTab(self.PanelHomePage, 'HomePage')

        self.PanelGenerateReport = FrameGenerateReport(self.conexionSQL)
        self.Tab_Dashboard.addTab(self.PanelGenerateReport, 'GenerateReport')

        self.PanelAccount = FrameAccount(self.conexionSQL)
        self.Tab_Dashboard.addTab(self.PanelAccount, 'Account')

        self.PanelSettings = FrameSettings(self, self.TabFrames, self.conexionSQL)
        self.Tab_Dashboard.addTab(self.PanelSettings, 'Settings')

        PanelBottom = QFrame(self)
        PanelBottom.setGeometry(0, 580, 360, 80)
        PanelBottom.setObjectName("PanelBottom")

        self.PanelIconHomePage = QFrame(PanelBottom)
        self.PanelIconHomePage.setGeometry(65, 15, 50, 50)
        self.PanelIconHomePage.setObjectName("FirstButtonPressed")
        self.CurrentStatePanel = self.PanelIconHomePage
        self.setShadowWidget(self.PanelIconHomePage)

        self.PanelIconHomePage.mouseReleaseEvent = self.PanelIconHomePageMouseClicked

        IconHomePage = QLabel(self.PanelIconHomePage)
        IconHomePage.setGeometry(15, 15, 20, 20)
        IconHomePage.setStyleSheet("background-color: transparent;")
        IconHomePage.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconHomePage, 'img/home.png')

        self.PanelIconGenerateReport = QFrame(PanelBottom)
        self.PanelIconGenerateReport.setGeometry(125, 15, 50, 50)
        self.PanelIconGenerateReport.setObjectName("ButtonsInDashboard")
    
        self.PanelIconGenerateReport.mouseReleaseEvent = self.PanelIconGenerateReportMouseClicked

        IconGenerateReport = QLabel(self.PanelIconGenerateReport)
        IconGenerateReport.setGeometry(15, 15, 20, 20)
        IconGenerateReport.setStyleSheet("background-color: transparent;")
        IconGenerateReport.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconGenerateReport, 'img/flag.png')

        self.PanelIconAccount = QFrame(PanelBottom)
        self.PanelIconAccount.setGeometry(185, 15, 50, 50)
        self.PanelIconAccount.setObjectName("ButtonsInDashboard")

        self.PanelIconAccount.mouseReleaseEvent = self.PanelIconAccountMouseClicked

        IconAccount = QLabel(self.PanelIconAccount)
        IconAccount.setGeometry(15, 15, 20, 20)
        IconAccount.setStyleSheet("background-color: transparent;")
        IconAccount.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconAccount, 'img/user.png')

        self.PanelIconSettings = QFrame(PanelBottom)
        self.PanelIconSettings.setGeometry(245, 15, 50, 50)
        self.PanelIconSettings.setObjectName("ButtonsInDashboard")

        self.PanelIconSettings.mouseReleaseEvent = self.PanelIconSettingsMouseClicked

        IconSettings = QLabel(self.PanelIconSettings)
        IconSettings.setGeometry(15, 15, 20, 20)
        IconSettings.setStyleSheet("background-color: transparent;")
        IconSettings.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconSettings, 'img/settings.png')

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    def initStyle(self):
        with open('source/css/styleDashboard.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    def verify_PanelGenerateReport(self, index, Panelcomponent):
        if((index in [0, 2, 3]) and (self.PanelGenerateReport.ListTypeIncident.currentText() != '' or self.PanelGenerateReport.TextEditDescription.toPlainText() != '' or self.PanelGenerateReport.InputAddress.text() != '' or self.PanelGenerateReport.InputEvidence.text() != "Archivo no seleccionado")):
            self.setEnabled(False)
            self.objFrameAlert = FrameAlertPanelGenerateReport(self, index, Panelcomponent)
            self.objFrameAlert.LabelMessage.setText("Estas seguro de salir de aquí?")
            self.objFrameAlert.setVisible(True)
        else:
            self.Update_PanelopcMouseClicked(index, Panelcomponent)
            self.PanelGenerateReport.PanelTypeIncident.setStyleSheet("#InputPanel{border: none}")
            self.PanelGenerateReport.PanelDescriptionIncident.setStyleSheet("#InputPanel{border: none}")
            self.PanelGenerateReport.PanelAddress.setStyleSheet("#InputPanel{border: none}")

    def Update_PanelopcMouseClicked(self, index, Panelcomponent):
        self.Tab_Dashboard.setCurrentIndex(index)
        self.CurrentStatePanel.setStyleSheet("background-color: transparent")
        Panelcomponent.setStyleSheet("background-color: lightblue;")
        self.CurrentStatePanel = Panelcomponent
        self.setShadowWidget(Panelcomponent)

    def setNone_FrameAlert(self):
        self.objFrameAlert = None

    # Eventos
    def PanelIconHomePageMouseClicked(self, event):
        self.verify_PanelGenerateReport(0, self.PanelIconHomePage)
        #self.Update_PanelopcMouseClicked(0, self.PanelIconHomePage)

    def PanelIconGenerateReportMouseClicked(self, event):
        self.Update_PanelopcMouseClicked(1, self.PanelIconGenerateReport)

    def PanelIconAccountMouseClicked(self, event):
        self.verify_PanelGenerateReport(2, self.PanelIconAccount)
        #self.Update_PanelopcMouseClicked(2, self.PanelIconAccount)

    def PanelIconSettingsMouseClicked(self, event):
        self.verify_PanelGenerateReport(3, self.PanelIconSettings)
        #self.Update_PanelopcMouseClicked(3, self.PanelIconSettings)

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlert != None):
            self.objFrameAlert.raise_()
            self.objFrameAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameHomePage(QFrame):
    
    def __init__(self, conexionSQL):
        super().__init__()
        self.conexionSQL = conexionSQL
        self.initComponents()
        self.initStyle()

    def initComponents(self):

        IconMap = QLabel(self)
        IconMap.setGeometry(25, 25, 25, 25)
        IconMap.setStyleSheet("background-color: transparent;")
        IconMap.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconMap, 'img/map.png')

        IconNotifications = QLabel(self)
        IconNotifications.setGeometry(310, 25, 25, 25)
        IconNotifications.setStyleSheet("background-color: transparent;")
        IconNotifications.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconNotifications, 'img/notivacia.png')

        LabelGreet = QLabel(self)
        LabelGreet.setObjectName("LabelGreet")
        LabelGreet.setGeometry(20, 100, 320, 60)
        LabelGreet.setWordWrap(True)
        LabelGreet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelGreet)

        try:
            result = ''
            with self.conexionSQL.cursor() as stm:
                result = stm.execute("SELECT R_Usuario FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()

            name = ''
            with self.conexionSQL.cursor() as stm:
                name = stm.execute(f"SELECT FullName FROM [BarrioSeguro].[dbo].[Usuario] WHERE U_User = '{result[0]}'").fetchone()
            name_split = name[0].split(' ')
            LabelGreet.setText(f"Bienvenido {name_split[0]} {name_split[1]}")
        except Exception as e:
            print(e)

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setGeometry(50, 190, 260, 60)
        LabelSuggestion.setText("Presione este botón en caso de emergencia.")
        LabelSuggestion.setWordWrap(True)
        LabelSuggestion.setObjectName("LabelSuggestion")
        LabelSuggestion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelSuggestion)

        ButtonEmergency = QFrame(self)
        ButtonEmergency.setGeometry(50, 270, 260, 260)
        ButtonEmergency.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonEmergency.setObjectName("ButtonEmergency")
        self.setShadowWidget(ButtonEmergency)

        ButtonEmergency.mouseReleaseEvent = self.ButtonEmergencyMouseClicked

        IconButtonEmergency = QLabel(ButtonEmergency)
        IconButtonEmergency.setGeometry(70, 70, 120, 120)
        IconButtonEmergency.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconButtonEmergency, 'img/megaphone.png')

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    def initStyle(self):
        with open('source/css/styleHomePage.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    #Eventos
    def ButtonEmergencyMouseClicked(self, event):
        self.sound_effect = QSoundEffect()
        url = QUrl.fromLocalFile("sound/morse-sos.wav")
        self.sound_effect.setSource(url)
        self.sound_effect.setLoopCount(1)  # Número de veces que se repetirá el sonido (-1 para bucle infinito)
        self.sound_effect.setVolume(0.5)  # Volumen del sonido (0.0 a 1.0)
        self.sound_effect.play()
        print("Comunicando a todos los contactos de emergencia.")
        print("Comunicando a seguridades cercanas.")

class FrameGenerateReport(QFrame):
    
    objFrameAlert = None

    def __init__(self, conexionSQL):
        super().__init__()
        self.conexionSQL= conexionSQL
        self.installEventFilter(self)
        self.initComponents()
        self.initStyle()

    def initComponents(self):

        IconTitle = QLabel(self)
        IconTitle.setGeometry(30, 35, 30, 30)
        IconTitle.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconTitle, 'img/formulario.png')

        LabelTitle = QLabel(self)
        LabelTitle.setText("Reportar incidente")
        LabelTitle.setGeometry(70, 30, 260, 40)
        LabelTitle.setObjectName("LabelTitle")
        self.setShadowWidget(LabelTitle)

        self.PanelTypeIncident = QFrame(self)
        self.PanelTypeIncident.setObjectName("InputPanel")
        self.PanelTypeIncident.setGeometry(30, 80, 300, 40)
        self.setShadowWidget(self.PanelTypeIncident)

        IconTypeIncident = QLabel(self.PanelTypeIncident)
        IconTypeIncident.setGeometry(10, 10, 20, 20)
        IconTypeIncident.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconTypeIncident, 'img/categorias.png')

        self.ListTypeIncident = QComboBox(self.PanelTypeIncident)
        self.ListTypeIncident.setGeometry(38, 5, 252, 30)
        self.ListTypeIncident.setPlaceholderText("Tipo de incidente...")

        self.ListTypeIncident.addItem('Robo')
        self.ListTypeIncident.addItem('Asalto')
        self.ListTypeIncident.addItem('Vandalismo')
        self.ListTypeIncident.addItem('Emergencia Médica')
        self.ListTypeIncident.addItem('Otro')

        self.PanelDescriptionIncident = QFrame(self)
        self.PanelDescriptionIncident.setGeometry(30, 130, 300, 80)
        self.PanelDescriptionIncident.setObjectName("InputPanel")
        self.setShadowWidget(self.PanelDescriptionIncident)

        IconDescriptionIncident = QLabel(self.PanelDescriptionIncident)
        IconDescriptionIncident.setGeometry(10, 10, 20, 20)
        IconDescriptionIncident.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconDescriptionIncident, 'img/mensaje.png')

        self.TextEditDescription = QTextEdit(self.PanelDescriptionIncident)
        self.TextEditDescription.setGeometry(38, 10, 252, 60)
        self.TextEditDescription.setPlaceholderText("Describe brevemente el incidente...")

        self.PanelAddress = QFrame(self)
        self.PanelAddress.setGeometry(30, 220, 300, 40)
        self.PanelAddress.setObjectName("InputPanel")
        self.setShadowWidget(self.PanelAddress)

        IconAddress = QLabel(self.PanelAddress)
        IconAddress.setGeometry(10, 10, 20, 20)
        IconAddress.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconAddress, 'img/ubicacion.png')

        self.InputAddress = QLineEdit(self.PanelAddress)
        self.InputAddress.setGeometry(38, 10, 252, 20)
        self.InputAddress.setObjectName("InputText")
        self.InputAddress.setPlaceholderText("Ingrese la ubicación del incidente")
        
        PanelDate = QFrame(self)
        PanelDate.setGeometry(30, 270, 140, 40)
        PanelDate.setObjectName("InputPanel")
        self.setShadowWidget(PanelDate)

        IconDate = QLabel(PanelDate)
        IconDate.setGeometry(10, 10, 20, 20)
        IconDate.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconDate, 'img/calendar.png')

        self.InputDate = QDateEdit(PanelDate)
        self.InputDate.setDate(QDate.currentDate())
        self.InputDate.setGeometry(38, 10, 90, 20)

        PanelHour = QFrame(self)
        PanelHour.setGeometry(190, 270, 140, 40)
        PanelHour.setObjectName("InputPanel")
        self.setShadowWidget(PanelHour)

        IconHour = QLabel(PanelHour)
        IconHour.setGeometry(10, 10, 20, 20)
        IconHour.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconHour, 'img/reloj.png')

        self.InputHour = QTimeEdit(PanelHour)
        self.InputHour.setTime(QTime.currentTime())
        self.InputHour.setGeometry(38, 10, 90, 20)

        PanelEvidence = QFrame(self)
        PanelEvidence.setGeometry(30, 320, 300, 40)
        PanelEvidence.setObjectName("InputPanel")
        self.setShadowWidget(PanelEvidence)

        IconEvidence = QLabel(PanelEvidence)
        IconEvidence.setGeometry(10, 10, 20, 20)
        IconEvidence.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconEvidence, 'img/subir.png')

        self.InputEvidence = QLabel(PanelEvidence)
        self.InputEvidence.setGeometry(38, 10, 222, 20)
        self.InputEvidence.setText("Archivo no seleccionado")
        self.InputEvidence.setObjectName("InputEvidence")

        IconAddEvidence = QLabel(PanelEvidence)
        IconAddEvidence.setGeometry(270, 10, 20, 20)
        IconAddEvidence.setStyleSheet("background-color: transparent;")
        IconAddEvidence.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconAddEvidence, 'img/openfile.png')

        IconAddEvidence.mouseReleaseEvent = self.IconAddEvidenceMouseClicked

        LabelSuggestion = QLabel(self)
        LabelSuggestion.setGeometry(30, 366, 300, 14)
        LabelSuggestion.setText("Información de Contacto (Opcional)")
        LabelSuggestion.setObjectName("LabelSuggestion")

        PanelNameContact = QFrame(self)
        PanelNameContact.setGeometry(30, 386, 300, 40)
        PanelNameContact.setObjectName("InputPanel")
        self.setShadowWidget(PanelNameContact)

        IconNameContact = QLabel(PanelNameContact)
        IconNameContact.setGeometry(10, 10, 20, 20)
        IconNameContact.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconNameContact, 'img/usuario.png')

        self.InputNameContact = QLineEdit(PanelNameContact)
        self.InputNameContact.setGeometry(38, 10, 252, 20)
        self.InputNameContact.setObjectName("InputText")
        self.InputNameContact.setPlaceholderText("Nombre")

        PanelNumberPhone = QFrame(self)
        PanelNumberPhone.setGeometry(30, 436, 300, 40)
        PanelNumberPhone.setObjectName("InputPanel")
        self.setShadowWidget(PanelNumberPhone)

        IconNumberPhone = QLabel(PanelNumberPhone)
        IconNumberPhone.setGeometry(10, 10, 20, 20)
        IconNumberPhone.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconNumberPhone, 'img/telefono.png')

        self.InputNumberPhone = QLineEdit(PanelNumberPhone)
        self.InputNumberPhone.setGeometry(38, 10, 252, 20)
        self.InputNumberPhone.setObjectName("InputText")
        self.InputNumberPhone.setPlaceholderText("Número de Teléfono")

        self.opcAnonymity = QCheckBox(self)
        self.opcAnonymity.setText("Reportar de manera anónima")
        self.opcAnonymity.setGeometry(43, 496, 180, 14)
        self.opcAnonymity.setObjectName("opcAnonymity")
        self.opcAnonymity.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.opcAnonymity.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(self.opcAnonymity)

        ButtonPerform = QPushButton(self)
        ButtonPerform.setText("Enviar Reporte")
        ButtonPerform.setGeometry(210, 525, 120, 40)
        ButtonPerform.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonPerform.setObjectName("ButtonPerform")
        self.setShadowWidget(ButtonPerform)

        ButtonPerform.clicked.connect(self.ButtonPerformMouseClicked)

    def verifyErrors(self):
        valor = True
        if(self.ListTypeIncident.currentText() == ''):
            self.PanelTypeIncident.setStyleSheet("#InputPanel{border: 1px solid rgba(189, 68, 68, 0.823);}")
            valor = False
        else:
            self.PanelTypeIncident.setStyleSheet("#InputPanel{border: none}")
        
        if(self.TextEditDescription.toPlainText() == ''):
            self.PanelDescriptionIncident.setStyleSheet("#InputPanel{border: 1px solid rgba(189, 68, 68, 0.823);}")
            valor = False
        else:
            self.PanelDescriptionIncident.setStyleSheet("#InputPanel{border: none}")

        if(self.InputAddress.text() == ''):
            self.PanelAddress.setStyleSheet("#InputPanel{border: 1px solid rgba(189, 68, 68, 0.823);}")
            valor = False
        else:
            self.PanelAddress.setStyleSheet("#InputPanel{border: none}")
        
        return valor

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    def initStyle(self):
        with open('source/css/styleGenerateReport.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    def setNone_FrameAlert(self):
        self.objFrameAlert = None

    # Eventos
    def IconAddEvidenceMouseClicked(self, event):
        options = QFileDialog.Option.ReadOnly
        FileDialog = QFileDialog()
        file_path, _ = FileDialog.getOpenFileName(self, "Abrir", "", "Archivos de imagen (*.jpg;*.jpeg;*.png;*.bmp);;Archivos de vídeo (*.mp4;*.avi;*.mkv;*.mov)", options=options)

        if(file_path):
            self.InputEvidence.setText(file_path)
        else:
            self.InputEvidence.setText("Archivo no seleccionado")

    def ButtonPerformMouseClicked(self, event):
        if(self.verifyErrors()):
            try:
                result = ''
                with self.conexionSQL.cursor() as stm:
                    result = stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()
                id = f"{QDate.currentDate().toString("yyyy-MM-dd").replace('-','')}{random.randint(0,100)}"
                with self.conexionSQL.cursor() as stm:
                    if(not self.opcAnonymity.isChecked()):
                        stm.execute("INSERT INTO [BarrioSeguro].[dbo].[Reporte] (ID_Reporte, Tipo, Descripcion, Ubicacion, FechaHora, file_path, R_Contacto, R_NTelefono, Autor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(int(id),self.ListTypeIncident.currentText(), self.TextEditDescription.toPlainText(), self.InputAddress.text(), f"{self.InputDate.date().toString("yyyy-MM-dd")} {self.InputHour.time().toString("HH:mm:ss")}", self.InputEvidence.text(), self.InputNameContact.text(), self.InputNumberPhone.text(), result[0]))
                    else:
                        stm.execute("INSERT INTO [BarrioSeguro].[dbo].[Reporte] (ID_Reporte, Tipo, Descripcion, Ubicacion, FechaHora, file_path, R_Contacto, R_NTelefono) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(int(id),self.ListTypeIncident.currentText(), self.TextEditDescription.toPlainText(), self.InputAddress.text(), f"{self.InputDate.date().toString("yyyy-MM-dd")} {self.InputHour.time().toString("HH:mm:ss")}", self.InputEvidence.text(), self.InputNameContact.text(), self.InputNumberPhone.text()))
                self.setEnabled(False)
                self.objFrameAlert = FrameAlert(self)
                self.objFrameAlert.LabelMessage.setText("Reporte enviado con exito.")
                self.objFrameAlert.setVisible(True)
            except Exception as e:
                print(e)

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlert != None):
            self.objFrameAlert.raise_()
            self.objFrameAlert.activateWindow()
        return super().eventFilter(obj, event)

class FrameAccount(QFrame):
    
    cant_contacts = 0
    a = 19
    objFrameAlertDeleteContact = None

    def __init__(self, conexionSQL):
        super().__init__()
        self.conexionSQL = conexionSQL
        self.installEventFilter(self)
        self.user = ''
        try:
            with self.conexionSQL.cursor() as stm:
                self.user = stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()
        except Exception as e:
            print(e)

        self.initComponents()
        self.initStyle()

    def initComponents(self):
        
        IconProfile = QLabel(self)
        IconProfile.setGeometry(20, 30, 50, 50)
        IconProfile.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconProfile, 'img/3.png')

        LabelName = QLabel(self)
        LabelName.setGeometry(85, 30, 200, 30)
        LabelName.setObjectName("LabelName")

        try:
            result = ''
            with self.conexionSQL.cursor() as stm:
                result = stm.execute(f"SELECT FullName FROM [BarrioSeguro].[dbo].[Usuario] WHERE U_User = '{self.user[0]}'").fetchone()
            name = result[0].split(' ')
            LabelName.setText(f"{name[0]} {name[1]}")
        except Exception as e:
            print(e)

        LabelMail = QLabel(self)
        LabelMail.setGeometry(85, 60, 200, 20)
        LabelMail.setObjectName("LabelMail")

        try:
            result = ''
            with self.conexionSQL.cursor() as stm:
                result = stm.execute(f"SELECT CorreoElectronico FROM [BarrioSeguro].[dbo].[Usuario] WHERE U_User = '{self.user[0]}'").fetchone()

            LabelMail.setText(result[0])
        except Exception as e:
            print(e)

        ButtonEditProfile = QFrame(self)
        ButtonEditProfile.setGeometry(305, 40, 30, 30)
        ButtonEditProfile.setObjectName("ButtonEditProfile")

        IconEditProfile = QLabel(ButtonEditProfile)
        IconEditProfile.setGeometry(5, 5, 20, 20)
        IconEditProfile.setStyleSheet("background-color: transparent;")
        IconEditProfile.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconEditProfile, 'img/lapiz.png')

        LabelContacts = QLabel(self)
        LabelContacts.setText("Contactos")
        LabelContacts.setGeometry(20, 110, 80, 30)
        LabelContacts.setObjectName("LabelContacts")
        
        ButtonAddContact = QPushButton(self)
        ButtonAddContact.setText("Añadir Contacto")
        ButtonAddContact.setGeometry(201, 110, 134, 30)
        ButtonAddContact.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonAddContact.setObjectName("ButtonAddContact")

        IconAddContact = QLabel(ButtonAddContact)
        IconAddContact.setGeometry(12, 8, 14, 14)
        IconAddContact.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconAddContact, 'img/suma_simbolo.png')

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setGeometry(11, 150, 332, self.a) # 332, 416
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        panel_scroll = QFrame()
        panel_scroll.setObjectName("panel_scroll")
        panel_scroll.setStyleSheet("#panel_scroll {background-color: transparent;}")
        self.layoutV = QVBoxLayout(panel_scroll)
        self.scroll_area.setWidget(panel_scroll)

        self.cargarContactos()

    def cargarContactos(self):
        result=[]
        try:
            with self.conexionSQL.cursor() as stm :
                result = stm.execute(f"SELECT CE_Nombre ,CE_NTelefono FROM [BarrioSeguro].[dbo].[ContactoEmergencia] WHERE P_User = '{self.user[0]}' ORDER BY CE_Nombre").fetchall()
        except Exception as e:
            print(e)
        
        for contact in result :
            if(self.cant_contacts < 10):
                self.scroll_area.setFixedHeight(self.scroll_area.height() + 40)

            contact_widget = QWidget()
            contact_widget.setFixedHeight(35)
            contact_widget.setObjectName("contact_widget")
            contact_widget.setStyleSheet("#contact_widget {background-color: transparent;}")

            IconContactProfile = QLabel(contact_widget)
            IconContactProfile.setGeometry(0, 0, 35, 35)
            IconContactProfile.setStyleSheet("background-color: transparent;")
            self.ResizeImage(IconContactProfile, 'img/contacto1.png')

            LabelNameContact = QLabel(contact_widget)
            LabelNameContact.setText(f"{contact[0]}")
            LabelNameContact.setGeometry(50, 0, 220, 17)
            LabelNameContact.setAlignment(Qt.AlignmentFlag.AlignBottom)
            LabelNameContact.setObjectName("LabelNameContact")

            LabelTelefono = QLabel(contact_widget)
            LabelTelefono.setText(f"{contact[1]}")
            LabelTelefono.setGeometry(50, 17, 220, 18)
            LabelTelefono.setAlignment(Qt.AlignmentFlag.AlignBottom)
            LabelTelefono.setObjectName("LabelTelefono")

            ButtonDelete = QPushButton(contact_widget)
            ButtonDelete.setGeometry(290, 6, 24, 24)
            ButtonDelete.setObjectName("ButtonDelete")

            ButtonDelete.clicked.connect(lambda: self.verifyDeleteContact(contact_widget))

            IconDeleteContactProfile = QLabel(ButtonDelete)
            IconDeleteContactProfile.setGeometry(5, 5, 14, 14)
            IconDeleteContactProfile.setStyleSheet("background-color: transparent;")
            IconDeleteContactProfile.setCursor(Qt.CursorShape.PointingHandCursor)
            self.ResizeImage(IconDeleteContactProfile, 'img/eliminar1.png')
            self.layoutV.addWidget(contact_widget)
            self.cant_contacts += 1

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    def initStyle(self):
        with open('source/css/styleAccount.css', 'r') as file:
            css = file.read()
        self.setStyleSheet(css)

    def setNone_FrameAlert(self):
        self.objFrameAlertDeleteContact = None

    # Eventos
    def ButtonAddContactMouseClicked(self):
        pass

    def ButtonDeleteMouseClicked(self, widget):
        try:
            user = ''
            with self.conexionSQL.cursor() as stm:
                user = stm.execute("SELECT * FROM [BarrioSeguro].[dbo].[RememberLogin]").fetchone()

            number_phone = ''
            for child in widget.children():
                if child.objectName() == 'LabelTelefono':
                    number_phone = child.text()

            with self.conexionSQL.cursor() as stm:
                stm.execute(f"DELETE FROM [BarrioSeguro].[dbo].[ContactoEmergencia] WHERE P_User = {user[0]} AND CE_NTelefono = {number_phone}")

            self.layoutV.removeWidget(widget)
            widget.deleteLater()
            self.cant_contacts -= 1
            if(self.cant_contacts < 10):
                self.scroll_area.setFixedHeight(self.scroll_area.height() - 40)
        except Exception as e:
            print(e)

    def verifyDeleteContact(self, widget):
        self.setEnabled(False)
        self.objFrameAlertDeleteContact = FrameAlertDeleteContact(self, widget)
        self.objFrameAlertDeleteContact.LabelMessage.setText("Estas seguro de borrar este contacto?")
        self.objFrameAlertDeleteContact.setVisible(True)

    def eventFilter(self, obj, event):
        if(event.type() == QEvent.Type.WindowActivate and self.objFrameAlertDeleteContact != None):
            self.objFrameAlertDeleteContact.raise_()
            self.objFrameAlertDeleteContact.activateWindow()
        return super().eventFilter(obj, event)

class FrameSettings(QFrame):
    
    def __init__(self, MainWidget, TabFrames, conexionSQL):
        super().__init__()
        self.MainWidget = MainWidget
        self.conexionSQL = conexionSQL
        self.TabFrames = TabFrames
        self.initComponents()

    def initComponents(self):
        
        LabelSettings = QLabel(self)
        LabelSettings.setText("Ajustes")
        LabelSettings.setGeometry(0, 25, 360, 30)
        LabelSettings.setAlignment(Qt.AlignmentFlag.AlignCenter)
        LabelSettings.setStyleSheet("""
                                        font-weight: bold;
                                        font-size: 18.4pt;
                                        font-family: 'Poppins Regular';
                                        font-style: normal;
                                        color: rgba(0,0,0,0.5);
                                        background-color: transparent;
                                    """)

        Separator = QFrame(self)
        Separator.setGeometry(0, 70, 360, 2)
        Separator.setStyleSheet("background-color: rgba(0, 0, 0, 0.5);")

        IconLogout = QLabel(self)
        IconLogout.setGeometry(21, 94, 20, 20)
        IconLogout.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconLogout, 'img/logout.png')

        LabelLogout = QLabel(self)
        LabelLogout.setText("Cerrar sesión")
        LabelLogout.setGeometry(55, 94, 100, 20)
        LabelLogout.setCursor(Qt.CursorShape.PointingHandCursor)
        LabelLogout.setStyleSheet("""
                                     font-weight: bold;
                                     font-size: 11pt;
                                     font-family: 'Roboto Black';
                                     font-style: normal;
                                     color: rgba(189, 68, 68, 0.823);
                                     background-color: transparent;
                                  """)
        
        LabelLogout.mouseReleaseEvent = self.LabelLogoutMouseClicked

    def setShadowWidget(self, widget):
        ShadowWindow = QGraphicsDropShadowEffect()
        ShadowWindow.setBlurRadius(15)
        ShadowWindow.setOffset(0.0, 0.0)
        widget.setGraphicsEffect(ShadowWindow)

    def ResizeImage(self, label, path):
        pixmap = QPixmap(path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setMargin(0)

    # Eventos
    def LabelLogoutMouseClicked(self, event):
        try:
            with self.conexionSQL.cursor() as stm:
                stm.execute("TRUNCATE TABLE [BarrioSeguro].[dbo].[RememberLogin]")
            self.TabFrames.setCurrentIndex(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameLogin')))
            self.TabFrames.removeTab(self.TabFrames.indexOf(self.TabFrames.findChild(QFrame, 'FrameDashboard')))
            self.MainWidget.close()
        except Exception as e:
            print(e)

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

class FrameAlertPanelGenerateReport(QFrame):

    def __init__(self, Frame, index, Panelcomponent):
        super().__init__()
        self.objFrame = Frame
        self.index = index
        self.Panelcomponent = Panelcomponent
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
        
        ButtonYes = QPushButton(PanelPrincipal)
        ButtonYes.setGeometry(75, 50, 50, 25)
        ButtonYes.setText('Sí')
        ButtonYes.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(ButtonYes)
        
        ButtonYes.clicked.connect(self.ButtonYesMouseClicked)

        ButtonNo = QPushButton(PanelPrincipal)
        ButtonNo.setGeometry(145, 50, 50, 25)
        ButtonNo.setText('No')
        ButtonNo.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonNo.setObjectName("ButtonNo")
        self.setShadowWidget(ButtonNo)
        
        ButtonNo.clicked.connect(self.ButtonNoMouseClicked)

    def resetStylePanelGenerateReport(self):
        self.objFrame.PanelGenerateReport.ListTypeIncident.setCurrentIndex(-1)
        self.objFrame.PanelGenerateReport.TextEditDescription.setText('')
        self.objFrame.PanelGenerateReport.InputAddress.setText('')
        self.objFrame.PanelGenerateReport.InputDate.setDate(QDate.currentDate())
        self.objFrame.PanelGenerateReport.InputHour.setTime(QTime.currentTime())
        self.objFrame.PanelGenerateReport.InputEvidence.setText("Archivo no seleccionado")
        self.objFrame.PanelGenerateReport.InputNameContact.setText('')
        self.objFrame.PanelGenerateReport.InputNumberPhone.setText('')
        self.objFrame.PanelGenerateReport.opcAnonymity.setChecked(False)
        self.objFrame.PanelGenerateReport.PanelTypeIncident.setStyleSheet("#InputPanel{border: none}")
        self.objFrame.PanelGenerateReport.PanelDescriptionIncident.setStyleSheet("#InputPanel{border: none}")
        self.objFrame.PanelGenerateReport.PanelAddress.setStyleSheet("#InputPanel{border: none}")

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
    def ButtonYesMouseClicked(self):
        self.objFrame.setEnabled(True)
        self.close()
        self.objFrame.Update_PanelopcMouseClicked(self.index, self.Panelcomponent)
        self.resetStylePanelGenerateReport()
        self.objFrame.setNone_FrameAlert()

    def ButtonNoMouseClicked(self):
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
    
class FrameAlertDeleteContact(QFrame):

    def __init__(self, Frame, widget):
        super().__init__()
        self.objFrame = Frame
        self.widget = widget
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
        
        ButtonYes = QPushButton(PanelPrincipal)
        ButtonYes.setGeometry(75, 50, 50, 25)
        ButtonYes.setText('Sí')
        ButtonYes.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(ButtonYes)
        
        ButtonYes.clicked.connect(self.ButtonYesMouseClicked)

        ButtonNo = QPushButton(PanelPrincipal)
        ButtonNo.setGeometry(145, 50, 50, 25)
        ButtonNo.setText('No')
        ButtonNo.setCursor(Qt.CursorShape.PointingHandCursor)
        ButtonNo.setObjectName("ButtonNo")
        self.setShadowWidget(ButtonNo)
        
        ButtonNo.clicked.connect(self.ButtonNoMouseClicked)

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
    def ButtonYesMouseClicked(self):
        self.objFrame.setEnabled(True)
        self.close()
        self.objFrame.ButtonDeleteMouseClicked(self.widget)
        self.objFrame.setNone_FrameAlert()

    def ButtonNoMouseClicked(self):
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