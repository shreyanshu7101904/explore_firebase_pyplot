from firebase_db.FirebaseCrud import performDatabaseOperation

if __name__ == '__main__':
    try:
        job  = performDatabaseOperation('test_data')
        reference = job.validateCredentials()
        print(reference)
        data = {
            'name' : 'shreyanshu"shankar',
            'type' : '123',
            'age'  : 30
        }
        #job.insertData(reference, data)
        job.readData(reference)
        job.readDataByValue(reference, "name", "shreyanshu")
        
    except Exception as e:
        print(e, "Exception")

