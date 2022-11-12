class TextProcessor:
    def __init__(self):
        self._punkt = ",.?!;:*/"
        
        
        
    def __is_punktiantian(self, char):
        if char in self._punkt:
            return True 
        else: return False

    def get_clean_string(self, string):
        b = ""
        for i in string:
            if self.__is_punktiantian(i) == False:
                b += i
        return b
        
                    
#a = TextProcessor()
#a.get_clean_string("Adsd: asd xz, asdq")
#print(a.get_clean_string("Adsd: asd xz, asdq"))

class TextLoader():
     def __init__(self):
         self._text_processor = TextProcessor()
         self._clean_string = None
     def set_clean_text(self, string):
         self._clean_string = self._text_processor.get_clean_string(string)
         return self._clean_string
     @property
     def clean_string(self):
         print("clean string =", self._clean_string)
         return self._clean_string
    

#b = TextLoader()
#b.set_clean_text("Adsd: asd xz, asdq,")
#b.clean_string
# b.clean_string
# print(b.string)
class DataInterface():
    def __init__(self):
        self.__text_loader = TextLoader()
    def process_texts(self, array):
        for i in array:
            print(self.__text_loader.set_clean_text(i))
di = DataInterface()
t = ['Adsd: asd xz, asdq', 'asdasdsad,sadas,wq,eqwelqwe;123 ?', 'dsfodsjf,sdfwe.rwqw/e']
ct = di.process_texts(t)        
            
    

    