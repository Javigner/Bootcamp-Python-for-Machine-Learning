from recipe import Recipe
desc = "Pad thai is a stir-fried rice noodle dish commonly served as a street food and at most restaurants in Thailand as part of the country's cuisine."
Padthai = Recipe('Pad thai', 5, 30, ['150g Nouille de riz', '30g cacahuetes', '250g poulet', '20ml fish sauce', '20g sriracha', '2 eggs', '1 oignons'], 'lunch', desc)
toprint = str(Padthai)
print(toprint)