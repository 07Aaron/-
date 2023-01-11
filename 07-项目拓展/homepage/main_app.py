from flask import Flask, render_template

app = Flask(__name__)


@app.route('/homepage')
def home_nav():
    return render_template('index.html')


@app.route('/homepage/my')
def home_my():
    return render_template('my.html')


@app.route('/homepage/class')
def home_class():
    return render_template('class.html')


@app.route('/homepage/school')
def home_school():
    return render_template('school.html')


if __name__ == '__main__':
	app.run(port=5001,debug= True)


