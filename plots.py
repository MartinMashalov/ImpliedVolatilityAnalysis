from matplotlib import pyplot as plt
import datetime_util

def plotPredictions(intraday_times, prediction):
    #print(datetime_util.convertMinutestoTime(intraday_times))
    plt.plot(datetime_util.convertMinutestoTime(intraday_times), prediction)
    print("finished plot")
    plt.ylabel('VIX Prediction')
    plt.title('Intraday VIX Predictions')
    plt.savefig('vixprediction.pdf')
    plt.savefig('vixprediction.png')
    plt.show()
