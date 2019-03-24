import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class performDatabaseOperation:

    def __init__(self, name):
        self.databse_name = name

    def validateCredentials(self):
        cred = credentials.Certificate("./key_secret.json")
        firebase_admin.initialize_app(
            cred, {
                "databaseURL": "https://testing-firebase-databas-ccbca.firebaseio.com"
                })
        ref = db.reference('/')
        return ref

    def insertData(self, reference, data):
        ref.child(self.databse_name).set(data)
        print("data sucessfully inserted")

