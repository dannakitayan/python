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
#XOR algorithm
class XOR:
    message = ''
    key = 1
    crypt_message = ''

    def __init__(self, message_, key_):
        self.key = key_
        self.message = message_
        pass

#Encrypt the messages using the key
    def encrypt(self):
        current_messages = bytearray(self.message.encode('utf-8', errors = 'backslashreplace'))
        for i in range(len(self.message)):
            self.crypt_message += chr(current_messages[i]^self.key)
        return self.crypt_message

#Now, decrypt the messages using the key
def decrypt(string, key):
    new_string = bytearray(string.encode('utf-8', errors = 'backslashreplace'))
    decrypted_message = ''
    for i in range(len(string)):
        decrypted_message += chr(new_string[i]^key)
    return print(decrypted_message)
    
#Result    
a = XOR('Today is great day', 23)
decrypt(a.encrypt(), 23)