from __future__ import print_function
updatedSpaces=['-','-','-','-','-']
word='steve'
lives=5
def initialize():
    word = 'steve'
    print['-','-','-','-','-']

def getLetter():
    print('Guess a letter.')
    letter = raw_input()
    global letter
    
def won():
    if letter in word:
        print('Yay, you won!!') 
    if letter not in word:
        print(getLetter)      
        global letter
          
                         
def main():
    initialize()
    getLetter()                

                     
def check(letter):
    global lives
    global updatedSpaces
    global word
    global letter
    if letter in word:
        for i in range(0,len(word)-1):
            Hamza=word.find(letter, i, len(word))
            if Hamza != -1:
                updatedSpaces[Hamza]=letter
    else:
        lives=lives-1
        print('Not in word,', lives, 'lives left!')
    print(updatedSpaces)
        
        
        
        
    
        
        
    

        
