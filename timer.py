
import termcolor
import time


def start_timer():
    try:
        s = input('Set your timer in SECONDS')
        s = int(s)
        def countdown_second(s):
            secondslist = [seconds for seconds in range(1, s + 1)]
            secondslist.sort(reverse=True)
            if s > 0:
                count = 0
                run = True
                while run is True:
                    try:
                        while s > 0 and run == True:
                            print('---------- ')
                            print('|        | ')
                            print('|   ' + str(termcolor.colored(secondslist[count], 'blue')) + '   | ')
                            print('|        | ')
                            print('---------- ')
                            time.sleep(1)
                            count += 1
                            while secondslist[count] < round((s / 3) + 2):
                                print('--------- ')
                                print('|       | ')
                                print('|   ' + str(termcolor.colored(secondslist[count], 'yellow')) + '   | ')
                                print('|       | ')
                                print('--------- ')
                                time.sleep(1)
                                count += 1
                    except IndexError:
                        print(termcolor.colored("TIME'S UP !", 'red'))
                        break
        countdown_second(s)
    except:
        print('Please enter number(s) only')


ask = input("press 'q' to quit or 's' to start")
play = True
start = True
while start is True:
    if ask == 's':
        play = True
        while play == True:
            start_timer()
    elif ask == 'q':
        break
    else:
        print('Please choose only \'p\' or \'q\' !')
        ask = input("press 'q' to quit during the game or 's' to start")
