import random
from sklearn import svm

input_data = [[1, 2], [2, 3], [3, 1]]

output_data = [
    1,
    2,
    3,
]

player_choice_history = []


def get_next_choice_for_computer():

  if len(player_choice_history) > 2:
    input_data.append([player_choice_history[-3], player_choice_history[-2]])
    output_data.append(player_choice_history[-1])
    print("Input data: ", input_data)
    print("Output data: ", output_data)
    model = svm.SVC()
    model.fit(input_data, output_data)
    player_next_choice = model.predict(
        [[player_choice_history[-2], player_choice_history[-1]]])[0]  ##
  else:
    player_next_choice = random.randint(1, 3)
  print("Predicting the human player's next choice: ", player_next_choice)

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

  # checking the winner
  if player_choice == 1 and computer_choice == 2 \
          or player_choice == 2 and computer_choice == 3 \
          or player_choice == 3 and computer_choice == 1:
    print("You lose!")
  elif player_choice == 2 and computer_choice == 1 \
          or player_choice == 3 and computer_choice == 2 \
          or player_choice == 1 and computer_choice == 3:
    print("You win!")
  else:
    print("Tie!")

  player_choice_history.append(player_choice)
