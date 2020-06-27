from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

from .utils import find_content, OpenGraphImage


@app.route('/')
@app.route('/index/')
def index():
    description = """Texte INDEX : Toi, tu sais comment utiliser la console ! Jamais à court d'idées pour réaliser 
    ton objectif, tu es déterminé-e et persévérant-e. Tes amis disent d'ailleurs volontiers que tu as du caractère et 
    que tu ne te laisses pas marcher sur les pieds. Un peu hacker sur les bords, tu aimes trouver des solutions à 
    tout problème. N'aurais-tu pas un petit problème d'autorité ? ;-) """

    if 'img' in request.args:
        img = request.args['img']
        og_url = url_for('index', img=img, _external=True)
        og_image = url_for('static', filename=img, _external=True)

    else:
        og_url = url_for('index', _external=True)
        og_image = url_for('static', filename="tmp/sample.jpg", _external=True)

    return render_template('index.html',
                           user_name='John_index',
                           user_image=url_for('static', filename='img/profil.png'),
                           description=description,
                           blur=True,
                           og_url=og_url,
                           og_image=og_image)


@app.route('/result/')
def result():
    gender = request.args.get('gender')
    description = find_content(gender).description
    user_name = request.args.get('first_name')
    uid = request.args.get('id')
    profil_pic = 'http://graph.facebook.com/' + uid + '/picture?type=large'
    img = OpenGraphImage(uid, user_name, description).location
    og_url = url_for('index', _external=True, img=img)
    return render_template('result.html',
                           user_name=user_name,
                           user_image=profil_pic,
                           description=description,
                           og_url=og_url)
