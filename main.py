from sklearn.datasets import load_wine #cargar la base de datos del vino
from sklearn.tree import DecisionTreeClassifier, export_text #crear el clasificador basado en reglas
from sklearn.model_selection import train_test_split #dividir los datos en entrenamiento y prueba

wine = load_wine() #cargar la base de datos del vino
x,y = wine.data, wine.target 

#dividir datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(x_train, y_train)

rules = export_text(tree, feature_names=wine.feature_names)
print("Reglas del árbol:\n")
print(rules)

# Exactitud
accuracy = tree.score(x_test, y_test)
print("Precisión en datos de prueba:", accuracy)