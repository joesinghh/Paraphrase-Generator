from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from random_word import RandomWords
import nltk 
from threading import Thread
from pattern.en import superlative,pluralize,comparative,superlative
import spacy
from tkinter import filedialog
import csv
import ast
import requests
import os
import random 
import en_core_web_lg
from pyinflect import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
import random
quotes_list=['“ Trees that are slow to grow bear the best fruit. ”\n\n      ― Moliere','“ He that can have patience can have what he will. ”\n \n      ― Benjamin Franklin','“ Patience is a conquering virtue. ” \n\n        ― Geoffrey Chaucer','“ Patience is bitter, but its fruit is sweet. ”\n\n        ― Aristotle','“ The strongest of all warriors are these two — Time and Patience. ” \n\n         ― Leo Tolstoy, War and Peace','“ Rivers know this: there is no hurry. We shall get there some day. ”\n\n           ― A.A. Milne, Winnie-the-Pooh']


root=Tk() #main GUI window

#model which contains word vectors (used in program to compare similarities)
root.wm_title('Paraphrase Generator')
#nlp = spacy.load('en_core_web_lg')
nlp =en_core_web_lg.load()
#file containing input
def progressbar(i):
    label['text']=str(i+1)+'/'+str(total_length)
    bar['value']=(100/total_length)*(i+1)
    status.config(text=words[i])
    quote['text']=quotes_list[random.randint(0,len(quotes_list)-1)]
    if i+1==total_length:
        top.destroy()
#1st function to find similarities
def synonyms2(term):
    synonyms_ = [] 
    for syn in wordnet.synsets(term): 
        for l in syn.lemmas(): 
            synonyms_.append(l.name()) 
        
    return synonyms_

def synonyms(string):
 
    try:
        if string!=u'"' and string!=u'\"' and string!=u'\'' and string!=u"'":
            stripped_string = string.strip()
            fixed_string = stripped_string.replace(" ", "_")
   
        # Set the url using the amended string
            my_url = f'https://thesaurus.plus/thesaurus/{fixed_string}'
        # Open and read the HTMLz
            uClient = uReq(my_url)
            page_html = uClient.read()
            uClient.close()
        # Parse the html into text
            page_soup = soup(page_html, "html.parser")
            word_boxes = page_soup.find("ul", {"class": "list paper"})
            results = word_boxes.find_all("div", "list_item")
            sim_words_list=[]
       # Iterate over results and print
            for result in results:
                sim_words_list.append(result.text)
        # Remove whitespace before and after word and use underscore between words
        
    except Exception as e:
        sim_words_list=[]
        
        if "_" in fixed_string:
            print(e)

        else:
            print(e)
    print('yeahh')
    return sim_words_list
def syn(word):
    urls=["https://dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=a24dfaa9-ffe0-4a9a-8906-c8ff3e8dd406".format(word),"https://dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=92432adb-24d2-46a1-a979-f1b701155bf2".format(word)]
    return_list=[]
    try:
        url=urls[random.randint(0,1)]
        
        
        r = requests.get(url)
        
        if r.json()!=[] or  r.json()!='':
            return_list=r.json()[0]['meta']['syns'][0]
            
        else:
            raise Exception('error')
        print('1')
    except:
        try:
            url=urls[random.randint(0,1)]
            r = requests.get(url)
            if r.json()!=[] or  r.json()!='':
                return_list=r.json()[0]['meta']['syns'][0]
            else:
                return_list=r.json()[0]['meta']['syns'][0]
                raise Exception('error')
            print('2')
        except:
            try:
                url = "https://dictionaryapi.com/api/v3/references/ithesaurus/json/{}?key=61d0a7b2-125f-4b16-b0d8-1f3593627bf9".format(word)
                r = requests.get(url)
                if r.json()!=[] or  r.json()!='':
                    return_list=r.json()[0]['meta']['syns'][0]
                else:
                    return_list=r.json()[0]['meta']['syns'][0]
                    raise Exception('error')
                print('3')
            except:
                try:
                    url = "https://dictionaryapi.com/api/v3/references/ithesaurus/json/{}?key=ea94eb40-67b0-4a3d-ba53-5a3da9079906".format(word)
                   
                    r = requests.get(url)
                    if r.json()!=[] or  r.json()!='':
                        return_list=r.json()[0]['meta']['syns'][0]
                    print('4')
                except:
                    if  word not in ['.',',','(' ,')','',' (','( ',' )',') ',' .','. ','!','doesn','t','don','\'','i','l',' t','t ','\'t', "'",'wasn','didn','couldn','wouldn','weren',';',':','|','I','l','L','s','ain','shouldn','&','?',"\'","'",'"','\"']:
                        if word!='\"' and word!='"' and word!='\'' and word!="'":

                            return_list=[]
                    else:
                        return_list=[]
                
    

    if return_list!=[]:
        with open('.img\\words.csv','a',newline='') as csvfile:
            wr=csv.writer(csvfile)
            global d
            d={'id':word,'value':return_list}
            for i in range(int(len(d)/2)):
                k=tuple(d.values())
                
                w=k[0]
                v=k[1]
                
                wr.writerow([w,v])
        
    return return_list

