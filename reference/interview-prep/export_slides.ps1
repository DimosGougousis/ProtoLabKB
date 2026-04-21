param(
  [string]$pptxPath = "C:\Users\dimos\ProtoLab\interview_presentation.pptx",
  [string]$outDir   = "C:\Users\dimos\ProtoLab\slides_out"
)

if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir | Out-Null }
Get-ChildItem $outDir -Filter "slide_*.png" -ErrorAction SilentlyContinue | Remove-Item -Force

$ppt = New-Object -ComObject PowerPoint.Application
# 1920x1080 target — LAYOUT_WIDE is 13.333 x 7.5 inches at ~144 DPI
$scaleW = 1920
$scaleH = 1080

$pres = $ppt.Presentations.Open($pptxPath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)

$i = 1
foreach ($slide in $pres.Slides) {
  $num = "{0:D2}" -f $i
  $out = Join-Path $outDir ("slide_" + $num + ".png")
  $slide.Export($out, "PNG", $scaleW, $scaleH)
  Write-Host ("Exported slide " + $i + " -> " + $out)
  $i++
}

$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
Write-Host "Done."
