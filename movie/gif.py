from moviepy.editor import ImageSequenceClip

def create_gif():
    img_names = ['baidu/最美风景/'+str(i)+'_1.jpg' for i in range(0,20)]
    img_names.reverse()
    clip = ImageSequenceClip(img_names,fps=1)
    clip.write_gif('demo.gif')

##图片生成视频
def create_mp4(dir):
    img_names = ['baidu/'+dir+'/'+str(i)+'_1.jpg' for i in range(0,20)]
    img_names.reverse()
    clip = ImageSequenceClip(img_names,fps=1)
    # clip.write_gif('demo.gif')
    clip.write_videofile("baidu/"+dir+"/"+dir+'.mp4')