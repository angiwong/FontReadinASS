import os

# 获取目录下的文件
def file_name(file_dir):
	for root, dirs, files in os.walk(file_dir):
		return (files)

#字幕文件目录
file_dir = "D:\\Anime\\Try"


file_list = file_name(file_dir)
font_list = list()

#   print(file_list)

for name in file_list:
    
	file_path = file_dir + "/" + name
	fp = open(file_path, 'r', encoding='UTF-8')
	file_data = fp.readlines()
	fp.close()

	for line in file_data:
		string_find1 = -1
		string_find2 = -1
		string_find1 = line.find('Style:')
		string_find2 = line.find('\\fn')

		if string_find1 != -1:
			temp_str = line.split(',')
			
			if len(temp_str) > 10:
				font_list.append(temp_str[1])

		if string_find2 != -1:
			font_string_1 = line.split('\\fn')[1]
			font_string_2 = font_string_1.split('}')[0]

			k = font_string_2.find('\\')

			if k != -1:
				font_list.append(font_string_2.split('\\')[0])
			else:
				font_list.append(font_string_2)

final = list(set(font_list))

print(final)

input("Press <enter> to finish task")

