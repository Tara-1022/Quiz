#defining the questions, answers
questions = {0:'What is the capital of India?',
             1:'What is the national bird?',
             2:'Who is the Father of our Nation',
             3:'Who was the first President of India?',
             4:'Which is the most sensitive organ of our body?',
             5:'Giddha is the folk dance of this state',
             6:'Who invented the computer?',
             7:'1024 Kilobytes is equal to?',
             8:'The brain of the computer is the',
             9:'India lies in this continent',
             10:'Which country are the Pyramids of Giza in?',
             11:'What city is the Statue of Liberty in?',
             12:'How many Cricket World cups does India have?',
             13:"Martyr's Day is celebrated each year on",
             14:'Which is the smallest state of India?'}

options = {0:('Jaipur','Delhi','Ahmedabad','Pune'),
           1:('Crow','Sparrow','Owl','Peacock'),
           2:("Subhash Chandra Bose", "Mahatma Gandhi", "Jawaharlal Nehru", "Mother Teresa"),
           3:("Jawaharlal Nehru","Mahatma Gandhi","Morarji Desai","Dr Rajendra Prasad"),
           4:("Skin","Eyes","Heart","Tongue"),
           5:("Haryana","Jharkhand","Punjab","Orissa"),
           6:("Thomas Edison","Joseph Swan","Humphrey Davy","Charles Babbage"),
           7:("1 MB(Megabyte)","1 GB(Gigabyte)","1000 KB(Kilobyte)","2 GB(Gigabyte)"),
           8:("Keyboard","Mouse","CPU","Memory Card"),
           9:("Antartica","Asia","South America","Africa"),
           10:("Libya","Macchu Pichu","South America","Egypt"),
           11:("New York City","Chicago","California","New Jersey"),
           12:("5","7","3","2"),
           13:("26 January","30 January","31 December","24 November"),
           14:("Goa","Karnataka","Jharkhand","Gangtok")}

correct_ans = {0:'Delhi',
               1:'Peacock',
               2:'Mahatma Gandhi',
               3:'Dr Rajendra Prasad',
               4:'Skin',
               5:'Punjab',
               6:'Charles Babbage',
               7:'1 MB(Megabyte)',
               8:'CPU',
               9:'Asia',
               10:'Egypt',
               11:'New York City',
               12:'2',
               13:'30 January',
               14:'Goa'}

#displays player's score
def display_score(data):
    print('-'*80)
    print('\nQuestion \t\t\tScore')
    print('- '*40)
    tot=0
    for i in data:
        print(i[0],i[1], sep='\t')
        if i[1] == None:
            tot = tot + 0
        else:
            tot = tot + i[1]
    print('- '*40)
    print("\nTotal score",tot,sep='\t')
    print('-'*80)
