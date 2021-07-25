# import librairies from packages
from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForTokenClassification
# python3 -c "from transformers import pipeline"
# uncomment the line above if you encounter issues with the line below
# then comment the line with an issue
from transformers import pipeline
import pandas as pd


# using a pre-trained transformer model
# it's a fine-tuned model based on the original "base-base-cased" model
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)        


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/extractor',methods=["POST"])
def process():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        ner_results = nlp(rawtext)

        companies_found = []
        for elts in ner_results:
        # only filling the list created above with the entities like B-ORG or I-ORG
        # B-ORG means, the entity detected is the beginning of an organisation, right after an organisation
        # I-ORG means, the entity detected is an organisation
        # their scores or confidences are also stored in the list
          if (elts['entity'] == "B-ORG" or elts['entity'] == "I-ORG"):
            companies_found.append((elts['word'],elts['score']))
            
        nb_companies = len(companies_found)
        df_comp = pd.DataFrame(companies_found, columns=["companies' name","confidences"])
        
    return render_template("index.html",results=[df_comp.to_html(classes='data', header="true")],num_of_results = nb_companies)


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True, use_reloader=False)
    #app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
    #app.run(host="192.168.0.12", port=5000, threaded=True, debug=True)
    #app.run(host="0.0.0.0")
    #app.run(debug=False)