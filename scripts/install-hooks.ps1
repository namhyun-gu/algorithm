Write-Output "Copy scripts\hooks to .git\hooks"
Copy-Item -Path ".\scripts\hooks\*" -Destination ".\.git\hooks"