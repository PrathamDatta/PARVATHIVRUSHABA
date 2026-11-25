"""One-off helper: tweak orbit CSS, add ?service= prefill to the form JS, and render the social share image."""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)

p = 'assets/css/styles.css'
s = open(p).read()
s = s.replace(".orbit .core { position: absolute; inset: 22%;", ".orbit .core { position: absolute; inset: 25%;")
s = s.replace(".orbit .textring { position: absolute; inset: 4%;", ".orbit .textring { position: absolute; inset: .5%;")
s = s.replace(".orbit .r1 { inset: 12%;", ".orbit .r1 { inset: 13.5%;")
open(p, 'w').write(s)

j = 'assets/js/main.js'
t = open(j).read()
if 'prefill contact form' not in t:
    t = t.replace("  onScroll();\n})();", """  /* ---- prefill contact form from ?service= ---- */
  var qs = new URLSearchParams(w.location.search).get('service'), sel = $('#f-service');
  if (qs && sel) { $$('option', sel).some(function (o) { if (o.textContent.toLowerCase().indexOf(qs.toLowerCase().split(' ')[0]) === 0) { sel.value = o.textContent; return true; } }); }

  onScroll();
})();""")
    open(j, 'w').write(t)

W, H = 1200, 630
im = Image.new('RGB', (W, H), '#fffdf8')
d = ImageDraw.Draw(im, 'RGBA')
for (cx, cy, r, c) in [(1100, 60, 330, (143, 236, 240, 110)), (40, 90, 300, (201, 242, 91, 110)), (900, 640, 260, (242, 106, 61, 55))]:
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=c)
logo = Image.open('assets/img/logo.png').resize((400, 400), Image.LANCZOS)
im.paste(logo, (90, 115), logo)
B = '/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
M = '/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
f1, f2, f3, f4 = ImageFont.truetype(B, 60), ImageFont.truetype(B, 46), ImageFont.truetype(M, 28), ImageFont.truetype(M, 26)
d.text((540, 150), "PARVATHI", font=f1, fill='#1f55a4')
d.text((540, 215), "VRUSHABHA", font=f1, fill='#1f55a4')
d.text((540, 292), "HR Solution LLP", font=f2, fill='#1d2330')
d.text((540, 360), "Manpower • Staffing-Placement •", font=f3, fill='#4b5567')
d.text((540, 398), "Facility Management • HR Audits", font=f3, fill='#4b5567')
d.rounded_rectangle((540, 460, 1110, 520), radius=30, fill='#c9400f')
d.text((575, 474), "Strength in Service, Grace in Growth.", font=f4, fill='white')
im.save('assets/img/og-image.jpg', quality=88, optimize=True)
print('patched + og image ok')
