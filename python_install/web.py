from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='resources')


@app.route('/local/hello')
def Hello():
    return render_template('/hello.html')


@app.route("/register", methods=['GET', 'POST'])
def Register():
    if request.method == "GET":
        return render_template('/register.html')
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        sex = request.form.get("sex")
        return jsonify({'result':'success'})


def Register():
    return render_template('/hello.html')


if __name__ == '__main__':
    app.run(host="", port=8000);
