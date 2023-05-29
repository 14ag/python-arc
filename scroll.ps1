Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class MouseSettings
{
    [DllImport("user32.dll", EntryPoint = "SystemParametersInfo", SetLastError = true)]
    public static extern bool SystemParametersInfo(uint uiAction, uint uiParam, IntPtr pvParam, uint fWinIni);

    public const uint SPI_GETWHEELSCROLLLINES = 0x0068;
    public const uint SPI_SETWHEELSCROLLLINES = 0x0069;

    public static int GetWheelScrollLines()
    {
        uint lines = 0;
        SystemParametersInfo(SPI_GETWHEELSCROLLLINES, 0, out lines, 0);
        return (int)lines;
    }

    public static bool SetWheelScrollLines(int lines)
    {
        uint result = 0;
        return SystemParametersInfo(SPI_SETWHEELSCROLLLINES, (uint)lines, out result, 0);
    }
}
"@

# Get the current "lines to scroll" value
$currentLines = [MouseSettings]::GetWheelScrollLines()

# Toggle the "lines to scroll" option
$newLines = ($currentLines == 1) ? 4 : 1

# Set the new "lines to scroll" value
[MouseSettings]::SetWheelScrollLines($newLines)
