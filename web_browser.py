import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
)
from PySide6.QtWebEngineWidgets import QWebEngineView

domains = [".com", ".org", ".gov", ".au", ".io"]
prefixes = ["https://", "http://"]

class BrowserTab(QWidget):
    def __init__(self, url="https://google.com"):
        super().__init__()
        self.webview = QWebEngineView()
        self.webview.setUrl(url)

        self.url_bar = QLineEdit(url)
        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")
        self.refresh_btn = QPushButton("⟳")
        self.go_btn = QPushButton("Go")

        nav = QHBoxLayout()
        nav.addWidget(self.back_btn)
        nav.addWidget(self.forward_btn)
        nav.addWidget(self.refresh_btn)
        nav.addWidget(self.url_bar)
        nav.addWidget(self.go_btn)

        layout = QVBoxLayout()
        layout.addLayout(nav)
        layout.addWidget(self.webview)
        self.setLayout(layout)

        self.back_btn.clicked.connect(self.webview.back)
        self.forward_btn.clicked.connect(self.webview.forward)
        self.refresh_btn.clicked.connect(self.webview.reload)
        self.go_btn.clicked.connect(self.navigate)
        self.url_bar.returnPressed.connect(self.navigate)

    def navigate(self):
        url = self.url_bar.text()
        name_tab(url)
        if not url.startswith("http"):
            url = "https://" + url
        self.webview.setUrl(url)
        self.url_bar.setText(url)


def name_tab(url):
    global domains, prefixes
    name = url
    for i in prefixes:
        if i in name:
            name = list(name)
            for x in range(len(i)):
                name.pop(0)

    string_name = ""
    for i in name:
        string_name += i
    name = string_name

    for i in domains:
        print(i, name)
        if i in name:
            name = list(name)
            for x in range(len(i)):
                name.pop(-1)

    string_name = ""
    for i in name:
        string_name += i

    return string_name

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sLOCKED Browser")
        self.setGeometry(100, 100, 1000, 700)

        self.tabs = QTabWidget()
        self.number_of_tabs = 1
        self.setCentralWidget(self.tabs)

        self.add_new_tab("https://google.com")
        self.tabs.addTab(QWidget(), "+")
        self.tabs.currentChanged.connect(self.check_new_tab)

    def add_new_tab(self, url="https://google.com"):
        tab = BrowserTab(url)
        index = self.tabs.count() - 1
        self.tabs.insertTab(index, tab, f"{name_tab(url)}")
        self.number_of_tabs += 1
        self.tabs.setCurrentIndex(index)

    def check_new_tab(self, index):
        if self.tabs.tabText(index) == "+":
            self.add_new_tab()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
