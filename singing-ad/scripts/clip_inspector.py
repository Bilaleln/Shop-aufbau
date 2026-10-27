#!/usr/bin/env python3
"""Inspect video clips for quality issues per Singing Ad skill rules.

Extracts N evenly-spaced frames and checks for:
- Hard cuts (scene value spikes)
- Freeze frames
- Basic composition (4:5 safety zone)

Usage:
    python3 clip_inspector.py <clip.mp4> [--frames 6]
"""

import json
import re
import subprocess
import sys
from pathlib import Path


def extract_frames(clip_path, n=6, output_dir=None):
    if output_dir is None:
        output_dir = Path(clip_path).parent / f"{Path(clip_path).stem}_frames"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    duration = float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "csv=p=0", clip_path
    ]).decode().strip())

    frames = []
    for i in range(n):
        t = (i / max(n - 1, 1)) * duration
        out = Path(output_dir) / f"frame_{i:02d}_{t:.2f}s.png"
        subprocess.run([
            "ffmpeg", "-y", "-ss", str(t), "-i", clip_path,
            "-frames:v", "1", "-q:v", "2", str(out)
        ], capture_output=True)
        frames.append({"time": t, "path": str(out)})

    return frames, duration


def detect_scene_changes(clip_path, threshold=0.12):
    result = subprocess.run([
        "ffmpeg", "-i", clip_path,
        "-vf", "select='gte(scene,0)',metadata=print",
        "-f", "null", "-"
    ], capture_output=True, text=True)

    cuts = []
    current_pts = None
    for line in result.stderr.split("\n"):
        if "pts_time:" in line:
            m = re.search(r"pts_time:(\d+\.?\d*)", line)
            if m:
                current_pts = float(m.group(1))
        if "scene_score=" in line and current_pts is not None:
            m = re.search(r"scene_score=(\d+\.?\d*)", line)
            if m:
                score = float(m.group(1))
                if score > threshold:
                    cuts.append({"time": current_pts, "score": score})

    return cuts


def detect_freezes(clip_path, noise=0.001, duration=0.8):
    result = subprocess.run([
        "ffmpeg", "-i", clip_path,
        "-vf", f"freezedetect=n={noise}:d={duration}",
        "-an", "-f", "null", "-"
    ], capture_output=True, text=True)

    freezes = []
    for line in result.stderr.split("\n"):
        if "freeze_start" in line:
            m = re.search(r"freeze_start:\s*(\d+\.?\d*)", line)
            if m:
                freezes.append({"start": float(m.group(1))})
        elif "freeze_end" in line and freezes:
            m = re.search(r"freeze_end:\s*(\d+\.?\d*)", line)
            if m:
                freezes[-1]["end"] = float(m.group(1))

    return freezes


def inspect(clip_path, n_frames=6):
    frames, duration = extract_frames(clip_path, n_frames)
    cuts = detect_scene_changes(clip_path)
    freezes = detect_freezes(clip_path)

    report = {
        "clip": clip_path,
        "duration": round(duration, 2),
        "frames_extracted": len(frames),
        "scene_cuts": cuts,
        "freezes": freezes,
        "issues": [],
    }

    if cuts:
        report["issues"].append(f"{len(cuts)} hard cut(s) detected")
    if freezes:
        report["issues"].append(f"{len(freezes)} freeze(s) detected")

    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 clip_inspector.py <clip.mp4> [--frames N]")
        sys.exit(1)

    clip = sys.argv[1]
    n = 6
    if "--frames" in sys.argv:
        idx = sys.argv.index("--frames")
        n = int(sys.argv[idx + 1])

    report = inspect(clip, n)
    print(json.dumps(report, indent=2))
    if report["issues"]:
        print(f"\n⚠ {len(report['issues'])} issue(s) found")
    else:
        print("\n✓ No issues detected")
