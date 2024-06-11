from PyQt6.QtCore import Qt, QDate, QTime
from PyQt6.QtWidgets import (QFrame, QLabel, QGraphicsDropShadowEffect, QTabWidget, QLineEdit, QComboBox, QTextEdit, QCheckBox, QFileDialog, QDateEdit, QTimeEdit, QPushButton, QScrollArea, QVBoxLayout, QWidget)
from PyQt6.QtGui import QPixmap

class FrameDashboard(QFrame):

    def __init__(self, TabFrames, conexionSQL):
        super().__init__()
        self.TabFrames = TabFrames
        self.conexionSQL = conexionSQL
        self.setObjectName("MainPanel")
        self.initComponents()
        self.initStyle()

    def initComponents(self):
        self.Tab_Dashboard = QTabWidget(self)
        self.Tab_Dashboard.resize(360, 580)
        self.Tab_Dashboard.tabBar().hide()
        self.Tab_Dashboard.setObjectName("Tab_Dashboard")
        self.Tab_Dashboard.setStyleSheet("#Tab_Dashboard::pane{border: 0; background-color: rgb(229, 231, 234); border-top-left-radius: 32px; border-top-right-radius: 32px;}")

        PanelHomePage = FrameHomePage()
        self.Tab_Dashboard.addTab(PanelHomePage, 'HomePage')

        PanelGenerateReport = FrameGenerateReport()
        self.Tab_Dashboard.addTab(PanelGenerateReport, 'GenerateReport')

        PanelAccount = FrameAccount()
        self.Tab_Dashboard.addTab(PanelAccount, 'Account')

        PanelSettings = FrameSettings(self.TabFrames)
        self.Tab_Dashboard.addTab(PanelSettings, 'Settings')

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

    def Update_PanelopcMouseClicked(self, index, Panelcomponent):
        self.Tab_Dashboard.setCurrentIndex(index)
        self.CurrentStatePanel.setStyleSheet("background-color: transparent")
        Panelcomponent.setStyleSheet("background-color: lightblue;")
        self.CurrentStatePanel = Panelcomponent
        self.setShadowWidget(Panelcomponent)

    # Eventos
    def PanelIconHomePageMouseClicked(self, event):
        self.Update_PanelopcMouseClicked(0, self.PanelIconHomePage)

    def PanelIconGenerateReportMouseClicked(self, event):
        self.Update_PanelopcMouseClicked(1, self.PanelIconGenerateReport)

    def PanelIconAccountMouseClicked(self, event):
        self.Update_PanelopcMouseClicked(2, self.PanelIconAccount)

    def PanelIconSettingsMouseClicked(self, event):
        self.Update_PanelopcMouseClicked(3, self.PanelIconSettings)

class FrameHomePage(QFrame):
    
    def __init__(self):
        super().__init__()
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
        LabelGreet.setText("Bienvenido Jean Pierre")
        LabelGreet.setObjectName("LabelGreet")
        LabelGreet.setGeometry(20, 100, 320, 40)
        LabelGreet.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setShadowWidget(LabelGreet)

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

