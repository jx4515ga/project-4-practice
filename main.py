import ui
import nutritionix
import api_controller 

# appId=b3203af1
# 1
# &appKey=2b9b96bfe1278528cc9717ce7055a037
def main():
    while True:
        try:
            display_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                search_drink()
            elif choice == 2:
                print('Good bye!')
                break
            else:
                print('\nNot a valid choice.\n')
        except ValueError as e:
            print('\nPlease enter a numeric choice.\n')


def display_menu(): # Menu option for user
    print('1: Search drink')
    print('2: Exit')


def search_drink():
    search_drink = ui.get_search_term()
    drink_name = api_controller.get_drink_info(search_drink)
    return drink_name



if __name__ == "__main__":
    main()