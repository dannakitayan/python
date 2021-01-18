"""
           .          -       -'-·:.·               ...---::--.+++,---,+-- ''     --.   _:`   :'              .:'   :'
         `-           ;,     ___--            `__-/.--------.:        '/...:',_,   .:--`--   `.              :.    '.
         ;             _ ,_,`             `.:/:::.''''       --      '-::--.       -/::-`    :              __     :
         '.            '/:'            _-+-:.''         ·     _:- `·-·'      '---'  /-::::   /              /      /
         `.             '_,'        `.::-`             ·-       ' ''            ''-.:. `-::` /             :'      /
         _                ·-;.'   ,::.'               __        ·              '        '-:-:·           _-       :`
         |-                  ·,-+-,                  '-        '-              :.         '_/.          _-        _-
         '/       ,           ·_·                    :         ·                /           ':-       '-.          /
          :      ;  ,        __                     -'         :                --            ./.   `,.`           /
          .-      '' '     ·.·                     '-''''     ':                 .             ./-.-.·             /
           `:`      ,,-'. ·-              __   ''../...'''____-.                 ''              +·                /
            ':-       '·''·               /   __' .:         '/                  ·_              :'/              -.
             /.;;'       -               '-       :           /                ''_/''            -.':            '/
            ;;-·'·--''  ,               :        __          .:               _''':''''___`       : :' '' _''   '/
           '√'      ·--+♪              ':       `:           /.                   :       _-_     :  / -.-...  -:
          ';            ♪              :'       ::          .:               -    ::              :' :' :.`  ,:.
          :            ';              /       .-:          .:    -          -    :/              __  / ` _-:.
         --            :`             ':      ':.`         -.:    /          `    ::`         /   `:  :---`..
        ';             ';             /`      -./          : :    :          ''   /.:        -`    /  `:    -
       '♪            ,;'              /       : /         .: :   `:          ''   /':        '     /   :    ''
''   .--          _.'-                /      :-'/         /'':   -;               / :              :   -'   '-
 ♪·--'           '_;  _              .-      /`-:     '   :'':   //          _`   :'-        -`    :    _   -.
 ,·'           '..'. '.              .'     -.':.    .:  --'-:   /\          :-   / _'       ''    :    :   :    
   ._..'            ·,·              ;      /'':',,,,:/''/.'/-   /\`         ::   /  _       _     /    _  .-
     '''·-···-·----- ♪               ;     ··`.:.'''-:-.-:-:--   /\`         /-   / '_      -:     /    _  /
         :  '''''   :/-             '-::___:.-::/-/-::-.:-.:.-   //`       '.:/___:'':      ::    _-    _` /
        :'          //-.            .':/-__/-'../..':/'':''::-  `::`       '.:/''_:-':      :/    :`    __ .:`
       .:          ::/-:            - -::-.-/'''---+-+::/--+--' '-.'      :-//:-'-:-,:     :`:    /     __  '---
       /'         ':::-/            --//....   -:      /  .' '.--· _--++·`/./`:-'-/--/..''':':    /     .:'''.-/
      :.          :::-./            .` :'-...  -:  '_.'/  .          ''.'.h:-.u/::-''/''+++::·   `:     .:....·
     '-          -/.'.'/            -  __  '/''''  :_.': ''              ';----';''''-.:-.-::·   :'     _·
    '·   ;      ·/:'/.·/            '  .'   -://::-' ':'''               :'__' _:   '  ': :.`:··:/:  :  :`
   ';   .      '/:- -  /           ''   ___.-  ''-.'-:'''                :-.:. -:  -::''/ - .:--:'   /  /
  _<    .      :-·'   :·           ·      ·_,,,,,:-:-''                  :` .:''''./ ./:..` /-''/    /  /
 .,    ·      `" .-   ·/           ·                                     ':'--:::/:  '+-.`  .-.'':   :::-
'·/    /      /·  .'  '_           ·   .·. .                              '-4 ''''/.:_,,'   : ''--  `;/ `
:^:^   ;/;.   "'   |'  ':          -   ·____;                                ...--:--'     _· · -   -/
·:·;.  .2'-- '^    ·__··/     ·    :     .,,..                                '            _ '' :   ::
  __·   ;♪ --.'     ''..:                                                       ,,,       :` ''':   ♪
   ·__· ·,_'//      '' '--    -    -                                          _-   -      /  '' /  ·
      _,_';/':,  '  ''' _/                                                     ... .-     :.''  /  ..
         _:;;:/' '  '   ':.   :    ''                                                     :''  '/  :
            .:.:''--_____'/         :                                                    ./ '  -'  :
                '____...../.  .     ..:.                                                -: ''''-  ♪
                  __.      /        :  `--.                                          `-._  '''__  :
                    '..."  _.   ·   .'    '...'                                  `--;-'  _  _♪   `:
                         .../   :   ./.        ___'_       ~.               `-.--.''     `/'-/   ♪
                        ·...:'  :.   /'''''''.',,,/:;..:'''''''''''_'..-/`---'''''       -:''"   :
                            ':  :.   :-----"                              --::---------:-/`'':  _
                             /  :.'  -''''                                    ''''''''   /`'.:  :
                             ·- :-"  `-                                                 `- '   .-
                              :':.:.  "                                                 :''    :
                              '.:  -.'"                                                 /''.- .-
                                    ···                                                 --.♪  /
                                                                                          .:  ♪
                                                                                           :__
                                                                                            ·u·
"""
import datetime as d
import math as m

