import subprocess
import sys

def install_packages():
    packages = [
        "django",
        "docx2pdf",
        "docxtpl",
        "gTTS",
        "matplotlib",
        "numpy",
        "Pillow",
        "pygame",
        "python-docx",
        "jupyter",
        "jinja2"
    ]

    print("Iniciando la instalación de las librerías necesarias...")

    for package in packages:
        try:
            print(f"Instalando {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✔ {package} instalado correctamente.")
        except subprocess.CalledProcessError:
            print(f"✘ Error al instalar {package}.")
        except Exception as e:
            print(f"✘ Ocurrió un error inesperado con {package}: {e}")

    print("\nProceso de instalación finalizado.")

if __name__ == "__main__":
    install_packages()
