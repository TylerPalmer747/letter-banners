#tyler palmer 2026
#program to print custom letter banners
#version 1.8
import pyperclip
#used to copy the output to the clipboard. 

def colorcvrt(color):
    #convert letter color to number
    colorlist = ["white","orange","magenta","light_blue","yellow","lime","pink","gray","light_gray","cyan","purple","blue","brown","green","red","black"]
    i = 0
    for i in range(16):
        if colorlist[i] == color:
            return i
    return
    
    
    
def genban(bkg_color,bkg_color_int,ltr_color,ltr_color_int,char,iterator):
    #generate and return the block entity part of the command. called once for each banner.
    bkg_color_int = str(bkg_color_int)
    ltr_color_int = str(ltr_color_int)
    iterator = str(iterator)
    if char != 'h' and char != 'q' and char != 's' and char != 'd':
        output1 = "{Slot:" + iterator + ",id:\"minecraft:" + bkg_color + "_banner\",Count:1b,tag:"
    else:
        output1 = "{Slot:" + iterator + ",id:\"minecraft:" + ltr_color + "_banner\",Count:1b,tag:"
    #chooses beginning of chulker command. h, q, s, and b require background color to be the 
    #letter color. the rest use the background color.
    
    if char == 'a':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"ms\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'b':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"cbo\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"ms\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'c':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"ms\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'd':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"bts\",Color:" + bkg_color_int + "},{Pattern:\"tts\",Color:" + bkg_color_int + "},{Pattern:\"cs\",Color:" + ltr_color_int + "},{Pattern:\"mc\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'e':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"ms\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'f':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ms\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + bkg_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'g':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"hh\",Color:" + bkg_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'i':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"cs\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'j':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"hh\",Color:" + bkg_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'h':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ts\",Color:" + bkg_color_int + "},{Pattern:\"bs\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'k':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"drs\",Color:" + ltr_color_int + "},{Pattern:\"hh\",Color:" + bkg_color_int + "},{Pattern:\"dls\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'l':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'm':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"tt\",Color:" + ltr_color_int + "},{Pattern:\"tts\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'n':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"tt\",Color:" + bkg_color_int + "},{Pattern:\"drs\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'o':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'p':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"hhb\",Color:" + bkg_color_int + "},{Pattern:\"ms\",Color:" + ltr_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'q':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"mr\",Color:" + bkg_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"br\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'r':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"hh\",Color:" + ltr_color_int + "},{Pattern:\"cs\",Color:" + bkg_color_int + "},{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"drs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 's':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"mr\",Color:" + bkg_color_int + "},{Pattern:\"ms\",Color:" + bkg_color_int + "},{Pattern:\"drs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 't':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"cs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'u':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'v':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"dls\",Color:" + ltr_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"bt\",Color:" + bkg_color_int + "},{Pattern:\"dls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'w':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"bt\",Color:" + ltr_color_int + "},{Pattern:\"bts\",Color:" + bkg_color_int + "},{Pattern:\"ls\",Color:" + ltr_color_int + "},{Pattern:\"rs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'x':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"cr\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'y':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"drs\",Color:" + ltr_color_int + "},{Pattern:\"hhb\",Color:" + bkg_color_int + "},{Pattern:\"dls\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    if char == 'z':
        output2 = "{BlockEntityTag:{Patterns:[{Pattern:\"ts\",Color:" + ltr_color_int + "},{Pattern:\"dls\",Color:" + ltr_color_int + "},{Pattern:\"bs\",Color:" + ltr_color_int + "},{Pattern:\"bo\",Color:" + bkg_color_int + "}]}}}"
    return output1 + output2
    
    
def main():
    print("welcome to Tyler's banner program \n")
    copychoice = input("would you like the output to be copied to the clipboard automatically? type y or n: ")
    
    print("\n\ncolor options: white, orange, magenta, light_blue, yellow, lime, pink, gray,")
    print("light_gray, cyan, purple, blue, brown, green, red, black\n")
    
    exit = "yay"
    while exit != "exit":
        bkg_color = input("background color in lowercase: ")
        bkg_color_int = colorcvrt(bkg_color)
        ltr_color = input("letter color in lowercase: ")
        ltr_color_int = colorcvrt(ltr_color)
        #print(bkg_color_int)
        #print(ltr_color_int)
        output_list = []
        inputwrd = input("enter your banner words - no spaces: ")
        iterator = 0
        for char in inputwrd:
            output_list.append(genban(bkg_color,bkg_color_int,ltr_color,ltr_color_int,char,iterator))
            iterator = iterator + 1
        finalstring = "/give @p minecraft:white_shulker_box{BlockEntityTag:{Items:["
        i = 0
        for str in output_list:
            finalstring = finalstring + output_list[i]
            if i != len(output_list) - 1:
                finalstring = finalstring + ","
            i = i + 1
        finalstring = finalstring + "]}} 1"
        charlen = 0
        for char in finalstring:
            charlen = charlen + 1 
        if charlen >= 2048:
            print("output too long! it will crash your game")
        else:
            print (finalstring)
            if copychoice == 'y':
                pyperclip.copy(finalstring)
                print("\nOutput has been copied to clipboard")
        print(" ")
        print(" ")
    return 
	
main()
