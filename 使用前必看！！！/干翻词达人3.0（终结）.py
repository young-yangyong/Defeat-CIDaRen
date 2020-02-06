import os
import json
import time

start_flag = True
answer_type = 0
select_flag = 0

print("《干翻词达人》只支持“开始学习”，不支持“继续任务”，注意！！！")
print("开始监听！！！需手动关闭正常运行的程序。")
print("答案：")
while start_flag:

    if os.path.isfile('./json/json.txt'):
        fr = open('./json/json.txt', 'r', encoding='utf-16')
        fr_str = fr.readline()
        fr.close()
        try:
            fr_json = json.loads(fr_str)
            #print(fr_json)

            for i in fr_json['data']:
                if i == 'tips' and fr_json['data'][i] is not None:

                    answer_type = fr_json['data'][i]

                    if answer_type == '选出句中划线单词词义(全部词义）' \
                            or answer_type == '听单词，选出词义（全部词义）' \
                            or answer_type == '选出与所给单词常见的搭配词' \
                            or answer_type == '选择合适的单词,补全句子（全部词义）':
                        select_flag = 1

                    if answer_type == '按正确顺序选择单词，组成正确的表达':
                        select_flag = 2

                    if answer_type == '根据中文意思，填入所缺单词（基本词义）':
                        select_flag = 3

                    break
                    # print(answer_flag, answer_type)

            if select_flag == 0:
                continue

            context = '\r'

            if select_flag == 1:
                for i in fr_json['data']['options']:
                    if i['answer']:
                        context = context + i['content'] + '; '
                print(context.ljust(40), end='')

            if select_flag == 2:
                context = context + fr_json['data']['answer_content']['answer_str'] + '; '
                print(context.ljust(40), end='')

            if select_flag == 3:
                context = context + fr_json['data']['answer_content'] + '; '
                print(context.ljust(40), end='')

        except:
            if fr_str == '':
                print("空文件！！！")
            elif fr_str[0] != '{':
                print("不是json数据！！！")
        finally:
            os.remove("./json/json.txt")
            # exit()
    else:
        time.sleep(1)
