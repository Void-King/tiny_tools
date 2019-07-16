# pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple
import pyautogui as pag
import time
import re
import sys
import msvcrt
def pstfx():
    pst = re.findall('\d+', str(pag.position()))
    pst[0] = int (pst[0])
    pst[1] = int (pst[1])
    return pst

def bAndr(i, pst):
    print ('\n第' + str(i+1) + '个')
    pag.click(pst[0], pst[1])
    time.sleep(1)
    for i in range(0,200):
        time.sleep(1)
        if i % 10 == 0:
            pag.scroll(-100)
        sys.stdout.write('\r正在观看 还有' + str(199-i) + '秒   ')
        sys.stdout.flush()
    pag.click(pst[0]-295, pst[1]-508)
    time.sleep(1)
    pag.moveTo(pst[0], pst[1])

def rAndr(i, pst):
    print ('\n第' + str(i+1) + '个')
    pag.click(pst[0], pst[1])
    time.sleep(1)
    for i in range(0,130):
        time.sleep(1)
        if i % 10 == 0:
            pag.scroll(-100)
        sys.stdout.write('\r正在阅读 还有' + str(129-i) + '秒   ')
        sys.stdout.flush()
    pag.click(pst[0]-411, pst[1]-402)
    time.sleep(1)
    pag.moveTo(pst[0], pst[1])

if __name__ == "__main__":
    # print (pag.position())
    time.sleep(5)
    pag.hotkey('alt', 'tab')
    time.sleep(0.5)
    pag.moveTo(1168, 979)
    # input ('请将鼠标放到界面右下角"我的"上面，不要点击鼠标，在键盘按回车继续')
    input ('确认app界面打开后，按回车继续（请勿移动鼠标！！！）')
    time.sleep(0.5)
    pag.moveTo(1168, 979)
    time.sleep(0.5)
    pst = pstfx()
    print('坐标获取成功: (' + str(pst[0]) + \
        ','+str(pst[1]) + ')\n\n切换到"试听学习"')
    
    # 观看视频
    pag.click(pst[0]-108, pst[1])
    time.sleep(2)
    pst[0] = pst[0] - 137
    pst[1] = pst[1] - 334
    for i in range(0,8):
        pag.moveTo(pst[0], pst[1])
        img = pag.screenshot()
        if pag.pixelMatchesColor(pst[0], pst[1], (255,255,255)):
            bAndr(i, pst)
            pag.dragTo(pst[0], pst[1] - 158, duration=2)
        else:# 非常规排布视频
            bAndr(i, pst)
            pag.dragTo(pst[0], pst[1] - 390, duration=4)
        time.sleep(1)
    time.sleep(1)
    # 阅读文章
    pst[0] = pst[0] + 137
    pst[1] = pst[1] + 334
    pag.click(pst[0]-210, pst[1])
    time.sleep(1)
    pag.click(pst[0]-376, pst[1]-802)
    print('\n\n切换到"学习"-"要闻"')
    time.sleep(1)
    pst[0] = pst[0] - 32
    pst[1] = pst[1] - 451
    pag.moveTo(pst[0], pst[1])
    time.sleep(1)
    for i in range(0,8):
        pag.moveTo(pst[0], pst[1])
        img = pag.screenshot()
        if pag.pixelMatchesColor(pst[0], pst[1], (255,255,255)):
            if pag.pixelMatchesColor(pst[0], pst[1]+40, (255,255,255)):
                rAndr(i, pst)
                pag.dragTo(pst[0], pst[1] - 110, duration=1.5)
            else:
                if pag.pixelMatchesColor(pst[0], pst[1]+144, (255,255,255)):
                    rAndr(i, pst)
                    pag.dragTo(pst[0], pst[1] - 250, duration=2.5)
                else:
                    rAndr(i, pst)
                    pag.dragTo(pst[0], pst[1] - 410, duration=4)
        else:
            rAndr(i, pst)
            pag.dragTo(pst[0], pst[1] - 158, duration=1.8)
        # elif pag.pixelMatchesColor(pst[0], pst[1], (255,255,255)):
    print ('\n\n完成，按任意键退出')
    msvcrt.getch()