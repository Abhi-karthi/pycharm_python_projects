import sys
from difflib import IS_LINE_JUNK
import processing_units

from PySide6 import *
from PySide6 import QtCore
from openai import OpenAI
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import threading

from processing_units import remove_char_in_string

client = OpenAI(api_key="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")
current_messages = []
first = False

def query(prompt="", ai_model="gpt-4-turbo"):

    global current_messages
    current_messages.append({"role": "system", "content": f"{prompt}"})
    response = client.chat.completions.create(
        model=ai_model,
        messages=current_messages
    )

    return response.choices[-1].message.content


# print(query("How dow you change the font and font size in a label in Pyside6?"))
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Chatbot")
window.setGeometry(100, 100, 400, 200)

palette = window.palette()
palette.setColor(QPalette.Window, QColor(20, 20, 148))
window.setPalette(palette)

window.resize(750, 421)
main_title_font = QFont()
main_title_font.setFamily("Times New Roman")
main_title_font.setPointSize(32)
main_title_label = QLabel("Chatbot:", parent=window) # , QFont="Arial")
main_title_label.setFont(main_title_font)
# main_title_label.setAlignment(Qt.AlignCenter)
main_title_label.setFixedWidth(200)

chat_response_font = QFont()
chat_response_font.setFamily("Times New Roman")
chat_response_font.setPointSize(18)
chat_response_label = QLabel("", parent=window)
chat_response_label.setFont(chat_response_font)
chat_response_label.setMaximumWidth(window.width()-40)
chat_response_label.setWordWrap(True)
chat_response_label.setAlignment(Qt.AlignCenter)

scroll_area = QScrollArea()
scroll_area.setWidget(chat_response_label)
scroll_area.setWidgetResizable(True)
scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())


query_entry = QLineEdit()
query_entry.setText("Enter query here")
query_entry_text = ""

enter_button = QPushButton("Enter")


def enter_button_command():
    global scroll_area, query_entry, query_entry_text
    global first, chat_response_label

    current_chat_response_label_text = chat_response_label.text()
    number_of_dashes = (window.width()-40)/6
    dashes = ""

    for i in range(int(number_of_dashes)):
        dashes += "-"
    if first:
        chat_response_label.setText(current_chat_response_label_text + "\n" + "\n" + f"{dashes}" + "\n" + f"\n{remove_char_in_string('*', query(query_entry_text))}")
    else:
        chat_response_label.setText(remove_char_in_string('*', query(query_entry_text)))


    # query_entry.clear()
    # print("1")
    chat_response_label.adjustSize()
    scroll_area.verticalScrollBar().setValue(scroll_area.verticalScrollBar().maximum())
    first = True
    # print("enter")


def enter_button_thread():
    global query_entry_text, query_entry
    query_entry_text = query_entry.text()
    query_entry.setText("")
    new_thread = threading.Thread(target=enter_button_command)
    new_thread.start()
    # print("hi")


enter_button.clicked.connect(enter_button_thread)
query_entry.returnPressed.connect(enter_button_thread)

# quit_button = QPushButton("Quit")

layout = QGridLayout()
layout.addWidget(main_title_label, 0, 0) #, alignment=Qt.AlignCenter)
layout.addWidget(scroll_area, 0, 0)
layout.addWidget(query_entry, 2, 0)
layout.addWidget(enter_button, 3, 0) # , alignment=Qt.AlignCenter)
# layout.addWidget(quit_button, 3, 0)
window.setLayout(layout)
window.show()
app.exec()
