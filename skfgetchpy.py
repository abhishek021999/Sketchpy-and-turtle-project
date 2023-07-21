
def local():
    # this is first sketch 
    # pic uploaded from local drive

    import sketchpy
    from sketchpy import canvas
    obj=canvas.sketch_from_image("C:/Users/Abhis/Downloads/WhatsApp Image 2023-05-25 at 9.32.40 AM.jpeg")
    obj.draw(threshold=120)

def apj():
     # this is 2nd sketchpy image
     from sketchpy import library as l
     apjabdul_kalam=l.apj()
     apjabdul_kalam.draw()

def flag():
    #  this is 3rd sketchpy image
    from sketchpy import library
    myObject = library.flag()
    myObject.draw()

     
select_option=int(input("press->1 for downloaded pic sketch or press->2 for apj sketch or press->3 for flag sketch  "))
if select_option==1:
    local()
if select_option==2:
    apj()
if select_option==3:
    flag()        












    



