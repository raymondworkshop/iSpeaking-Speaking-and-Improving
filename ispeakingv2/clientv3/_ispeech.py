from flask import Flask
from flask import jsonify, request
from flask import render_template
#from flask import Blueprint
#from flask_cors import CORS

#from app import app
app = Flask(__name__)
app.debug = True
#app.config.from_object(__name__)

#CORS(app, resources={r'/*': {'origins': '*'}})

#bp = Blueprint('ispeech', __name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():
        return "Hello, World!"

@app.route('/')
def index():
    # fetch from db
    #
    txt=""
    _ipa= ""
    """
    dir = 'C:/Users/raymondzhao/myproject/dev.speech/speech/audio/'
    demo = sr.AudioFile( dir + 'english81.wav')

    txt = get_post(demo)
    _ipa = ipa.convert(txt)
    return render_template('ispeech/record.html', posts=txt, _ipa=_ipa)
    """
    #return "tornado call flask!"
    return render_template('../templates/index.html')

@app.route('/record', methods=['GET', 'POST'])
def record():
    print("record the audio")
    
    return "record the audio"


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
