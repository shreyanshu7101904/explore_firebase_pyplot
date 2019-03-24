import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class performDatabaseOperation:

    def __init__(self, name):
        self.databse_name = name

    def validateCredentials(self):
        cred = credentials.Certificate("/root/Documents/explore_firebase_pyplot/firebase_db/secret.json")
        firebase_admin.initialize_app(
            cred, {
                "databaseURL": "https://testing-firebase-databas-ccbca.firebaseio.com"
                })
        ref = db.reference('/')
        return ref


    def insertData(self, reference, data):
        reference.child(self.databse_name).push().set(data)
        print("data sucessfully inserted")


    def readData(self, reference):
        data = reference.child(self.databse_name).get()
        print(data)
    

    def readDataByValue(self, ref, key, value ):
        data  = ref.child(self.databse_name).order_by_child('name').equal_to('shreyanshu').get()
        print(data.keys())
        for i in data.keys():
            print(data[i])
            for j in data[i].keys():
                print(j, data[i][j])
        


