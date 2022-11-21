import glob,os

#Losslessly convert weird .wav codecs into 16-bit PCM, so Rimworld can load it.  
for f in glob.glob("C:\Steam\steamapps\common\RimWorld\Mods\Rimworld-Planetside-Vehicles\Sounds\Colossus_Gecko*.wav"):
    os.system('ffmpeg -i "' + f + '" -f wav -acodec pcm_s16le "' + f + '2"')
    os.remove(f)
    os.rename(f + "2", f)