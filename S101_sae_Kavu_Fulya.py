# SAE S1.01  ETUDE DE COMMUNAUTES DANS UN RESEAU SOCIAL #

# Question préliminaire : Modélisation d'un réseau par un tableau : #
p_amis=["Muriel", "Yasmine","Muriel", "Joël", "Yasmine", "Joël", "Yasmine", "Thomas", "Thomas", "Diara", "Thomas", "Carole", "Joël", "Nassim", "Joël", "Andréa", "Joël", "Ali", "Nassim", "Andréa", "Nassim", "Ali", "Andréa", "Ali", "Andréa", "Valentin", "Valentin", "Léo", "Léo", "Axel", "Léo", "Thierry", "Axel", "Thierry"]


amis = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]

# Question 1 #



# Première version #

def nb_amis(amis,prenom) :
    compteur = 0
    for val in amis :
        if val == prenom :
            compteur += 1
    return compteur



a = nb_amis(p_amis,"Joël")
#print(a)

# Deuxième version #

def nb_amis1(amis,prenom) :
    compteur = 0
    i = 0
    while i < len(amis):
        if prenom == amis[i] :
            compteur += 1
        i += 1
    return compteur


a1 = nb_amis1(p_amis,"Joël")
#print(a1)


# Fonction tests unitaires pour les fonctions nb_amis et nb_amis1 #

def test_nb_amis() :
        assert nb_amis(p_amis,"Joël") == 5
        assert nb_amis(p_amis,"Valentin") != 4
        print ("La fonction nb_amis est vérifiée.")


def test_nb_amis1() :
        assert nb_amis1(p_amis,"Diara") != 2
        assert nb_amis1(p_amis,"Léo") == 3
        print ("La fontion nb_amis1 est vérifiée.")

#test_nb_amis()
#test_nb_amis1()

# Question 2:


def taille_reseau(amis) :
    t = []
    i = 0
    while i < len(amis) :
        if amis[i] not in t:
            t.append(amis[i])
        i += 1
    return t

b = taille_reseau(p_amis)
#print(b)
#print(len(b))


# Foction test unitaire pour la fonction taille_reseau #

def test_taille_reseau() :
    assert taille_reseau(p_amis) != 34
    print ("La fonction taille_reseau fonctionne.")


#test_taille_reseau()



# Question 3 #


def lecture_reseau(path):
    ov = open(path,encoding = "utf-8", mode = "r")
    t = []
    reseau = []
    li = ov.readline()

    while li != "" :
        li = li.strip()
        li = li.split(';')
        t.append(li)
        li = ov.readline()
    ov.close()
    for i in range(len(t)) :
        reseau.append(t[i][0])
        reseau.append(t[i][1])

    return reseau

c = lecture_reseau("SAE_S101/Communaute1.csv")
#print(c)


# Foction test unitaire pour la fonction lecture_reseau #

def test_lecture_reseau():
    assert lecture_reseau("SAE_S101/Communaute1.csv")
    print("La fonction lecture_reseau est vérifiée.")

#test_lecture_reseau()

# Question 4 #

def dico_reseau(amis) :
    dico = {}
    t = []
    i = 0
    j = 0
    while i < len(amis) :
        if amis[i] not in dico :
            while j < len(amis) :
                if j % 2 == 0 :
                    if amis[i] == amis[j] :
                        t.append(amis[j + 1])
                elif j % 2 == 1 :
                    if amis[i] == amis[j] :
                        t.append(amis[j - 1])
                j += 1
            j = 0
            dico[amis[i]] = t
        i +=1
    return dico

d = dico_reseau(p_amis)
#print(d)



# Foction test unitaire pour la foction dico_reseau #

def test_dico_reseau() :
    assert dico_reseau(p_amis)
    print("La fonction dico_reseau est vérifiée.")

#test_dico_reseau()

# Question 5 #

def nb_amis_plus_pop (dico_reseau) :
    d = dico_reseau # dico qui utilise la fonction précédente, donc, ici, dico = d
    maximum = 0
    for a in d.values():
        if len(a) > maximum:
            maximum = len(a)
    return maximum

e = nb_amis_plus_pop(dico_reseau("SAE_S101/Communaute1.csv"))
#print(e)

# Foction test unitaire pour a foction nb_amis_plus_pop #

def test_nb_amis_plus_pop() :
    assert nb_amis_plus_pop(dico_reseau(p_amis)) == 5
    assert nb_amis_plus_pop(dico_reseau(lecture_reseau("Communaute1.csv"))) != 10
    print("La fonction nb_amis_plus_pop est vérifiée.")

#test_nb_amis_plus_pop()

# Question 6 #

def les_plus_pop(dico_reseau) :
    t_p = []
    nb_maximum = nb_amis_plus_pop(dico_reseau)
    for cle,val in dico_reseau.items() :
        if len(val) == nb_maximum :
            t_p.append(cle)
    return t_p

print(les_plus_pop(dico_reseau(lecture_reseau("SAE_S101/Communaute1.csv"))))
