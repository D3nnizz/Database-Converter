$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectRoot

$versionInfoPath = Join-Path $projectRoot "version_info.txt"
if (-not (Test-Path $versionInfoPath)) {
    throw "Version info file not found: $versionInfoPath"
}

$versionMatch = Select-String -Path $versionInfoPath -Pattern "StringStruct\('ProductVersion',\s*'([^']+)'\)"
if (-not $versionMatch) {
    throw "Could not read ProductVersion from version_info.txt"
}

$version = $versionMatch.Matches[0].Groups[1].Value
if (-not $version) {
    throw "ProductVersion value is empty in version_info.txt"
}

$zipVersion = $version -replace "[^0-9A-Za-z._-]", "_"

& (Join-Path $projectRoot "build_exe.ps1")

$distDir = Join-Path $projectRoot "dist"
$exePath = Join-Path $distDir "DatabaseConverter.exe"
if (-not (Test-Path $exePath)) {
    throw "Expected executable not found: $exePath"
}

$zipName = "DatabaseConverter-v$zipVersion-win64.zip"
$zipPath = Join-Path $distDir $zipName

if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Compress-Archive -Path $exePath -DestinationPath $zipPath -CompressionLevel Optimal

Write-Host "Release package created: $zipPath"
