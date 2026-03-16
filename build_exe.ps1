$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) {
    throw "Python executable not found: $pythonExe"
}

$iconPath = Join-Path $projectRoot "assets\DatabaseConverter.ico"
if (-not (Test-Path $iconPath)) {
    throw "Icon file not found: $iconPath"
}

$versionInfoPath = Join-Path $projectRoot "version_info.txt"
if (-not (Test-Path $versionInfoPath)) {
    throw "Version info file not found: $versionInfoPath"
}

& $pythonExe -m PyInstaller --noconfirm --clean --onefile --windowed --name DatabaseConverter --icon $iconPath --version-file $versionInfoPath main.py

Write-Host "Build finished. Executable: dist\DatabaseConverter.exe"
