param(
    [string]$EnvName = ".venv-windows",
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"

$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$venvPath = Join-Path $projectRoot $EnvName
$activatePath = Join-Path $venvPath "Scripts\Activate.ps1"

if (-not (Test-Path $activatePath)) {
    Write-Host "Windows virtual environment not found at $venvPath. Running setup..."
    & (Join-Path $PSScriptRoot "setup.ps1") -Python $Python -EnvName $EnvName
}

$pythonExe = Join-Path $venvPath "Scripts\python.exe"
$appPath = Join-Path $projectRoot "app.py"

Write-Host "Starting Streamlit app with environment at $venvPath..."
& $pythonExe -m streamlit run $appPath
