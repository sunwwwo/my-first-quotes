import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit
import pathlib
import textwrap
import PIL.Image
import google.generativeai as genai

class StoryGenerator(QWidget):
    def __init__(self):
        super().__init__()
        
        # API 키 설정
        GOOGLE_API_KEY = 'AIzaSyBL1ggCd-RTSBdId9LchT5ASrpOuKmGCNk'
        genai.configure(api_key=GOOGLE_API_KEY)
        
        # 모델 선택 (텍스트 전용)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("잼얘 생성기")
        layout = QVBoxLayout()
        
        keyword_label = QLabel("키워드:")
        layout.addWidget(keyword_label)
        
        self.keyword_input = QLineEdit()
        layout.addWidget(self.keyword_input)
        
        style_label = QLabel("문체:")
        layout.addWidget(style_label)
        
        self.style_input = QComboBox()
        self.style_input.addItems(["유머러스", "서정적", "모험심", "판타지", "미스터리", "공포", "로맨스", "SF", "역사"])
        layout.addWidget(self.style_input)
        
        generate_button = QPushButton("이야기 생성")
        generate_button.clicked.connect(self.generate_story)
        layout.addWidget(generate_button)
        
        self.story_output = QTextEdit()
        self.story_output.setReadOnly(True)
        layout.addWidget(self.story_output)
        
        self.setLayout(layout)
        self.show()
        
    def generate_story(self):
        keywords = self.keyword_input.text()
        style = self.style_input.currentText()
        
        prompt = f"다음 조건을 지켜 7문장 정도의 재미있는 이야기를 지어주세요. 포함할 키워드: {keywords}, 이야기의 문체: {style}"
        
        try:
            # 스트리밍 응답 없이 생성
            response = self.model.generate_content(prompt)
            self.story_output.setText(response.text)
        except Exception as e:
            self.story_output.setText(f"오류가 발생했습니다: {str(e)}")

def main():
    app = QApplication(sys.argv)
    ex = StoryGenerator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()