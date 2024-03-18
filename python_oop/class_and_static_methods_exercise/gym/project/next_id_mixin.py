class NextIdMixin:
    id = 0 # not necessary only to avoid worning by IDE

    """  
    Тук е много важно да се отбележи, че cls в този случай няма 
    да сочи към класа NextIdMixin, а всъщност ще е връзката към обект
    клас customer. Съответно когато кажем cls.id ще се вземе ID-то
    от class customer, което сега е 1.
    
    Ако в класът, който наследява NextIdMixin, няма зададено ID чак тогава return cls.id 
    ще вземе ID- то от този клас 
    
    """


    @classmethod
    def get_next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1
