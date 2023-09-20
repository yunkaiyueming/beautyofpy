# # from moviepy.editor import ImageSequenceClip, TextClip, CompositeVideoClip
# # import os

# # # Image folder path
# # image_folder = 'baidu/最美风景/'

# # # Output video file name
# # output_video = 'output_video.mp4'

# # # Get image file list
# # image_files = [image_folder + filename for filename in sorted(os.listdir(image_folder))]

# # # Load the first image to get dimensions
# # first_image = ImageSequenceClip([image_files[0]], fps=24)
# # video_width, video_height = first_image.size

# # # Function to add text to a frame
# # def add_text_to_frame(frame, text, fontsize=30, color='white'):
# #     txt_clip = TextClip(text, fontsize=fontsize, color=color)
# #     txt_clip = txt_clip.set_duration(frame.duration)  # Set text duration
# #     txt_clip = txt_clip.set_position(("center", "bottom")).set_start(0)  # Set text position and timing
# #     return CompositeVideoClip([frame, txt_clip])

# # # Create a video clip by adding text to each frame
# # video_clip = CompositeVideoClip([add_text_to_frame(ImageSequenceClip([image], fps=24), "Your Text Here") for image in image_files], size=(video_width, video_height))

# # # Write the video to a file
# # video_clip.write_videofile(output_video, codec='libx264')

# # print("Video creation completed.")




# if __name__ == '__main__':
#     txt_cplis = []
#     image_clips = []
#     for x in range(20):
#         jpgname = "baidu/最美风景/"+str(x)+".jpg"
#         print(jpgname)
#         # 读取视频
#         imgclip = VideoFileClip(jpgname).set_duration(2)
#         # 文字视频
#         txt_clip: TextClip = TextClip("num_"+str(x) , fontsize=70, color='white')
#         txt_clip = txt_clip.set_position("center","bottom").set_duration(2)
#         # txt_clip.set_duration(2)
#         # txt_clip = txt_clip.set_position(("center", "bottom")).set_start(0).set_end(2)
#         # txt_clip = txt_clip.set_position((10,20)).set_duration(10)
#         image_clips.append(imgclip)
#         txt_cplis.append(txt_clip)

#     # print(cplis)

#     videocct = concatenate_videoclips(image_clips)
#     videocct = CompositeVideoClip([videocct, *txt_cplis])

#     #保存结果
#     videocct.write_videofile('./output.mp4', fps=12, audio_codec='aac')


# # from moviepy.editor import *
 
# # if __name__ == '__main__':
# #     # 读取视频
# #     clip = VideoFileClip("baidu/最美风景/1.jpg").set_duration(10)
# #     # 文字视频
# #     text_clip: TextClip = TextClip("显示中文，不仅仅是English", font='hwfs.ttf', fontsize=70, color='white')
 
# #     # text_clip = text_clip.set_position("center").set_duration(10)
# #     text_clip = text_clip.set_position((10,20)).set_duration(10)
 
# #     # 合成视频
# #     composite_video_clip = concatenate_videoclips([clip, text_clip])
 
# #     # 导出视频
# #     composite_video_clip.write_videofile("2.mp4")

from moviepy.editor import *
from os import *
from re import *
import math

def pic_to_mp4(pic_dir, title, h_flag):
    """
    图片转视频
    """
    #图片集,语音集,视频集,字幕集
    pic_files = []
    mp3_clips = []
    image_clips = []
    txt_clips = []

    #字幕开始时间
    time_pos = 0

    #图片列表
    pic_files = [pic_dir+"/"+fn for fn in listdir(pic_dir) if fn.endswith('.jpg')]
    pic_files.sort(key=lambda fn:int(findall(r'\d+', fn)[-1]))

    print(pic_files)

    # #片头
    # mp3_list = []
    # for f in listdir('./data/mp3/'):
    #     mp3_list.append(path.splitext(f)[0])

    # if title not in mp3_list:
    #     print('正在处理title...[{}]'.format(title))
    #     text_to_mp3_by_api(title)
    # else:
    #     print('跳过...[{}]'.format(title))

    # mp3_path = './data/mp3/{}.mp3'.format(title)
    # mp3_clip = AudioFileClip(mp3_path)
    # mp3_clips.append(mp3_clip)

    duration=2
    txt_clip =  (TextClip(title, fontsize=120,
                        font='hwfs.ttf',
                        method='label',
                        align='center', color='red')
                    .set_position('center')
                    .set_duration(duration).set_start(time_pos))

    txt_clips.append(txt_clip)
    time_pos = time_pos + duration
    image_clips.append(ImageClip(pic_files[5], duration=duration))

    #正剧
    num = 0
    for pic in pic_files:
        print(pic)
        txt = str(num)
        num = num+1
        #音频处理
        # mp3_path = './data/mp3/{}.mp3'.format(txt)
        # mp3_clip = AudioFileClip(mp3_path)
        # mp3_clips.append(mp3_clip)

        #字幕处理
        mul = math.ceil(len(txt)/14)
        per_duration = duration/mul
        for i in range(mul):
            s_pos = i*14
            e_pos = s_pos + 14
            if e_pos > len(txt):
                e_pos = len(txt)
            #print(i,s_pos,e_pos)
            #print(txt[s_pos:e_pos])
            txt_clip =  (TextClip(txt[s_pos:e_pos], fontsize=60,
                        font='hwfs.ttf', size=(900, 200),
                        align='center', color='red')
                    .set_position('bottom')
                    .set_duration(per_duration).set_start(time_pos+i*per_duration))
            txt_clips.append(txt_clip)

        #视频处理
        image_clips.append(ImageClip(pic, duration=duration))

        #字幕时间处理
        time_pos = time_pos + duration

    #合成视频
    videocct = concatenate_videoclips(image_clips)

    #语音合成
    # mp3cct =  concatenate_audioclips(mp3_clips)
    # mp3cct.volumex(1.0)

    # #背景音乐
    # bgm_files = [join('./data/bgm/',fn) for fn in listdir('./data/bgm/') if fn.endswith('.mp3')]
    # cur = random.randrange(len(bgm_files)-1)
    # print(bgm_files[cur])

    # #音量
    # bgm_clip = AudioFileClip(bgm_files[cur]).volumex(0.05)
    # bgm_loop = afx.audio_loop(bgm_clip, duration=mp3cct.duration)

    # #最终语音
    # mp3_final = CompositeAudioClip([mp3cct, bgm_loop])

    #添加字幕
    videocct =  CompositeVideoClip([videocct, *txt_clips])

    #添加语音
    # videocct = videocct.set_audio(mp3_final)

    #保存结果
    videocct.write_videofile('./{}.mp4'.format(title), fps=24)

    #竖屏转换成横屏
    # if h_flag:
    #     v_to_h('./output/{}.mp4'.format(title))

    print('完成')

pic_to_mp4("./baidu/最美风景", "最美风景", 0)