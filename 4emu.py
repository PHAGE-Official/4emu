import tkinter as t
top=t.Tk()
#variable
running_file='Boot'
ax=bx=cx=dx=0
cs=0    #the maxium value is 0b11
es=ds=ss=0b0000
ip=sp=bp=bi=0b0000
lax=lbx=lcx=ldx=None
lcs=lds=lss=les=None
lip=lbp=lsp=lbi=None
lpr=None
powerstate=1



#set the window attributes
top.title('4emu      -'+running_file)
top.geometry('800x600+400+200')
top.configure(bg='#cccccc')
top.attributes('-alpha',0.90)
top.resizable(0,0)

#default UI
l=t.Label(text='Command:',fg='#ffffff',bg='#f05400',width=10,anchor='w')
l.place(x=160,y=0)


#screen class
class monitor:
    def reg():
        global lax,lcx,lbx,ldx
        if lax != None and lbx != None and cx != None and ldx != None:
            lax.destroy()
            lbx.destroy()
            lcx.destroy()
            ldx.destroy()
        lax=t.Label(text=('AX:',bin(ax)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lax.place(x=0,y=0)
        lbx=t.Label(text=('BX:',bin(bx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lbx.place(x=0,y=25)
        lcx=t.Label(text=('CX:',bin(cx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lcx.place(x=0,y=50)
        ldx=t.Label(text=('DX:',bin(dx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        ldx.place(x=0,y=75)
    def seg_reg():
        global lcs,lds,lss,les
        if lcs != None and lds != None and lss != None and les!=None:
            lcs.destroy()
            lds.destroy()
            lss.destroy()
            les.destroy()
        lcs=t.Label(text=('CS:',bin(cs)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lcs.place(x=0,y=100)
        lds=t.Label(text=('DS:',bin(ds)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lds.place(x=0,y=125)
        lss=t.Label(text=('ES:',bin(es)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lss.place(x=0,y=150)
        les=t.Label(text=('SS:',bin(ss)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        les.place(x=0,y=175)
    def ptr_reg():
        global lip,lsp,lbp,lbi
        if lip != None and lsp != None and lbp != None and lbi != None:
            lip.destroy()
            lsp.destroy()
            lbp.destroy()
            lbi.destroy()
        lip=t.Label(text=('IP:',bin(ip)),fg='#000000',bg='#ffffff',anchor='w',width=10)
        lip.place(x=80,y=0)
        lsp=t.Label(text=('SP:',bin(sp)),fg='#000000',bg='#ffffff',anchor='w',width=10)
        lsp.place(x=80,y=25)
        lbp=t.Label(text=('BP:',bin(bp)),fg='#ffff00',bg='#0000ff',anchor='w',width=10)
        lbp.place(x=80,y=50)
        lbi=t.Label(text=('BI:',bin(bi)),fg='#ffff00',bg='#0000ff',anchor='w',width=10)
        lbi.place(x=80,y=75)
    def vga_opt():
        global w
        w=t.Canvas(width=320,height=240,bg='#000000')
        w.place(x=470,y=0)
        w.create_text(5,0,text='VPS is loading...\nBIOS info:\n|-CPU:Virtual 4010\n|-RAM:default\n|-ROM:default',tag='boot',fill='#0cff00',anchor='nw')
        monitor.reg()
        monitor.seg_reg()
        monitor.ptr_reg()
    def mech(extension):
        global seg,cs,ip
        me_x=600
        me_y=100
        if extension == 0:
            ip=ip-8
            value=str(seg[cs*4+ip])
            for i in range(0,7):
                ip=ip+1
                value=value+str(seg[cs*4+ip])
            l=t.Label(text=value,width=10,anchor='w')
            l.place(x=240)
#command class
class cmd:
    def mov(reg,fig):
        global ax,cx,seg,cs,ip
        if reg=='ax':
            ax=fig
            reg_flag=0
            reg_de=0
        if reg=='bx':
            bx=fig
            reg_flag=0
            reg_de=1
        if reg=='cx':
            cx=fig
            reg_flag=1
            reg_de=0
        if reg=='dx':
            dx=fig
            reg_flag=1
            reg_de=1
        monitor.reg()

#------------------------------------------------translate mech-------------------------------------
        for i in range(0,2):
            seg[cs*4+ip]=0  #mov的开头标志位为00
            ip=ip+1         #下一位
        seg[cs*4+ip]=reg_flag
        ip=ip+1
        seg[cs*4+ip]=reg_de
        #第三位为寄存器类
        #the third bit means the sort of register
        #0代表ax或bx,1代表cx或dx
        #0 means ax or bx while 1 means cx or dx
        #第四位表示具体寄存器
        
        if fig>15:
            assert()
            #fig < 0b11
        ip=ip+4
        for i in range(0,4):
            fig_m=fig%2     #取余,二进制高位   mod and the result is binary high bit
            fig=int(fig/2)      #向下取整          round down
            seg[cs*4+ip]=fig_m
            ip=ip-1
        ip=ip+5
        monitor.mech(0)


    def movs(seg_reg,reg):
        global cs,ds,es,ss,seg,ip
        if seg_reg == 'cs':
            if reg == 'ax':
                fig=ax
                cs=ax
            if reg == 'bx':
                fig=bx
                cs=bx
            if reg == 'cx':
                fig=cx
                cs=cx
            if reg == 'dx':
                fig=dx
                cs=dx
            reg_flag=0
            reg_de=0
        if seg_reg == 'ds':
            if reg == 'ax':
                fig=ax
                ds=ax
            if reg == 'bx':
                fig=bx
                ds=bx
            if reg == 'cx':
                fig=cx
                ds=cx
            if reg == 'dx':
                fig=dx
                ds=dx
            reg_flag=0
            reg_de=1
        if seg_reg == 'ss':
            if reg == 'ax':
                fig=ax
                ss=ax
            if reg == 'bx':
                fig=bx
                ss=bx
            if reg == 'cx':
                fig=cx
                ss=cx
            if reg == 'dx':
                fig=dx
                ss=dx
            reg_flag=1
            reg_de=0
        if seg_reg == 'es':
            if reg == 'ax':
                fig=ax
                es=ax
            if reg == 'bx':
                fig=bx
                es=bx
            if reg == 'cx':
                fig=cx
                es=cx
            if reg == 'dx':
                fig=dx
                es=dx
            reg_flag=1
            reg_de=1
        monitor.seg_reg()
#------------------------------------------------translate mech-------------------------------------        
        seg[cs*4+ip]=0  #movs的开头标志位为01
        ip=ip+1
        seg[cs*4+ip]=1
        ip=ip+1
        seg[cs*4+ip]=reg_flag
        ip=ip+1
        seg[cs*4+ip]=reg_de
        #从第五位开始为立即数
        #from the 5th bit is immeidate data
        if fig>15:
            assert()
        ip=ip+4
        for i in range(0,4):
            fig_m=fig%2
            fig=int(fig/2)
            seg[cs*4+ip]=fig_m
            ip=ip-1
        ip=ip+5



    def movp(ptr_reg,fig):
        global ip,bp,sp,bi
        if ptr_reg == 'ip':
            ip = fig
        monitor.ptr_reg()
        print('mov',ptr_reg,bin(fig))
    def add(reg,fig):
        global ax,cx
        if reg == 'ax':
            ax=ax+fig
        if reg == 'cx':
            cx=cx+fig
        monitor.reg()
    def jmp(seg_reg,fig=0,reg=0):
        global cs,ip,adr
        adr=cs*4+ip
        print('jump to',adr)
        
#CPU class
class cpu:
    def read():
        if mechcode == '00':
            print('this is the mov command')
        elif mechcode == '01':
            print('this is movs command')
        elif mechcode == '10':
            pass
        #注意:以11开头的标志位不代表任何指令只代表此段数据将扩展为16位指令
    def write():
        pass



#RAM classs
class rom():
    def bios(ip):
        global cs,seg
        #create a virtual random access memory
        #最大地址为15, 0b11 x 4 +0b11
        seg=[0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0,0,0,0,0,
             0]
        if cs*4+ip > 16:
            #reset
            cs=0
            ip=0
        adr=cs*4+ip
    def check():
        global cs,ip,adr,seg
        adr = cs * 4 + ip
        print(adr)


        
class boot:
    def bios():
        cmd.mov('ax',2)
        cmd.mov('cx',9)
        cmd.movs('ds','cx')
        cmd.mov('bx',12)
        rom.check()



class user:
    def ramarrange():
        from exRAM import arrange
        arrange.manual_arrange()
        arrange.create_RAM(12)



class hotkey():
    #This class define a large sum of functions of hotkey such as power off/power on
    def power():
        global powerstate,w,ax,cx
        global es,ds,ss,cs,ip,bp,sp,bi
        if powerstate == 1:
            powerstate =0
            ax=cx=0
            es=ds=ss=cs=0
            ip=bp=sp=bi=0
            monitor.reg()
            monitor.seg_reg()
            monitor.ptr_reg()
            w.delete('all')
        else:
            powerstate = 1
            bus()
    def mute():
        pass
        # we will add a 4-bit sb later
b=t.Button(text='power',width=10,command=hotkey.power)
b.place(x=710,y=250)
b1=t.Button(text='mute',width=10,command=hotkey.mute)
b1.place(x=470,y=250)

class program:
    def load():
        import complier.complier as c
        global running_file
        running_file=c.openfile()#执行函数同时接收返回值
        top.title('4emu      -'+running_file)
        #ram.load()
        #cpu.read()

def bus():
    rom.bios(0b1111)
    boot.bios()
    monitor.vga_opt()
    


def oscheck():
    import platform
    os=platform.system()
    if os == 'Windows':
        import soundblaster.win as sw
        sw.info()
    else:
        print('sorry your Opearting System can not use sound blaster now')
    
oscheck()
bus()


menu=t.Menu(top)

filemenu=t.Menu(menu,tearoff=0)
cfgmenu=t.Menu(menu,tearoff=0)

menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Open',command=program.load)
filemenu.add_command(label='Exit',command=exit)


menu.add_cascade(label='Config',menu=cfgmenu)
cfgmenu.add_command(label='RAM',command=user.ramarrange)

top.config(menu=menu)
top.mainloop()
