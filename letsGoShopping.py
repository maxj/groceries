
import ConfigParser


recipeSelections = []

def getRecipeSelection(prompt, recepies, recipeSelections, safeWord="done"):
    result = raw_input(prompt)
    if result == safeWord:
        print ("OK!  All done picking recipes")
        return recipeSelections

    if result in recepies:
        recipeSelections.append(result)
        getRecipeSelection("Great! Pick another recepie or say done \n", recepies, recipeSelections)
    else:
        getRecipeSelection("Sorry!  I could not find that recepie.  Try another option or say done \n", recepies, recipeSelections)


def createGroceryList(recipeBook, recipeSelections):
    groceryList = {}
    for selection in recipeSelections:
        for item in recipeBook.options(selection):
            parseIngredient(groceryList, item)
    return groceryList

def parseIngredient(groceryList, item):
    ingredient = item.strip()
    quantity = 1
    if item[0] == "(":
        quantity = item[1:item.index(")")]
        ingredient = item[item.index(")") + 1:]
        #print quantity + " :::: " + ingredient
        
    if ingredient  in groceryList:
        groceryList[ingredient].append(quantity)
    else:
        groceryList[ingredient] = [quantity]

recipeBook = ConfigParser.ConfigParser(allow_no_value=True)
recipeBook.read("recipes.ini")

recipes = recipeBook.sections()

print ("Hi Gabe!  I was thinking of some of the following recipies:")
for recipe in recipes:
    print recipe

getRecipeSelection("So what are you thinking of? \n", recipes, recipeSelections)

print ("Ok, good choices: ")
for selection in set(recipeSelections):
    print (selection)

groceryList = createGroceryList(recipeBook, set(recipeSelections))


print ("\n\n Grocery List!\n")
for groceryItem in groceryList:
    if len(groceryList[groceryItem]) > 1:
        amount = 0
        for measurement in groceryList[groceryItem]:
            m = measurement.split()
            amount = amount + float(m[0].strip())
            unit = m[1]
        print str(amount) + " " + unit + " " + groceryItem
    else:
        m = groceryList[groceryItem][0]
        print str(m) + " " + groceryItem

