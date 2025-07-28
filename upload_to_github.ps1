# PowerShell script to upload all files to your GitHub repository
# Make sure you have git installed and are authenticated with GitHub

$repoUrl = "https://github.com/himanshu19704/Wipro---Python-with-Data-Science.git"
$localDir = "$PSScriptRoot"

Set-Location $localDir

# Initialize git repo if not already
if (-not (Test-Path "$localDir\.git")) {
    git init
}

# Add all files
git add .

# Commit the files
git commit -m "Upload all Wipro TalentNext files" -a

# Set the remote (force set in case it already exists)
git remote remove origin 2>$null

git remote add origin $repoUrl

# Push to GitHub (force overwrite)
git push -f origin main

Write-Host "All files uploaded to GitHub repository."
