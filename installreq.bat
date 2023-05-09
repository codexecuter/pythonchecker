@echo off
REM Excode

REM Pip yoksa:
where pip > nul || (echo "pip yüklü değil. Lütfen önce pip kurun." & pause & exit /b 1)

REM paketleri indir
for /f "delims=" %%i in (requirements.txt) do (
    REM Excode
    pip install %%i
)

echo "Kurulum Tamamlandi.."
pause
