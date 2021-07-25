# company_name_extractor
The aim of this project is to extract company names from a paragraph feeded to an api interface, which renders the companies' names along with their confidences. To do so, we use a transformer model.

# How to run the app

Before running the app please make sure you run the commands below in your terminal :
- pip3 install -U spacy
- pip3 install spacy[transformers]
- python3 -m spacy download en_core_web_trf
- pip3 install flask-markdown

When you've successfully ran the commands above follow as described below :
- download the folder named "templates" and the file named "app.py"
- put those 2 (1 folder + 1 file) in a same folder, you create
- go to this folder via your terminal
- then type : python3 app.py

You should get the following message : "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)". When you see this, copy the whole http address and paste it in your favorite browser. Then load the page and follow the instructions. It's very straightforward !
