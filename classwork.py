'''
@ 项目名：homework
@ 文件名：classwork.py
@ 创建日期：2025/3/17
@ 作者：2024215290
@ 创建时间：13:00
'''
import math

#每次下落到反弹所需总时间 下落+反弹为一个周期
def function(h, g = 9.8):
    t_down = math.sqrt(2*h/g) #最高点落下时间
    t_up = math.sqrt(h/g)     #反弹到一半时间
    t_tol = t_down + t_up     #总时间
    return t_tol

t_sum = 0  #总时间
h_sum = 0  #总路程
h = 100    #初始高度
n = 10     #掉落次数
for i in range(n):
    t_sum += function(h)   #累加每一个周期所需时间
    h_sum += h*3/2         #累加每一个周期运动距离
    h /= 2                 #每次反弹高度减半

print("第{}次掉落反弹了{:.4f}米，此时球一共运动{:.4f}米，运动了{:.4f}秒".format(n, h, h_sum, t_sum))
#输出结果：第10次掉落反弹了0.0977米，此时球一共运动299.7070米，运动了25.5073秒