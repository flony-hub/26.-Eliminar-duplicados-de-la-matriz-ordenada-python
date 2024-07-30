# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:01:30 2024

@author: auten
"""

class Solution:
    def removeDuplicate(self, nums):
        # Crea una nueva lista para almacenar los elementos únicos
        lista_resultado = []
        for i in range(len(nums)):
            elemento = nums[i]
            # Verifica si el elemento ya está en la lista_resultado
            if elemento not in lista_resultado:
                lista_resultado.append(elemento)
        # Calcula la cantidad de guiones bajos necesarios
        guiones_bajos = len(nums) - len(lista_resultado)
        # Agrega los guiones bajos al final de la lista_resultado
        lista_resultado.extend(["_"] * guiones_bajos)
        # Devuelve la longitud de la lista_resultado y la lista_resultado
        return len(lista_resultado), lista_resultado

nums = [1, 1, 2]
objeto = Solution()
entero_resultado, lista_resultado = objeto.removeDuplicate(nums)

print(f"Entero: {entero_resultado}")
print(f"Lista: {lista_resultado}")
