import streamlit as st
import math

st.image("https://images.theconversation.com/files/339172/original/file-20200602-133875-1u1teus.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=754&fit=clip", width=500)

st.title("Simulador de neurona")

n_sel = st.slider("Elige el número de entradas/pesos que tendrá la neurona", 1, 10)

st.markdown("### Pesos")
cols_w = st.columns(n_sel) # crear columnas

weights_list = [] # lista para almacenar los pesos
inputs_list = [] # lista para almacenar las entradas

for i, col in enumerate(cols_w): # bucle para meter varios pesos segun lo seleccionado
   weights_list.append(col.number_input(f"w{i}", key=f"weight_{i}"))
st.text(f"w = {weights_list}")

st.markdown("### Entradas")
cols_i = st.columns(n_sel) # crear columnas

for i, col_z in enumerate(cols_i): # bucle para meter varias entradas segun lo seleccionado
   inputs_list.append(col_z.number_input(f"x{i}", key=f"input_{i}"))
st.text(f"i = {inputs_list}")

col1, col2 = st.columns(2)
with col1:
   st.subheader("Sesgo")
   input_sesgo = st.number_input("Introduzca el valor del sesgo")
with col2:
   st.subheader("Función de activación")
   input_func = st.selectbox("Elige la función de activación", ("relu", "sigmoid", "tanh"))

class Neuron:
   def __init__(self, weights, bias, func):
      self.weights = weights
      self.bias = bias
      self.func = func

   def run(self, input_data):
      result = sum(x * w for x, w in zip(input_data, self.weights)) + self.bias # operación de la neurona

      if self.func == "relu": # funciones de activación
         return max(0, result)
      elif self.func == "sigmoid":
         return 1 / (1 + math.exp(-result))
      elif self.func == "tanh":
         return math.tanh(result)
      else:
         raise ValueError("Esta función de activación no es válida")

   def change_bias(self, new_bias):
      self.bias = new_bias

if st.button("Calcular la salida"):
   n1 = Neuron(weights_list, input_sesgo, input_func) # instancia de la neurona
   x = inputs_list
   output = n1.run(input_data=x)
   st.text(f"La salida de la neurona es {output}")