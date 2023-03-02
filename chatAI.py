import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QMainWindow
import openai
openai.api_key = "YOUR API KEY"

class ChatAI(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("ChatAI Message")
        self.setGeometry(100, 100, 500, 300)

        
        self.question_label = QLabel("Question:")
        self.question_text = QTextEdit()
        self.answer_label = QLabel("Answer:")
        self.answer_text = QTextEdit()
        self.answer_text.setReadOnly(True)
        self.ask_button = QPushButton("Ask to CHAT AI")
        self.ask_button.clicked.connect(self.get_answer)

        
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.question_label)
        hbox1.addWidget(self.question_text)
        vbox.addLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.answer_label)
        hbox2.addWidget(self.answer_text)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.ask_button)

       
        self.setLayout(vbox)

    def get_answer(self):
        
        question = self.question_text.toPlainText()

       
        completions = openai.Completion.create(
            engine="davinci-codex",
            prompt=question,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            
        )

        
        answer = completions.choices[0].text.strip()

        
        self.answer_text.setText(answer)

