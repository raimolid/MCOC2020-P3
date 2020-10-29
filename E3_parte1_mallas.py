from matplotlib.pylab import *

L = 1.04 #m
ns = [10,20,40,60,100] #Malla 20

#Arreglo con la solucion
Nt = 100000 # s => +25 hr
dt = 60

#Propiedades
K = 0.001495	     #kJ/m hr C
c = 1.023      	 #kJ/kg C
ρ = 2476   	     #kg/m3
  
xs = [0.104,0.208,0.416]
xu = [1,2,4,6,10,2,4,8,12,20,4,8,16,24,40]
contador = 0

for x in xs:
	
	figure()
	
	for n in ns:
		
		#Modelo 1-D
		dx = L / n
		T = Nt//dt
		u = zeros((T, n+1))
		
		#CB
		u_izq = 0
		u_der = 0
		u_ini = 20
		
		u[:,0] = u_izq
		u[:,-1] = u_der
		
		#Cond inicial
		u[0,1:n] = u_ini
		
		α = K*dt/(c*ρ*dx**2)
		
		for k in range(T-1):
			t = dt*k
			for i in range(1,n):	
				u[k+1,i]=u[k,i]+α*(u[k,i+1]-2*u[k,i]+u[k,i-1])
		
		
		tiempo = linspace(0,Nt,T)
		plot(tiempo,u[:,xu[contador]], label = f"M{n}: Malla {n}")	
		contador += 1
	#Serie de Fourier	
	α = K/(c*ρ) #m2/hr
	u_fourier = []
	
	for ti in range(Nt):
		fourier = 0
		for ni in range(1,50):
			fourier += 40*(1-(-1)**ni)/(ni*pi)*sin(ni*pi*x/L)*exp(-α*(ni*pi/L)**2*ti)
		u_fourier.append(fourier)
	
	tiempo_f = linspace(0,Nt,Nt)
	plot(tiempo_f,u_fourier,label = "Serie de Fourier",color = 'black', linestyle='--' )	
		
	title(f"x = {x}")
	plt.xticks([18000,36000,54000,72000,90000],["5","10","15","20","25"])
	plt.ylabel("Temperatura [C]")
	plt.xlabel("Tiempo [horas]")
	plt.legend()
	grid()
	show()