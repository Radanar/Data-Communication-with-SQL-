"""
Created on Wed Oct 18 18:41:28 2023

- read the lines by opening the .txt file 
- reading all the lines by readline() function by looping (while loop) 
- count the number of lines the text file have

"""
import nltk
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer

filename = r"F:\Parami\Courses\2023, Fall Semester Materials\Parami Courses\Data Communication and Ethics\Projects & Assignments\DataSource\data.txt"

with open(filename) as fn:
    # print("------- Reading only one line with readline() function---------\n")
    # ln = fn.readline() #read one line
    # print("This is one line:",ln)
    
    # print("------- Reading the lines left line by line by while loop -------")
    
    # ln1 = fn.readline() #readline() reads only the sentences that are left after the first reading
    # counter = 0
    # while ln1:
    #     print(ln1)
    #     ln1 = fn.readline()
    #     counter += 1
    # print("------------- Counting the number of lines ------------")
    # print("Number of lines:", counter)
    
    # print("\n----------- Splitting the characters ------------\n")
    # split_txt = fn.readline().split()
    # print(split_txt)
    
    # print("\n------- Counting the frequency of the characters' appearance by Counter Module------------\n")
    # p = Counter(fn.read().split()) # ,. commas and full-stop are also determined as one charaacter in the machine
    # print(p)
    
    mydata = fn.read()
    print("\n----------- My Words - Tokenize the texts in the file as words ------------\n")
    words = nltk.word_tokenize(mydata)
    print(words)
    
    print("\n----- My Sentences - Tokenize the texts in the file as sentences -------\n")
   
    sentences = nltk.sent_tokenize(mydata) 
    print(sentences)
    
    print("\n----- My Stems - Stemming the words -------\n")
    
    porter_stemmer = PorterStemmer() #creating a Porter Stemmer object
    
    for w in words:
        print(w, "---stem--> ", porter_stemmer.stem(w))
    
    print("\n----- My Lemmatizer - Lemmatizing the words -------\n")
    wordnet_lemmatizer = WordNetLemmatizer()
    for w in words:
        print(w, "---->", wordnet_lemmatizer.lemmatize(w))
  
    
test_word = "web based technologies" 
#word_1 = "Information systems"

splits = test_word.split()
test_word =" ".join(wordnet_lemmatizer.lemmatize(w) for w in splits)
print(test_word)
    
    
    
    