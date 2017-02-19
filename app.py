from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session 
import os, inspect

class MyServer(Flask):
  def __init__(self, *args, **kwargs):
    super(MyServer, self).__init__(*args, **kwargs)

    #instanciate your variables here
    self.df = []

            
app = MyServer(__name__)


app.config['IMAGE_FOLDER'] = '/Users/gerardharte/Documents/Side Projects/WhaleTinder/static/img/unclassified/'

@app.route("/")
def index():
    print "Rendering index.html"

    img_files = [ f for f in os.listdir(app.config['IMAGE_FOLDER']) if f <> '.DS_Store' ]

    return render_template("index.html", file_list = img_files[:50])

@app.route("/liked", methods=['POST', 'GET'])
def liked():
    img_to_move = request.form['img'].rstrip()

    path_from = os.path.join(app.config['IMAGE_FOLDER'], img_to_move)
    path_to = os.path.join("/Users/gerardharte/Documents/Side Projects/WhaleTinder/static/img/whales/", img_to_move)
 
    print 'from: ' + path_from 
    print 'to: ' + path_to

    os.rename(path_from, path_to)

    return ('', 204)

@app.route("/disliked", methods=['POST', 'GET'])
def disliked():
    img_to_move = request.form['img'].rstrip()

    path_from = os.path.join(app.config['IMAGE_FOLDER'], img_to_move)
    path_to = os.path.join("/Users/gerardharte/Documents/Side Projects/WhaleTinder/static/img/non_whales/", img_to_move)
 
    print 'from: ' + path_from 
    print 'to: ' + path_to

    os.rename(path_from, path_to)
    return ('', 204)



@app.route("/view", methods=['POST', 'GET'])
def view():
    img_path = 'static/img/raw_images'
    img_files = [ f for f in os.listdir(img_path)[:10] ]
    print img_files
    return render_template('view.html', file_list = img_files)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5001,debug=True)
    
