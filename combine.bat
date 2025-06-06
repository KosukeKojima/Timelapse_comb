@echo off

set FILES=
set N=0

:REPEAT
set /a N=N+1
set FILES=%FILES% -i %1

if "%~2"=="" GOTO EXIT
shift
GOTO REPEAT
:EXIT

echo %FILES%

pause

ffmpeg %FILES% -filter_complex "concat=n=%N%:v=1:a=0" %1.merged.mp4

pause