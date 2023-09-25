from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.audio.fx import audio_fadein, audio_fadeout
from moviepy.editor import *
from importlib.metadata import version

import image
import claw_baiduimg
import gif
import os

def moveOpe():
    # 加载视频剪辑
    video_clip = VideoFileClip("最美风景.mp4")

    # 剪辑视频的一部分（从第2秒到第6秒）
    clip_segment = video_clip.subclip(2, 6)

    # 裁剪视频，保留左上角区域
    # cropped_clip = clip_segment.crop(x1=0, y1=0, x2=500, y2=300)

    # 添加文本到视频
    text_clip = TextClip("爱跳舞", fontsize=50, font='./hwfs.ttf', color='white')
    video_with_text = CompositeVideoClip([clip_segment.set_duration(4), text_clip.set_duration(4).set_position(("center", "bottom"))])

    # # 获取视频剪辑的音频部分
    # video_audio = video_clip.audio.subclip(2, 6)

    # # 添加音频效果（淡入和淡出）
    # audio_fadein_out = audio_fadein(audio_fadeout(video_audio, 2), 2)

    # # 设置视频的音频
    # video_with_audio = video_with_text.set_audio(audio_fadein_out)

    # 保存处理后的视频
    video_with_text.write_videofile("a1_out.mp4", codec='libx264', audio_codec='aac')

def getMoveInfo(file):
    video_clip = VideoFileClip(file)
    # print(dir(video_clip))
    print("视频总时长", video_clip.duration,'视频高度',video_clip.h, '视频宽度',video_clip.w)
    print('视频分辨率', video_clip.size)
    print('视频文件大小',os.path.getsize(file))
    print(video_clip.fps)  # 获取帧数


##从视频中抽取音频

def getaudio_from_video(src_file, dst_file):
    """
    # 提取出来的格式为mp3
    :param src_file:
    :param dst_file:
    :return:
    """

    # 1. 读取目标文件
    video = VideoFileClip(filename=src_file)

    # 2. 取出其中的音频数据结构
    video.audio.write_audiofile(filename=dst_file)

    print("done")

# getaudio_from_video("douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp4", 'douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp3')

def del_videofile_audio(file):
    video = VideoFileClip(file)
    video = video.without_audio()
    video.write_videofile("nomusic_"+file, codec='libx264', audio_codec='aac')

# add_audio_tovideo():
def add_audio_tovideo():
    video_clip = VideoFileClip('douyin_1.mp4')
    #提取视频对应的音频，并调节音量
    # video_audio_clip = video_clip.audio.volumex(0.8)
    #背景音乐
    audio_clip = AudioFileClip('douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp3')
    #设置背景音乐循环，时间与视频时间一致
    # audio_clip = audio_clip.subclip(0, video_clip.duration)
    # audio = afx.audio_loop( audio_clip, duration=video_clip.duration)

    # num_audio_repeats = int(video_clip.duration / audio_clip.duration)+1

    # 使用 afx.audio_loop 来匹配音频长度
    # audio = afx.audio_loop(audio_clip, nloops=num_audio_repeats)


    #视频声音和背景音乐，音频叠加
    # audio_clip_add = CompositeAudioClip([video_audio_clip,audio])
    #视频写入背景音
    final_video = video_clip.set_audio(audio_clip)
    #将处理完成的视频保存
    final_video.write_videofile("douyin_1_music.mp4")

# add_audio_tovideo()

# pip freeze | grep moviepy 获取版本信息
def getversion():
    print(version('moviepy'))

##穿插混合2个视频
def diff_two_movies():
    diff_num = 5

    video_clipa = VideoFileClip("baidu/绝美星空/绝美星空.mp4")
    video_alist = []
    piece_len = (video_clipa.duration/diff_num)
    for x in range(diff_num):
        print('a',int(x*piece_len), int((x+1)*piece_len)-1)
        videoa = video_clipa.subclip(int(x*piece_len)-1, int((x+1)*piece_len)-1)
        video_alist.append(videoa)

    video_clipb = VideoFileClip("baidu/水果/水果.mp4")
    video_blist = []
    piece_len = int(video_clipb.duration/diff_num)
    for x in range(diff_num):
        print('b',int(x*piece_len), int((x+1)*piece_len)-1)
        videoa = video_clipb.subclip(0, int((x+1)*piece_len)-1)
        video_blist.append(videoa)

    last_list = []
    for x in range(diff_num):
        print(x)
        last_list.append(video_alist[x])
        last_list.append(video_blist[x])
    
    final_video= concatenate_videoclips(last_list)
    final_video.write_videofile("星空水果.mp4")
    getMoveInfo("星空水果.mp4")

##合并视频-视频拼接
def double_movie():
    video_1 = VideoFileClip("a1.mp4")
    video_2 = VideoFileClip("a2.mp4")

    final_video= concatenate_videoclips([video_1, video_2])
    final_video.write_videofile("final_video.mp4")

