# setup_and_run.py
import os
import sys
import subprocess
import platform
import webbrowser
from time import sleep


def is_windows():
    return platform.system().lower() == "windows"


def create_venv():
    print("Création de l'environnement virtuel...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])


def get_venv_python():
    if is_windows():
        return os.path.join("venv", "Scripts", "python.exe")
    return os.path.join("venv", "bin", "python")


def get_venv_pip():
    if is_windows():
        return os.path.join("venv", "Scripts", "pip.exe")
    return os.path.join("venv", "bin", "pip")


def install_requirements():
    print("Installation des dépendances...")
    subprocess.run([get_venv_pip(), "install", "-r", "requirements.txt"])


def run_migrations():
    print("Application des migrations Django...")
    subprocess.run([get_venv_python(), "manage.py", "migrate"])


def collect_static():
    print("Collection des fichiers statiques...")
    subprocess.run([get_venv_python(), "manage.py", "collectstatic", "--noinput"])


def run_server():
    print("Démarrage du serveur...")
    server_process = subprocess.Popen([get_venv_python(), "manage.py", "runserver"])
    return server_process


def main():
    try:
        # Création et activation de l'environnement virtuel
        create_venv()

        # Installation des dépendances
        install_requirements()

        # Migrations Django
        run_migrations()

        # Collection des fichiers statiques
        collect_static()

        # Démarrage du serveur
        server_process = run_server()

        # Attente pour que le serveur démarre
        print("Attente du démarrage du serveur...")
        sleep(3)

        # Ouverture du navigateur
        webbrowser.open('http://127.0.0.1:8000')

        print("\nL'application est prête !")
        print("Accédez à l'interface via : http://127.0.0.1:8000")
        print("Pour arrêter le serveur, appuyez sur Ctrl+C\n")

        # Maintien du serveur actif
        server_process.wait()

    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
        if 'server_process' in locals():
            server_process.terminate()
        sys.exit(0)
    except Exception as e:
        print(f"Une erreur est survenue : {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()