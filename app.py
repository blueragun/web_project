import os #디렉토리 절대 경로
from flask import Flask
from flask import render_template #template폴더 안에 파일을 쓰겠다
from flask import request #회원정보를 제출할 때 쓰는 request, post요청 처리
from flask import redirect #리다이렉트
#from flask_sqlalchemy import SQLAlchemy
from Models import db
from Models import User
from flask import session #세션
from flask_wtf.csrf import CSRFProtect #csrf
from Forms import RegisterForm, LoginForm
from datetime import datetime
app = Flask(__name__)

# db 연결
app.config.from_pyfile('config.py')
database = create_engin(app.config['DB_URL'], encoding = 'utf-8')
app.database = database


@app.route('/')
def mainpage():
    userid = session.get('userid',None)
    return render_template('main.html', userid=userid)
    

@app.route('/register', methods=['GET', 'POST']) #GET(정보보기), POST(정보수정) 메서드 허용
def register():
    form = RegisterForm()
    if form.validate_on_submit(): #유효성 검사. 내용 채우지 않은 항목이 있는지까지 체크
        usertable = User() 
        usertable.userid = form.data.get('userid')
        usertable.email = form.data.get('email')
        usertable.password = form.data.get('password')

        conn = database.connect()
        cursor =conn.cursur()

        sql ="INSERT INTO 0000"
        cursor.execute(sql)

        data =cursor.fetchall()

        if not data :
            conn.commit()
            return "등록완료"
                return redirect(url_for('mainpage'))
        else :
            conn.rollback()
            return "등록실패"

        cursor.close()
        conn.close()
        
    return render_template('register.html', form=form) #form이 어떤 form인지 명시한다

@app.route('/login', methods=['GET','POST'])  
def login():
    form = LoginForm() #로그인폼
    if form.validate_on_submit(): #유효성 검사
        print('{}가 로그인 했습니다'.format(form.data.get('userid')))
        session['userid']=form.data.get('userid') #form에서 가져온 userid를 세션에 저장
        return redirect('/') #성공하면 main.html로
    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('userid', None)
    return redirect('/')

if __name__ == "__main__":
    app.run()