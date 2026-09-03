# ================================================================
# Script: Hoan tat Symlink Antigravity 2.0 -> Antigravity IDE
# ================================================================
# Chay script nay SAU KHI dong hoan toan Antigravity IDE.
# Mo PowerShell va chay:
#   powershell -ExecutionPolicy Bypass -File "D:\folder\rac\finish_symlink.ps1"
# ================================================================

Write-Host "============================================"
Write-Host " Antigravity Sync Fix Script"
Write-Host "============================================"
Write-Host ""

# Step 1: Check no Antigravity processes are running
$procs = Get-Process | Where-Object { $_.ProcessName -like "*Antigravity*" }
if ($procs) {
    Write-Host "[!] Antigravity is still running! Close ALL Antigravity windows first."
    Write-Host "   Running processes:"
    $procs | ForEach-Object { Write-Host "   - $($_.ProcessName) (PID: $($_.Id))" }
    Write-Host ""
    $confirm = Read-Host "Force kill all? (y/n)"
    if ($confirm -eq 'y') {
        $procs | Stop-Process -Force
        Start-Sleep -Seconds 2
        Write-Host "[OK] All processes killed"
    } else {
        Write-Host "Exiting. Close the apps manually and try again."
        exit 1
    }
}

# Step 2: Remove remaining antigravity folder
$antigravityDir = "C:\Users\Acer\.gemini\antigravity"

if (Test-Path $antigravityDir) {
    Write-Host ""
    Write-Host "Step 1: Removing remaining antigravity folder..."
    try {
        Remove-Item $antigravityDir -Recurse -Force -ErrorAction Stop
        Write-Host "[OK] Removed antigravity folder"
    } catch {
        Write-Host "[FAIL] $($_.Exception.Message)"
        Write-Host "   Try running this script as Administrator."
        exit 1
    }
} else {
    Write-Host "[OK] antigravity folder already removed"
}

# Step 3: Create junction point (doesn't require admin)
$target = "C:\Users\Acer\.gemini\antigravity-ide"
Write-Host ""
Write-Host "Step 2: Creating junction point..."
Write-Host "   antigravity -> antigravity-ide"

try {
    $result = cmd /c "mklink /J `"$antigravityDir`" `"$target`"" 2>&1
    Write-Host "   $result"
    
    if (Test-Path $antigravityDir) {
        Write-Host "[OK] Junction created successfully!"
    } else {
        throw "Junction was not created"
    }
} catch {
    Write-Host "[FAIL] $($_.Exception.Message)"
    Write-Host "   Trying symbolic link (requires admin)..."
    try {
        New-Item -ItemType SymbolicLink -Path $antigravityDir -Target $target -Force
        Write-Host "[OK] Symbolic link created!"
    } catch {
        Write-Host "[FAIL] Also failed. Please run as Administrator."
        exit 1
    }
}

# Step 4: Verify
Write-Host ""
Write-Host "Step 3: Verifying..."
$testFile = "$antigravityDir\agyhub_summaries_proto.pb"
if (Test-Path $testFile) {
    Write-Host "[OK] Can access data through junction"
    
    $brainCount = (Get-ChildItem "$antigravityDir\brain" -Directory -ErrorAction SilentlyContinue).Count
    $convCount = (Get-ChildItem "$antigravityDir\conversations" -File -Filter "*.db" -ErrorAction SilentlyContinue).Count
    Write-Host "   Brain folders: $brainCount"
    Write-Host "   Conversations: $convCount"
} else {
    Write-Host "[FAIL] Cannot access data through junction"
    exit 1
}

Write-Host ""
Write-Host "============================================"
Write-Host " DONE! Now open Antigravity 2.0"
Write-Host "    Your chat history should appear!"
Write-Host "============================================"
Write-Host ""
Write-Host "Press Enter to exit..."
Read-Host
