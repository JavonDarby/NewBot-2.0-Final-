Param(
    [string]$RemoteUrl = 'https://github.com/JavonDarby/NewBot-2.0-Final-'
)

# Determine repo path (current directory)
$RepoPath = (Get-Location).Path
Write-Host "Repository path: $RepoPath"

# Check git availability
try {
    git --version > $null 2>&1
} catch {
    Write-Error "Git is not installed or not on PATH. Install Git for Windows first: https://git-scm.com/download/win"
    exit 1
}

# Ensure we're inside the intended folder
if (-not (Test-Path "$RepoPath\.git")) {
    Write-Host "No .git folder found, initializing a new repository..."
    git init
} else {
    Write-Host ".git folder found. Using existing repository." 
}

# Ensure branch exists and set to main if necessary
$branch = ''
try {
    $branch = git rev-parse --abbrev-ref HEAD 2>$null
} catch {
    $branch = ''
}
if ([string]::IsNullOrWhiteSpace($branch) -or $branch -eq 'HEAD') {
    Write-Host "Creating and switching to branch 'main'..."
    git checkout -b main
    $branch = 'main'
}
Write-Host "Current branch: $branch"

# Stage all changes
Write-Host "Staging files..."
git add -A

# Commit if there are staged changes
$status = git status --porcelain
if (-not [string]::IsNullOrWhiteSpace($status)) {
    $msg = "Initial project scaffold: add code, notebooks, tests, and docs"
    Write-Host "Committing: $msg"
    git commit -m $msg
} else {
    Write-Host "No changes to commit."
}

# Add remote if not present or update if different
$remoteExists = $false
try {
    $existing = git remote get-url origin 2>$null
    if (-not [string]::IsNullOrWhiteSpace($existing)) { $remoteExists = $true }
} catch {
    $remoteExists = $false
}

if ($remoteExists) {
    Write-Host "Remote 'origin' exists: $existing"
    if ($existing -ne $RemoteUrl) {
        Write-Host "Updating remote 'origin' to $RemoteUrl"
        git remote set-url origin $RemoteUrl
    }
} else {
    Write-Host "Adding remote origin -> $RemoteUrl"
    git remote add origin $RemoteUrl
}

# Push to origin
Write-Host "Pushing branch '$branch' to origin (this will prompt for credentials if needed)..."
try {
    git push -u origin $branch
    Write-Host "Push completed."
} catch {
    Write-Error "Push failed. If the remote repo doesn't exist, create it on GitHub or use 'gh repo create'.\nIf authentication fails, use a PAT (personal access token) when prompted for password, or configure SSH keys."
    exit 1
}

Write-Host "Done. If you want CI to run, make sure GitHub Actions is enabled on the target repository and that workflow files exist in .github/workflows/."