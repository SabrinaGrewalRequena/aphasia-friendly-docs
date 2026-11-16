"""Hand-made-looking decorations for the Home and About Me banners: painted pastel
shapes, a scatter of dots and a thin drawn sprig. Run by build_artifact.py."""
import math
import random

BLOB1 = "M421 64c74 41 118 133 104 216s-86 158-176 182-198-3-262-62S-2 260 21 177 112 22 199 8s148 15 222 56z"
BLOB2 = "M370 40c66 27 102 99 96 168s-55 135-128 160-160 9-220-38S30 205 50 132 130 15 205 8s99 5 165 32z"
PINK, BLUE, DOT_BLUE, DOT_PINK, STEM = "#f0d5cf", "#ffffff", "#bf8c80", "#e6b5af", "#a8776a"  # blush, white, rose-brown dots, pink dots, rose-brown sprig


def dots(rng, cx, cy, n, r, color, spread):
    out = []
    for _ in range(n):
        a = rng.uniform(0, 2 * math.pi); d = spread * math.sqrt(rng.random())
        x = cx + d * math.cos(a); y = cy + d * math.sin(a) * 0.8
        rx = r * rng.uniform(.6, 1.15); ry = rx * rng.uniform(.7, 1.05)
        out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{rx:.1f}" ry="{ry:.1f}" transform="rotate({rng.randint(0, 180)} {x:.0f} {y:.0f})"/>')
    return f'<g fill="{color}">' + "".join(out) + "</g>"


def sprig(x, y, s, color, flip=False):
    sx = -1 if flip else 1
    leaves = []
    for t, side in [(.18, 1), (.30, -1), (.44, 1), (.56, -1), (.68, 1), (.78, -1)]:
        py = y - t * 220 * s; px = x + sx * (12 * math.sin(t * 3.2)) * s; L = 24 * s * (1 - t * .4)
        leaves.append(f'<path d="M{px:.1f} {py:.1f} q {sx*side*L*.5:.1f} {-L*.55:.1f} {sx*side*L:.1f} {-L*.2:.1f} q {-sx*side*L*.45:.1f} {L*.35:.1f} {-sx*side*L:.1f} {L*.2:.1f}"/>')
    stem = f'<path d="M{x} {y} C {x+sx*10*s} {y-80*s}, {x-sx*6*s} {y-150*s}, {x+sx*14*s} {y-232*s}"/>'
    tx, ty = x + sx * 14 * s, y - 232 * s
    buds = (f'<path d="M{tx:.1f} {ty:.1f} q {-6*s:.1f} {-10*s:.1f} 0 {-18*s:.1f} q {6*s:.1f} {8*s:.1f} 0 {18*s:.1f}"/>'
            f'<circle cx="{x+sx*24*s:.1f}" cy="{y-196*s:.1f}" r="{4*s:.1f}"/><path d="M{x+sx*6*s:.1f} {y-170*s:.1f} l {sx*18*s:.1f} {-26*s:.1f}"/>')
    return f'<g fill="none" stroke="{color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{stem}{"".join(leaves)}{buds}</g>'


def piece(cls, viewbox, inner):
    return f'<svg class="d {cls}" viewBox="{viewbox}">{inner}</svg>'


def dot_piece(cls, seed, n, r, color):
    return piece(cls, "0 0 160 130", dots(random.Random(seed), 80, 65, n, r, color, 58))


def sprig_piece(cls, flip=False):
    return piece(cls, "0 0 70 250", sprig(35, 248, 1.0, STEM, flip))


# Each shape is its own small drawing pinned to a corner of the banner, so it keeps its
# rounded, painted edge at every screen size and never sits on top of the words.
def hero():
    return ('<div class="deco" aria-hidden="true">'
            + piece("blob-a", "-70 -70 680 620", f'<path d="{BLOB1}" fill="{PINK}" filter="url(#paint)"/>')
            + piece("blob-b", "-60 -70 620 540", f'<path d="{BLOB2}" fill="{BLUE}" filter="url(#paint)"/>')
            + dot_piece("dots-a", 7, 24, 7, DOT_BLUE) + dot_piece("dots-b", 3, 16, 6, DOT_PINK)
            + sprig_piece("sprig") + "</div>")


def about():
    return ('<div class="deco" aria-hidden="true">'
            + piece("blob-a", "-60 -70 620 540", f'<path d="{BLOB2}" fill="{PINK}" filter="url(#paint)"/>')
            + piece("blob-b", "-70 -70 680 620", f'<path d="{BLOB1}" fill="{BLUE}" filter="url(#paint)"/>')
            + dot_piece("dots-a", 11, 22, 6, DOT_BLUE) + dot_piece("dots-b", 5, 14, 5, DOT_PINK)
            + sprig_piece("sprig", flip=True) + "</div>")


DEFS = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="paint" x="-50%" y="-50%" width="200%" height="200%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="3" seed="4"/><feDisplacementMap in="SourceGraphic" scale="18"/></filter></svg>')
