; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1C16AF93-EDCE-45FC-98C2-CFE9A3D5A7A6}
AppName=Hermes
AppVersion=0.3
;AppVerName=Hermes 0.3
AppPublisher=Arbaaz Laskar
DefaultDirName={autopf}\Hermes
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=C:\Users\arbaaz\Documents\Release\Packaging\LICENSE.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\arbaaz\Documents\Release\Setup
OutputBaseFilename=Hermes Setup
SetupIconFile=C:\Users\arbaaz\Documents\Release\Packaging\Hermes\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Hermes.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\pytz\*"; DestDir: "{app}\pytz"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\shiboken2\*"; DestDir: "{app}\shiboken2"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_asyncio.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_bz2.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_ctypes.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_decimal.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_elementtree.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_hashlib.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_lzma.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_multiprocessing.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_overlapped.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_queue.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_socket.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_sqlite3.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\_ssl.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-console-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-datetime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-debug-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-errorhandling-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-file-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-file-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-file-l2-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-handle-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-interlocked-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-libraryloader-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-localization-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-memory-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-namedpipe-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-processenvironment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-processthreads-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-processthreads-l1-1-1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-profile-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-rtlsupport-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-synch-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-synch-l1-2-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-sysinfo-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-timezone-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-core-util-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-conio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-convert-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-environment-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-filesystem-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-heap-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-locale-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-math-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-process-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-runtime-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-stdio-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-string-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-time-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\api-ms-win-crt-utility-l1-1-0.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\base_library.zip"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\d3dcompiler_47.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Hermes.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Hermes.exe.manifest"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libcrypto-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libEGL.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libffi-7.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libGLESv2.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libopenblas.3JEZX7MU2MO3QXAHU7L6VB7M4UJAWPR4.gfortran-win32.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\libssl-1_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\MSVCP140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\MSVCP140_1.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\opengl32sw.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\pyexpat.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\pyside2.abi3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\python3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\python38.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Core.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5DBus.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Gui.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Network.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Pdf.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Qml.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5QmlModels.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Quick.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Svg.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5VirtualKeyboard.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5WebSockets.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Qt5Widgets.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\select.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\shiboken2.abi3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\sqlite3.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\ucrtbase.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\unicodedata.pyd"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\VCRUNTIME140.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\Include\*"; DestDir: "{app}\Include"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\numpy\*"; DestDir: "{app}\numpy"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\pandas\*"; DestDir: "{app}\pandas"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\arbaaz\Documents\Release\Packaging\Hermes\PySide2\*"; DestDir: "{app}\PySide2"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\.myp\OpenWithProgids"; ValueType: string; ValueName: "HermesFile.myp"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\HermesFile.myp"; ValueType: string; ValueName: ""; ValueData: "Hermes File"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\HermesFile.myp\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\Hermes.exe,0"
Root: HKA; Subkey: "Software\Classes\HermesFile.myp\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\Hermes.exe"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\Hermes.exe\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\Hermes"; Filename: "{app}\Hermes.exe"
Name: "{autodesktop}\Hermes"; Filename: "{app}\Hermes.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Hermes.exe"; Description: "{cm:LaunchProgram,Hermes}"; Flags: nowait postinstall skipifsilent
