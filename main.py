import random
from sklearn import svm

# Data for model prediction
input_data = []
output_data = []

# Player choice history
player_choice_history = []

# Show/hide input/output data
view_data = False

# Predicton model
model = svm.SVC()

# Get computer's choice
def get_next_choice_for_computer():
  if len(input_data) > 2 and len(output_data) > 2:

    ## print data if requested
    if view_data:
      print("Input data: ", input_data)
      print("Output data: ", output_data)

    ## fit data to model
    model.fit(input_data, output_data)

    ## predict based off two most recent player choices
    player_next_choice = model.predict(
        [[player_choice_history[-2], player_choice_history[-1]]])[0]
  else:
    ## choose a random choice if there is not enough data
    player_next_choice = random.randint(1, 3)
  print("Predicting the human player's next choice: ", player_next_choice)

  ## computer's response to predicted player choice
  if player_next_choice == 1:
    return 2
  elif player_next_choice == 2:
    return 3
  else:
    return 1


# Main game loop
while True:
  player_choice = int(
      input("Please make a choice (1: Rock, 2: Paper, 3: Scissors): "))
  computer_choice = get_next_choice_for_computer()
  print("Computer chose:", computer_choice)

  ## checking the winner
  if player_choice == 1 and computer_choice == 2 \
          or player_choice == 2 and computer_choice == 3 \
          or player_choice == 3 and computer_choice == 1:
    print("You lose!\n")
  elif player_choice == 2 and computer_choice == 1 \
          or player_choice == 3 and computer_choice == 2 \
          or player_choice == 1 and computer_choice == 3:
    print("You win!\n")
  else:
    print("Tie!\n")

  ## update player choice history
  player_choice_history.append(player_choice)

  ## update input data and output data from player choice history
  if len(player_choice_history) > 2:
    input_data.append([player_choice_history[-3], player_choice_history[-2]])
    output_data.append(player_choice_history[-1])
