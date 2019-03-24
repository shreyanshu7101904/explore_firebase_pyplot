import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("key_secrets.json")
documents = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://testing-firebase-databas-ccbca.firebaseio.com"
})
print(documents.name)
ref = db.reference('/employee')
print(ref.get())
users_ref = ref.child('users')
users_ref.set({
    'alanisawesome': {
        'date_of_birth': 'June 23, 1912',
        'full_name': 'Alan Turing'
    },
    'gracehop': {
        'date_of_birth': 'December 9, 1906',
        'full_name': 'Grace Hopper'
    }
})
