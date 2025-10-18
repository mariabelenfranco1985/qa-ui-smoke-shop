
#FORMULAS CONDICIONALES

#Las condicionales en Python sirven para que el programa tome decisiones.
#Permiten ejecutar un bloque de código solo si se cumple una condición.

#👉 En palabras simples:
#“Si algo pasa, entonces hacé esto; si no, hacé otra cosa.”

#Python usa las siguientes palabras clave:

#if → significa si

#elif → significa sino si (para evaluar otra condición)

#else → significa en caso contrario



#🩵 Condicional simple
edad = 20

if edad >= 18:
    print("Sos mayor de edad ✅")
else:
    print("Sos menor de edad ❌")


#🖥️ Resultado:

#Sos mayor de edad ✅

#🔍 Explicación:

#if edad >= 18: → verifica si la edad es 18 o más.

#Si es verdadero, imprime "Sos mayor de edad ✅".



#🧠 FORMULAS CONDICIONALES ANIDADAS:

#Las condicionales anidadas se usan cuando necesitás tomar una decisión dentro de otra.
#Es decir, primero se cumple una condición general, y dentro de esa, verificás otra más específica.

#🩵 En palabras simples:

#“Si pasa esto... y además pasa esto otro... entonces hacé tal cosa.”

#Por ejemplo, si alguien es mayor de edad, podés preguntar además si tiene un permiso para manejar.



#PALABRAS CLAVE

#IF → significa si

#ELIF → significa sino si (para evaluar otra condición)

#ELSE → significa en caso contrario

#🔹 Estructura general:
#IF condicion:
    # código si la CONDICION VERDADERA

#ELIF otra_condicion:
    # código si la primera fue falsa pero esta es verdadera
#eELSE:
    # código si ninguna condición se cumple

#🪄 2. INSTRUCCIONES PASO A PASO

#Escribí un pequeño bloque con if, elif y else.

#Asegurate de usar la indentación correcta (4 espacios o una tabulación después de cada :).

#Probalo cambiando los valores para ver qué rama se ejecuta.

#Ejecutá el código para ver el resultado en la consola.

#💡 3. Ejemplo práctico:

edad = 20
tiene_licencia = True

if edad >= 18:
    if tiene_licencia:
        print("Podés manejar un auto")
    else:
        print("Sos mayor de edad, pero no tenés licencia")
else:
    print("No podés manejar, sos menor de edad ")




#EXPLICACION POR LINEA

#edad = 20 → guardamos la edad de la persona.

#tiene_licencia = True → significa que sí tiene licencia.

#if edad >= 18: → si tiene 18 o más años...

#if tiene_licencia: → si además tiene licencia, se imprime “Podés manejar un auto”.

#else: → si no tiene licencia, se imprime “Sos mayor de edad, pero no tenés licencia”.

#else: → si no tiene 18 años, se imprime “No podés manejar, sos menor de edad”.

#🖥️ Resultado:

#Podés manejar un auto 🚗

#4.EJERCICIO PRACTICO

#Escribí un programa que diga si una persona puede entrar a una fiesta:

#Solo pueden entrar si tienen 18 años o más.

#Si tiene más de 18 años, preguntá si tiene invitación:

#Si tiene invitación, mostrar: "Bienvenido a la fiesta 🎉".

#Si no tiene invitación, mostrar: "Lo siento, necesitás invitación 🚫".

#Si es menor de edad, mostrar: "No podés entrar, sos menor ❌".

#💬 Pista: necesitás usar un if dentro de otro if.