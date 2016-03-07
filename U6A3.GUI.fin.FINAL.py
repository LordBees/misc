from tkinter import *
import time
import datetime##import nessecary libraries

root = Tk()##instancing the tkinter class 
root.geometry('470x320')##sets window dimensions
root.title('room painter')##sets room title
##functions/proc##
extraroomspace=[list(),list()]##global lists for height and width of roomspace 
datasnap = []## global variable used between functions so global
BOOL_undercoat = IntVar()##instancing the intvar class for use with a integer in tkinter it is interpreted as a boolean with either 1 or 0 
def getpaintingprice():
    global datasnap
    extra_roomwin_height = 0.0##these variablews used to temporarily store the extra height and width of the addiotional space
    extra_roomwin_width = 0.0
    
    
    try:
    #if 1:
        if len (LISTBOX_s_price.curselection())== 0: ##data input check
            print('ERROR paintband not selected!')
        elif len (ENTRY_room_height.get()) == 0:##not in range(doesnt exist)
            print('please fill in height for room')
        elif len (ENTRY_room_width01.get()) == 0:
            print('please fill in height for first wall') 
        elif len (ENTRY_room_width02.get()) == 0:
            print('please fill in height for second wall')
        elif len (ENTRY_room_width03.get()) == 0:
            print('please fill in height for third wall')
        elif len (ENTRY_room_width04.get()) == 0:
            print('please fill in height for fourth wall')
        else:##if data exists get it from the boxes 
            paint_band   = float(LISTBOX_s_price.get(LISTBOX_s_price.curselection(),last=None).strip('£'))
            room_height  = float(ENTRY_room_height.get())
            room_width01 = float(ENTRY_room_width01.get())
            room_width02 = float(ENTRY_room_width02.get())
            room_width03 = float(ENTRY_room_width03.get())
            room_width04 = float(ENTRY_room_width04.get())
            #if paint_band == None:
            
            if not (room_height  >= 2.5 and room_height <= 6):##not in range
                print('invalid height supplied for room\n please input betweeen 2.5 and 6 m') ##data validation of inputs 
            elif not (room_width01 >= 1   and room_width01 <= 25):
                print('invalid height supplied for first wall\n please input betweeen 1 and 25 m') 
            elif not (room_width02 >= 1   and room_width02 <= 25):
                print('invalid height supplied for second wall\n please input betweeen 1 and 25 m')
            elif not (room_width03 >= 1   and room_width03 <= 25):
                print('invalid height supplied for third wall\n please input betweeen 1 and 25 m')
            elif not (room_width04 >= 1   and room_width04 <= 25):
                print('invalid height supplied for fourth wall\n please input betweeen 1 and 25 m')
            else:
                ##actual maths##
                sqm_room = room_height*(room_width01+room_width02+room_width03+room_width04)##adds together room 1-4 using Height*(sum of rooms width)
                
                for x in range (len(extraroomspace[0])):
                    extra_roomwin_height +=extraroomspace[0][x]##adds together additional roomspace height and width seperately    
                    extra_roomwin_width  +=extraroomspace[1][x]

                #for x in LISTBOX_addit_RoomWin:
                for x in LISTBOX_addit_RoomWin.get(0,last= LISTBOX_addit_RoomWin.size()):##for each list entry in listbox
                    pairf = x.split(',')
                    extra_roomwin_height += float(pairf[0])
                    extra_roomwin_width += float(pairf[1])
                    #print('final = H,W',extra_roomwin_height,extra_roomwin_width)


                            
                                
                
                
                sqm_roomwin = extra_roomwin_height*extra_roomwin_width# square meters of additional space to subtract

                sqm_total = sqm_room-sqm_roomwin #subtracts additional roomspace from  total roomspace

                if  BOOL_undercoat.get()== 1:
                    sqm_paintercost = (paint_band+0.45)*sqm_total #(paint cost per SQM+0.45p for undercoat)*total area
                else:
                    sqm_paintercost = paint_band*sqm_total #paint cost per SQM*total area
                ##end##
                LABEL_room_SQm_result.config(text = str(sqm_room)+'sqm')
                LABEL_WindowDoor_result.config(text = str(sqm_roomwin)+'sqm')         ##update labels to show results
                LABEL_SQmtotal_result.config(text = str(sqm_total)+'sqm')
                LABEL_paintcosttotal_result.config(text = '£'+str(sqm_paintercost))
                datasnap = ['square meters of walls:   '+str(sqm_room)+'sqm','window space to subtract: '+str(sqm_roomwin)+'sqm','actual paintable area:    '+str(sqm_total)+'sqm','cost to paint room :      £'+str(sqm_paintercost),'paint band:               £'+str(paint_band)+' per sqm']
                #print(carpet_band,carpet_height,carpet_width,',',fittingcost,carpetcost,totalcost)
    except:
        print('ERROR unhandled exception')##catch all unknown errors to prevent crashing

