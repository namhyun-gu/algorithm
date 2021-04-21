function New-Solution {
    [CmdletBinding()]
    param (
        $Path,
        $SolutionName
    )

    if ($null -ne $Path -and $null -ne $SolutionName) {
        $SolutionName = $SolutionName -replace " ", "_"

        $null = New-Item -ItemType Directory -Path "$Path" -Name "$SolutionName"
        echo "Created $Path\$SolutionName"
        $null = New-Item -ItemType File -Path "$Path\$SolutionName" -Name "Solution.py"
        echo "Created $Path\$SolutionName\Solution.py"
    }
    else {
        echo "Require solution path and solution name"
    }
}

function Add-Solution {
    git commit -m "[leetcode] Add today solution"
}

Set-Alias -Name newsol -Value New-Solution
Set-Alias -Name addsol -Value Add-Solution
