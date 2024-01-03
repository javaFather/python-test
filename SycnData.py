from demo import price_guangdong
from Login import login_with_captcha

# 用户名和密码
username = "lyy"
password = "111111"

# 登录 获取cookie,更新全局变量
login_with_captcha(username, password)

# 日前溪右送出侧电量和价格广东
# price_guangdong()
