from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def csscompare():  # firstlevel css compare
    # Flesh out CSS

    return render_template('test.html')


#if __name__ == '__main__':
#    app.run()
