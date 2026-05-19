#!/usr/bin/env python3
"""Generate logic-flow schematic PNG for opioid behavioral model proposal."""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parent / "logic_flow_schematic.png"


def box(ax, xy, w, h, text, fc, ec="#333333", fontsize=9):
    x, y = xy
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.02",
        linewidth=1.2,
        edgecolor=ec,
        facecolor=fc,
    )
    ax.add_patch(p)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        wrap=True,
    )
    return (x + w / 2, y, x + w / 2, y + h)  # bottom center, top center


def arrow(ax, p1, p2):
    arr = FancyArrowPatch(
        p1,
        p2,
        arrowstyle="-|>",
        mutation_scale=12,
        linewidth=1.2,
        color="#444444",
    )
    ax.add_patch(arr)


def main():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title(
        "Opioid PR: Logic Flow (behavior-only computational model)",
        fontsize=14,
        fontweight="bold",
        pad=12,
    )

    # Row 1: question
    q = box(
        ax,
        (0.15, 0.88),
        0.7,
        0.08,
        "Normative Q: What latent states explain lick / seek / escalate\n"
        "and re-exposure after withdrawal?",
        "#E8F4FC",
        fontsize=10,
    )

    # Row 2: motifs
    motifs = [
        (0.02, 0.72, 0.22, "A. Reward integrator\nV_t"),
        (0.27, 0.72, 0.22, "B. Deficit integrator\nD_t"),
        (0.52, 0.72, 0.22, "C. Seeking dynamics\nbouts / pause"),
        (0.77, 0.72, 0.21, "D. Context gain\ncue × phase"),
    ]
    motif_centers = []
    for x, y, w, t in motifs:
        _, _, _, top_y = box(ax, (x, y), w, 0.1, t, "#FFF8E6")
        motif_centers.append((x + w / 2, top_y))

    for c in motif_centers:
        arrow(ax, (0.5, 0.88), c)

    # Row 3: groups
    box(
        ax,
        (0.05, 0.48),
        0.42,
        0.18,
        "PASSIVE (patient-relevant)\n"
        "• Pavlovian/context memory (During)\n"
        "• Withdrawal: PIT-like ↑ seeking\n"
        "• Re-exposure: weak action value\n"
        "Seeking ~ C_t × G_withdrawal",
        "#FDE8E8",
        fontsize=8.5,
    )
    box(
        ax,
        (0.53, 0.48),
        0.42,
        0.18,
        "ACTIVE (contingency-dependent)\n"
        "• Strong V_t / action–outcome\n"
        "• Withdrawal: deficit D_t\n"
        "• Re-exposure: V × D amplification\n"
        "Seeking ~ V_t × W_t",
        "#E8FDE8",
        fontsize=8.5,
    )
    arrow(ax, (0.25, 0.72), (0.26, 0.66))
    arrow(ax, (0.75, 0.72), (0.74, 0.66))

    # Row 4: models
    box(
        ax,
        (0.08, 0.28),
        0.84,
        0.14,
        "Model ladder:  (0) drift x_t  →  (1) x_t → λ_t  →  (2) V_t, D_t  →  (3) passive C_t×G\n"
        "Fit: SBI (MNLE/MCMC)  |  PR = single patch (no leave); continue / pause / quit",
        "#EEEEFF",
        fontsize=9,
    )
    arrow(ax, (0.26, 0.48), (0.35, 0.42))
    arrow(ax, (0.74, 0.48), (0.65, 0.42))

    # Row 5: data & output
    box(
        ax,
        (0.08, 0.08),
        0.38,
        0.14,
        "INPUT\nJSONL licks/rewards\n"
        "group × phase\nPR requirement T",
        "#F0F0F0",
        fontsize=8.5,
    )
    box(
        ax,
        (0.54, 0.08),
        0.38,
        0.14,
        "OUTPUT\nGroup parameters\n"
        "Model comparison\n"
        "Test H1–H3 → future neural",
        "#F0F0F0",
        fontsize=8.5,
    )
    arrow(ax, (0.5, 0.28), (0.27, 0.22))
    arrow(ax, (0.5, 0.28), (0.73, 0.22))

    # Legend
    leg = [
        mpatches.Patch(facecolor="#FDE8E8", edgecolor="#333", label="Passive mechanism"),
        mpatches.Patch(facecolor="#E8FDE8", edgecolor="#333", label="Active mechanism"),
        mpatches.Patch(facecolor="#EEEEFF", edgecolor="#333", label="Computational fit"),
    ]
    ax.legend(handles=leg, loc="lower center", ncol=3, fontsize=8, frameon=True)

    fig.tight_layout()
    fig.savefig(OUT, dpi=200, bbox_inches="tight", facecolor="white")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
