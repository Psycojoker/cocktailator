from pprint import pprint
from csv import reader

def get_cocktails():
    cocktails = []
    cocktail = {}

    for row in list(reader(open("cocktails.csv", "rb"), delimiter=",", quotechar='"'))[1:]:
        if cocktail and row[1]:
            cocktails.append(cocktail)
            cocktail = {}
        if row[0]:
            cocktail["section"] = row[0].replace("\n", "")
        if row[1]:
            cocktail["name"] = row[1]
        if row[4]:
            cocktail["method"] = row[4]
        if row[5]:
            cocktail["comment"] = row[5]

        cocktail.setdefault("ingredients", []).append({"name": row[2].replace("\n", " "), "proportion": row[3]})

        print row
        print pprint(cocktail)

def get_ingredients():
    ingredients = set()

    for row in list(reader(open("cocktails.csv", "rb"), delimiter=",", quotechar='"'))[1:]:
        ingredients.add(row[2].replace("\n", " "))

    return sorted(list(ingredients))

if __name__ == '__main__':
    print get_ingredients()
