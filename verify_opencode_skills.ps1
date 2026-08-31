$ErrorActionPreference = "Stop"

$SkillsDir = Join-Path (Get-Location).Path ".opencode\skills"

if (-not (Test-Path $SkillsDir)) {
    throw ".opencode\skills does not exist. Run install_kdense_opencode.ps1 first."
}

$valid = @()
$invalid = @()

Get-ChildItem $SkillsDir -Directory | ForEach-Object {
    $skillMd = Join-Path $_.FullName "SKILL.md"
    if (Test-Path $skillMd) {
        $valid += $_.Name
    } else {
        $invalid += $_.Name
    }
}

Write-Host "Valid skill folders: $($valid.Count)"
$valid | Sort-Object | ForEach-Object { Write-Host "  - $_" }

if ($invalid.Count -gt 0) {
    Write-Host ""
    Write-Warning "Folders without SKILL.md:"
    $invalid | Sort-Object | ForEach-Object { Write-Host "  - $_" }
}

Write-Host ""
Write-Host "OpenCode should discover these project-local skills automatically."
