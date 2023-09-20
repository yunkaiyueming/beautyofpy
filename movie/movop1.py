from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.audio.fx import audio_fadein, audio_fadeout
from moviepy.editor import *
from importlib.metadata import version

import image
import claw_baiduimg
import gif

def moveOpe():
    # 加载视频剪辑
    video_clip = VideoFileClip("最美风景.mp4")

    # 剪辑视频的一部分（从第2秒到第6秒）
    clip_segment = video_clip.subclip(2, 6)

    # 裁剪视频，保留左上角区域
    # cropped_clip = clip_segment.crop(x1=0, y1=0, x2=500, y2=300)

    # 添加文本到视频
    text_clip = TextClip("甜蜜，爱跳舞", fontsize=50, font='./hwfs.ttf', color='white')
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
    print(dir(video_clip))
    print(video_clip.duration,video_clip.h,video_clip.w)


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

def add_audio_tovideo():
    video_clip = VideoFileClip('baidu/最美风景/最美风景.mp4')
    #提取视频对应的音频，并调节音量
    # video_audio_clip = video_clip.audio.volumex(0.8)
    #背景音乐
    audio_clip = AudioFileClip('source/蜜雪.mp3')
    #设置背景音乐循环，时间与视频时间一致
    # audio_clip = audio_clip.subclip(0, video_clip.duration)
    # audio = afx.audio_loop( audio_clip, duration=video_clip.duration)

    num_audio_repeats = int(video_clip.duration / audio_clip.duration)+1

    # 使用 afx.audio_loop 来匹配音频长度
    audio = afx.audio_loop(audio_clip, nloops=num_audio_repeats)


    #视频声音和背景音乐，音频叠加
    # audio_clip_add = CompositeAudioClip([video_audio_clip,audio])
    #视频写入背景音
    final_video = video_clip.set_audio(audio)
    #将处理完成的视频保存
    final_video.write_videofile("baidu/最美风景/最美风景_music.mp4", codec='libx264', audio_codec='aac')

def getversion():
    print(version('moviepy'))

def diff_two_movies():
    diff_num = 5

    video_clipa = VideoFileClip("baidu/最美风景/最美风景.mp4")
    video_alist = []
    piece_len = (video_clipa.duration/diff_num)
    for x in range(diff_num):
        print('a',int(x*piece_len), int((x+1)*piece_len)-1)
        videoa = video_clipa.subclip(int(x*piece_len)-1, int((x+1)*piece_len)-1)
        video_alist.append(videoa)

    video_clipb = VideoFileClip("source/a3.mp4")
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
    final_video.write_videofile("最美蜜雪.mp4")
    getMoveInfo("最美蜜雪.mp4")


def double_movie():
    video_1 = VideoFileClip("a1.mp4")
    video_2 = VideoFileClip("a2.mp4")

    final_video= concatenate_videoclips([video_1, video_2])
    final_video.write_videofile("final_video.mp4")

# getaudio_from_video('source/a1.mp4', 'source/蜜雪.mp3')
# add_audio_tovideo()
# getversion()
# getMoveInfo()
# diff_two_movies()

dir = input("请输入搜索主题：")
claw_baiduimg.claw_baidu_img(dir)
image.cropImg(dir)
gif.create_mp4(dir)