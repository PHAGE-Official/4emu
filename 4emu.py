import tkinter as t
top=t.Tk()
#variable
running_file='Boot'
ax=bx=cx=dx=0
cs=0b1111         #the maxium value is 0b1111
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
        w.create_text(5,0,text='VPS is loading...',tag='boot',fill='#ff0000',anchor='nw')



#command class
class cmd:
    def mov(reg,fig):
        global ax,bx,cx,dx,seg,cs,ip
        if reg=='ax':
            ax=fig
            reg_flag=0
        if reg=='bx':
            bx=fig
            reg_flag=0
        if reg=='cx':
            cx=fig
            reg_flag=1
        if reg=='dx':
            dx=fig
            reg_flag=1
        monitor.reg()
        seg[cs*4+ip]=1
        ip=ip+1
        seg[cs*4+ip]=reg_flag
        print('mov',reg,bin(fig))
        print('bios rom:',seg)
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
    def movp(ptr_reg,fig):
        global ip,bp,sp,bi
        if ptr_reg == 'ip':
            ip = fig
            print(seg[cs*4+ip])
        monitor.ptr_reg()
        print('mov',ptr_reg,bin(fig))
    def add(reg,fig):
        global ax,bx,cx,dx
        if reg == 'ax':
            ax=ax+fig
            print('ax is',bin(ax))
        if reg == 'bx':
            bx=bx+fig
        if reg == 'cx':
            cx=cx+fig
        if reg == 'dx':
            dx=dx+fig
        monitor.reg()
    def jmp():
        pass
        
#CPU class
class cpu:
    def self_check():
        print('CS set as',bin(cs))
    def read():
        pass
    def write():
        pass
        


#RAM classs
class rom():
    def bios(ip):
        global cs,seg
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
            print('overflow')
            #reset
            cs=0
            ip=0
        adr=cs*4+ip
        print('point at number',adr,'adress')
        print(seg[adr])
        print('default RAM:',len(seg),'bit')
    def check():
        global cs,ip,adr,seg
        adr = cs * 4 + ip
        print('point at number',adr,'adress')
        print('data=',seg[adr])


        
class boot:
    def bios():
        cmd.mov('ax',2)
        cmd.movs('cs','ax')
        cmd.movp('ip',3)
        rom.check()
        cmd.mov('cx',5)
        cmd.add('ax',10)
        cmd.jmp()



class user:
    def ramarrange():
        from exRAM import arrange
        #this is a new module!!!!🦾🦾🦾
        arrange.manual_arrange()



class hotkey():
    #This class define a large sum of functions of hotkey such as power off/power on
    #later will add VGA on/off
    def power():
        global powerstate,w,ax,bx,cx,dx
        global es,ds,ss,cs,ip,bp,sp,bi
        if powerstate == 1:
            print('power off')
            powerstate =0
            ax=bx=cx=dx=0
            es=ds=ss=cs=0
            ip=bp=sp=bi=0
            monitor.reg()
            monitor.seg_reg()
            monitor.ptr_reg()
            w.delete('all')
        else:
            print('power on')
            powerstate = 1
            bus()
b=t.Button(text='power',width=10,command=hotkey.power)
b.place(x=710,y=250)



def bus():
    monitor.info()
    cpu.self_check()
    rom.bios(0b1111)
    boot.bios()
    monitor.vga_opt()
    user.ramarrange()
bus()
top.mainloop()
