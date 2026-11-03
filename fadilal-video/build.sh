#!/usr/bin/env bash
# Builds the seamless-loop FADILAL "Warm-Seal" product video.
# Inputs (this folder): A.png, B_cc.png, C_cc.png (B/C colour-matched to A), optional kling.mp4
# Outputs: fadilal-warm-seal.mp4, fadilal-warm-seal.webm, poster.jpg
set -euo pipefail
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
FF="ffmpeg -hide_banner -loglevel error -y"

# Zoom target on A (found by gloss detection): pixel (911,708) of 1254x1254
TX=0.72648; TY=0.56459; ZMAX=4.5

# ---- 1) ZOOM: A upscaled (Lanczos) to 8640 px, zoompan at 60 fps, 3.0 s, cosine ease-in-out ----
$FF -i A.png -vf "scale=8640:8640:flags=lanczos,format=yuv444p,\
zoompan=d=180:fps=60:s=1080x1080:\
z='pow($ZMAX,(1-cos(PI*on/179))/2)':\
x='iw*(0.5+($TX-0.5)*(1-1/zoom)/(1-1/$ZMAX))-iw/zoom/2':\
y='ih*(0.5+($TY-0.5)*(1-1/zoom)/(1-1/$ZMAX))-ih/zoom/2',\
fps=30" -c:v ffv1 "$T/zoom.nut"

# ---- 2+3) B / C (or kling) stream: 6.2 s = 0.6 transition-in + 5.0 + 0.6 loop-out ----
if [[ -f kling.mp4 ]]; then
  # Kling clip: centre-crop 1:1, 1080x1080, 30 fps; B (100->108 %) leads into it for 0.6 s
  $FF -i kling.mp4 -vf "crop='min(iw,ih)':'min(iw,ih)',scale=1080:1080:flags=lanczos,fps=30,format=yuv444p,\
trim=duration=5.6,setpts=PTS-STARTPTS,tpad=stop_mode=clone:stop_duration=1" -c:v ffv1 "$T/k.nut"
  $FF -loop 1 -framerate 30 -i B_cc.png -vf "scale=4320:4320:flags=lanczos,format=yuv444p,\
zoompan=d=1:fps=30:s=1080x1080:z='1+0.08*sin(PI/2*on/18)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'" \
    -frames:v 36 -c:v ffv1 "$T/bin.nut"
  $FF -i "$T/bin.nut" -i "$T/k.nut" -filter_complex "[0][1]xfade=transition=fade:duration=0.6:offset=0.6,trim=start=0.6,setpts=PTS-STARTPTS,trim=end_frame=186" \
    -c:v ffv1 "$T/bc.nut"
else
  # Fallback: B hold, 3.5 s slow fade to C (smoothstep), C hold.
  # Zoom curve (t = seconds since B appears): 100->108 % in 0.6 s (ease-out), then continuing
  # linearly and C1-continuous -> ~115 % at the end of the B->C fade (t = 5.1 s).
  ZB="if(lt(T,0.6),1+0.2511*T-0.1963*T*T,1.08+0.015556*(T-0.6))"
  zb() { echo "${ZB//T/($1)}"; }
  $FF -i B_cc.png -vf "scale=4320:4320:flags=lanczos,format=yuv444p,\
zoompan=d=153:fps=30:s=1080x1080:z='$(zb on/30)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'" -c:v ffv1 "$T/b.nut"
  $FF -i C_cc.png -vf "scale=4320:4320:flags=lanczos,format=yuv444p,\
zoompan=d=138:fps=30:s=1080x1080:z='$(zb on/30+1.6)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2'" -c:v ffv1 "$T/c.nut"
  $FF -i "$T/b.nut" -i "$T/c.nut" -filter_complex "[0][1]xfade=transition=custom:duration=3.5:offset=1.6:\
expr='A*P*P*(3-2*P)+B*(1-P*P*(3-2*P))+0.5',trim=end_frame=186" -c:v ffv1 "$T/bc.nut"
fi

# ---- assemble: zoom -> xfade 0.6 -> BC -> xfade 0.6 back to first frame of zoom (A @100 %) ----
$FF -i "$T/zoom.nut" -i "$T/bc.nut" -filter_complex "\
[0]split[z][z2];\
[z]tpad=stop_mode=clone:stop_duration=0.6[za];\
[z2]trim=end_frame=1,tpad=stop_mode=clone:stop_duration=1,setpts=PTS-STARTPTS[a0];\
[za][1]xfade=transition=fade:duration=0.6:offset=3.0[m];\
[m][a0]xfade=transition=fade:duration=0.6:offset=8.6,trim=end_frame=276,setsar=1" -c:v ffv1 "$T/master.nut"

[[ -n "${KEEP_MASTER:-}" ]] && cp "$T/master.nut" "$KEEP_MASTER"
N=$(ffprobe -v error -count_frames -select_streams v -show_entries stream=nb_read_frames -of csv=p=0 "$T/master.nut")
echo "master frames: $N"

# ---- H.264 MP4 < 5 MB ----
CRF=${CRF:-20}
while :; do
  $FF -i "$T/master.nut" -an -c:v libx264 -preset medium -crf $CRF -pix_fmt yuv420p -profile:v high \
    -colorspace bt709 -color_primaries bt709 -color_trc bt709 -g 60 -movflags +faststart fadilal-warm-seal.mp4
  SZ=$(stat -c %s fadilal-warm-seal.mp4)
  echo "mp4 crf=$CRF size=$SZ"
  (( SZ < 5000000 )) && break
  CRF=$((CRF+1))
done

# ---- VP9 WebM ----
$FF -i "$T/master.nut" -an -c:v libvpx-vp9 -b:v 0 -crf 36 -pix_fmt yuv420p -row-mt 1 -deadline good -cpu-used 2 \
  -pass 1 -passlogfile "$T/vp9" -f null /dev/null
$FF -i "$T/master.nut" -an -c:v libvpx-vp9 -b:v 0 -crf 36 -pix_fmt yuv420p -row-mt 1 -deadline good -cpu-used 2 \
  -pass 2 -passlogfile "$T/vp9" fadilal-warm-seal.webm
echo "webm size=$(stat -c %s fadilal-warm-seal.webm)"

# ---- poster from first frame ----
$FF -i "$T/master.nut" -frames:v 1 -q:v 2 poster.jpg
