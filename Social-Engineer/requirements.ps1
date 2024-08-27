# Set PowerShell execution policy for this session
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

# Function to check if command exists
function Test-CommandExists {
    $command = Get-Command $args[0] -ErrorAction SilentlyContinue
    return $command -ne $null
}

# Function to fetch the latest Python installer URL for Windows
function Get-LatestPythonInstallerUrl {
    $page = Invoke-WebRequest -Uri "https://www.python.org/downloads/windows/"
    $links = $page.Links | Where-Object { $_.href -like "*amd64.exe" } | Select-Object -ExpandProperty href
    return $links[0]
}

# List of libraries to install with pip
$libraries_to_install = "jinja2 pandas openpyxl beautifulsoup4 flask"

# Check if Python is installed
if (Test-CommandExists "python") {
    Write-Host "Python is already installed."
} else {
    Write-Host "Python is not installed. Finding and installing the latest version..."
    $installerUrl = Get-LatestPythonInstallerUrl
    if ($installerUrl -eq $null) {
        Write-Host "Failed to find the Python installer."
        return
    }
    $installerPath = "C:\Temp\python-installer.exe"
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath
    # Run the installer
    Start-Process -FilePath $installerPath -Args "/quiet InstallAllUsers=1 PrependPath=1" -Wait
    Remove-Item -Path $installerPath
}

# Check again to make sure installation was successful
if (Test-CommandExists "python") {
    Write-Host "Installing Python libraries: $libraries_to_install"
    # Install libraries using pip
    pip install jinja2 pandas openpyxl beautifulsoup4 flask
} else {
    Write-Host "Failed to install Python. Please install Python manually."
}