#Write the function "arithmetic" that takes 3 arguments: the first 2 are numbers, the third is the operation to be performed on them.
#If the third argument is +, add; if -, subtract; * - multiply; / - split (first by second).
#In other cases, return the string "Unknown operation"
#arithmetic(2, 3, '+')
def arithmetic(numeric1, numeric2, operator):
    if (operator == '+'):
        return numeric1 + numeric2
    elif (operator == '-'):
        return numeric1 - numeric2
    elif (operator == '*'):
        return numeric1 * numeric2
    elif (operator == '-'):
        return numeric1 - numeric2
    else:
        return "Unknown operation"

#Write the function "is_year_leap" that takes 1 argument - a year, and returns 'True' if the year is a leap year, and 'False' otherwise.
def is_year_leap(year_):
    try:
        if (d.date(year_, 2, 29)):
            return True
        elif (d.date(year_, 2, 28)):
            return False
    except ValueError:
        return False

#Write the function "season" that takes 1 argument - a number of the month (from 1 to 12), and returns the season 
#to which this month belongs (winter, spring, summer, or autumn).
def season(month):
    if (month < 3 or month == 12):
        return "Winter"
    elif (month > 2 and month < 6):
        return "Spring"
    elif (month > 5 and month < 9):
        return "Summer"
    else:
        return "Autumn"

#Write a function "is_prime" that takes 1 argument, a number from 0 to 1000, if it is prime, returns True or False otherwise.
def is_prime(numeric):
    if (numeric%2 == 0 and numeric != 2):
        return False
    elif (numeric%3 == 0 and numeric != 3):
        return False
    elif (numeric%5 == 0 and numeric != 5):
        return False
    elif (numeric%7 == 0 and numeric != 7):
        return False
    else:
        return True

#Write the function "date_" that takes 3 arguments - a day, a month, a year. If it is today return True, else False.
def date_(day_, month_, year_):
    try:
        if (d.date.today() == d.date(year_, month_, day_)):
            return True
        else:
            return False
    except ValueError:
        return False

#Write the function "bank" that takes 2 arguments - 'deposit' and 'years'. Return the sum of bank account (every year bank account rise 10%).
def bank(deposit, years):
    for i in range(years):
        deposit += (deposit/100)*10
    return f"Your bank account total: {deposit}$"

#Write the function "square" that takes 1 argument - 'length' of the square side. Return (a tuple) the perimeter of the square, 
#the area of the square, and the diagonal of the square.
def square(length):
    S = length**2
    P = 4*length
    d = length * m.sqrt(2)
    return (S, P, d)
