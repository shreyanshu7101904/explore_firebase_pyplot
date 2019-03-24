from firebase_db.FirebaseCrud import performDatabaseOperation
from Plot.PlotData import Plotter

if __name__ == '__main__':
    try:
        job  = performDatabaseOperation('test_data')
        reference = job.validateCredentials()
        data = {
            'name' : 'shreyanshu"shankar',
            'type' : '123',
            'age'  : 30
        }
        #job.insertData(reference, data)
        x , y = job.readData(reference)
        #job.readDataByValue(reference, "name", "shreyanshu")
        print(x,y)
        plot_figure = Plotter("Users Age")
        plot_figure.createBarPlot(x, y)
        
    except Exception as e:
        print(e, "Exception")

