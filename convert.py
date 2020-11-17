# Python code to convert video to audio 


import moviepy.editor as mp 

clip = mp.VideoFileClip(r'Enter Your File Location (video)')
clip.audio.write_audiofile(r'Enter Your audio File saving Location')
