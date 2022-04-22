import os


def updateFile(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    import os
    file_data = ""
    with open(file, "r+", encoding="ANSI") as f:
        for line in f:
            line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)

i = 1
j = 32
while True:

    file = "setip.cmd"
    old_str = f"rand_num={i}"
    new_str = f"rand_num={i + 1}"
    old_strs = f"rand_nu={j}"
    new_strs = f"rand_nu={j + 1}"
    old_str1 = "rand_num=255"
    new_str1 = "rand_num=1"
    i += 1
    updateFile(file, old_str, new_str)
    print(i)
    if i > 254:
        updateFile(file, old_strs, new_strs)
        j += 1
        if j > 38:
            pass
        updateFile(file, old_str1, new_str1)
        i = 0



# # old_str =
# def replacefile(file, old_str, new_str):
#     data = ''
#     with open(file, 'r+') as f:
#         for line in f.readlines():
#             if line.find('Server') == 0:
#                 line = 'Server=%s' % new_str + '\n'
#                 data += line
#
#     with open('zhai.conf', 'r+') as f:
#
#         f.writelines(data)
# """
# import os
#
# def alter(file,old_str,new_str):
# # :param file: 文件路径
# #
# # :param old_str: 需要替换的字符串
# #
# # :param new_str: 替换的字符串
#     with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
#
#     for lin in f1:
#
#         print(lin)
#
#         if old_str in lin:
#
#             lin = lin.replace(old_str, new_str)
#
#             f2.write(lin)
#
#             os.remove(file)
#
#             os.rename("%s.bak" % file, file)
#
#             alter(r"E:\abc\1.txt", "a", "b")#将"E:\abc"路径的1.txt文件把所有的a改为b
# """
# def replacefile(file, old_str, new_str):
#     data = ''
#     with open(file, 'r+', encoding="ANSI") as f:
#         for line in f.readlines():
#             if line.find('Server') == 0:
#                 line = 'Server=%s' % (new_str,) + '\n'
#                 data += line
#
#     # with open('setip.cmd', 'r+') as f:
#     #
#     #     f.writelines(data)
#
#
# i = 1
# j = 32
# while True:
#     file = "setip.cmd"
#     old_str = f"rand_num={i}"
#     new_str = i + 1
#     old_strs = f"rand_nu={j}"
#     new_strs = f"rand_nu={j + 1}"
#     replacefile(file, old_str, new_str)
#     i += 1
#     print(i)
#     if i > 254:
#         i = 0
#         replacefile(file, old_strs, new_strs)
#         j += 1
#     if j > 38:
#         break
