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

    def list_all_users(self):
        result = self.db.users.find()
        return result

    def get_user(self, user_id):
        return self.db.users.find({"id": user_id})

    def insert_user(self, data):
        return self.db.users.insert_one(data.to_dict()).inserted_id


@app.route('/')
def index():
    return "Hello World!"


@app.route('/master_admin/')
def all_orgs():
    db = Database()
    orgs = db.list_all_orgs()
    users = db.list_all_users()
    return render_template('master_admin.html', orgs=orgs, users=users, content_type='application/json')


@app.route('/org_details/<path:text>/')
def org_details(text):
    db = Database()
    res = db.get_org(text)
    return render_template('org_details.html', result=res[0], content_type='application/json')


@app.route('/org_edit/<path:text>/')
def org_dashboard(text):
    db = Database()
    res = db.get_org(text)
    return render_template('org_edit.html', result=res[0], content_type='application/json')


@app.route('/user_dash/<path:text>/')
def user_dashboard(text):
    db = Database()
    res = db.get_user(text)
    return render_template('user_dash.html', result=res[0], content_type='application/json')


@app.route('/insert_org/', methods=['POST'])
def insert_org():
    form_data = request.form
    db = Database()
    response = db.insert_org(form_data)
    print(response)
    return redirect('/')


@app.route('/update_org/', methods=['POST'])
def update_org():
    form_data = request.form
    db = Database()
    response = db.update_org(form_data)
    print(response)
    return redirect('/')


@app.route('/insert_user/', methods=['POST'])
def insert_user():
    form_data = request.form
    db = Database()
    response = db.insert_user(form_data)
    print(response)
    return redirect('/master_admin/')


if __name__ == '__main__':
    app.run()
