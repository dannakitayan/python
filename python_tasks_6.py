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
#Write a comma-separated number input program and convert that string to a list of integers. 
#Use the map function here to convert the elements of a sequence to a sequence of numbers.
#Implement the use of exceptions for this conversion.
def first():
    try:
        list_ = list(map(int, input("Please enter numbers: ").split(',')))
        print(list_)
    except ValueError:
        return "Non-numeric value received"
    else:
        return list_

#Write a function for calculating the arithmetic mean of the elements of the list passed to it. 
#Implement handling of possible exceptions during its operation.
def second(*args):
    try:
        result = sum(args)/len(args)
    except ValueError:
        return "Non-numeric value received"
    else:
        return result

#Write a generator function (using the yield) to remove the first element from the set (using the pop()). 
#The function must return the value of the removed element.
#Implement handling of possible exceptions during its operation.
def third(length):
    try: 
        def generator():
            for i in range(length):
                yield i
    except ValueError:
        return "Non-numeric value received"
    else:
        return set(generator()).pop()   