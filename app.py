""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ Эта функция запуская и отвечает за процесс возврата результата index.html. """

    return render_template('index.html')


@app.route("/ui_test")
def ui_test():
    """ Эта функция запуская и отвечает за генерацию отчета по UI автотестам в allure. """
    cmd = ["C:/Program Files/Git/bin/bash.exe"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


@app.route("/api_test_get")
def api_tes_get():
    """ Эта функция запуская и отвечает за генерацию отчета проверки статус кода Get в allure. """
    cmd = ["C:/Program Files/Git/bin/bash.exe"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


@app.route("/api_test_put")
def api_test_put():
    """ Эта функция запуская и отвечает за генерацию отчета проверки Post. """
    cmd = ["C:/Program Files/Git/bin/bash.exe"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('welcome.html', text=out, json=out)


@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["C:/Program Files/Git/bin/bash.exe", "./scripts/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/run_ui")
def run_ui():
    """ Эта функция запуская и отвечает за тесты страницы /example. """

    cmd = ["C:/Program Files/Git/bin/bash.exe"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
