print('successfully import arrange')
def manual_arrange():
    import tkinter as t
    from tkinter.simpledialog import askstring
    app=t.Tk()
    app.withdraw()
    global ram_size
    ram_size=askstring('ram',prompt='arrange ram for your virtual machine(KB)')
    app.destroy()
    if ram_size == '' or None:
        assert()
    if ram_size != '' or None:
        pass
def create_RAM(ram_size):
    pass
