#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def _free_port_if_in_use():
    if 'runserver' not in sys.argv:
        return
    if os.environ.get('DJANGO_AUTORELOAD_ENV') == 'true' or os.environ.get('RUN_MAIN') == 'true':
        return

    port = 8000
    for arg in sys.argv[sys.argv.index('runserver') + 1:]:
        if not arg.startswith('-'):
            port_str = arg.split(':')[-1] if ':' in arg else arg
            if port_str.isdigit():
                port = int(port_str)
            break

    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if s.connect_ex(('127.0.0.1', port)) == 0:
            import shutil
            import subprocess
            import time
            print(f"[LinkSnip] Port {port} is in use by another process. Freeing port {port}...")
            if shutil.which('fuser'):
                subprocess.run(['fuser', '-k', '-9', f'{port}/tcp'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            elif shutil.which('lsof'):
                subprocess.run(f"lsof -ti:{port} | xargs -r kill -9", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            time.sleep(0.5)


def main():
    """Run administrative tasks."""
    _free_port_if_in_use()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
