import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    Line = "*"*50
    
    #step1
    dataset = pd.read_csv('MarvellousInfosystems_PlayPredictor.csv')
    
    #step2
    labelEncoder = LabelEncoder()
    
    dataset['weather_new'] = labelEncoder.fit_transform(dataset['Wether'])
    dataset['temperature_new'] = labelEncoder.fit_transform(dataset['Temperature'])
    dataset['play_new'] = labelEncoder.fit_transform(dataset['Play'])
   
    data = dataset.loc[:,["weather_new","temperature_new"]]
    target = dataset.loc[:,["play_new"]]
    
    print("Actual Data Set")
    print(Line)
    for i in range(len(data)):
        print("Id : %d Label : [ %s %s ] Feature : %s" %(i, data.weather_new[i], data.temperature_new[i], target.play_new[i]))

    print(Line)
    
    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size = 0.5)   
    
    data_train = data_train.reset_index()
    data_test = data_test.reset_index()
    target_train = target_train.reset_index()
    target_test = target_test.reset_index()
    
    print(Line)
    print("Training Data Set")
    print(Line)
    for i in range(len(data_train)):
        print("Id : %d Label : [ %s %s ] Feature : %s " %(i, data_train.weather_new[i], data_train.temperature_new[i], target_train.play_new[i]))
        
    print(Line)
    
    
    print(Line)
    print("Test Data Set")
    print(Line)
    for i in range(len(data_test)):
        print("Id : %d Label : [ %s %s ] Feature : %s " %(i, data_test.weather_new[i], data_test.temperature_new[i], target_test.play_new[i]))
        
    print(Line)
    
    #step3
    cobj = KNeighborsClassifier(7)
    
    cobj.fit(data_train,target_train)
    
    #step4
    output = cobj.predict(data_test)
    
    output = output[:,-1]
    
    print(Line)
    print("Result of Machine Learning Model")
    print(Line)
    for i in range(len(output)):
        print("Id : %d Expectation : %s Prediction : %s " %(i, target_test.play_new[i], output[i]))
        
    print(Line)

    
    icnt = 0
    wrong = 0
    for i in range(len(data_test)):
        if target_test.play_new[i] != output[i]:
            icnt = icnt + 1
            wrong = icnt
    print("Number of wrong answers by the ML model : ",icnt)
    print(Line)
    
    icnt = 0
    right = 0
    for i in range(len(data_test)):
        if target_test.play_new[i] == output[i]:
            icnt = icnt + 1
            right = icnt
    print("Number of right answers by the ML model : ",icnt)
    print(Line)
    
    #step 5
    Accuracy = (right/(right+wrong)) * 100
    
    print(Line)
    print("Result of Accuracy of Machine Learning Model : ",Accuracy)
    print(Line)

if __name__ == "__main__":
    main()