class FrameGenerateReport(QFrame):
    
    def __init__(self):
        super().__init__()
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

        PanelTypeIncident = QFrame(self)
        PanelTypeIncident.setObjectName("InputPanel")
        PanelTypeIncident.setGeometry(30, 80, 300, 40)
        self.setShadowWidget(PanelTypeIncident)

        IconTypeIncident = QLabel(PanelTypeIncident)
        IconTypeIncident.setGeometry(10, 10, 20, 20)
        IconTypeIncident.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconTypeIncident, 'img/categorias.png')

        ListTypeIncident = QComboBox(PanelTypeIncident)
        ListTypeIncident.setGeometry(38, 5, 252, 30)
        ListTypeIncident.setPlaceholderText("Tipo de incidente...")

        ListTypeIncident.addItem('Robo')
        ListTypeIncident.addItem('Asalto')
        ListTypeIncident.addItem('Vandalismo')
        ListTypeIncident.addItem('Emergencia Médica')
        ListTypeIncident.addItem('Otro')

        PanelDescriptionIncident = QFrame(self)
        PanelDescriptionIncident.setGeometry(30, 130, 300, 80)
        PanelDescriptionIncident.setObjectName("InputPanel")
        self.setShadowWidget(PanelDescriptionIncident)

        IconDescriptionIncident = QLabel(PanelDescriptionIncident)
        IconDescriptionIncident.setGeometry(10, 10, 20, 20)
        IconDescriptionIncident.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconDescriptionIncident, 'img/mensaje.png')

        TextEditDescription = QTextEdit(PanelDescriptionIncident)
        TextEditDescription.setGeometry(38, 10, 252, 60)
        TextEditDescription.setPlaceholderText("Describe brevemente el incidente...")

        PanelAddress = QFrame(self)
        PanelAddress.setGeometry(30, 220, 300, 40)
        PanelAddress.setObjectName("InputPanel")
        self.setShadowWidget(PanelAddress)

        IconAddress = QLabel(PanelAddress)
        IconAddress.setGeometry(10, 10, 20, 20)
        IconAddress.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconAddress, 'img/ubicacion.png')

        InputAddress = QLineEdit(PanelAddress)
        InputAddress.setGeometry(38, 10, 252, 20)
        InputAddress.setObjectName("InputText")
        InputAddress.setPlaceholderText("Ingrese la ubicación del incidente")
        
        PanelDate = QFrame(self)
        PanelDate.setGeometry(30, 270, 140, 40)
        PanelDate.setObjectName("InputPanel")
        self.setShadowWidget(PanelDate)

        IconDate = QLabel(PanelDate)
        IconDate.setGeometry(10, 10, 20, 20)
        IconDate.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconDate, 'img/calendar.png')

        InputDate = QDateEdit(PanelDate)
        InputDate.setCalendarPopup(True)
        InputDate.setDate(QDate.currentDate())
        InputDate.setGeometry(38, 10, 90, 20)

        PanelHour = QFrame(self)
        PanelHour.setGeometry(190, 270, 140, 40)
        PanelHour.setObjectName("InputPanel")
        self.setShadowWidget(PanelHour)

        IconHour = QLabel(PanelHour)
        IconHour.setGeometry(10, 10, 20, 20)
        IconHour.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconHour, 'img/reloj.png')

        InputHour = QTimeEdit(PanelHour)
        InputHour.setTime(QTime.currentTime())
        InputHour.setGeometry(38, 10, 90, 20)

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

        InputNameContact = QLineEdit(PanelNameContact)
        InputNameContact.setGeometry(38, 10, 252, 20)
        InputNameContact.setObjectName("InputText")
        InputNameContact.setPlaceholderText("Nombre")

        PanelNumberPhone = QFrame(self)
        PanelNumberPhone.setGeometry(30, 436, 300, 40)
        PanelNumberPhone.setObjectName("InputPanel")
        self.setShadowWidget(PanelNumberPhone)

        IconNumberPhone = QLabel(PanelNumberPhone)
        IconNumberPhone.setGeometry(10, 10, 20, 20)
        IconNumberPhone.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconNumberPhone, 'img/telefono.png')

        InputNumberPhone = QLineEdit(PanelNumberPhone)
        InputNumberPhone.setGeometry(38, 10, 252, 20)
        InputNumberPhone.setObjectName("InputText")
        InputNumberPhone.setPlaceholderText("Número de Teléfono")

        opcAnonymity = QCheckBox(self)
        opcAnonymity.setText("Reportar de manera anónima")
        opcAnonymity.setGeometry(43, 496, 180, 14)
        opcAnonymity.setObjectName("opcAnonymity")
        opcAnonymity.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        opcAnonymity.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setShadowWidget(opcAnonymity)

        ButtonPerform = QLabel(self)
        ButtonPerform.setGeometry(280, 520, 50, 50)
        ButtonPerform.setStyleSheet("background-color: transparent;")
        ButtonPerform.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(ButtonPerform, 'img/next.png')
        self.setShadowWidget(ButtonPerform)

        ButtonPerform.mouseReleaseEvent = self.ButtonPerformMouseClicked

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

    # Eventos
    def IconAddEvidenceMouseClicked(self, event):
        options = QFileDialog.Option.ReadOnly
        FileDialog = QFileDialog()
        file_path, _ = FileDialog.getOpenFileName(self, "Abrir", "", "All Files (*);;Archivos de imagen (*.jpg;*.jpeg;*.png;*.bmp);;Archivos de vídeo (*.mp4;*.avi;*.mkv;*.mov)", options=options)

        if(file_path):
            self.InputEvidence.setText(file_path)
        else:
            self.InputEvidence.setText("Archivo no seleccionado")

    def ButtonPerformMouseClicked(self, event):
        pass

class FrameAccount(QFrame):
    
    cant_contacts = 0
    a = 19

    def __init__(self):
        super().__init__()
        self.initComponents()
        self.initStyle()

    def initComponents(self):
        
        IconProfile = QLabel(self)
        IconProfile.setGeometry(20, 30, 50, 50)
        IconProfile.setStyleSheet("background-color: transparent;")
        self.ResizeImage(IconProfile, 'img/3.png')

        LabelName = QLabel(self)
        LabelName.setText("Jean Pierre")
        LabelName.setGeometry(85, 30, 200, 30)
        LabelName.setObjectName("LabelName")

        LabelMail = QLabel(self)
        LabelMail.setText("jeanestrella578@gmail.com")
        LabelMail.setGeometry(85, 60, 200, 20)
        LabelMail.setObjectName("LabelMail")

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

        ButtonAddContact.clicked.connect(self.ButtonAddContactMouseClicked)

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

        self.ButtonAddContactMouseClicked()

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

    # Eventos
    def ButtonAddContactMouseClicked(self):

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
        LabelNameContact.setText("Jean Pierre")
        LabelNameContact.setGeometry(50, 0, 220, 15)
        LabelNameContact.setObjectName("LabelNameContact")

        LabelMail = QLabel(contact_widget)
        LabelMail.setText("jeanestrella578@gmail.com")
        LabelMail.setGeometry(50, 15, 220, 20)
        LabelMail.setObjectName("LabelMail")

        ButtonDelete = QPushButton(contact_widget)
        ButtonDelete.setGeometry(290, 6, 24, 24)
        ButtonDelete.setObjectName("ButtonDelete")

        ButtonDelete.clicked.connect(lambda: self.ButtonDeleteMouseClicked(contact_widget))

        IconDeleteContactProfile = QLabel(ButtonDelete)
        IconDeleteContactProfile.setGeometry(5, 5, 14, 14)
        IconDeleteContactProfile.setStyleSheet("background-color: transparent;")
        IconDeleteContactProfile.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ResizeImage(IconDeleteContactProfile, 'img/eliminar1.png')

        self.layoutV.addWidget(contact_widget)
        self.cant_contacts += 1

    def ButtonDeleteMouseClicked(self, widget):
        self.layoutV.removeWidget(widget)
        widget.deleteLater()
        self.cant_contacts -= 1
        if(self.cant_contacts < 10):
            self.scroll_area.setFixedHeight(self.scroll_area.height() - 40)

class FrameSettings(QFrame):
    
    def __init__(self, TabFrames):
        super().__init__()
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
        self.TabFrames.setCurrentIndex(0)