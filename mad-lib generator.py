from tkinter import *

window = Tk()
window.geometry('300x300')
window.title('Mad-Lib Generator')
Label(window,text='Mad Lib Generator \n Have Fun',font='arial 20 bold').pack()
Label(window,text='Click Any One',font='arial 15 bold').place(x=80,y=80)

def madlib1():

    input_collection = ['animals','profession','cloth','thing','name','place','verb','food']
    for word in input_collection:
        if word == 'name':
            globals()[word] = input(f'enter a {word}: ')
        elif word == 'verb':
            globals()[word] = input(f'enter a {word} in ing form: ')
        else:
            globals()[word] = input(f'enter a {word} name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + thing + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():
    input_collection = ['adjactive','color','thing','place','person','adjactive1','insect','food','verb']
    
    for word in input_collection:
        if word == 'adjactive' or word == 'adjactive1' or word == 'verb':
            globals()[word] = input(f'enter a {word}: ')
        else:
            globals()[word] = input(f'enter a {word} name: ')
    print('Last night I dreamed I was a ' +adjactive+ ' butterfly with ' + color+ ' splocthes that looked like '+thing+ ' .I flew to ' + place+ ' with my bestfriend and '+person+ ' who was a '+adjactive1+ ' ' +insect +' .We ate some ' +food+ ' when we got there and then decided to '+verb+ ' and the dream ended when I said-- lets ' +verb+ '.')

def madlib3():
    input_collection = ['person','color','foods','adjective','thing','place','verb','adverb','food','things']
    
    for word in input_collection:
        if word == 'adjactive' or word == 'adverb' or word == 'verb':
            globals()[word] = input(f'enter a {word}: ')
        else:
            globals()[word] = input(f'enter a {word} name: ')
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make appple '+food+ ' and '+things+' pies!.')

Button(window,text='The Photographer',font='arial 15',bg='ghost white',command=madlib1).place(x=60,y=120)
Button(window,text='apple and apple',font='arial 15',bg='ghost white',command=madlib2).place(x=70,y=180)
Button(window,text='The Butterfly',font='arial 15',bg='ghost white',command=madlib3).place(x=80,y=240)
    
window.mainloop()
