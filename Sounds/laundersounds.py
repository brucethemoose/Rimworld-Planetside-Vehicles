import glob,os

for f in glob.glob("C:\Steam\steamapps\common\RimWorld\Mods\Rimworld-Planetside-Vehicles\Sounds\*.wav"):
    os.system('ffmpeg -i "' + f + '" -f wav -acodec pcm_s16le "' + f + '2"')
    os.remove(f)
    os.rename(f + "2", f)