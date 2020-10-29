# MCOC2020-P3

## Verificación 1-D

Para la verificación del programa utilizado para el problema 1-D, se replicaron los resultados de la sección 4.5 de la memoria de Contreras. Para esto se comparó la solución analítica, admitida por series de Fourier, con los resultados del programa.

En el programa se usaron los siguientes parámetros utilizados por Contreras:
+ ρ  = 2476 (kg/m3)
+ κ  = 0.001495 (kW/m C)
+ Cp = 1.023 (kJ/kg C)
+ α  = κ/(Cp ρ) (m2/hr)

Primero se estudió la convergencia del método utilizando una malla de 20 elementos, con intervalos de Δt=1(s), Δt=5(s), Δt=10(s), Δt=50(s) y Δt=100(s).

(Gráficos)

Como se puede observar en los resultados replicados, el método converge a la solución analítica sin importar el intervalo utilizado.

Luego, se replicó el segundo caso de estudio, donde se analizó la convergencia utilizando distintas mallas y un Δt=60(s).

(Gráficos)

Como se puede ver en los resultados obtenidos, el error es mayor para las mallas 10, 20 y 40, mientras que para las mallas 60 y 100 el error disminuye, como se puede observar en la siguiente figura.
(Gráfico con zoom)
