 $src ="C:\Users\safraz\Documents\Automation\"
 cd "$src"
 rm "$src\cis-cat" -Recurse -Force
 mkdir "cis-cat"
 Write-Host "Unzipping cis-cat zip"
 Expand-Archive "$src\cis-cat.zip" "$src\cis-cat"
 cd "$src\cis-cat\Assessor-CLI"
 
 cmd /c "$src\script.bat"
 
 
 $uri = "https://infra.omegatooling.com/confluence/rest/api/content/80381305/child/attachment"
$txtpath="$src\cis-cat\Assessor-CLI\reports\.*"
Invoke-RestMethod -Uri $uri -Method  post  -InFile $txtpath
  
 