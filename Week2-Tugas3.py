import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QCheckBox, QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import Qt


class LoginForm(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setFixedSize(380, 320)

        self.setStyleSheet("""
        QWidget{
            background:#f3f4f6;
            font-family:Segoe UI;
        }

        QLabel#judul{
            background:#8e5bb5;
            color:white;
            font-size:18px;
            font-weight:bold;
            padding:10px;
            border-radius:6px;
        }

       QLineEdit{
            padding:6px;
            border-radius:6px;
            border:2px solid #2ecc71;
            background:#eaf5ec;
            color:#2c3e50;
        }
        QLineEdit::placeholder{
            color:#9aa0a6;
        }
        QCheckBox{
            color:#2c3e50;
        }

        QCheckBox::indicator{
            width:16px;
            height:16px;
        }

        QCheckBox::indicator:unchecked{
            border:2px solid #7f8c8d;
            background:white;
        }

        QCheckBox::indicator:checked{
            border:2px solid #2ecc71;
            background:#2ecc71;
        }
        QPushButton{
            padding:8px;
            border-radius:6px;
            font-weight:bold;
            color:white;
        }

        QPushButton#login{
            background:#27ae60;
        }

        QPushButton#reset{
            background:#95a5a6;
        }

        QLabel#success{
            background:#d4edda;
            border-left:5px solid #2ecc71;
            padding:10px;
            border-radius:6px;
        }
        QLabel{
            color:#2c3e50;
            font-weight:500;
        }

        QLabel#error{
            background:#f8d7da;
            border-left:5px solid #e74c3c;
            padding:10px;
            border-radius:6px;
        }
        """)

        self.judul = QLabel("LOGIN")
        self.judul.setObjectName("judul")
        self.judul.setAlignment(Qt.AlignCenter)

        self.username = QLineEdit()
        self.password = QLineEdit()

        self.password.setEchoMode(QLineEdit.Password)

        self.show_pass = QCheckBox("Tampilkan Password")

        self.btn_login = QPushButton("Login")
        self.btn_login.setObjectName("login")

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setObjectName("reset")

        self.pesan = QLabel("")
        self.pesan.hide()

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_login)
        btn_layout.addWidget(self.btn_reset)

        layout = QVBoxLayout()

        layout.addWidget(self.judul)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)

        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)

        layout.addWidget(self.show_pass)

        layout.addLayout(btn_layout)

        layout.addWidget(self.pesan)

        self.setLayout(layout)

        self.show_pass.stateChanged.connect(self.toggle_password)
        self.btn_login.clicked.connect(self.login)
        self.btn_reset.clicked.connect(self.reset)

    def toggle_password(self):

        if self.show_pass.isChecked():
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)

    def login(self):

        user = self.username.text()
        pw = self.password.text()

        if user == "admin" and pw == "12345":

            self.pesan.setObjectName("success")
            self.pesan.setText("Login berhasil! Selamat datang, admin.")
            self.pesan.show()

        else:

            self.pesan.setObjectName("error")
            self.pesan.setText("Login gagal! Username atau password salah.")
            self.pesan.show()

        self.pesan.setStyle(self.style())

    def reset(self):

        self.username.clear()
        self.password.clear()
        self.show_pass.setChecked(False)
        self.password.setEchoMode(QLineEdit.Password)
        self.pesan.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())