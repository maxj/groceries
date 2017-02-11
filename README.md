# Grocery List Maker

Hi Gabe!  Hopefully this helps us purchase groceries.  Sorry my
flights are a mess but this gave me something to do!

## Usage

```sh
[mjordan@localhost groceries]$ python letsGoShopping.py 
Hi Gabe!  I was thinking of some of the following recipes:
pizza
pancakes
PBJ
spinach_omelet
spaghetti_and_meatballs
scrambled_eggs
grilled_steak_and_mashed_potatoes
greek_yogurt_and_honey
So what are you thinking of? 

```

At the prompt pick items we should eat this week.  After each
selection you can pick more or type in ```done``` to end to program.  

When done, it should print out a list of items to pick up.

The recipe config files assumes we eat the same thing at meal time for
one morning/night.  So if we want to have pancakes multiple nights we
should scale up the recipe.