##获取视频封面
def get_video_shotimg(file):
    clip = VideoFileClip(file)
    clip.save_frame("frame.jpg")  # 保存第1帧
    clip.save_frame("frame.png", t=2)  # 保存2s时刻的那1帧

def get_gif_fromvideo():
    clip = VideoFileClip('./1644974996.mp4').subclip(10, 20)
    # clip.write_gif('demo.gif',fps=15) # 生成之后的文件大
    clip.write_gif('demo.gif',fps=5) # 生成之后的文件小

##视频叠加
def array_movie():
    # from moviepy.editor import VideoFileClip, clips_array, vfx
 
    # clip1 = VideoFileClip("baidu/高清电影/高清电影.mp4").margin(10)
    # clip2 = clip1.fx(vfx.mirror_x)#x轴镜像
    # clip3 = clip1.fx(vfx.mirror_y)#y轴镜像
    # clip4 = clip1.resize(0.6)#尺寸等比缩放0.6
    
    # final_clip = clips_array([
    #                             [clip1, clip3],
    #                             [clip2, clip4]
    #                         ])
    # final_clip.resize(width=480).write_videofile("my_stack.mp4")

    clip1 = VideoFileClip("douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp4").margin(10)
    clip2 = VideoFileClip("douyin/7081234022608751910-.mp4").margin(10)
    final_clip = clips_array([ [clip1, clip2],])
    
    # audio_clip = AudioFileClip('source/蜜雪.mp3')
    #设置背景音乐循环，时间与视频时间一致
    # audio_clip = audio_clip.subclip(0, video_clip.duration)
    # audio = afx.audio_loop( audio_clip, duration=audio_clip.duration)

    # num_audio_repeats = int(final_clip.duration / audio_clip.duration)+1
    # print(num_audio_repeats)

    # 使用 afx.audio_loop 来匹配音频长度
    # audio = afx.audio_loop(audio_clip, nloops=num_audio_repeats)
    # final_clip.set_audio(audio)
    # final_clip.resize(width=240).write_videofile("my_stack.mp4",codec='libx264', audio_codec='aac')
    final_clip.write_videofile("douyin_1.mp4")

##修改视频属性
def modify_video():
    video_clip = VideoFileClip("xxx.mp4").subclip(10, 20)
    video_clip=(
        #调整尺寸，保持比例
        video_clip.fx(vfx.resize,width=460)
        #倍数播放
        .fx(vfx.speedx,2)
        #画面调暗
        .fx(vfx.colorx,0.5)
    )

##
def compo_pos_vides():
    clip1 = VideoFileClip('douyin/7281068322991377703-无忧美女千千谁是你的NO你可以永远相信无忧传媒.mp4').without_audio()
    clip2 = VideoFileClip('douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp4').without_audio()
    # clip = VideoFileClip('douyin/7081234022608751910-.mp4')
    clip3 = VideoFileClip('douyin/7081234022608751910-.mp4').without_audio()
    video = CompositeVideoClip([
        clip1,
        clip2.set_pos((45,150)).set_start(2),
        clip3.set_pos((90,100)).set_start(5),
    ], size=(720, 480))

    # clip2.set_pos((45,150)) #像素坐标
    # clip2.set_pos("center") #居中
    # clip2.set_pos(("center","top")) #水平方向居中，但是处置方向放置在顶部
    # clip2.set_pos(("left","center")) #水平方向放置在左边，垂直方向居中
    # clip2.set_pos((0.4,0.7), relative=True) #0.4倍宽，0.7倍高处
    # clip2.set_pos(lambda t: ('center', 50+t)) #水平居中，向下移动
    video = video.without_audio()

    audio_clip = AudioFileClip('douyin/7280470491683507467-兄弟们又来学钢琴啦#今天你练琴了吗.mp3')
    #设置背景音乐循环，时间与视频时间一致
    # audio_clip = audio_clip.subclip(0, video_clip.duration)

    # audio = afx.audio_loop( audio_clip, duration=video_clip.duration)
    num_audio_repeats = int(video.duration / audio_clip.duration)+1

    # 使用 afx.audio_loop 来匹配音频长度
    audio_clip = afx.audio_loop(audio_clip, nloops=num_audio_repeats)

    #视频声音和背景音乐，音频叠加
    # audio_clip_add = CompositeAudioClip([video_audio_clip,audio])
    #视频写入背景音
    final_video = video.set_audio(audio_clip)
    #将处理完成的视频保存
    final_video.write_videofile("douyin_2_music.mp4", )

# getaudio_from_video('source/a1.mp4', 'source/蜜雪.mp3')
# add_audio_tovideo()
# getversion()
# getMoveInfo()
# diff_two_movies()


# dir = input("请输入搜索主题：")
# claw_baiduimg.claw_baidu_img(dir)
# image.cropImg(dir)
# gif.create_mp4(dir)

# diff_two_movies()

# add_audio_tovideo()

# get_video_shotimg('baidu/仙女湖/仙女湖.mp4')

# array_movie()

compo_pos_vides()