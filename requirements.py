import subprocess
import time

REQUIREMENTS = {}

def add(name, version):
    REQUIREMENTS[name] = version

def check_reqs():
    print(time.ctime())
    print('[*] Checking requirements, please wait...')
    try:
        pip_out = subprocess.check_output('pip list').decode()
        for req in REQUIREMENTS.keys():
            VERSION = '=='+str(REQUIREMENTS[req]) if REQUIREMENTS[req] else ''
            if f"{req}{(' '*15)+REQUIREMENTS[req] if VERSION else ''}" in pip_out:
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
        print(f'Error: pip not working!')
        print('[!] quitting program...')
        exit(1)
    except Exception as e:
        print(f'Error: {e}')
        print('[!] quitting program...')
        exit(1)