# Skyline QR

Turn any link into a pixel city whose rooftops form a scannable QR code.

**Live:** https://skyline-qr.vercel.app · **Code:** https://github.com/DantinaWay/skyline-qr

Type a link, pick a city and a colour set, then hit **Fly up**. The camera rises from a street-level view of the skyline to directly overhead, where the rooftops line up into a QR code any phone camera can read. Download the top-down view as a PNG.

## Cities

| City | Landmarks and details |
|---|---|
| New York | Water tanks, yellow cabs, Statue of Liberty, suspension bridge |
| Tokyo | Neon signs, red-and-white lattice tower, Mt Fuji |
| Rio de Janeiro | Hillside houses, Sugarloaf, the Christ statue, wave-pattern promenade |
| Santorini | Terraced cliffs, blue domes, windmill, sailboat |
| Lisbon | Pastel hills, pitched terracotta roofs, castle, red bridge, trams |
| Marrakech | Pink medina, ramparts, square minaret, palm groves, the Atlas |
| Dubai | Glass towers, the needle tower, sail hotel, palm island, dunes |
| Paris | Mansard zinc roofs, domed monument, the iron tower, the river |

Each city has three colour sets and a day/night mode.

## How it works

- The link is encoded with high error correction (level H) using [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator).
- Every dark module becomes a building; neighbouring dark modules are merged into larger blocks. Light modules are streets, and the required four-module quiet zone is kept clear around the code.
- The three corner finder patterns always become landmark buildings.
- Buildings can be any height: from directly above, with an orthographic camera and flat lighting, only the roof colours show. Roofs are always dark and streets always light, so the code keeps its contrast.
- Rendering uses [three.js](https://threejs.org) (r128). All geometry is generated in code and batched into a few meshes.

## Files

| Path | What it is |
|---|---|
| `skyline-qr.html` | The whole app: markup, styles and script in one file. Edit this one. |
| `build-site.py` | Wraps `skyline-qr.html` into a full HTML document at `site/index.html` and copies the icons. |
| `site/` | The static site deployed to Vercel (generated). |
| `assets/` | Logo and icon sources. |

## Run locally

```bash
python3 build-site.py
python3 -m http.server 8000 --directory site
```

Then open http://localhost:8000.

## Deploy

The `site/` folder is a plain static site with no build step, so any static host works. With Vercel:

```bash
python3 build-site.py
cd site && npx vercel deploy --prod
```

## License

Code: [MIT](LICENSE) © 2026 FD. Studio.

The FD. Studio name and logo are not covered by the MIT License; see [TRADEMARKS.md](TRADEMARKS.md). If you fork the project, replace them with your own branding.

Third-party libraries loaded from CDNs keep their own licenses: three.js (MIT) and qrcode-generator (MIT). Fonts are from Google Fonts under the SIL Open Font License.
