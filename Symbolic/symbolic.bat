::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCuDJH2F4EMMCxRQRQqFAFujEr0T5tTL9v6PrUMhZ/syeoDX07eyKeMc5AvtdplN
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
::YxY4rhs+aU+IeA==
::cxY6rQJ7JhzQF1fEqQJhZksaHErSXA==
::ZQ05rAF9IBncCkqN+0xwdVsFAlTMbCXqZg==
::ZQ05rAF9IAHYFVzEqQIDMRZWQwiLPyuWD7sXqMvp6uuTrV99
::eg0/rx1wNQPfEVWB+kM9LVsJDBebMWm1Crwfpur6+4o=
::fBEirQZwNQPfEVWB+kM9LVsJDDebMWezCL4o5+f3jw==
::cRolqwZ3JBvQF1fEqQITJxZZTQqGcWezCLBc/Of046qTrQ0eRuc+bIqbya2DIu8f40akeZ8j3WkajMRMChRUehe5fU8humdMsSSIPMuVvQSB
::dhA7uBVwLU+EWFyW500+KRcUfBaNNm65EtU=
::YQ03rBFzNR3SWATE2k0+LXs=
::dhAmsQZ3MwfNWATEVotieEkBDDabPXja
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRm24UxwKQgUbQCPNWWzFaEO6fz0/aqBrV9dRPAwaIrJmrKbLuMH40rqdJokwmM6
::Zh4grVQjdCuDJH2F4EMMCxRQRQqFAFujEr0T5tTL9v6PrUMhZ/syeoDX07eyM/ke6ErofJVj02Jf+A==
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

:: Bersihkan tanda kutip jika user memasukkan dengan kutip
set sourcePath=%sourcePath:"=%

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
