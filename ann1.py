## Author: Sai Medavarapu


# Artificial Neural Network

# Installing Theano
# pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#Since we have three different types of attributes in country we have to encode those both.
labelencoder_X_1 = LabelEncoder() 
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])





## When we execute the above two lines and run code, it will convert te=hose into integers.

## Now we are doing for the other column Gender
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])



## Label encoder thinks that higher integer value has more priority. Therefore, we have to encode it us
## it using the oneHotEncoder.
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()

##Here we have to delete one column. To overcome the dummy variable trap.
X = X[:, 1:]






# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)







# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras



##Sequential model is uset to inititalize our ANN
from keras.models import Sequential

##Dense Layer is used to add hidden layer to our NN.
from keras.layers import Dense




                                    # Initialising the ANN

## Create an object(classifier(our ANN)) that uses sequential method to build the ANN.
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))





                                    # Compiling the ANN
                                    
                                    
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


                            # Fitting the ANN to the Training set
                            
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

                    # Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)



               #  Part4 - Single prediction


## adding seconf pair of elements will add the elements to next column
new_prediction = classifier.predict(sc.transform(np.array([[0,0,600, 1, 40, 3, 60000, 2, 1, 1, 50000  ]]))) 
new_prediction == (new_prediction>0.5)   

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

