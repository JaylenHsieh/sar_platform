#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time
import os
import matlab.engine

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("星载SAR演示平台")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')       #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.label_H = Label(self.init_window_name, text="H", width=20, height=2)
        self.label_H.grid(row=0, column=0, rowspan=1, columnspan=3)
        self.label_Wr = Label(self.init_window_name, text="Wr", width=20, height=2)
        self.label_Wr.grid(row=0, column=5, rowspan=1, columnspan=3)
        self.label_fc = Label(self.init_window_name, text="fc", width=20, height=2)
        self.label_fc.grid(row=0, column=10, rowspan=1, columnspan=3)
        self.label_Da = Label(self.init_window_name, text="Da", width=20, height=2)
        self.label_Da.grid(row=2, column=0, rowspan=1, columnspan=3)
        self.label_Dr = Label(self.init_window_name, text="Dr", width=20, height=2)
        self.label_Dr.grid(row=2, column=5, rowspan=1, columnspan=3)
        self.label_Br = Label(self.init_window_name, text="Br", width=20, height=2)
        self.label_Br.grid(row=4, column=0, rowspan=1, columnspan=3)
        self.label_Prf = Label(self.init_window_name, text="Prf", width=20, height=2)
        self.label_Prf.grid(row=4, column=5, rowspan=1, columnspan=3)
        self.label_mu = Label(self.init_window_name, text="mu", width=20, height=2)
        self.label_mu.grid(row=4, column=10, rowspan=1, columnspan=3)
        self.label_phi0_tx = Label(self.init_window_name, text="phi0_tx", width=20, height=2)
        self.label_phi0_tx.grid(row=6, column=0, rowspan=1, columnspan=3)
        self.label_phi0_rx = Label(self.init_window_name, text="phi0_rx", width=20, height=2)
        self.label_phi0_rx.grid(row=6, column=5, rowspan=1, columnspan=3)
        self.label_theta_tx = Label(self.init_window_name, text="theta_tx", width=20, height=2)
        self.label_theta_tx.grid(row=8, column=0, rowspan=1, columnspan=3)
        self.label_theta_rx = Label(self.init_window_name, text="theta_rx", width=20, height=2)
        self.label_theta_rx.grid(row=8, column=5, rowspan=1, columnspan=3)
        self.label_Vst_tx = Label(self.init_window_name, text="Vst_tx", width=20, height=2)
        self.label_Vst_tx.grid(row=10, column=0, rowspan=1, columnspan=3)
        self.label_Vst_rx = Label(self.init_window_name, text="Vst_rx", width=20, height=2)
        self.label_Vst_rx.grid(row=10, column=5, rowspan=1, columnspan=3)
        self.label_num_t = Label(self.init_window_name, text="num_t", width=20, height=2)
        self.label_num_t.grid(row=12, column=0, rowspan=1, columnspan=3)
        self.label_log = Label(self.init_window_name, text="日志打印", width=20, height=2)
        self.label_log.grid(row=14, column=0, rowspan=1, columnspan=3)
        
        #文本框
        self.Text_H = Text(self.init_window_name, width=20, height=1)
        self.Text_H.grid(row=1, column=0, rowspan=1, columnspan=3)
        self.Text_Wr = Text(self.init_window_name, width=20, height=1)
        self.Text_Wr.grid(row=1, column=5, rowspan=1, columnspan=3)
        self.Text_fc = Text(self.init_window_name, width=20, height=1)
        self.Text_fc.grid(row=1, column=10, rowspan=1, columnspan=3)
        self.Text_Da = Text(self.init_window_name, width=20, height=1)
        self.Text_Da.grid(row=3, column=0, rowspan=1, columnspan=3)
        self.Text_Dr = Text(self.init_window_name, width=20, height=1)
        self.Text_Dr.grid(row=3, column=5, rowspan=1, columnspan=3)
        self.Text_Br = Text(self.init_window_name, width=20, height=1)
        self.Text_Br.grid(row=5, column=0, rowspan=1, columnspan=3)
        self.Text_Prf = Text(self.init_window_name, width=20, height=1)
        self.Text_Prf.grid(row=5, column=5, rowspan=1, columnspan=3)
        self.Text_mu = Text(self.init_window_name, width=20, height=1)
        self.Text_mu.grid(row=5, column=10, rowspan=1, columnspan=3)
        self.Text_phi0_tx = Text(self.init_window_name, width=20, height=1)
        self.Text_phi0_tx.grid(row=7, column=0, rowspan=1, columnspan=3)
        self.Text_phi0_rx = Text(self.init_window_name, width=20, height=1)
        self.Text_phi0_rx.grid(row=7, column=5, rowspan=1, columnspan=3)
        self.Text_theta_tx = Text(self.init_window_name, width=20, height=1)
        self.Text_theta_tx.grid(row=9, column=0, rowspan=1, columnspan=3)
        self.Text_theta_rx = Text(self.init_window_name, width=20, height=1)
        self.Text_theta_rx.grid(row=9, column=5, rowspan=1, columnspan=3)
        self.Text_Vst_tx = Text(self.init_window_name, width=20, height=1)
        self.Text_Vst_tx.grid(row=11, column=0, rowspan=1, columnspan=3)
        self.Text_Vst_rx = Text(self.init_window_name, width=20, height=1)
        self.Text_Vst_rx.grid(row=11, column=5, rowspan=1, columnspan=3)
        self.Text_num_t = Text(self.init_window_name, width=20, height=1)
        self.Text_num_t.grid(row=13, column=0, rowspan=1, columnspan=3)

        
        #self.Text_result = Text(self.init_window_name, width=1, height=48)  #处理结果展示
        #self.Text_result.grid(row=1, column=20, rowspan=15, columnspan=13)
        
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=15, column=0, columnspan=10)

        #按钮
        self.Button_write_data = Button(self.init_window_name, text="写入数据", bg="lightblue", width=15,height=1,command=self.save_data)  # 调用内部方法  加()为直接调用
        self.Button_write_data.grid(row=1, column=20)
        self.Button_execute = Button(self.init_window_name, text="执行bi_sig.exe", bg="lightblue", width=15,height=1,command=self.execute_bi_sig)  # 调用内部方法  加()为直接调用
        self.Button_execute.grid(row=3, column=20)
        self.Button_execute = Button(self.init_window_name, text="执行程序bi_dcs.exe", bg="lightblue", width=15,height=1,command=self.execute_bi_dcs)  # 调用内部方法  加()为直接调用
        self.Button_execute.grid(row=5, column=20)
        self.Button_execute = Button(self.init_window_name, text="执行matlab", bg="lightblue", width=15,height=1,command=self.execute_matlab)  # 调用内部方法  加()为直接调用
        self.Button_execute.grid(row=7, column=20)

    
    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
    

    def save_data(self):
        f = open("target_param.dat", 'w')
        f.write('H='+self.Text_H.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Wr='+self.Text_Wr.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('fc='+self.Text_fc.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Da='+self.Text_Da.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Dr='+self.Text_Dr.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Br='+self.Text_Br.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Prf='+self.Text_Prf.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('mu='+self.Text_mu.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('phi0_tx='+self.Text_phi0_tx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('phi0_rx='+self.Text_phi0_rx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('theta_tx='+self.Text_theta_tx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('theta_rx='+self.Text_theta_rx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Vst_tx='+self.Text_Vst_tx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('Vst_rx='+self.Text_Vst_rx.get(1.0,END).strip().replace("\n","")+'\n')
        f.write('num_t='+self.Text_num_t.get(1.0,END).strip().replace("\n","")+'\n')
        
        
        
        print("write success")
        self.write_log_to_Text("INFO:写入数据成功")
        

    def execute_bi_sig(self):
        path = os.getcwd()+"\\bi_sig.exe"
        result = os.system(path)
        self.write_log_to_Text("INFO:bi_sig.exe运行成功")

    def execute_bi_dcs(self):
        path = os.getcwd()+"\\bi_dcs.exe"
        result = os.system(path)
        self.write_log_to_Text("INFO:bi_dcs.exe运行成功")
    
    def execute_matlab(self):
        path = os.path.abspath(os.path.join(os.getcwd, "..")) + "SAR_data\\execute_matlab.py"
        result = os.system(path)
        self.write_log_to_Text("INFO:matlab脚本运行成功")

        
    
    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()