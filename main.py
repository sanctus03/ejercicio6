import statistics as st
data = list()
for indice in range(3):
    data.append(float(input("siguiente dato?: ")))

dato1= st.mean(data)
print("media: ", dato1)

dato2= st.median(data)
print("mediana: ", dato2)

dato3= st.variance(data)
print("varianza: ",dato3)