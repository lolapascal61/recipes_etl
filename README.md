# recipes_etl
Case study Hello Fresh

The code can be run form the hellofresh.py file. 

First a data set containing 1042 recipes is uploaded. Each recipe is described by several fields such as ingredients, name, description, image, ect.
Then, all the recipes containing the ingredient 'chilli' are selected. The code takes into acccount the possible mispelling of the word.
Then, a new variable evaluating the difficulty of a recipe is created. To do so, the variables prepTime and cookTime had to be transformed in the right format (datetime). Then the sum of the two variables is computed. The difficulty of a recipe is assesed based on the sum of these two variables. A recipe is considered as hard if it takes longer than 1 hour, medium if it takes between 30 minutes and 1 hour and easy if it takes less than 30 minutes.
Finally, the resuting table is exported into a csv file: recipes_chilli.csv
