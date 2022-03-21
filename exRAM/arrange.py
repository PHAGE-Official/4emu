print('successfully import arrange')
def manual_arrange():
    import tkinter as t
    from tkinter.simpledialog import askstring
    app=t.Tk()
    app.withdraw()
    ram_size=askstring('ram',prompt='arrange ram for your virtual machine(KB)')
    app.destroy()
    if ram_size == '':
        print('This is an invalid value')
    if ram_size != '' or None:
        print('You have arrange',int(ram_size),'KB for your VM')
