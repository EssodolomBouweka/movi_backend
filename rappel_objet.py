### Classes ###

class chien:
    pass

# %% 
mon_chien = chien()
mon_chien.nom = "Rex"
mon_chien.age = 5
mon_chien.couleur = "marron"
mon_chien.aboyer = lambda: "Woof!"  
print(f"Mon chien s'appelle {mon_chien.nom}, il a {mon_chien.age} ans, sa couleur est {mon_chien.couleur} et il dit {mon_chien.aboyer()}")
# %%
class Chien:
    def __init__(self, nom, age, couleur):
        self.nom = nom
        self.age = age
        self.couleur = couleur
    
    def aboyer(self):
        return "Woof!"  
# %%
mon_chien = Chien("Rex", 5, "marron")
print(f"Mon chien s'appelle {mon_chien.nom}, il a {mon_chien.age} ans, sa couleur est {mon_chien.couleur} et il dit {mon_chien.aboyer()}")
# %%
