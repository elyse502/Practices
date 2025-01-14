# Editor Setup Guide

This guide explains how to set up commands to open VS Code and Cursor from the terminal in both Windows and WSL.

## Windows Setup (PowerShell)

1. **Open PowerShell as Administrator** and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

2. **Install Cursor** from the [Cursor website](https://docs.cursor.com/install).

3. **Install VS Code** from the [VS Code website](https://code.visualstudio.com/download).

4. **Create and edit PowerShell profile**:

```powershell
# Check if profile exists
Test-Path $PROFILE

# Create profile if it doesn't exist
New-Item -Path $PROFILE -Type File -Force

# Open profile in Notepad
notepad $PROFILE
```

5. **Add these functions** to your profile:

```powershell
# For VS Code
function vscode { & "C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe" $args }

# For Cursor
function cursor { & "C:\Users\YourUsername\AppData\Local\Programs\cursor\Cursor.exe" $args }
```

6. **Reload your profile**:

```powershell
. $PROFILE
```

## WSL Setup

1. **Edit your shell configuration file**:

```bash
# For bash
nano ~/.bashrc

# For zsh
nano ~/.zshrc
```

2. **Add these aliases**:

```bash
# For VS Code
alias vscode="/mnt/c/Users/YourUsername/AppData/Local/Programs/Microsoft\ VS\ Code/bin/code"

# For Cursor
alias cursor="/mnt/c/Users/YourUsername/AppData/Local/Programs/cursor/resources/app/bin/code"
```

3. **Reload your configuration**:

```bash
# For bash
source ~/.bashrc

# For zsh
source ~/.zshrc
```

## Usage

After setup, you can use these commands in either environment:

```bash
# Open current directory in VS Code
vscode .

# Open current directory in Cursor
cursor .
```

Note: Replace `YourUsername` in the paths with your actual Windows username.
