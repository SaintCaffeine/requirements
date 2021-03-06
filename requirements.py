import subprocess
import time

REQUIREMENTS = {}

def add(name, version):
    REQUIREMENTS[name] = version
   
def quit(message):
    print(message)
    print('[!] Requirements are:')
    for req in REQUIREMENTS:
        print(f"{req}{'=='+str(REQUIREMENTS[req]) if REQUIREMENTS[req] else ''}")
    print('You can try installing them manually.')
    print('[!] quitting program...')
    exit(1)
    
def check_reqs():
    print(time.ctime())
    print('[*] Checking requirements, please wait...')
    try:
        pip_out = subprocess.check_output('pip list').decode().replace(' ', '')
        for req in REQUIREMENTS.keys():
            VERSION = '=='+str(REQUIREMENTS[req]) if REQUIREMENTS[req] else ''
            if f"{req}{REQUIREMENTS[req] if VERSION else ''}" in pip_out:
                print('[*] All requirements are satisfied!\n') if req == list(REQUIREMENTS.keys())[-1] else ''
                continue
            else: 
                x = input(f"[!] Requirement not found: {req}{VERSION}, do you want to install {req}{VERSION} (important for the program)? [Y/N] ")
                if x.lower() == 'y' or x.lower() == 'yes':
                    subprocess.os.system(f"pip install {req}{VERSION}")
                else:
                    print('[!] quitting program...')
                    exit(1)
    except (FileNotFoundError):
        quit('ERROR: pip not working!')
    except Exception as e:
        quit(f'ERROR: {e}')