def addroomspace():##adds values to listbox
    #sel = int(LISTBOX_addit_RoomWin.get(LISTBOX_addit_RoomWin.curselection(),last=None).strip('m'))
    global LISTBOX_addit_RoomWin
    if len(ENTRY_addit_height.get()) == 0:## if box for additional height is blank(zero is an invalid value anyway)
        print('invalid height entry')
    elif len(ENTRY_addit_width.get())== 0:## if box for additional width is blank(zero is an invalid value anyway)
        print('invalid width entry')
    else:
        height_addit = ENTRY_addit_height.get()##get the two  items from the additional height and width boxes
        width_addit  = ENTRY_addit_width.get()###
        LISTBOX_addit_RoomWin.insert(END,height_addit+','+width_addit)##append to listbox list and insert into array 
        #reset to blank
    
def deleteroomspace():##deletes listbox values
    if len(LISTBOX_addit_RoomWin.curselection()) == 0 :##if no entry clicked on the listbox
        print('no value selected to remove!')
    else:
        LISTBOX_addit_RoomWin.delete(LISTBOX_addit_RoomWin.curselection(),last=None )## find the element in the listbox array with the index of the cursor
def savereciept():
    global datasnap
    #header = ['Painting and Decorating R Us\n','2 Main Street\n','Devon\n','PL5 3TL\n','*********']
    reciept = ['Painting and Decorating R Us\n','2 Main Street\n','Devon\n','PL5 3TL\n','*********']##base strings for printing into the reciept file
    for line in datasnap:
        reciept.append(line)
    #for line in reciept:
        #print(line)
    #input('HALT!')
    f = open(str(time.strftime("-DATE %d,%m,%Y -TIME %H.%M.%S"))+'.txt','w')##uses the time library to print the file name as a date followed by time as a.txt file
    for line in reciept:
        f.write(line+'\n')
    f.close()
    print('reciept printed!')
##end##
##interactibles## ##defining the GUI widgets to be displayed in the window
LISTBOX_s_price = Listbox(root,height = '3',width = '5')                            #.place(x=25,y=25)
BUTTON_calcualte_total=Button(root,text = 'calculate!',command = getpaintingprice)  #.place(x=70,y=125)
ENTRY_room_height = Entry(root,width = '8')                                         #.place(x=75,y=25)
ENTRY_room_width01 = Entry(root,width = '8')                                        #.place(x=150,y=25)
ENTRY_room_width02 = Entry(root,width = '8')                                        #.place(x=150,y=50)
ENTRY_room_width03 = Entry(root,width = '8')                                        #.place(x=150,y=75)
ENTRY_room_width04 = Entry(root,width = '8')                                        #.place(x=150,y=100)

LABEL_room_height = Label(root,text = 'room height')                                #.place(x=75,y=0)
LABEL_room_width = Label(root,text = 'room side widths')                            #.place(x=150,y=0)
LABEL_paintband_type = Label(root,text = 'paint band')                              #.place(x=5,y=0)

LABEL_room_SQm = Label(root,text = 'room SQm:')                                     #.place(x=110,y=175)
LABEL_WindowDoor_SQm = Label(root,text = 'window/door SQm:')                        #.place(x=67,y=200)
LABEL_SQmtotal_SQm = Label(root,text = 'total SQm:')                                #.place(x=115,y=225)
LABEL_paintcosttotal_SQm = Label(root,text = 'total cost for painting:')            #.place(x=55,y=250)

LABEL_room_SQm_result = Label(root,text = '0sqm')                                     #.place(x=175,y=175)
LABEL_WindowDoor_result = Label(root,text = '0sqm')                                   #.place(x=175,y=200)
LABEL_SQmtotal_result = Label(root,text = '0sqm')                                     #.place(x=175,y=225)
LABEL_paintcosttotal_result = Label(root,text = '£0')                               #.place(x=175,y=250)

