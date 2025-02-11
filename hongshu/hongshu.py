from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image_path, text, position, font_size=20, font_color=(0, 0, 0)):
    # 打开图片
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    # 指定字体，这里使用系统默认字体，你可以根据需要更换为其他字体文件路径
    font = ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc /System/Library/Fonts/STHeiti Medium.ttc", font_size)
    # 将文字添加到图片上
    draw.text(position, text, font=font, fill=font_color)
    return image

# 示例使用
if __name__ == "__main__":
    # 图片路径
    image_path = "bg.png"

    # 要添加的文案列表
    text_list = ["文案1 ： 先喂母乳，让宝宝充分吸吮，尽量排空乳房，刺激乳汁分泌。", "文案2 ：母乳不足时再补充奶粉，注意观察宝宝的食量，避免过度喂养。", "文案3： 每次喂养的时间和量要相对固定，帮助宝宝建立规律的饮食习惯"]

    # 文字要放置的位置，这里假设每个文案都放在相同位置
    position = (100, 100)
    # 字体大小
    font_size = 40
    # 字体颜色，这里使用黑色
    font_color = (255, 215, 0)
    # 遍历文案列表，为每个文案生成一张新图片
    for index, text in enumerate(text_list):
        # 调用函数添加文字
        new_image = add_text_to_image(image_path, text, position, font_size, font_color)
        # 保存处理后的图片，文件名根据文案索引命名
        output_image_path = f"output_image_{index + 1}.jpg"
        new_image.save(output_image_path)
        print(f"图片处理完成，已保存为 {output_image_path}")