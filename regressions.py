import numpy as np
import pandas as pd
import sklearn
from sklearn import linear_model
import pickle

SAVE = "models/{0}_model.sav"


# Create the linear regression model and stores it in SAVE
def create_model(csv, label):
    data = pd.read_csv(csv, sep=",")
    data = data[["HP", "AC", "CR"]]
    x = np.array(data.drop([label], 1))
    y = np.array(data[label])
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    regression = linear_model.LinearRegression()
    regression.fit(x_train, y_train)
    accuracy = regression.score(x_test, y_test)
    print(accuracy)
    pickle.dump(regression, open(SAVE.format(label), 'wb'))
    return accuracy


def neural_model(csv, label):
    pass


# Predicts a monster's challenge rating off of the model
# Feed the method the hp, the armor class, and the average damage per turn over 10 turns
def predict(target=None, hp=0, ac=0, cr=0,):
    try:
        regression = pickle.load(open(SAVE.format(target), 'rb'))
        result = regression.intercept_
        coefficients = regression.coef_
        if target.lower() == "hp":
            result += coefficients[0] * ac
            result += coefficients[1] * cr
        elif target.lower() == "ac":
            result += coefficients[0] * hp
            result += coefficients[1] * cr
        elif target.lower() == "cr":
            result += coefficients[0] * hp
            result += coefficients[1] * ac
        return result
    except FileNotFoundError:
        raise Exception(FileNotFoundError, "Enter target as : cr, hp, or ac")


def predict_neural():
    pass