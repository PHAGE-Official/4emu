import tkinter as t
top=t.Tk()
#variable
running_file='Boot'
ax=bx=cx=dx=0
cs=0b1111         #the maxium value is 0b1111
es=ds=ss=0
lax=lbx=lcx=ldx=None
lcs=lds=lss=les=None
#set the window attributes
top.title('4emu      -'+running_file)
top.geometry('800x600+400+200')
top.configure(bg='#cccccc')
top.attributes('-alpha',0.9)
top.resizable(0,0)
#screen class
class monitor:
    def info():
        print('Phage Virtual Monitor Version 101\nRAM:None\nROM:None\nCPU:Virtual P4010 @ 0.5 MHZ')
    def reg():
        global lax,lbx,lcx,ldx
        if lax != None and lbx != None and lcx != None and ldx!=None:
            lax.destroy()
            lbx.destroy()
            lcx.destroy()
            ldx.destroy()
        lax=t.Label(text=('AX:',hex(ax)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lax.place(x=0,y=0)
        lbx=t.Label(text=('BX:',hex(bx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lbx.place(x=0,y=25)
        lcx=t.Label(text=('CX:',hex(cx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lcx.place(x=0,y=50)
        ldx=t.Label(text=('BX:',hex(bx)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        ldx.place(x=0,y=75)
    def seg_reg():
        global lcs,lds,lss,les
        if lcs != None and lds != None and lss != None and les!=None:
            lcs.destroy()
            lds.destroy()
            lss.destroy()
            les.destroy()
        lcs=t.Label(text=('CS:',hex(cs)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lcs.place(x=0,y=100)
        lds=t.Label(text=('DS:',hex(ds)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lds.place(x=0,y=125)
        lss=t.Label(text=('ES:',hex(es)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        lss.place(x=0,y=150)
        les=t.Label(text=('SS:',hex(ss)),fg='#ffffff',bg='#000000',anchor='w',width=10)
        les.place(x=0,y=175)
#command class
class cmd:
    def mov(reg,fig):
        global ax,bx,cx,dx
        if reg=='ax':
            ax=fig
        if reg=='bx':
            bx=fig
        if reg=='cx':
            cx=fig
        if reg=='dx':
            dx=fig
        monitor.reg()
        print('mov',reg,hex(fig))
    def movs(seg_reg,reg):
        global cs,ds,es,ss
        if seg_reg == 'cs':
            if reg == 'ax':
                cs=ax
            if reg == 'bx':
                cs=bx
            if reg == 'cx':
                cs=cx
            if reg == 'dx':
                cs=dx
        if seg_reg == 'ds':
            if reg == 'ax':
                ds=ax
            if reg == 'bx':
                ds=bx
            if reg == 'cx':
                ds=cx
            if reg == 'dx':
                ds=dx
        monitor.seg_reg()
        print('mov',seg_reg,reg)
#CPU class
class cpu:
    def self_check():
        print('CS set as',hex(cs))
    def read():
        pass
#RAM classs
class ram():
    def segment(ip):
        global cs
        #create a virtual random access memory
        #最大地址为75, 0x0f x 0x04 +0x0f
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
        if cs*4+ip > 75:
            print('overflow')   #overflow alert,溢出警告
            #reset
            cs=0
            ip=0
        adr=cs*4+ip
        print('point at number',adr,'adress')
        print(seg[adr])
class boot:
    def bios():
        cmd.mov('ax',2)
        cmd.movs('cs','ax')
        cmd.movs('ds','ax')
monitor.info()
cpu.self_check()
ram.segment(0b1111)
boot.bios()
top.mainloop()
