from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# Below is a list of dictionaries
JOBS = [
    {
        'id' : 0,
        'title' : 'Data Analist',
        'location' : 'Tilburg, the Netherlands',
        'salary': "EUR 44.000"
    },
    {
        'id' : 1,
        'title' : 'Front-End Web Developer',
        'location' : 'Tilburg, the Netherlands',
        'salary': "EUR 40.000"
    },
        {
        'id' : 2,
        'title' : 'Back-End Web Developer',
        'location' : 'Breda, the Netherlands',
        'salary': "EUR 45.000"
    },
        {
        'id' : 3,
        'title' : 'Scrum Bachelor',
        'location' : 'Tilburg, the Netherlands',
        'salary': "EUR 25.000"
    },
        {
        'id' : 4,
        'title' : "IoT thingy do-er",
        'Location' : "remote",
        'salary' : "+- 55.000"
        }
    
    ]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run('0.0.0.0', debug = True)