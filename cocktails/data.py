from csv import reader

def get_cocktails(with_ingredients=None):
    cocktails = []
    cocktail = {}

    for row in list(reader(open("cocktails.csv", "rb"), delimiter=",", quotechar='"'))[1:]:
        if cocktail and row[1]:
            if cocktail["name"] == "Apple Jack":
                print cocktail
            if with_ingredients:
                for ingredient in cocktail["ingredients"]:
                    if ingredient["name"].lower() not in map(lambda x: x.lower(), with_ingredients):
                        break
                else:
                    print "adding", cocktail
                    cocktails.append(cocktail)
            else:
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

        cocktail.setdefault("ingredients", []).append({"name": row[2].replace("\n", " ").decode("Utf-8"), "proportion": row[3]})

    return sorted(cocktails, key=lambda x: x["name"].lower())

def get_ingredients(filtering_string=None):
    ingredients = set()

    for row in list(reader(open("cocktails.csv", "rb"), delimiter=",", quotechar='"'))[1:]:
        ingredient = row[2].replace("\n", " ")
        if filtering_string and filtering_string in ingredient.decode("Utf-8"):
            ingredients.add(ingredient)
        elif not filtering_string:
            ingredients.add(ingredient)

    return sorted(list(ingredients), key=lambda x: x.lower())

if __name__ == '__main__':
    print get_ingredients()
