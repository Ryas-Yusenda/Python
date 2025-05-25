::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFAlNXxSWAE+1EbsQ5+n//NaBrUEZUfBxcYzUug==
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSTk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpSI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAjk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFAlNXxSWAE+/Fb4I5/jH/POKoEIRXeFxfZfeug==
::YB416Ek+ZW8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
setlocal enabledelayedexpansion

:loop
cls
echo Masukkan folder path sumber (asli):
set /p sourcePath=Path: 

if "%sourcePath%"=="" (
    echo Tidak ada input. Keluar...
    goto :eof
)

REM Ambil nama folder terakhir dari path
for %%F in ("%sourcePath%") do set folderName=%%~nxF

set linkPath=%cd%\%folderName%

if exist "%linkPath%" (
    echo.
    echo Folder "%linkPath%" sudah ada.
) else (
    echo.
    echo Membuat symbolic link:
    echo Target: %linkPath%
    echo Source: %sourcePath%
    echo.

    mklink /J "%linkPath%" "%sourcePath%"
    if errorlevel 1 (
        echo Gagal membuat link. Jalankan script ini sebagai Administrator.
    ) else (
        echo Link berhasil dibuat!
    )
)

echo.
pause
goto loop
