from flask import Flask, render_template
import pymysql
app = Flask(__name__)


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "user"
        password = "password"
        db = "student_orgs"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def list_all_orgs(self):
        self.cur.execute("SELECT org_id, org_name FROM orgs LIMIT 50")
        result = self.cur.fetchall()
        return result


@app.route('/')
def all_orgs():
    db = Database()
    res = db.list_all_orgs()
    print(res)
    return render_template('all_orgs.html', result=res, content_type='application/json')


if __name__ == '__main__':
    app.run()
