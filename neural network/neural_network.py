import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import initializers
import matplotlib.pyplot as plt

#function for choosing point of rounding up or down numbers
def rounder(x):
  index = 0
  while index < x.shape[0]:
    value =  x[index]
    remainer = value - int(value)
    if remainer > .62:
      remainder = 1
    else:
      remainder = 0
    x[index] = int(value) + remainder
    index+=1
  return x

raw_data = pd.read_csv("../../3rd_year_project/2019-ca326-eharkin-soccer-score-predictor-and-fantasy-league-web-application-using-machine-learning/code/results_and_players/training_results.csv")
data = raw_data.copy()
train_dataset = data.sample(frac=0.90,random_state=0)
test_dataset = data.drop(train_dataset.index)
train_labels_home = train_dataset.pop("home_result_score")
train_labels_away = train_dataset.pop("away_result_score")
test_labels_home = test_dataset.pop("home_result_score")
test_labels_away = test_dataset.pop("away_result_score")

train_stats = train_dataset.describe()
train_stats = train_stats.transpose()


#function for normalizing all the various inputs
def norm(x):
  return (x - train_stats['mean']) / train_stats['std']

normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)


def build_model():
  model = keras.Sequential([
    layers.Dense(4, activation=tf.nn.leaky_relu,input_shape=[len(train_dataset.keys())]),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.Adam(0.001)

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model


class PrintDot(keras.callbacks.Callback):
  #function for visualizing how long training is taking
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

home_model = build_model()
away_model = build_model()
home_model.summary()

EPOCHS = 2000

# The patience argument is the amount of epochs to check for improvement before exiting training
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=100)

history_home = home_model.fit(
  normed_train_data, train_labels_home,
  epochs=EPOCHS, validation_split = 0.2, shuffle=True,verbose=0,
  callbacks=[early_stop,PrintDot()])
history_away = away_model.fit(
  normed_train_data, train_labels_away,
  epochs=EPOCHS, validation_split = 0.2, shuffle=True,verbose=0,
  callbacks=[early_stop,PrintDot()])

home_model.save('home_score_NN.model')
away_model.save('away_score_NN.model')

#history shows the improvement over time
def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  
  #drawing the graph of improvement over time
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [home_result_score]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.legend()
  plt.ylim([0,5])
  

plot_history(history_home)
plt.show()
plot_history(history_away)
plt.show()



loss, mae, mse = home_model.evaluate(normed_test_data, test_labels_home, verbose=0)

print("Testing set Mean Abs Error: {:5.2f} score".format(mae))

home_test_predictions = home_model.predict(normed_test_data).flatten()
away_test_predictions = away_model.predict(normed_test_data).flatten()

#how far off home score was from predicted
error = home_test_predictions - test_labels_home
#how far off rounded for home
error1 = abs(np.around(home_test_predictions) - test_labels_home)
#how many goals total it was off
total_error =(abs(rounder(home_test_predictions) - test_labels_home)) +  (abs(rounder(away_test_predictions) - test_labels_away)) 
#if was correct outcome or not, home prediction multiplied by 2 to ensure a predicted loss and an actual win did not result in return a correctly predicted draw
result_error =(2 * np.sign((rounder(home_test_predictions) - rounder(away_test_predictions)))) + (np.sign(test_labels_home - test_labels_away))
plt.hist(total_error, bins = 25)
plt.hist(result_error, bins = 25)
plt.xlabel("Prediction Error [home_result_score]")
_ = plt.ylabel("Count")
plt.show() 
error2= error1
error1 = error1.describe()
error1 = error1.transpose()

print(error1["mean"])
plt.hist(error2, bins = 25)
plt.xlabel("Prediction Error [home_result_score]")
_ = plt.ylabel("Count")




#generate predictions for upcoming games
game = pd.read_csv("../results_and_players/test_games.csv")
normed_game = norm(game)
home_test_predictions = home_model.predict(normed_game).flatten()
away_test_predictions = away_model.predict(normed_game).flatten()

file_name = "../../3rd_year_project/2019-ca326-eharkin-soccer-score-predictor-and-fantasy-league-web-application-using-machine-learning/code/fixtures/fixtures.csv"
file = open(file_name,"r")
file = file.readlines()
file = file[1:]
i = 0
predicted = ""
while i < len(home_test_predictions):
  predicted += file[i].strip() + "," + str(round(home_test_predictions[i])) + "," +  str(round(away_test_predictions[i])) + "\n"
  i+=1
file_write = open("../../3rd_year_project/2019-ca326-eharkin-soccer-score-predictor-and-fantasy-league-web-application-using-machine-learning/code/fixtures/predictions.txt","w")
