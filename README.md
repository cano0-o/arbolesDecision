#  Clasificación con Árbol de Decisión – Wine Dataset

## Descripción del proyecto

Este proyecto implementa un **clasificador basado en Árboles de Decisión** utilizando el **Wine Dataset** incluido en scikit-learn.  
El objetivo principal es:

- Entrenar un modelo de clasificación.
- Interpretar las reglas generadas por el árbol.
- Analizar cómo afecta el parámetro `max_depth` al comportamiento del modelo.
- Evaluar la precisión del clasificador usando datos de prueba.

El Wine Dataset contiene **178 muestras de vino**, cada una con **13 características químicas** y una etiqueta que indica uno de **3 tipos de vino** producidos en Piamonte, Italia.

---

## Proceso del modelo

### 1. Carga del dataset

Se utiliza `load_wine()` para obtener:
- **X**: características químicas (alcohol, flavanoides, proline, etc.)
- **y**: clase del vino (0, 1 o 2)

### 2. División del dataset

Mediante `train_test_split` se divide en:
- 80% datos de entrenamiento  
- 20% datos de prueba  

### 3. Entrenamiento del árbol de decisión

Se entrenó el clasificador variando el parámetro `max_depth`:

- `max_depth = 1`
- `max_depth = 2`
- `max_depth = 3`

Para cada valor se imprimieron las reglas del árbol con `export_text` y se evaluó la precisión del modelo en los datos de prueba.

---

## 📊 Resultados obtenidos

### 🔹 **max_depth = 1**

|--- color_intensity <= 3.82
| |--- class: 1
|--- color_intensity > 3.82
| |--- class: 0

**Precisión:** 0.66  

**Análisis:**  
- El modelo usa solo una característica.  
- Es demasiado simple → bajo rendimiento.  
- Existe **subajuste (underfitting)**.

---

### 🔹 **max_depth = 2**

|--- color_intensity <= 3.82
| |--- proline <= 1002.50 → class 1
| |--- proline > 1002.50 → class 0
|--- color_intensity > 3.82
| |--- flavanoids <= 1.40 → class 2
| |--- flavanoids > 1.40 → class 0

**Precisión:** 0.86  

**Análisis:**  
- Se utilizan más características relevantes.  
- Ahora el modelo distingue bien las tres clases.  
- Buen balance entre interpretabilidad y precisión.

---

### 🔹 **max_depth = 3**

El árbol creció más e incluyó características como **ash** y umbrales más específicos.

**Precisión:** 0.94 (mejor resultado)

**Análisis:**  
- Captura más relaciones del dataset.  
- Aún no muestra sobreajuste evidente.  
- Las reglas siguen siendo lo suficientemente interpretables.

---

## Conclusiones sobre el parámetro `max_depth`

- **Poca profundidad (1):**  
  - Árbol muy simple  
  - Baja precisión (0.6666666666666666)
  - Underfitting  

- **Profundidad media (2–3):**  
  - Reglas completas  
  - Mejor desempeño  
  - Buen equilibrio entre simplicidad y exactitud
  - Exactitud de 2: 0.8611111111111112
  - Exactitud de 3: 0.9444444444444444 

- **Profundidad alta o sin límite (`max_depth=None`):**  
  - El árbol crece demasiado  
  - Las reglas se vuelven largas y difíciles de interpretar  
  - Aparece el **sobreajuste**  

---

## Opinión personal sobre los resultados

Los resultados muestran claramente cómo la profundidad del árbol afecta la calidad del modelo.  
Cuando `max_depth` es muy bajo, el modelo no aprende lo suficiente y su precisión es baja.  
Al aumentar la profundidad, el modelo mejora y las reglas se vuelven más específicas sin perder interpretabilidad.

En mis pruebas, **max_depth = 3** ofreció el mejor equilibrio entre interpretabilidad y precisión. Esto demuestra la importancia de controlar la profundidad para evitar tanto el subajuste como el sobreajuste.

---

## ¿Mi base de conocimiento puede usarse en un árbol de decisión?

**No. Mi proyecto actual no usa árboles de decisión, sino un motor lógico basado en
Resolución SLD, unificación de variables, búsqueda DFS y reglas declarativas.**

Los árboles de decisión requieren:
- atributos numéricos o categóricos simples,
- condiciones tipo “si-entonces” fijas,
- caminos deterministas,
- datos tabulares.

Mi sistema, en cambio:
- usa predicados lógicos,
- maneja variables libres,
- deduce información mediante encadenamiento hacia atrás,
- aplica unificación y renombrado de variables,
- puede generar múltiples soluciones.

Por estas razones, **no es posible convertir la base de conocimiento directamente en un árbol de decisión.**

### ¿Qué cambios serían necesarios?

Para usar un árbol de decisión tendría que transformar toda la base de conocimiento en un dataset estructurado, donde cada trámite sea una fila, cada característica sea una columna y exista una “clase” fija a predecir. Las reglas lógicas tendrían que reemplazarse por atributos explícitos.

### ¿Podría usarse un modelo de regresión?

Solo si la salida deseada es numérica, como tiempo de trámite o costo.  
La mayoría de mis reglas generan categorías, requisitos o decisiones lógicas, por lo que la regresión **no sería adecuada en la mayoría de los casos.**

