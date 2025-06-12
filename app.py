from flask import Flask, render_template

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa route cho trang chủ
@app.route('/')
def index():
    """Hàm này sẽ được gọi khi người dùng truy cập vào URL /"""
    return render_template('index.html')

# Định nghĩa route cho trang giới thiệu
@app.route('/about')
def about():
    """Hàm này sẽ được gọi khi người dùng truy cập vào URL /about"""
    return render_template('about.html')

# Chạy ứng dụng khi file này được thực thi trực tiếp
if __name__ == '__main__':
    # debug=True giúp tự động tải lại server khi có thay đổi code
    app.run(debug=True)
