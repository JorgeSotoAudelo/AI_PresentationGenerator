""""The main app of my flask proyect"""


from flask import Flask, render_template
app = Flask('run',template_folder='app/views')


@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

