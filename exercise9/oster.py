cheeses = {
    'cheddar':
        ('A235-4','A236-1','A236-2','A236-3','A236-5','C31-1','C31-2'),
    'mozarella':
        ('Q456-9','Q456-8','A234-5','Q457-1','Q457-2'),
    'brie':
        ('ZLAFS55-4','ZLAFS55-9','GOMBOS-7','A236-4'),
    'geitost':
        ('SPAZ-1','SPAZ-3','EMACS45-0'),
    'port salut':
        ('B15-1','B15-2','B15-3','B15-4','B16-1','B16-2','B16-4'),
    'camembert':
        ('A243-1','A234-2','A234-3','A234-4','A235-1','A235-2','A235-3'),
    'ridder':
        ('GOMBOS-4','B16-3'),
}


print("Port salut is found in the following shelfs:")
list(map(print, cheeses['port salut']))


print("The following cheeses is potentionally infected:")
infected_shelfs = ['A234', 'A235', 'B13', 'B14', 'B15', 'C31']



pos_infected_cheeses = []
for cheese in cheeses.keys():
    [cheese for x in cheeses[cheese] if x.split('-')[0] in infected_shelfs]

def check_cheese(

list(map(print, pos_infected_cheeses))