# MCOC2020-P3 - Evolución térmica en hormigones masivos

# Entrega 3 - Réplica de la sección 4.5 de la tésis de Alvaro Contreras:

## Modelación de la difución y generación de calor en hormigones masivos por medio de elementos finitos (Contreras, 2020)
## Sección 4.5 - Convergencia y validación

* Para la verificación del programa utilizado para el problema 1-D, se replicaron los resultados de la sección 4.5 de la memoria de Contreras. Para esto se comparó la solución analítica, admitida por series de Fourier, con los resultados del programa.

En el programa se usaron los siguientes parámetros utilizados por Contreras:
+ ρ  = 2476 (kg/m3)
+ κ  = 0.001495 (kW/m hr C)
+ Cp = 1.023 (kJ/kg C)
+ α  = κ/(Cp ρ) (m2/hr)

Primero se estudió la convergencia del método utilizando una malla de 20 elementos, con intervalos de Δt=1(s), Δt=5(s), Δt=10(s), Δt=50(s) y Δt=100(s).

![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x104.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x208.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x416.png)

Como se puede observar en los resultados replicados, el método converge a la solución analítica sin importar el intervalo utilizado.

Luego, se replicó el segundo caso de estudio, donde se analizó la convergencia utilizando distintas mallas y un Δt=60(s).

![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x104.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x208.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x416.png)

Como se puede ver en los resultados obtenidos, el error es mayor para las mallas 10, 20 y 40, mientras que para las mallas 60 y 100 el error disminuye, como se puede observar en la siguiente figura.

![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/zoom.jpeg)



## Caso de estudio: Discretización de la condición de borde natural en extremo izquierdo

*
*
```
 from matplotlib.pylab import *

L=1.0
n=100   #discretizacion de intervalos
dx=L/n

x=linspace(0,L,n+1)

# Arreglo con la solución 
dt=2.
Nt=50000
tt=arange(0,Nt,dt)
u_k=zeros((n+1))
u_km1=zeros((n+1))


#Condicion inicial todos parten en 20
u_k[:]=20

K=79.5  #m2/s
c=450  #J/ kg C
p=7800  #kg/m3
alpha=K*dt/(c*p*dx**2)


for k in range(Nt-1):
    t=dt*k
    print(f'k={k} t={t}')
    
    #En cada paso CB
    u_k[-1]= 20          #borde der
    u_k[0]= u_k[1]-5*dx  #borde izq
    
    
    for i in range(1,n):
        u_km1[i]=u_k[i]+alpha*(u_k[i+1]-2*u_k[i]+u_k[i-1])
    
    Nplot=1000
    Nskip=3    
    if k % Nplot == 0:     #Graficar cada 1000 pasos
        plot(x,u_k[:])
        
    
    if k%(Nskip*Nplot)==0:
        text(x[0],u_k[0],f"{t/3600:.1f}",
             fontsize=8,
             horizontalalignment="center",
             verticalalignment="center",
             ).set_bbox(dict(facecolor='white', alpha=0.4, edgecolor='black',boxstyle='round'))
    u_k=u_km1 
           
title('k={} t={} s'.format(k,k*dt)) 
xlabel('Distancia, $x$ (m)')
ylabel('Temperature, $T$ (°C)')  
show()

    
```
