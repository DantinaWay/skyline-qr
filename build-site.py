"""Wrap skyline-qr.html (written as an Artifact page body) into a full document at site/index.html for static hosting."""
import shutil
from pathlib import Path

root = Path(__file__).parent
src = (root / "skyline-qr.html").read_text(encoding="utf-8")

split = src.index("</style>") + len("</style>")
head, body = src[:split], src[split:]

reset = """<style>
  :root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
  *, *::before, *::after { box-sizing: border-box; }
  body { margin: 0; -webkit-font-smoothing: antialiased; }
  img { max-width: 100%; }
</style>"""

meta = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Type a link, pick a pixel city, and fly up: from above, the rooftops form a QR code any phone can scan.">
<meta property="og:title" content="Skyline QR">
<meta property="og:description" content="Turn any link into a pixel city whose rooftops form a scannable QR code.">
<meta name="theme-color" content="#13151b">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="180x180" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">"""

out = f"""<!doctype html>
<html lang="en">
<head>
{meta}
{reset}
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""

(root / "site").mkdir(exist_ok=True)
for src_name, dst_name in [("fd-logo.png", "favicon.png"), ("favicon-32.png", "favicon-32.png"), ("apple-touch-icon.png", "apple-touch-icon.png")]:
    shutil.copyfile(root / "assets" / src_name, root / "site" / dst_name)
(root / "site" / "index.html").write_text(out, encoding="utf-8")
print("wrote site/index.html", len(out), "bytes")
