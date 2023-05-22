from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = generate_response(user_input)
        return jsonify({"response": response})
    return render_template("index.html")

def generate_response(user_input):
    # 在这里，你可以使用GPT模型生成回复。为简化示例，我们将返回一个简单的字符串。
    return f"你好！你刚才说了：{user_input}"

if __name__ == "__main__":
    app.run(debug=True)
