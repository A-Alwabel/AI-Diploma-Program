"""
Arabic Font Setup Utility for Matplotlib
أداة إعداد خطوط العربية لـ Matplotlib

This utility configures matplotlib to properly display Arabic text in visualizations.
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform

def setup_arabic_font():
    """
    Configure matplotlib to display Arabic text correctly.
    يُعد matplotlib لعرض النص العربي بشكل صحيح.
    
    Returns:
        bool: True if Arabic font was found and configured, False otherwise
    """
    system = platform.system()
    
    # List of common Arabic-supporting fonts by system
    arabic_fonts = {
        'Darwin': [  # macOS
            'Arial Unicode MS',
            'Helvetica Neue',
            'Tahoma',
            'Geeza Pro',
            'Baghdad',
        ],
        'Windows': [
            'Arial Unicode MS',
            'Tahoma',
            'Microsoft Sans Serif',
            'Segoe UI',
        ],
        'Linux': [
            'DejaVu Sans',
            'Arial Unicode MS',
            'Noto Sans Arabic',
            'Liberation Sans',
        ]
    }
    
    # Get available fonts
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    
    # Try to find an Arabic-supporting font
    system_fonts = arabic_fonts.get(system, arabic_fonts['Linux'])
    
    for font_name in system_fonts:
        if font_name in available_fonts:
            plt.rcParams['font.family'] = font_name
            plt.rcParams['axes.unicode_minus'] = False  # Fix minus sign issue
            print(f"✓ Arabic font configured: {font_name}")
            print(f"✓ تم إعداد الخط العربي: {font_name}")
            return True
    
    # Fallback: Use default font and enable unicode minus
    plt.rcParams['axes.unicode_minus'] = False
    print("⚠ Warning: No Arabic font found. Arabic text may not display correctly.")
    print("⚠ تحذير: لم يتم العثور على خط عربي. قد لا يظهر النص العربي بشكل صحيح.")
    return False

def configure_matplotlib_for_bilingual():
    """
    Configure matplotlib for bilingual (Arabic/English) visualizations.
    يُعد matplotlib للتصورات ثنائية اللغة (عربي/إنجليزي).
    """
    setup_arabic_font()
    
    # Enable right-to-left text rendering where needed
    plt.rcParams['text.usetex'] = False
    
    # Set figure DPI for better quality
    plt.rcParams['figure.dpi'] = 100
    
    # Better font rendering
    plt.rcParams['font.size'] = 10
    
    return True

# Auto-configure when imported
if __name__ == "__main__":
    configure_matplotlib_for_bilingual()
else:
    # Configure when module is imported
    configure_matplotlib_for_bilingual()

