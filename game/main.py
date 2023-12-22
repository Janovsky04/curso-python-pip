import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if not user_option in options:
    print("Ingresa una opción válida")
    #continue
    return None, None

  computer_option = random.choice(options)

  print('Opción del user => ', user_option)
  print('Opción de la compu => ', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empateeeee')

  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('Gana el user')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('Gana la compuu')
      computer_wins += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('Gana el user')
      user_wins += 1
    else:
      print('Tijera gana a papel')
      print('Gana la compuu')
      computer_wins += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('Gana el user')
      user_wins += 1
    else:
      print('Piedra gana a tijera')
      print('Gana la compuu')
      computer_wins += 1
  return user_wins, computer_wins

def who_wins(computer_wins, user_wins):
  if computer_wins == 2:
    print('El ganador es la computadora')
    exit()

  if user_wins == 2:
    print('El ganador es el user!')
    exit()
  


def run_game():
  computer_wins=0
  user_wins=0  
  rounds = 1

  while True: 
    print('*'*10)
    print('ROUND', rounds)
    print('*'*10)
  
    print('computer_wins',computer_wins)
    print('user_wins',user_wins)
  
    rounds += 1
  
    user_option, computer_option = choose_options()
    user_wins, computer_wins=check_rules(user_option, computer_option, user_wins, computer_wins)

    who_wins(computer_wins, user_wins )
    

run_game()