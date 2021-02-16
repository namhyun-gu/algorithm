function New-Solution {
    [CmdletBinding()]
    param (
        $SolutionName
    )

    if ($null -ne $SolutionName) {
        $SolutionName = $SolutionName -replace " ", "_"

        $null = New-Item -ItemType File -Name "$SolutionName.py"
        Write-Output "Created $SolutionName.py"
        code "$SolutionName.py"
    }
    else {
        Write-Output "Require solution path and solution name"
    }
}

function Add-Solution {
    git add .
    git commit -m "[hackerrank] Add today solution"
}

Set-Alias -Name newsol -Value New-Solution
Set-Alias -Name addsol -Value Add-Solution