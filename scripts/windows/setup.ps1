param(
    [string]$Python = "python",
    [string]$EnvName = ".venv-windows"
)

$ErrorActionPreference = "Stop"

$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$venvPath = Join-Path $projectRoot $EnvName

if (-not (Test-Path $venvPath)) {
    Write-Host "Creating Windows virtual environment at $venvPath..."
    & $Python -m venv $venvPath
} else {
    Write-Host "Using existing Windows virtual environment at $venvPath"
}

$pythonExe = Join-Path $venvPath "Scripts\python.exe"

Write-Host "Upgrading pip..."
& $pythonExe -m pip install --upgrade pip

Write-Host "Installing dependencies from requirements.txt..."
& $pythonExe -m pip install -r (Join-Path $projectRoot "requirements.txt")

Write-Host ""
Write-Host "Done. Activate with:"
Write-Host "    `& $venvPath\Scripts\Activate.ps1"
Write-Host "Then run:"
Write-Host "    streamlit run app.py"
