# Coconala profile icon 800x800: orange circle, tidy document, carpenter pencil (not crossing = no "prohibited" look).
import pathlib
from playwright.sync_api import sync_playwright
H=pathlib.Path(__file__).resolve().parent
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800" viewBox="0 0 800 800">
<circle cx="400" cy="400" r="392" fill="#F07A1A"/>
<rect x="232" y="168" width="330" height="430" rx="18" fill="#000" opacity=".12" transform="translate(12 14)"/>
<rect x="232" y="168" width="330" height="430" rx="18" fill="#FFFBF4"/>
<rect x="232" y="168" width="330" height="40" rx="18" fill="#C2552D"/><rect x="232" y="190" width="330" height="18" fill="#C2552D"/>
<rect x="268" y="240" width="200" height="26" rx="8" fill="#2B2622"/>
<rect x="268" y="290" width="258" height="12" rx="6" fill="#CFC4B8"/>
<rect x="268" y="316" width="230" height="12" rx="6" fill="#CFC4B8"/>
<g fill="#F3E7DA"><rect x="268" y="356" width="258" height="34" rx="6"/><rect x="268" y="398" width="258" height="34" rx="6"/><rect x="268" y="440" width="258" height="34" rx="6"/></g>
<g fill="#C2552D"><rect x="268" y="356" width="70" height="34" rx="6"/><rect x="268" y="398" width="70" height="34" rx="6"/><rect x="268" y="440" width="70" height="34" rx="6"/></g>
<rect x="268" y="500" width="200" height="12" rx="6" fill="#CFC4B8"/>
<g transform="translate(470 610) rotate(-45)">
 <rect x="-150" y="-26" width="240" height="52" rx="6" fill="#1F3A68"/>
 <rect x="-150" y="-26" width="240" height="17" fill="#2E5591"/>
 <polygon points="90,-26 150,0 90,26" fill="#F2C98A"/>
 <polygon points="132,-8 150,0 132,8" fill="#2B2622"/>
 <rect x="-150" y="-26" width="22" height="52" fill="#E9B44C"/>
</g>
</svg>'''
(H/'_icon.svg').write_text(svg)
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page(viewport={'width':800,'height':800})
    pg.goto((H/'_icon.svg').as_uri()); pg.screenshot(path=str(H/'icon.png'),omit_background=True); b.close()
(H/'_icon.svg').unlink(); print('ok')
