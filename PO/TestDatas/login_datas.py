# 正常场景
success = ("18684720553","python")


# 异常场景  - 用户名为空/密码为空/用户名格式不正确
cases = [
        {"user":"","passwd":"python","check":"请输入手机号"},
        {"user": "18684720553", "passwd": "", "check": "请输入密码"},
        {"user": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
    ]

