from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
import os
import markdown2

load_dotenv()

app = Flask(__name__)

# 初始化 Gemini 客戶端
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# 首頁路由
@app.route('/')
def home():
    return render_template('home.html')

# Gemini 路由
@app.route('/gemini', methods=['GET', 'POST'])
def gemini():
    response = None
    html_content = None
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        if user_input:
            # 生成回應
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_input)
            # 將回應轉換為 HTML
            if response and response.text:
                html_content = markdown2.markdown(response.text)
    return render_template('gemini.html', response=response, html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)