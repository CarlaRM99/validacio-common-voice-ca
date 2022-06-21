@ECHO OFF
setlocal EnableDelayedExpansion

set folderpath="F:\DATA (G)\Treball\TFG\Dades\clips"

for %%i in (%folderpath%\*.mp3) do (	
	set "nom=%%~ni"
	set "pre=!nom:~16,4!"
	
	md !folderpath!\!pre!
	move "%%i" !folderpath!\!pre!

	REM echo !nom!
	echo !pre! 
)