from pokemontcgsdk import Card

#Getting pokes from specific set
cards = Card.where(set="FireRed & LeafGreen")

#Array to handle pokes objects
pokemons_list = []

#Class to get each pokemon from api
class Pokemon():
    def __init__(self, name, number, image_url, supertype, subtype, rarity):
        self.name = name
        self.number = number
        self.image_url = image_url
        self.supertype = supertype
        self.subtype = subtype
        self.rarity = rarity


    def return_by_name(self, name):
        if self.name == name:
            return self

#Creating json
for card in cards:
    poke = Pokemon(card.name, card.number, card.image_url, card.supertype, card.subtype, card.rarity)
    pokemons_list.append(poke)
