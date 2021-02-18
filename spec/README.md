# Build the Hermes executables from scratch

In the /spec directory, you will find `.spec` files which will be needed by  <a href="https://github.com/pyinstaller/pyinstaller">PyInstaller</a> to build the executables and `.iss` file which will be needed  by <a href="https://jrsoftware.org/isinfo.php">Inno Setup</a> to create the installer for Windows after you have built the `.exe`.

## Requirements
`Python 3.8.7` is needed to build this application and you would need to install the required Python packages from  `requirements.txt`

`PyInstaller` is not a cross-compiler so to build the Windows executable i.e. `.exe`, you would need to run `PyInstaller` in Windows; to make a GNU/Linux executable, which will be a shared library in this case i.e. `.so`, you would need to run it in GNU/Linux, etc.

`Inno Setup` is a Windows software so you will need a Windows system to create the installer if you need it.

## Build Process
Begin by running the following commands-
```
git clone https://github.com/arbaazlaskar/Hermes.git
cd Hermes
```

Install `Python 3.8.7` and the required packages using-
```
pip install -r requirements.txt
```

Then build the executables using the following command-
```
pyinstaller Hermes_linux_dir.spec
```
Note:- Use the required `.spec` file to build the executable. `_dir` version of the `.spec` file will build the application into a single directory and `_one` version of the `.spec` file will build the application into a single executable.

The executables can be found in the `Hermes/dist/` directory.

In case of Linux, you will find a shared library file called `Hermes` which will be used to launch the application.
In case of Windows, you will find a file called `Hermes.exe` which will be used to launch the application.

## Creating the Windows Installer

Install the Inno Setup software from this website- 
https://jrsoftware.org/isdl.php

Edit the `Hermes Setup Script.iss` file and change the `OutputDir` and `File Sources` accordingly.
Launch the Inno Setup application and open the `Hermes Setup Script.iss`. Then run the compiler. You will find the installer in the `OutputDir` location as assigned in the `Hermes Setup Script.iss` file.

