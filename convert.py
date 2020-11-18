# Python code to convert video to audio 
# In this project i use python moviepy module
#for install moviepy module
#run this command:  'pip install moviepy'

import moviepy.editor as mp 

clip = mp.VideoFileClip(r'Enter Your File Location (video)')
clip.audio.write_audiofile(r'Enter Your audio File saving Location')
