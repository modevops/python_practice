from configparser import Configparser
p  = Configparser()
p.read('read_simple.ini')
print(p.get('bug_tracker', 'url'))