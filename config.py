db = {
    'user': 'lab03',
    'password': 'lab03',
    'host': '13.112.242.65',
    'port': 22 # 다른 번호로 포트번호를 만들었다면 다른 번호
    'database': UserInfo # 만든 database_name
}
 
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"