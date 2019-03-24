from firebase_db.FirebaseCrud import performDatabaseOperation

if __name__ == '__main__':
    try:
        job  = performDatabaseOperation('test_data')
        reference = job.validateCredentials()
        data = {
            'name' : 'shreyanshu',
            'type' : 'test_data'
        }
        job.insertData(reference, data)
    except Exception as e:
        print(e, "Exception")
