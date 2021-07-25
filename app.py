from flask import Flask,url_for,render_template,request
from flaskext.markdown import Markdown


import spacy
from spacy import displacy
import json
nlp = spacy.load('en_core_web_trf')


HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


# Init
app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')
   

@app.route('/extractor',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		doc = nlp(raw_text)
        # specification to only highlight company entities
		colors = {"ORG": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
		options = {"ents": ["ORG"], "colors": colors}
		html = displacy.render(doc,style="ent",options=options)
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

	return render_template('results.html',rawtext=raw_text,result=result)


if __name__ == '__main__':
	app.run(debug=True, use_reloader=False)





