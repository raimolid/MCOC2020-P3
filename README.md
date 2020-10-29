# MCOC2020-P3 - Evolución térmica en hormigones masivos

# Entrega 3 - Réplica de la sección 4.5 de la tésis de Alvaro Contreras:

## Modelación de la difución y generación de calor en hormigones masivos por medio de elementos finitos (Contreras, 2020)
## Sección 4.5 - Convergencia y validación

* En esta parte, se procedió a verificar el modelo 1-D usando los mismos parámetros usados por Álvaro Contreras y se analizo la temperatura en 3 distintos nodos (puntos en x) del
elemetos para distintos intervalos de tiempo.

![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x104.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x208.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/x416.png)

* Figura 4.7. Evolución térmica en diferentes dt.

![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x104.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x208.png)
![alt text](https://github.com/raimolid/MCOC2020-P3/blob/main/Mallas_x416.png)

* Figura 4.7. Evolución térmica en diferentes Mallas

## Caso de estudio: Discretización de la condición de borde natural en extremo izquierdo

* Considerando lo visto en el video y con las condicones de borde dadas como :
* CB : du/dx(t,0) = 5    
        u(t,L) = 20
        
* CI : u(0,x) = 20

* Se siguio a hacer la siguiente programación:

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
* El grafico que nos arrojo es el siguiente:

![alt text](https://github.com/jmbarriga1/MCOC2020-P3/blob/main/Figure%20caso%202.png)

* Se puede apreciar que cada 1000 pasos hasta llegar a 50.000 pasos a un intervalo de 2 segundos la grafica si converge a la temperatura de 20 °C.
