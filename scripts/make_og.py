"""Generate the 1200x630 social card for the personal site. Mirrors the page hero."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
INK, PAPER, GOLD, MUTED, LINE = "#0a0a0b", "#f4f2ee", "#d4af37", "#a09a90", "#26241f"
F = "C:/Windows/Fonts/"

serif = lambda s: ImageFont.truetype(F + "pala.ttf", s)
mono = lambda s: ImageFont.truetype(F + "consola.ttf", s)
sans = lambda s: ImageFont.truetype(F + "segoeui.ttf", s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# --- right: accreditation badge with headshot ---
BW, BX, BY = 300, 830, 92
photo = Image.open("assets/headshot.jpg").convert("RGB")
pw = BW - 40
ph = int(pw * 1.25)
photo = photo.resize((pw, ph), Image.LANCZOS)
BH = ph + 178
d.rectangle([BX, BY, BX + BW, BY + BH], fill="#111113", outline=LINE)
d.rectangle([BX, BY, BX + BW, BY + 2], fill=GOLD)                    # gold top rule
d.rounded_rectangle([BX + BW//2 - 23, BY + 12, BX + BW//2 + 23, BY + 18], 3, fill=INK, outline=LINE)
d.text((BX + 20, BY + 34), "ALL ACCESS · PRODUCTION", font=mono(11), fill=GOLD)
d.text((BX + BW - 20, BY + 34), "№ 01", font=mono(11), fill=MUTED, anchor="ra")
img.paste(photo, (BX + 20, BY + 58))
d.rectangle([BX + 20, BY + 58, BX + 20 + pw, BY + 58 + ph], outline=LINE)
ty = BY + 58 + ph + 16
d.text((BX + 20, ty), "Ibrahim Muhammad Naeem", font=serif(19), fill=PAPER)
d.text((BX + 20, ty + 30), "OPERATOR · BUILDER · FOUNDER", font=mono(9), fill=MUTED)
# barcode
bx, by = BX + 20, ty + 52
for i, w in enumerate([2, 1, 3, 1, 2, 1, 1, 3, 2, 1] * 12):
    if i % 2 == 0:
        d.rectangle([bx, by, bx + w, by + 26], fill=PAPER)
    bx += w + 1
    if bx > BX + BW - 24:
        break

# --- left: type ---
x = 72
d.text((x, 96), "PRODUCTION & OPERATIONS · AI SYSTEMS · FOUNDER", font=mono(13), fill=GOLD)

lines = [[("I run the floor at", PAPER)],
         [("world-scale events.", PAPER)],
         [("Then I build the ", PAPER), ("machine", GOLD)],
         [("that could run it.", PAPER)]]
y = 150
for line in lines:
    cx = x
    for text, colour in line:
        d.text((cx, y), text, font=serif(44), fill=colour)
        cx += d.textlength(text, font=serif(44))
    y += 58

d.line([x, y + 22, x + 90, y + 22], fill=GOLD, width=2)
d.text((x, y + 44), "Twelve years of UAE event production.", font=sans(20), fill=MUTED)
d.text((x, y + 74), "GITEX · COP28 · Dubai World Cup · Gulfood", font=sans(20), fill=MUTED)

d.text((x, H - 52), "IBRAHIM NAEEM · DUBAI, UAE · IBRIIEE.GITHUB.IO", font=mono(12), fill=MUTED)

img.save("assets/og-image.jpg", quality=88, optimize=True)
print("wrote assets/og-image.jpg", img.size)
