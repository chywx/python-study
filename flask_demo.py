from flask import Flask, jsonify, request
import re

app = Flask(__name__)

# 使通过jsonify返回的中文显示正常，否则显示为ASCII码
app.config["JSON_AS_ASCII"] = False

# 因为是简单模拟，所以数据就以下面字典形式存储，而不是存储在数据库
user_data = [
    {"id": 1, "username": "刘德华", "password": "123456", "telephone": "13838395588"},
    {"id": 2, "username": "梅艳芳", "password": "666666", "telephone": "13843895511"},
    {"id": 3, "username": "陈百强", "password": "888888", "telephone": "13853895510"}
]


@app.route("/users", methods=["GET"])
def get_all_users():
    """
    查询所有用户信息
    :return:
    """
    return jsonify({"code": 1000, "data": user_data, "msg": "查询成功"})


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """
    查询某个用户信息
    :param user_id: 用户id
    :return:
    """
    if user_id > 0 and user_id <= len(user_data):
        return jsonify({"code": 1000, "data": user_data[user_id - 1], "msg": "查询成功"})
    return jsonify({"code": 1000, "msg": "用户不存在"})


@app.route("/register", methods=['POST'])
def user_register():
    """
    注册用户
    :return:
    """
    # request.json.get("username")即从发送的json格式的请求参数中获取username的值
    username = request.json.get("username").strip()  # 用户名
    password = request.json.get("password").strip()  # 密码
    telephone = request.json.get("telephone", "").strip()  # 手机号，默认为空串
    if username and password and telephone:
        if username in ("刘德华", "梅艳芳", "张学友"):
            return jsonify({"code": 2001, "msg": "用户名已存在！"})
        elif not (len(telephone) == 11 and re.match("^1[3,5,7,8]\d{9}$", telephone)):
            return jsonify({"code": 4001, "msg": "手机号格式不正确！"})
        else:
            return jsonify({"code": 1000, "msg": "注册成功！"})
    else:
        return jsonify({"code": 2001, "msg": "用户名/密码/手机号不能为空，请检查！"})


@app.route("/login", methods=['POST'])
def user_login():
    """
    登录
    :return:
    """
    username = request.json.get("username")
    password = request.json.get("password")
    if username and password:
        if username == "刘德华" and password == "123456":
            return jsonify({"code": 1000, "msg": "登录成功！", "token": "sh34ljjl08s32730dj"})
        return jsonify({"code": 4001, "msg": "用户名或密码错误！"})
    else:
        return jsonify({"code": 2001, "msg": "用户名或密码不能为空！"})


if __name__ == '__main__':
    app.run(debug=True)