#add/rem box#
LISTBOX_addit_RoomWin = Listbox(root,height = '10',width = '7')                     #.place(x=225,y=0)
SCROLL_additional = Scrollbar(root)
BUTTON_addit_add=Button(root,text = 'add',command = addroomspace)        #.place(x=0,y=0)
BUTTON_addit_rem=Button(root,text = 'remove',command = deleteroomspace)        #.place(x=0,y=0)
LABEL_addit_desc = Label(root,text ='add/remove window/door!')
LABEL_addit__roomwin_desc = Label(root,text ='window/door\ndimensions\nH,W')
ENTRY_addit_height = Entry(root,width = '4')
ENTRY_addit_width = Entry(root,width = '4')
LABEL_addit_height_label = Label(root,text ='height\n (m)')
LABEL_addit_width_label = Label(root,text ='width\n (m)')
#end#
#printreciept button#
BUTTON_printdsk_total=Button(root,text = 'print reciept\nto disk!',command = savereciept)
#end#
#undercoat toggle checkbox widget#
CHECKBOX_undercoatsel = Checkbutton(root,variable = BOOL_undercoat, text = "apply undercoat?\n45p/sqm",onvalue = 1, offvalue = 0, height=2)
#end#
##END##

LISTBOX_s_price.insert(END,'£0.80')##populating listbox values
LISTBOX_s_price.insert(END,'£1.00')
LISTBOX_s_price.insert(END,'£1.75')

##configures scrollbar to work with additional window list
LISTBOX_addit_RoomWin.config(yscrollcommand = SCROLL_additional.set)
SCROLL_additional.config(command = LISTBOX_addit_RoomWin.yview)

##packs,place,grid##
LISTBOX_s_price.place(x=25,y=25)
ENTRY_room_height.place(x=75,y=25)
ENTRY_room_width01.place(x=150,y=25)##placing widgets
ENTRY_room_width02.place(x=150,y=50)
ENTRY_room_width03.place(x=150,y=75)
ENTRY_room_width04.place(x=150,y=100)

LABEL_room_height.place(x=75,y=0)
LABEL_room_width.place(x=150,y=0)
LABEL_paintband_type.place(x=5,y=0)
BUTTON_calcualte_total.place(x=70,y=125)

LABEL_room_SQm.place(x=110,y=175)
LABEL_WindowDoor_SQm.place(x=67,y=200)
LABEL_SQmtotal_SQm.place(x=115,y=225)
LABEL_paintcosttotal_SQm.place(x=55,y=250)

LABEL_room_SQm_result.place(x=175,y=175)
LABEL_WindowDoor_result.place(x=175,y=200)
LABEL_SQmtotal_result.place(x=175,y=225)
LABEL_paintcosttotal_result.place(x=175,y=250)

#add/rem box#

LISTBOX_addit_RoomWin.place(x=375,y=50)
SCROLL_additional.place(x=425,y=50)
BUTTON_addit_add.place(x=225,y=125)
BUTTON_addit_rem.place(x=275,y=125)
LABEL_addit_desc.place(x=225,y=100)
LABEL_addit__roomwin_desc.place(x=375,y=0)##placing widgets
ENTRY_addit_height.place(x=225,y=75)
ENTRY_addit_width.place(x=275,y=75)
LABEL_addit_height_label.place(x=225,y=25)
LABEL_addit_width_label.place(x=275,y=25)
#end#
#printreciept#
BUTTON_printdsk_total.place(x=135,y=125)
#end#

#undercoat toggle#
CHECKBOX_undercoatsel.place(x=5,y=80)
#end#
##END##

###the function below and the commented out function below are 2 previous iterations of trying to split the string got out of the listbox, i decided to use the .split command as it would be easier and more efficient instead
def dbg():
    temp = ''
    extra_roomwin_width =0.0
    extra_roomwin_height = 0.0
    for x in LISTBOX_addit_RoomWin.get(0,last= LISTBOX_addit_RoomWin.size()):##for each list entry in listbox
        pairf = x.split(',')
        extra_roomwin_height += float(pairf[0])
        extra_roomwin_width += float(pairf[1])
        print('final = H,W',extra_roomwin_height,extra_roomwin_width)
         

##def dbg():
##    temp = ''
##    extra_roomwin_width =0.0
##    extra_roomwin_height = 0.0
##    for x in LISTBOX_addit_RoomWin.get(0,last= LISTBOX_addit_RoomWin.size()):##for each list entry in listbox
##                    #temph = ''
##                    #tempw = ''
##                    #temp = ''
##                    comma = False
##                    for y in range(len(x)):
##                            print(x[y])
##                            #if comma:
##                            if x[y] == ',':
##                                print('temp= ',temp)
##                                if comma:
##                                    extra_roomwin_width += float(temp)
##                                    
##                                else:
##                                    extra_roomwin_height += float(temp) 
##                                    comma = True
##                                temp = ''
##                            temp +=x[y]
##    print('eoF',temp,extra_roomwin_width,extra_roomwin_height)
root.mainloop()
