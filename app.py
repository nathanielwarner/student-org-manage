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

    def get_org(self, acronym):
        result = self.db.orgs.find({"acronym": acronym})
        return result

    def insert_org(self, data):
        return self.db.orgs.insert_one(data.to_dict()).inserted_id

    def update_org(self, data):
        org_data = data.to_dict()
        return self.db.orgs.replace_one({"acronym": org_data["acronym"]}, org_data)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/master_admin')
def all_orgs():
    db = Database()
    res = db.list_all_orgs()
    return render_template('all_orgs.html', result=res, content_type='application/json')


@app.route('/org/details/<path:text>')
def org_details(text):
    db = Database()
    res = db.get_org(text)
    return render_template('org_details.html', result=res[0], content_type='application/json')


@app.route('/org/dashboard/<path:text>')
def org_dashboard(text):
    db = Database()
    res = db.get_org(text)
    return render_template('org_dashboard.html', result=res[0], content_type='application/json')


@app.route('/insert', methods=['POST'])
def insert_data():
    form_data = request.form
    db = Database()
    response = db.insert_org(form_data)
    print(response)
    return redirect('/')


@app.route('/update', methods=['POST'])
def update_data():
    form_data = request.form
    db = Database()
    response = db.update_org(form_data)
    print(response)
    return redirect('/')


if __name__ == '__main__':
    app.run()
