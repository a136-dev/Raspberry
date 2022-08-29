import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.setCentralWidget(self.tabs)

        self.tabs.tabBarDoubleClicked.connect(self.tab_open)

        self.tabs.tabCloseRequested.connect(self.close_tab)

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_button = QAction(QIcon('left-arrow.png'), "Back", self)
        back_button.triggered.connect(lambda: self.tabs.currentWidget().back())
        navbar.addAction(back_button)

        forward_button = QAction(QIcon('right-arrow.png'), "Forward", self)
        forward_button.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navbar.addAction(forward_button)

        refresh_button = QAction(QIcon('refresh.png'), "Refresh", self)
        refresh_button.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navbar.addAction(refresh_button)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText('Type a URL')
        navbar.addWidget(self.url_bar)
        self.url_bar.returnPressed.connect(self.navigate_url)

        self.setWindowTitle("Raspberry")
        self.setMinimumSize(1200, 900)
        self.setWindowIcon(QIcon('raspberry.png'))

        self.setStyleSheet("""QWidget{
           color: rgb(255, 255, 255);
        }
        
        * {
            background-color: rgb(48, 48, 48);
        }

        QLineEdit {
            margin-top: 1px;
            border: 2px solid rgb(77, 77, 77);
            border-radius: 10px;
            padding: 5px;
            background-color: rgb(77, 77, 77);
            color: rgb(255, 255, 255);
        }
        
        QLineEdit:focus {
            border: 2px solid rgb(0, 136, 255);
            color: rgb(200, 200, 200);
       }

        QTabBar::tab {
            background-color:#222;
            padding: 15px;
        }
 
         QTabBar::tab::selected, QTabBar::tab:hover{
            background-color:#555;
        }
        
        QLineEdit {
        }
        
        }""")

        self.add_new_tab(QUrl("file:///C:/Users/axell/OneDrive/Documents/Bureau/Dev/web/Raspberry/index.html"), "New tab")

        self.showMaximized()

    def add_new_tab(self, qurl=None, label="BLANK"):
        if qurl is None:
            qurl = QUrl('')

        browser = QWebEngineView()
        browser.setUrl(qurl)

        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)

        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                         self.tabs.setTabText(i, browser.page().title()))

    def tab_open(self):
            self.add_new_tab(QUrl("file:///C:/Users/axell/OneDrive/Documents/Bureau/Dev/web/Raspberry/index.html"), "New tab")

    def close_tab(self, i):
        if self.tabs.count() > 1:
            self.tabs.removeTab(i)

    def navigate_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.tabs.currentWidget().setUrl(q);

qapp = QApplication(sys.argv)
app = App()
qapp.exec_()