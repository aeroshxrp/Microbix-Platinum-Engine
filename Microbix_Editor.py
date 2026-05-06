"""
Microbix Media - PLATINUM ENTERPRISE V4.2
-------------------------------------------------------
FIXED: Positional Fade Arguments (Universal Compatibility)
"""

import os
import sys
import glob

# ==========================================
# 1. THE AUTO-LOCATOR & HOTFIXES
# ==========================================
print("=" * 70)
print("💎 BOOTING MICROBIX V4.2 PLATINUM ENGINE...")
print("=" * 70)

magick_paths = glob.glob(r"C:\Program Files\ImageMagick-*\magick.exe")
if magick_paths:
    os.environ["IMAGEMAGICK_BINARY"] = magick_paths[0]
else:
    print("❌ [CRITICAL] ImageMagick Engine not found.")
    sys.exit()

import PIL.Image
if not hasattr(PIL.Image, 'ANTIALIAS'):
    PIL.Image.ANTIALIAS = PIL.Image.LANCZOS 

try:
    from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
    import moviepy.video.fx.all as vfx 
except ImportError as e:
    print(f"\n❌ [CRITICAL ERROR] Library missing.\n{e}")
    sys.exit()

# ==========================================
# ULTRA-PREMIUM BRANDING (SIMPLIFIED FADES)
# ==========================================
def create_premium_title(text, duration, is_outro=False):
    from moviepy.video.VideoClip import ColorClip
    base = ColorClip(size=(1920, 1080), color=(10,10,10)).set_duration(duration)
    
    main_title = TextClip(text, fontsize=100, color='white', font='Arial', kerning=5)
    main_title = main_title.set_pos('center').set_duration(duration)
    
    if not is_outro:
        subtitle = TextClip("S I G N A T U R E   E D I T I O N", fontsize=30, color='#888888', font='Arial')
        subtitle = subtitle.set_pos(('center', 620)).set_duration(duration)
        # REMOVED KEYWORD ARGUMENTS: Just duration and color list
        return CompositeVideoClip([base, main_title, subtitle]).fx(vfx.fadein, 1).fx(vfx.fadeout, 0.3)
    
    return CompositeVideoClip([base, main_title]).fx(vfx.fadein, 0.5).fx(vfx.fadeout, 2)

# ==========================================
# THE KINETIC FX ENGINE (SIMPLIFIED FADES)
# ==========================================
def apply_platinum_fx(clip):
    c = clip.without_audio()
    duration = c.duration
    
    # Fast-Slow-Fast Ramp
    p1 = c.subclip(0, duration * 0.2).fx(vfx.speedx, 1.5)
    p2 = c.subclip(duration * 0.2, duration * 0.8).fx(vfx.speedx, 0.6)
    p3 = c.subclip(duration * 0.8, duration).fx(vfx.speedx, 1.5)
    
    ramped_clip = concatenate_videoclips([p1, p2, p3])
    ramped_clip = ramped_clip.fx(vfx.colorx, 1.15)
    ramped_clip = ramped_clip.fx(vfx.crop, y1=140, y2=940) 
    ramped_clip = ramped_clip.fx(vfx.margin, top=140, bottom=140, color=(0,0,0)) 
    
    # Using standard fades to avoid the color conflict
    ramped_clip = ramped_clip.fx(vfx.fadein, 0.2).fx(vfx.fadeout, 0.2)
    
    return ramped_clip

# ==========================================
# MAIN EXECUTION
# ==========================================
def run_platinum_processor():
    video_files = []
    print("\n🎬 [DIRECTOR'S QUEUE: PLATINUM]")
    print("Add your files. Type 'START' to render.\n")
    
    while True:
        file_name = input(f"Add Clip #{len(video_files) + 1} (or START): ").strip()
        if file_name.upper() == 'START':
            if len(video_files) == 0: continue
            break
        if os.path.exists(file_name):
            video_files.append(file_name)
            print(f"  ✅ INGESTED: '{file_name}'")
        else:
            print(f"  ❌ ERROR: File not found.")

    processed_clips = []
    print("-> Forging Premium Intro...")
    processed_clips.append(create_premium_title("M I C R O B I X", 3.5))

    for index, file in enumerate(video_files, start=1):
        print(f"💎 Ramping Clip {index}/{len(video_files)}: {file}")
        try:
            raw_clip = VideoFileClip(file).resize(height=1080)
            mid_point = raw_clip.duration / 2
            hero_shot = raw_clip.subclip(mid_point - 2.0, mid_point + 2.0)
            processed_clips.append(apply_platinum_fx(hero_shot))
        except Exception as e:
            print(f"   ⚠️ Error: {e}")

    from datetime import datetime
    year = datetime.now().strftime('%Y')
    processed_clips.append(create_premium_title(f"© {year} MICROBIX MEDIA", 3.5, is_outro=True))

    print("\n🔗 Compiling Platinum Master...")
    final_master = concatenate_videoclips(processed_clips, method="compose")
    output_filename = f"Microbix_PLATINUM_V4_2.mp4"

    try:
        # Final export
        final_master.write_videofile(output_filename, fps=30, codec="libx264", bitrate="25000k")
        print("\n✨ PLATINUM RENDER SUCCESSFUL!")
    except Exception as e:
        print(f"\n❌ [RENDER CRASH] {e}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    run_platinum_processor()