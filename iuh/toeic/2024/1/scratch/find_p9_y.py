import subprocess

ps_code = """
param([string]$ImagePath)
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$asTaskGeneric = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object { $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
function Await($WinRtTask, $ResultType) {
    $asTask = $asTaskGeneric.MakeGenericMethod($ResultType)
    $netTask = $asTask.Invoke($null, @($WinRtTask))
    $netTask.Wait(-1) | Out-Null
    $netTask.Result
}
[Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime] | Out-Null
[Windows.Media.Ocr.OcrEngine,Windows.Foundation,ContentType=WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder,Windows.Graphics.Imaging,ContentType=WindowsRuntime] | Out-Null
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync((Resolve-Path $ImagePath).Path)) ([Windows.Storage.StorageFile])
$stream = Await ($file.OpenAsync([Windows.Storage.FileAccessMode]::Read)) ([Windows.Storage.Streams.IRandomAccessStream])
$decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
$bitmap = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
$result = Await ($engine.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])

foreach ($line in $result.Lines) {
    if ($line.Text -match 'Area|scooter|Tree|Shelby|Train|Terminal') {
        Write-Output "$($line.Text) [y=$([int]$line.Words[0].BoundingRect.Y), x=$([int]$line.Words[0].BoundingRect.X), h=$([int]$line.Words[0].BoundingRect.Height), w=$([int]$line.Words[0].BoundingRect.Width)]"
    }
}
"""

with open(r"d:\folder\rac\iuh\toeic\2024\1\scratch\find_y.ps1", "w", encoding="utf-8") as f:
    f.write(ps_code)

cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", r"d:\folder\rac\iuh\toeic\2024\1\scratch\find_y.ps1", "-ImagePath", r"d:\folder\rac\iuh\toeic\2024\1\scratch\t2_lc_p9.png"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
print(res.stdout)
