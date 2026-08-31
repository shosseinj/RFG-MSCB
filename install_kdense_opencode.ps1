param(
    [switch]$All,
    [string]$Repo = "https://github.com/K-Dense-AI/scientific-agent-skills.git"
)

$ErrorActionPreference = "Stop"

$ProjectRoot = (Get-Location).Path
$OpenCodeDir = Join-Path $ProjectRoot ".opencode"
$SkillsDir = Join-Path $OpenCodeDir "skills"
$VendorDir = Join-Path $ProjectRoot ".vendor"
$RepoDir = Join-Path $VendorDir "scientific-agent-skills"

$RecommendedSkills = @(
    "scientific-writing",
    "research-lookup",
    "literature-review",
    "peer-review",
    "scientific-critical-thinking"
)

Write-Host "Project: $ProjectRoot"
Write-Host "OpenCode skills: $SkillsDir"

New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null
New-Item -ItemType Directory -Force -Path $VendorDir | Out-Null

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not available in PATH."
}

if (Test-Path $RepoDir) {
    Write-Host "Updating existing Scientific Agent Skills repository..."
    git -C $RepoDir pull --ff-only
} else {
    Write-Host "Cloning Scientific Agent Skills..."
    git clone --depth 1 $Repo $RepoDir
}

$SourceSkills = Join-Path $RepoDir "skills"
if (-not (Test-Path $SourceSkills)) {
    throw "Could not find the repository's skills directory: $SourceSkills"
}

if ($All) {
    Write-Host "Installing ALL skills into .opencode/skills ..."
    Get-ChildItem -Path $SourceSkills -Directory | ForEach-Object {
        $target = Join-Path $SkillsDir $_.Name
        if (Test-Path $target) { Remove-Item -Recurse -Force $target }
        Copy-Item -Recurse -Force $_.FullName $target
    }
} else {
    Write-Host "Installing recommended paper-writing skills..."
    foreach ($name in $RecommendedSkills) {
        $source = Join-Path $SourceSkills $name
        $target = Join-Path $SkillsDir $name

        if (-not (Test-Path $source)) {
            Write-Warning "Skill not found in current repository version: $name"
            continue
        }

        if (Test-Path $target) { Remove-Item -Recurse -Force $target }
        Copy-Item -Recurse -Force $source $target
        Write-Host "  installed: $name"
    }
}

Write-Host ""
Write-Host "Installed skills:"
Get-ChildItem -Path $SkillsDir -Directory | ForEach-Object {
    $skillMd = Join-Path $_.FullName "SKILL.md"
    if (Test-Path $skillMd) {
        Write-Host "  - $($_.Name)"
    }
}

Write-Host ""
Write-Host "Done."
Write-Host "Restart OpenCode from this project directory."
Write-Host 'Then ask: "List the available skills relevant to scientific paper writing."'