def fun(word):
     
    csv__file= open('.img\\words.csv','r') 
    reader=csv.reader(csv__file)
    k=True
    if reader!=[]:
        for row in reader:
            
            if row!=[]:
                if row[0].lower()==word.lower():
                    k=False
                    
                    return (ast.literal_eval(row[1]))

                else:
                    k=True
                    
        if k==True:
            return (syn(word))
def start(position=None,*args):
    
    global output,output2,total_length,words

    if input_box.get('1.0','end-1c')=='' or input_box.get('1.0','end-1c')==' ':
        result_box2.insert(END,'NOTHING TO PROCESS IN INPUTBOX !!!')
        result_box1.insert(END,'NOTHING TO PROCESS IN INPUTBOX !!!')
               
    words=word_tokenize(input_box.get('1.0','end-1c'))
    total_length=len(words)
    taggs=pos_tag(words)
    output=''
    output2=''

    real_words=[]
    for i in range(len(words)):
        a=taggs[i][1]
        print('word: ',words[i] ,'tag: ',a)

       
       
        
        
        r=[]
        # not to fin synonym for the name of a person,a decorator etc.
        if ( taggs[i][1]!='DP' and taggs[i][1]!='CD' and taggs[i][1]!='TO' and taggs[i][1]!='PRP$' and taggs[i][1]!='IN' and taggs[i][1]!='PRP'  and taggs[i][1]!='DT'  and taggs[i][1]!='WRB' and   taggs[i][1]!='WR') and( words[i] not in ['.',',','(' ,')','',' (','( ',' )',') ',' .','. ','!','doesn','t','don','\'','i','l',' t','t ','\'t', "'",'wasn','didn','couldn','wouldn','weren','I','L','1','|',';',':','s',' s','ain','ll','-','__']) and words[i].lower() not in ['time','second','seconds','month','months','year','years','minute','minutes','indian','countries','let']:
            if words[i]!='.' and words[i]!=',' and words[i]!="'" and words[i]!="\"" and words[i]!="\"" and words[i]!='"' and words[i]!=' "' and words[i]!='" ' and words[i]!='?':

                r=fun(words[i])
            
            
            
        
        progressbar(i)

        
        if r!=[]:

            print('list of words: ',r)
            
            real_words=[]
            # to make the similar words more similar by changing their tense etc.
            for j in r:
                
                tag=pos_tag([j])[0][1]
                
                if tag==a or a=='JJ':  
                               # if already similar
                    real_words.append(j) 
                
                elif tag!=a:           #check part-of speech tags and change accordingly
                    if a=='NNPS':
                        token=nlp(j)
                        
                        w=tokens[0]._.inflect('NNPS', form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(tokens[0]._.inflect('NNPS',inflect_oov=True, form_num=0))
                    
                    
                    elif a=='NNS':
                        token=nlp(j)
                        w=token[0]._.inflect('NNS',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            
                            real_words.append(token[0]._.inflect('NNS',inflect_oov=True,form_num=0))
                    elif a=='NNP':
                        token=nlp(j)
                        w=token[0]._.inflect('NNP',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(token[0]._.inflect('NNP',inflect_oov=True,from_num=0))
                    elif a=='NN':
                        token=nlp(j)
                        w=token[0]._.inflect('NN',form_num=0)
                        real_words.append(w)
                    elif a=='RB':
                        token=nlp(j)
                        w=token[0]._.inflect('RB',inflect_oov=True,form_num=0)
                        real_words.append(token[0]._.inflect("RB",inflect_oov=True,form_num=0))
                    elif a=='RBR':
                        token=nlp(j)
                        w=token[0]._.inflect('RBR', inflect_oov=True,form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(token[0]._.inflect('RBR',inflect_oov=True,form_num=0))
                    elif a=='RBS':
                        token=nlp(j)
                        w=token[0]._.inflect('RBS',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(token[0]._.inflect('RBS',inflect_oov=True,form_num=0))
                            
                    elif a=='VB' :
                        tokens = nlp(j)
                        w=tokens[0]._.inflect('VB',inflect_oov=True, form_num=0)
                        if w!=None :
                            real_words.append(tokens[0]._.inflect('VB',inflect_oov=True, form_num=0))
                    elif a=='VBD' :
                        tokens = nlp(j)
                        w=tokens[0]._.inflect('VBD', form_num=1)
                        
                        if w!=None :
                            real_words.append(tokens[0]._.inflect('VBD', inflect_oov=True,form_num=0))
                    elif a=='VBG':
                        tokens=nlp(j)
                        w=tokens[0]._.inflect('VBG',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(tokens[0]._.inflect('VBG',inflect_oov=True, form_num=0))
                    elif a=='VBN ':
                        tokens=nlp(j)
                        w=tokens[0]._.inflect('VBN',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(tokens[0]._.inflect('VBN', inflect_oov=True,form_num=0))
                    elif a=='VBP':
                        tokens=nlp(j)
                        w=tokens[0]._.inflect('VBP',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(tokens[0]._.inflect('VBP',inflect_oov=True, form_num=0))
                    elif a=='VBZ':
                        tokens=nlp(j)
                        w=tokens[0]._.inflect('VBZ',inflect_oov=True, form_num=0)
                        if w!=None and pos_tag([w])==a:
                            real_words.append(tokens[0]._.inflect('VBZ',inflect_oov=True, form_num=0))
                    elif a=='JJR' :
                        real_words.append(comparative(j))
                    elif a=='JJS' :
                        real_words.append(superlative(j))
        print('real words: ',real_words)        
        if real_words==[] or r==[]:         #if no similar word is found 
            output=output+' '+words[i]
            output2=output2+' '+words[i]
        else :
            
            output_words=[]
            max_sim=[]
            token1=nlp(words[i])
            
            for h in real_words:
                if h!=None and h!='' :
                    token2=nlp(h)
                    
                    f1=h.replace(' ','')
                    f=f1.replace('_',' ')
                    sim=token1.similarity(token2)
                    if  h not in  output_words and (f not in output_words ) and words[i].lower()!=h.lower() and  words[i].lower()!=f.lower()  :   #adding appropriate word
                    
                        output_words.append(f)
                        max_sim.append(sim)

                else:
                    sim=0
            

                           
            final_listwords=[]
            for jj in max_sim:
                final_listwords.append(output_words[max_sim.index(max(max_sim))])
                max_sim[max_sim.index(max(max_sim))]=-1
            if output_words==[]:
                output=output+' '+words[i]
                output2=output2+' '+words[i]
            
            elif position==None or type(position)!=int:
                              
                print('final_listwords: ',final_listwords)
                if len(output_words)>3:
                                        
                    output=output+' '+final_listwords[0]  
                else:
                    output=output+' '+final_listwords[random.randint(0,len(final_listwords)-1)] 
                
            elif position!=None and (type(position)==int or type(position)==str): 
                if type(position)==str:                                  #choose a specific position of word from list of similar words
                    if len(output_words)>int(position)  :
                        output=output+' '+final_listwords[int(position)]
                elif type(position)==int:
                    if len(output_words)>(position):
                        output=output+' '+final_listwords[position]

                else:
                    output=output+' '+final_listwords[len(output_words)-1]
            if len(output_words)>7:
                    output2=output2+' '+str([words[i]]+final_listwords[0:8])
                     # if number of similar words is less than 4 than choose randomly
            elif len(output_words)<=7:
                    output2=output2+' '+str([words[i]]+final_listwords[0:])
    result_box1.insert(END,output) #to display result
    result_box2.insert(END,output2)


def go_(): 
    messagebox.showinfo('INFO','For better result turn \n on the internet connection')
    global bar,label,top,quote,status
    top=Toplevel(root,bg='black')
    top.title('progress...') 
    top.geometry('500x300')
    
    top.iconbitmap('.img\\photo2.ico')
    style = ttk.Style()
    style.theme_use('vista')
    style.configure("black.Horizontal.TProgressbar", background='blue')
    bar = Progressbar(top, length=200, style='black.Horizontal.TProgressbar')
    bar['value'] = 0
    bar.place(relx=0.3,rely=0.07)
    status=Label(top,bg='black',fg='white')
    status.place(relx=0.13,rely=0.07)

    label=Label(top,bg='black',fg='white')
    label.place(relx=0.45,rely=0.2)
    quote=Label(top,font=('Arial',12),text=quotes_list[random.randint(0,len(quotes_list)-1)],bg='black',fg='white',justify=CENTER,anchor=CENTER)
    quote.place(relwidth=1,relx=0,rely=0.4,relheight=0.6)
    result_box2.delete('1.0',END)
    result_box1.delete('1.0',END)
    if pos.get()==-1:
        Thread(target=start).start()
    else:
        Thread(target=start,args=(pos.get(),)).start()
        pos.set(-1)
def exit_():  #exit
    ms = messagebox.askquestion('exit??', 'do you really wanna exit +_+ ?')
    if ms == 'yes':
        root.destroy()
def save_(): #to save
    if input_box.get('1.0','end-1c')=='' or input_box.get('1.0','end-1c')==' ' or result_box1.get('1.0','end-1c')=='':
        msg1=messagebox.showinfo('info','NOTHING TO SAVE')
    else:
        
        
        root.filename=filedialog.asksaveasfilename(title='save',filetype=(('all files','*.*'),('text files','*.txt',)))
        print(root.filename)
        f_l=open(root.filename,'w')
        f_l.write(result_box1.get('1.0','end-1c'))

def clear_(): #to clear screen
    input_box.delete('1.0',END)
    result_box1.delete('1.0',END)
    result_box2.delete('1.0',END)

#############################GUI######################################
root.geometry('1300x600')# window dimension
root.resizable(0,0) #do not change window dimension
main_frame=Frame(root,bg='white')
main_frame.place(relwidth=1,relheight=1)

scrollbar = Scrollbar(main_frame)
scrollbar.place(x=781,y=0,relheight=0.5)

input_box = Text(main_frame, wrap=WORD, yscrollcommand=scrollbar.set)
input_box.place(x=1,relheight=0.5,relwidth=0.6)

input_box['font'] = ('consolas', '11')

scrollbar2 = Scrollbar(main_frame)
scrollbar2.place(x=781,y=299,relheight=0.5)

result_box1=Text(main_frame,bg='white',yscrollcommand=scrollbar2.set,wrap=WORD)
result_box1.place(x=1,y=299,relwidth=0.6,relheight=0.5)  

result_box1['font'] = ('consolas', '11')

result_box1.insert(END,'#'*10+' R E S U L T '+'#'*10)

scrollbar3=Scrollbar(main_frame)
scrollbar3.place(x=1170,y=0,relheight=1)

result_box2=Text(main_frame,bg='white',yscrollcommand=scrollbar3.set,wrap=WORD)
result_box2.place(x=800,y=0,relwidth=0.2849,relheight=1)
result_box2['font'] = ('consolas', '11')
scrollbar2.config(command=result_box1.yview)
scrollbar.config(command=input_box.yview)
scrollbar3.config(command=result_box2.yview)
# start button

button_start=Button(main_frame,text='GO',command=go_,font=('Calibri',20),bg='white',activebackground='black',activeforeground='white',borderwidth=7)
button_start.place(relwidth=0.087,relheight=.193,x=1187,y=0)

menu1 = Menu(root, bg='red', fg='blue', activeforeground='#209EFF', font=('Areial', 10))
sub1 = Menu(menu1, tearoff=0, activebackground='white', activeforeground='#209EFF', bg='white', )
menu1.add_command(label='SAVE ', command=save_, )
menu1.add_command(label='CLEAR ', command=clear_,)

menu1.add_command(label='EXIT', command=exit_, )
root.config(menu=menu1)
pos=IntVar()
pos.set(-1)
#radiobuttonns

r1 = Radiobutton(main_frame,fg='#2058B6',variable=pos,bg='white',activeforeground='white',activebackground='white',
                         value=1, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'),text='1')
r2 = Radiobutton(main_frame,fg='#2058B6', variable=pos,bg='white',activeforeground='white',activebackground='white',
                         value=2, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'),text='2')
r3 = Radiobutton(main_frame,fg='#2058B6', variable=pos,bg='white',activeforeground='white',activebackground='white',
                         value=3, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'),text='3')
r4 = Radiobutton(main_frame,fg='#2058B6', variable=pos,bg='white',activeforeground='white',activebackground='white',
                         value=4, justify='left', font=('Myanmar Text', 17, 'bold',
                                                        'italic'),text='4')

r5=Radiobutton(main_frame,fg='#2058B6',variable=pos,bg='white',activeforeground='white',activebackground='white',
                          value=5,justify='left',font=('Myanmar Text', 17, 'bold','italic'),text='5')
                                                        
r6=Radiobutton(main_frame,fg='#2058B6',variable=pos,bg='white',activeforeground='white',activebackground='white',
                          value=6,justify='left',font=('Myanmar Text', 17, 'bold','italic'),text='6')

r7=Radiobutton(main_frame,fg='#2058B6',variable=pos,bg='white',activeforeground='white',activebackground='white',
                          value=7,justify='left',font=('Myanmar Text', 17, 'bold','italic'),text='7')
                                                                 
r1.place(relwidth=0.08,relheight=.2,x=1187,y=115)
r2.place(relwidth=0.08,relheight=.2,x=1187,y=180)
r3.place(relwidth=0.08,relheight=.2,x=1187,y=245)
r4.place(relwidth=0.08,relheight=.2,x=1187,y=310)
r5.place(relwidth=0.08,relheight=.2,x=1187,y=375)
r6.place(relwidth=0.08,relheight=.2,x=1187,y=440)
r7.place(relwidth=0.08,relheight=.2,x=1187,y=505)

root.iconbitmap('.img\\photo2.ico')
root.mainloop()# to keep displaying   root window


                      




        



    





        


