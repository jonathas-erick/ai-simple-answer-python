from PySide6.QtWidgets import QApplication
from chatAI import ChatAI
import sys

app = QApplication(sys.argv)

window = ChatAI(app)
window.show()

app.exec()
''