import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QComboBox, QVBoxLayout,
    QMessageBox, QHBoxLayout
)
from PySide6.QtGui import QFont


class FormBiodata(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedSize(420, 450)

        self.setFont(QFont("Segoe UI", 10))

        self.setStyleSheet("""
        QWidget{
            background:#f3f4f6;
        }

        QLabel{
            color:#2c3e50;
        }

        QLineEdit{
            background:#eaf5ec;
            border:2px solid #2ecc71;
            border-radius:6px;
            padding:6px;
            color:#2c3e50;
        }

        QLineEdit::placeholder{
            color:#9aa0a6;
        }

        QComboBox{
            background:white;
            border:1px solid #cfcfcf;
            border-radius:6px;
            padding:6px;
            color:#2c3e50;
        }

        QComboBox QAbstractItemView{
            color:#2c3e50;
            background:white;
        }

        QPushButton{
            padding:8px;
            border-radius:6px;
            font-weight:bold;
        }

        QPushButton#btn_tampil{
            background:#3498db;
            color:white;
        }

        QPushButton#btn_reset{
            background:#95a5a6;
            color:white;
        }

        QLabel#hasil{
            background:#cfe6d5;
            border-left:5px solid #2ecc71;
            border-radius:6px;
            padding:12px;
        }
        """)

        self.nama = QLineEdit()
        self.nama.setPlaceholderText("Masukkan Nama")

        self.nim = QLineEdit()
        self.nim.setPlaceholderText("Masukkan NIM")

        self.kelas = QLineEdit()
        self.kelas.setPlaceholderText("Contoh: TI-2A")

        self.jk = QComboBox()
        self.jk.setEditable(False)
        self.jk.addItems(["Pilih Jenis Kelamin", "Laki-laki", "Perempuan"])

        self.btn_tampil = QPushButton("Tampilkan")
        self.btn_tampil.setObjectName("btn_tampil")

        self.btn_reset = QPushButton("Reset")
        self.btn_reset.setObjectName("btn_reset")

        self.hasil = QLabel("")
        self.hasil.setObjectName("hasil")

        form = QVBoxLayout()

        form.addWidget(QLabel("Nama Lengkap"))
        form.addWidget(self.nama)

        form.addWidget(QLabel("NIM"))
        form.addWidget(self.nim)

        form.addWidget(QLabel("Kelas"))
        form.addWidget(self.kelas)

        form.addWidget(QLabel("Jenis Kelamin"))
        form.addWidget(self.jk)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_tampil)
        btn_layout.addWidget(self.btn_reset)

        layout = QVBoxLayout()
        layout.addLayout(form)
        layout.addLayout(btn_layout)
        layout.addWidget(self.hasil)

        self.setLayout(layout)

        self.btn_tampil.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_form)

    def tampilkan_data(self):

        nama = self.nama.text()
        nim = self.nim.text()
        kelas = self.kelas.text()
        jk = self.jk.currentText()

        if nama == "" or nim == "" or kelas == "" or self.jk.currentIndex() == 0:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
            return

        self.hasil.setText(
            f"<b>DATA BIODATA</b><br><br>"
            f"Nama: {nama}<br>"
            f"NIM: {nim}<br>"
            f"Kelas: {kelas}<br>"
            f"Jenis Kelamin: {jk}"
        )

    def reset_form(self):
        self.nama.clear()
        self.nim.clear()
        self.kelas.clear()
        self.jk.setCurrentIndex(0)
        self.hasil.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())