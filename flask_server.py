from flask import Flask, url_for, request, render_template
import pandas as pd
import json
app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('resources\Hospitals.csv')
    #TODO: GRAB THESE AND PUT THEM IN JSON THEN PASS TO THE TEMPLATE
    #print(df.NAME,df.LATITUDE,df.LONGITUDE)
    hospitals_df = df.filter(['NAME','LATITUDE','LONGITUDE'], axis=1)
    #print(hospitals_df.head())
    hospitals_json = json.loads(hospitals_df.to_json(orient='records'))
    print(type(hospitals_json))

    return render_template('index.html', hosptials_json=hospitals_json)


if __name__ == "__main__":
    app.run(debug=True)