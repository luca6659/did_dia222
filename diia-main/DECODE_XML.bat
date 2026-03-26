@echo off
REM Android APK XML Decoder Batch Script
REM This script decodes binary XML files from Android APK resources

echo.
echo ========================================
echo Android APK XML Decoder
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found. Installing androguard...
python -m pip install -q androguard

if %errorlevel% neq 0 (
    echo ERROR: Failed to install androguard
    echo.
    echo Try installing manually:
    echo   python -m pip install androguard
    echo.
    pause
    exit /b 1
)

echo.
echo Starting decoder...
echo.

REM Run the decoder script
python "%~dp0decode_apk_xml.py"

if %errorlevel% equ 0 (
    echo.
    echo ✓ Decoding completed successfully!
    echo Decoded files are in: %USERPROFILE%\Desktop\diia\resources\decoded_drawables
) else (
    echo.
    echo ✗ Decoding failed with errors (see above)
)

echo.
pause
