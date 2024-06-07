
# 数据库连接配置
sql_type = "mysql"
sql_driver = "pymysql"
sql_host = "localhost"
sql_port = "3306"
sql_user = "root"
sql_password = "020316"
sql_database = "pims"

SECRET_KEY = "0704abcde"
ALGORITHM = "HS256"


# 数据库连接字符串
sql_dsn = f"{sql_type}+{sql_driver}://{sql_user}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"

