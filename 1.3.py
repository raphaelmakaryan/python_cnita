from dataclasses import dataclass


@dataclass
class Contact:
    def __init__(self, tel: str, adresseMail: str):
        self.tel = tel
        self.adresseMail = adresseMail

    def __repr__(self):
        return (f'Tel = {self.tel}, Mail = {self.adresseMail}')


@dataclass
class addressePostal:
    def __init__(self, adresse: str, codePostal: float, ville: str):
        self.adresse = adresse
        self.codePostal = codePostal
        self.ville = ville

    def __repr__(self):
        return (f'Adresse = {self.adresse}, Code postal = {self.codePostal}, Ville = {self.ville}')


@dataclass
class Repertoire:
    def __init__(self, nom: str, prenom: str, dateDeNaissance: str, contact: Contact, adressePostal: addressePostal):
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance
        self.contact = contact
        self.adressePostal = adressePostal

    def __repr__(self):
        return (
            f'Prenom = {self.prenom}, Nom = {self.nom}, Date de naissance = {self.dateDeNaissance}, {self.contact}, {self.adressePostal}')


repertoire = Repertoire('DALTON', 'Joe', "10/02/2004", Contact("80800808080", "toto@toto.com"),
                        addressePostal("Rue de totot", "74960", "Annecy"))
print(repertoire)
