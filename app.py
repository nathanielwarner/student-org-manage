from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
app = Flask(__name__)


class Database:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.student_orgs

    def list_all_orgs(self):
        result = self.db.orgs.find()
        return result

    def get_one_org(self, org_id):
        print("todo")

    def insert_org(self, data):
        return self.db.orgs.insert_one(data.to_dict()).inserted_id


@app.route('/')
def all_orgs():
    db = Database()
    res = db.list_all_orgs()
    return render_template('all_orgs.html', result=res, content_type='application/json')


@app.route('/org/<path:text>')
def one_org(text):
    db = Database()


@app.route('/insert', methods=['POST'])
def insert_data():
    form_data = request.form
    db = Database()
    response = db.insert_org(form_data)
    print(response)
    return redirect('/')

if __name__ == '__main__':
    app.run()
