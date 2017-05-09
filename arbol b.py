#Imports
import os

#Pagina
class Pagina():
    def __init__(self):
        self.cuentas=0
        self.rama0 = None
        self.rama1=None
        self.rama2 = None
        self.rama3 = None
        self.rama4 = None
        self.clave0 = None
        self.clave1 = None
        self.clave2 = None
        self.clave3 = None

    def cambiarCuenta(self,cuenta):
        self.cuentas=cuenta

#Clave
class Clave():
    def __init__(self,nombre):
        self.nombre=nombre
        self.archivos=None
        self.carpetas=None

#Arbo B
class ArbolB():
    def __init__(self):
        self. p = None
        self.xder = None
        self.xizq =None
        self.x_clave=None
        self.xr_pag=None
        self.empa=False
        self.esta=False
        self.val=0

    def crearCarpeta(self, clave, nombre):
        clave.carpetas= ArbolB()
        nueva = Clave(nombre)
        clave.carpetas.inserta(nueva)

    #Inserta
    def inserta(self, clave):
        self.insertar(clave, self.p)

    #Insertaa
    def insertar(self,clave,raiz):
        clave,raiz = self.empujar(clave, raiz)
        if self.empa:
            self.p = Pagina()
            self.p.cuentas=1
            self.p.clave0=self.x_clave
            self.p.rama0=raiz
            self.p.rama1=self.xr_pag

    #Empujar
    def empujar(self,clave,raiz):
        k=0
        self.esta=False
        if self.vacio(raiz):
            self.empa=True
            self.x_clave=clave
            self.xr_pag=None
        else:
            k=self.buscarNodo(clave,raiz)
            if self.esta:
                self.empa=False
            else:
                if k==4:
                    self.empujar(clave,raiz.rama4)
                elif k==3:
                    self.empujar(clave,raiz.rama3)
                elif k==2:
                    self.empujar(clave,raiz.rama2)
                elif k==1:
                    self.empujar(clave,raiz.rama1)
                elif k==0:
                    self.empujar(clave,raiz.rama0)
                else:
                    pass

                if self.empa:
                    if raiz.cuentas<4:
                        self.empa=False
                        self.meterHoja(self.x_clave,raiz,k)
                    else:
                        self.empa=True
                        self.dividirN(self.x_clave,raiz,k)
        return clave,raiz

    #DividirN
    def dividirN(self, clave, raiz,k):
        pos=0
        posmda=0
        if k<=2:
            posmda=2
        else:
            posmda=3
        mder= Pagina()
        pos=posmda+1

        while pos!=5:
            vale=pos-posmda-1
            if posmda==2:

                if vale==1:
                    mder.clave1 = raiz.clave3
                    mder.rama2 = raiz.rama4
                elif vale==0:
                    mder.clave0=raiz.clave2
                    mder.rama1=raiz.rama3
                else:
                    pass

            if posmda==3:
                if vale==0:
                    mder.clave0=raiz.clave3
                    mder.rama1 = raiz.rama4
                else:
                    pass
            pos=pos+1

        mder.cuentas = 4-posmda
        raiz.cuentas = posmda

        if k<=2:
            self.meterHoja(clave,raiz,k)
        else:
            self.meterHoja(clave,mder,(k-posmda))

        vale=raiz.cuentas -1

        if vale==3:
            self.x_clave=raiz.clave3
        elif vale==2:
            self.x_clave=raiz.clave2
        elif vale==1:
            self.x_clave=raiz.clave1
        elif vale==0:
            self.x_clave=raiz.clave0
        else:
            pass

        vale=raiz.cuentas

        if vale==4:
            mder.rama0=raiz.rama4
        elif vale==3:
            mder.rama0=raiz.rama3
        elif vale==2:
            mder.rama0=raiz.rama2
        elif vale==1:
            mder.rama0=raiz.rama1
        elif vale==0:
            mder.rama0=raiz.rama0
        else:
            pass

        raiz.cuentas=raiz.cuentas-1
        self.xr_pag=mder

    #MeterHoja
    def meterHoja(self,clave,raiz,k):
        i=raiz.cuentas
        while i!=k:
            if i==3:
                raiz.clave3= raiz.clave2
                raiz.rama4 = raiz.rama3
            elif i==2:
                raiz.clave2= raiz.clave1
                raiz.rama3=raiz.rama2
            elif i==1:
                raiz.clave1 = raiz.clave0
                raiz.rama2=raiz.rama1
            else:
                pass
            i=i-1

        if k==3:
            raiz.clave3 = clave
            raiz.rama4=self.xr_pag
        elif k==2:
            raiz.clave2 = clave
            raiz.rama3=self.xr_pag
        elif k==1:
            raiz.clave1=clave
            raiz.rama2=self.xr_pag
        elif k==0:
            raiz.clave0=clave
            raiz.rama1 = self.xr_pag

        raiz.cuentas = raiz.cuentas+1

    #BuscarNodo
    def buscarNodo(self,clave,raiz):
        j=0
        if clave.nombre<raiz.clave0.nombre:
            self.esta=False
            j=0
        else:
            j=raiz.cuentas
            ii=j
            for x in range(ii,0,-1):
                if raiz.clave3 != None and x==4:
                    if clave.nombre<raiz.clave3.nombre and j>1:
                        j=j-1
                if raiz.clave2!=None and x==3:
                    if clave.nombre<raiz.clave2.nombre and j>1:
                        j=j-1
                if raiz.clave1!=None and x==2:
                    if clave.nombre<raiz.clave1.nombre and j>1:
                        j=j-1
                if raiz.clave0!=None and x==1:
                    if clave.nombre<raiz.clave0.nombre and j>1:
                        j=j-1

            if j==4:
                if raiz.clave3!=None:
                    self.esta=clave.nombre==raiz.clave3.nombre
            elif j==3:
                if raiz.clave2!=None:
                    self.esta=clave.nombre==raiz.clave2.nombre
            elif j==2:
                if raiz.clave1!=None:
                    self.esta=clave.nombre==raiz.clave1.nombre
            elif j==1:
                if raiz.clave0!=None:
                    self.esta=clave.nombre==raiz.clave0.nombre
        return j

    #Miembro
    def miembro(self, clave,raiz):
        si=False
        if self.vacio(self.p)==False:
            if clave.nombre<raiz.clave0.nombre:
                si=False
                j=0
            else:
                j=raiz.cuentas
                ii=j
                for x in range(ii, 1, 1):
                    if raiz.clave3!=None and x==4:
                        if clave.nombre<raiz.clave3.nombre and j>1:
                            j=j-1
                    if raiz.clave2!=None and x==3:
                        if clave.nombre<raiz.clave2.nombre and j>1:
                            j=j-1
                    if raiz.clave1!=None and x==2:
                        if clave.nombre<raiz.clave1.nombre and j>1:
                            j=j-1

                    if j==4:
                        si = clave.nombre==raiz.clave3.nombre
                    elif j==3:
                        si=clave.nombre==raiz.clave2.nombre
                    elif j==2:
                        si=clave.nombre==raiz.clave1.nombre
                    elif j==1:
                        si=clave.nombre==raiz.clave0.nombre
        return si

    #Vacio
    def vacio(self,raiz):
        return (raiz==None or raiz.cuentas==0)

    #Graficar File
    def graficarArbol(self, nodo):
        val=0
        outfile = open('C:\\Users\\KMMG\\Desktop\\arbolb.dot', 'w')
        outfile.write('\ndigraph G {\r\n node [shape=record] ;\n')
        outfile.close()
        self.graficar(nodo,val)
        outfile = open('C:\\Users\\KMMG\\Desktop\\arbolb.dot', 'a')
        outfile.write('}')
        outfile.close()

        os.system("dot -Tpng C:\\Users\\KMMG\\Desktop\\arbolb.dot -o C:\\Users\\KMMG\\Desktop\\arbolb.png")

    #devolver direccione de memoria
    def codificar(self,objeto):
        respuesta = hash(objeto)
        if respuesta<0:
            respuesta= respuesta*(-1)
        return respuesta

    #Graficar_B
    def graficar(self,nodo,val):
        k=0
        c=0
        outfile = open('C:\\Users\\KMMG\\Desktop\\arbolb.dot', 'a')
        outfile.write('Nodo'+str(val)+'[label=\"<P0>')
        while c<4:
            if c==0:
                if nodo.clave0==None:
                    break
            elif c==1:
                if nodo.clave1==None:
                    break
            elif c==2:
                if nodo.clave2==None:
                    break
            elif c==3:
                if nodo.clave3==None:
                    break
            if c==0:
                outfile.write('|'+nodo.clave0.nombre)
                outfile.write('|<P'+str((c+1))+'>')
            elif c==1:
                outfile.write('|' + nodo.clave1.nombre)
                outfile.write('|<P' + str((c + 1)) + '>')
            elif c==2:
                outfile.write('|' + nodo.clave2.nombre)
                outfile.write('|<P' + str((c + 1)) + '>')
            elif c==3:
                outfile.write('|' + nodo.clave4.nombre)
                outfile.write('|<P' + str((c + 1)) + '>')
            c=c+1
        outfile.write('\"];\n')
        pasa = 'Nodo' + str(val)
        while k < 5 and nodo.cuentas >= k:
            if k == 0:
                if nodo.rama0 == None:
                    return
                if nodo.rama0.cuentas == 0:
                    return
            elif k == 1:
                if nodo.rama1 == None:
                    return
                if nodo.rama1.cuentas == 0:
                    return
            elif k == 2:
                if nodo.rama2 == None:
                    return
                if nodo.rama2.cuentas == 0:
                    return
            elif k == 3:
                if nodo.rama3 == None:
                    return
                if nodo.rama3.cuentas == 0:
                    return
            elif k == 4:
                if nodo.rama4 == None:
                    return
                if nodo.rama4.cuentas == 0:
                    return
            val = val + 1
            outfile.write(pasa + ':P' + str(k) + ' -> Nodo' + str(val) + ';\n')
            if k == 0:
                self.recursivoGraf(nodo.rama0, val)
            elif k == 1:
                self.recursivoGraf(nodo.rama1, val)
            elif k == 2:
                self.recursivoGraf(nodo.rama2, val)
            elif k == 3:
                self.recursivoGraf(nodo.rama3, val)
            elif k == 4:
                self.recursivoGraf(nodo.rama4, val)
            k = k + 1

        outfile.close()

    #RecursivoGrafica
    def recursivoGraf(self,nodo,val):
        k = 0
        c = 0
        outfile = open('C:\\Users\\KMMG\\Desktop\\arbolb.dot', 'a')
        outfile.write('Nodo' + str(val) + '[label=\"<P0>')
        while c<4:
            if c!=nodo.cuentas and nodo.cuentas!=0:
                if c==0:
                    if nodo.clave0==None:
                        break
                elif c==1:
                    if nodo.clave1==None:
                        break
                elif c==2:
                    if nodo.clave2==None:
                        break
                elif c==3:
                    if nodo.clave3==None:
                        break

                if c==0:
                    outfile.write('|' + nodo.clave0.nombre)
                    outfile.write('|<P' + str((c + 1)) + '>')
                elif c==1:
                    outfile.write('|' + nodo.clave1.nombre)
                    outfile.write('|<P' + str((c + 1)) + '>')
                elif c==2:
                    outfile.write('|' + nodo.clave2.nombre)
                    outfile.write('|<P' + str((c + 1)) + '>')
                elif c==3:
                    outfile.write('|' + nodo.clave3.nombre)
                    outfile.write('|<P' + str((c + 1)) + '>')
                c=c+1
            else:
                break
        outfile.write('\"];\n')
        pasa = 'Nodo' + str(val)
        while k<5 and nodo.cuentas>=k:
            if k==0:
                if nodo.rama0==None:
                    return
                if nodo.rama0.cuentas==0:
                    return
            elif k==1:
                if nodo.rama1==None:
                    return
                if nodo.rama1.cuentas==0:
                    return
            elif k==2:
                if nodo.rama2==None:
                    return
                if nodo.rama2.cuentas==0:
                    return
            elif k==3:
                if nodo.rama3==None:
                    return
                if nodo.rama3.cuentas==0:
                    return
            elif k==4:
                if nodo.rama4==None:
                    return
                if nodo.rama4.cuentas==0:
                    return
            val=val+1
            outfile.write(pasa+':P'+str(k)+' -> Nodo'+str(val)+';\n')
            if k==0:
                self.recursivoGraf(nodo.rama0,val)
            elif k==1:
                self.recursivoGraf(nodo.rama1,val)
            elif k==2:
                self.recursivoGraf(nodo.rama2,val)
            elif k==3:
                self.recursivoGraf(nodo.rama3,val)
            elif k==4:
                self.recursivoGraf(nodo.rama4,val)
            k=k+1

        outfile.close()

    #Eliminar
    def eliminar(self, clave):
        if self.vacio(self.p):
            print("no hay elementos")
        else:
            self.eliminacion(self.p, clave)

    #Eliminaraa
    def eliminacion(self,raiz,clave):
        try:
            self.eliminarRegistro(raiz,clave)
        except:
            self.esta=False
        if self.esta==False:
            print("No se encontro el elemento")
        else:
            if raiz.cuentas==0:
                raiz=raiz.rama0
            self.p=raiz

    #EliminarRegistro
    def eliminarRegistro(self,raiz, clave):
        pos=0
        sucesor=None
        if self.vacio(raiz):
            self.esta=False
        else:
            pos=self.buscarNodo(clave,raiz)
            if self.esta==True:
                x=pos-1
                if x==4:
                    if self.vacio(raiz.rama4):
                        self.quitar(raiz,pos)
                    else:
                        self.sucesor(raiz,pos)
                        if pos==4:
                            self.eliminarRegistro(raiz.rama4,raiz.clave3)
                        elif pos==3:
                            self.eliminarRegistro(raiz.rama3,raiz.clave2)
                        elif pos==2:
                            self.eliminarRegistro(raiz.rama2,raiz.clave1)
                        elif pos==1:
                            self.eliminarRegistro(raiz.rama1,raiz.clave0)
                elif x==3:
                    if self.vacio(raiz.rama3):
                        self.quitar(raiz,pos)
                    else:
                        self.sucesor(raiz,pos)
                        if pos==4:
                            self.eliminarRegistro(raiz.rama4,raiz.clave3)
                        elif pos==3:
                            self.eliminarRegistro(raiz.rama3,raiz.clave2)
                        elif pos==2:
                            self.eliminarRegistro(raiz.rama2,raiz.clave1)
                        elif pos==1:
                            self.eliminarRegistro(raiz.rama1,raiz.clave0)
                elif x==2:
                    if self.vacio(raiz.rama2):
                        self.quitar(raiz,pos)
                    else:
                        self.sucesor(raiz,pos)
                        if pos==4:
                            self.eliminarRegistro(raiz.rama4,raiz.clave3)
                        elif pos==3:
                            self.eliminarRegistro(raiz.rama3,raiz.clave2)
                        elif pos==2:
                            self.eliminarRegistro(raiz.rama2,raiz.clave1)
                        elif pos==1:
                            self.eliminarRegistro(raiz.rama1,raiz.clave0)
                elif x==1:
                    if self.vacio(raiz.rama1):
                        self.quitar(raiz,pos)
                    else:
                        self.sucesor(raiz,pos)
                        if pos==4:
                            self.eliminarRegistro(raiz.rama4,raiz.clave3)
                        elif pos==3:
                            self.eliminarRegistro(raiz.rama3,raiz.clave2)
                        elif pos==2:
                            self.eliminarRegistro(raiz.rama2,raiz.clave1)
                        elif pos==1:
                            self.eliminarRegistro(raiz.rama1,raiz.clave0)
                elif x==0:
                    if self.vacio(raiz.rama0):
                        self.quitar(raiz,pos)
                    else:
                        self.sucesor(raiz,pos)
                        if pos==4:
                            self.eliminarRegistro(raiz.rama4,raiz.clave3)
                        elif pos==3:
                            self.eliminarRegistro(raiz.rama3,raiz.clave2)
                        elif pos==2:
                            self.eliminarRegistro(raiz.rama2,raiz.clave1)
                        elif pos==1:
                            self.eliminarRegistro(raiz.rama1,raiz.clave0)
            else:
                if pos==4:
                    self.eliminarRegistro(raiz.rama4,clave)
                elif pos==3:
                    self.eliminarRegistro(raiz.rama3,clave)
                elif pos==2:
                    self.eliminarRegistro(raiz.rama2,clave)
                elif pos==1:
                    self.eliminarRegistro(raiz.rama1,clave)
                elif pos==0:
                    self.eliminarRegistro(raiz.rama0,clave)

                if pos==4:
                    if raiz.rama4!=None and raiz.rama4.cuentas<2:
                        self.restablecer(raiz,pos)
                elif pos==3:
                    if raiz.rama3!=None and raiz.rama3.cuentas<2:
                        self.restablecer(raiz,pos)
                elif pos==2:
                    if raiz.rama2!=None and raiz.rama2.cuentas<2:
                        self.restablecer(raiz,pos)
                elif pos==1:
                    if raiz.rama1!=None and raiz.rama1.cuentas<2:
                        self.restablecer(raiz,pos)
                elif pos==0:
                    if raiz.rama0!=None and raiz.rama0.cuentas<2:
                        self.restablecer(raiz,pos)

    #Sucesor
    def sucesor(self,raiz,k):
        q=None
        if k==4:
            q=raiz.rama4
        elif k==3:
            q=raiz.rama3
        elif k==2:
            q=raiz.rama2
        elif k==1:
            q=raiz.rama1
        elif k==0:
            q=raiz.rama0

        while self.vacio(q.rama0)==False:
            q=q.rama0
        if k==4:
            raiz.clave3=q.clave0
        elif k==3:
            raiz.clave2 = q.clave0
        elif k==2:
            raiz.clave1 = q.clave0
        elif k==1:
            raiz.clave0 = q.clave0

    #Quitar
    def quitar(self,raiz, pos):
        j=pos+1
        while j!= (raiz.cuentas+1):
            if j==4:
                raiz.clave2=raiz.clave3
                raiz.rama3=raiz.rama4
            elif j==3:
                raiz.clave1=raiz.clave2
                raiz.rama2=raiz.rama3
            elif j==2:
                raiz.clave0=raiz.clave1
                raiz.rama1=raiz.rama2
            elif j==1:
                break
            elif j==0:
                break
            j=j+1
        raiz.cuentas=raiz.cuentas-1

    #Restablecer
    def restablecer(self,raiz, pos):
        if pos>0:
            if pos==4:
                if raiz.rama3.cuentas>2:
                    self.movDer(raiz,pos)
                else:
                    self.combina(raiz,pos)
            elif pos==3:
                if raiz.rama2.cuentas>2:
                    self.movDer(raiz,pos)
                else:
                    self.combina(raiz,pos)
            elif pos==2:
                if raiz.rama1.cuentas>2:
                    self.movDer(raiz,pos)
                else:
                    self.combina(raiz,pos)
            elif pos==1:
                if raiz.rama0.cuentas>2:
                    self.movDer(raiz,pos)
                else:
                    self.combina(raiz,pos)
        elif raiz.rama1.cuentas>2:
            self.movIzq(raiz,1)
        else:
            self.combina(raiz,1)

    #Combina
    def combina(self,raiz,pos):
        if pos==4:
            self.xder=raiz.rama4
        elif pos==3:
            self.xder=raiz.rama3
        elif pos==2:
            self.xder=raiz.rama2
        elif pos==1:
            self.xder=raiz.rama1
        elif pos==0:
            self.xder=raiz.rama0
        z=pos-1
        if z==4:
            self.xizq=raiz.rama4
        elif z==3:
            self.xizq=raiz.rama3
        elif z==2:
            self.xizq=raiz.rama2
        elif z==1:
            self.xizq=raiz.rama1
        elif z==0:
            self.xizq=raiz.rama0
        self.xizq.cuentas=self.xizq.cuentas+1
        m=self.xizq-1
        n=pos-1
        if m==3:
            if n==3:
                self.xizq.clave3=raiz.clave3
            elif n==2:
                self.xizq.clave3 = raiz.clave2
            elif n==1:
                self.xizq.clave3 = raiz.clave1
            elif n==0:
                self.xizq.clave3 = raiz.clave0
        elif m==2:
            if n==3:
                self.xizq.clave2=raiz.clave3
            elif n==2:
                self.xizq.clave2 = raiz.clave2
            elif n==1:
                self.xizq.clave2 = raiz.clave1
            elif n==0:
                self.xizq.clave2 = raiz.clave0
        elif m==1:
            if n==3:
                self.xizq.clave1=raiz.clave3
            elif n==2:
                self.xizq.clave1 = raiz.clave2
            elif n==1:
                self.xizq.clave1 = raiz.clave1
            elif n==0:
                self.xizq.clave1 = raiz.clave0
        elif m==0:
            if n==3:
                self.xizq.clave0=raiz.clave3
            elif n==2:
                self.xizq.clave0 = raiz.clave2
            elif n==1:
                self.xizq.clave0 = raiz.clave1
            elif n==0:
                self.xizq.clave0 = raiz.clave0
        r=self.xizq.cuentas
        if r==4:
            self.xizq.rama4=self.xder.rama0
        elif r==3:
            self.xizq.rama3 = self.xder.rama0
        elif r==2:
            self.xizq.rama2 = self.xder.rama0
        elif r==1:
            self.xizq.rama1 = self.xder.rama0
        elif r==0:
            self.xizq.rama0 = self.xder.rama0
        j=1
        while (j != (self.xder.cuentas + 1)):
            self.xizq.cuentas=self.xizq.cuentas+1
            t=self.xizq.cuentas - 1
            q=j-1
            if t==3:
                if q==3:
                    self.xizq.clave3=self.xder.clave3
                    self.xizq.rama4=self.xder.rama4
                elif q==2:
                    self.xizq.clave3 = self.xder.clave2
                    self.xizq.rama4 = self.xder.rama3
                elif q==1:
                    self.xizq.clave3 = self.xder.clave1
                    self.xizq.rama4 = self.xder.rama2
                elif q==0:
                    self.xizq.clave3 = self.xder.clave0
                    self.xizq.rama4 = self.xder.rama1
            elif t==2:
                if q==3:
                    self.xizq.clave2=self.xder.clave3
                    self.xizq.rama3=self.xder.rama4
                elif q==2:
                    self.xizq.clave2 = self.xder.clave2
                    self.xizq.rama3 = self.xder.rama3
                elif q==1:
                    self.xizq.clave2 = self.xder.clave1
                    self.xizq.rama3 = self.xder.rama2
                elif q==0:
                    self.xizq.clave2 = self.xder.clave0
                    self.xizq.rama3 = self.xder.rama1
            elif t==1:
                if q==3:
                    self.xizq.clave1=self.xder.clave3
                    self.xizq.rama2=self.xder.rama4
                elif q==2:
                    self.xizq.clave1 = self.xder.clave2
                    self.xizq.rama2 = self.xder.rama3
                elif q==1:
                    self.xizq.clave1 = self.xder.clave1
                    self.xizq.rama2 = self.xder.rama2
                elif q==0:
                    self.xizq.clave1 = self.xder.clave0
                    self.xizq.rama2 = self.xder.rama1
            elif t==0:
                if q==3:
                    self.xizq.clave0=self.xder.clave3
                    self.xizq.rama1=self.xder.rama4
                elif q==2:
                    self.xizq.clave0 = self.xder.clave2
                    self.xizq.rama1 = self.xder.rama3
                elif q==1:
                    self.xizq.clave0 = self.xder.clave1
                    self.xizq.rama1 = self.xder.rama2
                elif q==0:
                    self.xizq.clave0 = self.xder.clave0
                    self.xizq.rama1 = self.xder.rama1
            j=j+1
        self.quitar(raiz,pos)

    #MoverDer
    def movDer(self,raiz, pos):

        i=0
        if pos==4:
            i=raiz.rama4.cuentas
        elif pos==3:
            i = raiz.rama3.cuentas
        elif pos==2:
            i = raiz.rama2.cuentas
        elif pos==1:
            i = raiz.rama1.cuentas
        elif pos==0:
            i = raiz.rama0.cuentas

        while(i!=0):
            if i==3:
                if pos==4:
                    raiz.rama4.clave3 = raiz.rama4.clave2
                    raiz.rama4.rama4 = raiz.rama4.rama3
                elif pos==3:
                    raiz.rama3.clave3 = raiz.rama3.clave2
                    raiz.rama3.rama4 = raiz.rama3.rama3
                elif pos==2:
                    raiz.rama2.clave3 = raiz.rama2.clave2
                    raiz.rama2.rama4 = raiz.rama2.rama3
                elif pos==1:
                    raiz.rama1.clave3 = raiz.rama1.clave2
                    raiz.rama1.rama4 = raiz.rama1.rama3
                elif pos==0:
                    raiz.rama0.clave3 = raiz.rama0.clave2
                    raiz.rama0.rama4 = raiz.rama0.rama3
            elif i==2:
                if pos==4:
                    raiz.rama4.clave2 = raiz.rama4.clave1
                    raiz.rama4.rama3 = raiz.rama4.rama2
                elif pos==3:
                    raiz.rama3.clave2 = raiz.rama3.clave1
                    raiz.rama3.rama3 = raiz.rama3.rama2
                elif pos==2:
                    raiz.rama2.clave2 = raiz.rama2.clave1
                    raiz.rama2.rama3 = raiz.rama2.rama2
                elif pos==1:
                    raiz.rama1.clave2 = raiz.rama1.clave1
                    raiz.rama1.rama3 = raiz.rama1.rama2
                elif pos==0:
                    raiz.rama0.clave2 = raiz.rama0.clave1
                    raiz.rama0.rama3 = raiz.rama0.rama2
            elif i==1:
                if pos==4:
                    raiz.rama4.clave1 = raiz.rama4.clave0
                    raiz.rama4.rama2 = raiz.rama4.rama1
                elif pos==3:
                    raiz.rama3.clave1 = raiz.rama3.clave0
                    raiz.rama3.rama2 = raiz.rama3.rama1
                elif pos==2:
                    raiz.rama2.clave1 = raiz.rama2.clave0
                    raiz.rama2.rama2 = raiz.rama2.rama1
                elif pos==1:
                    raiz.rama1.clave1 = raiz.rama1.clave0
                    raiz.rama1.rama2 = raiz.rama1.rama1
                elif pos==0:
                    raiz.rama0.clave1 = raiz.rama0.clave0
                    raiz.rama0.rama2 = raiz.rama0.rama1
            i=i-1

        if pos==4:
            raiz.rama4.cuentas=raiz.rama4.cuentas + 1
            raiz.rama4.rama1 = raiz.rama4.rama0
            raiz.rama4.clave0 = raiz.clave3

            a= raiz.rama3.cuentas - 1
            if a==3:
                raiz.clave3=raiz.rama3.clave3
            elif a==2:
                raiz.clave3=raiz.rama3.clave2
            elif a==1:
                raiz.clave3 = raiz.rama3.clave1
            elif a==0:
                raiz.clave3 = raiz.rama3.clave0

            a=raiz.rama3.cuentas - 1
            if a==3:
                raiz.clave3=raiz.rama3.clave3
            elif a==2:
                raiz.clave3 = raiz.rama3.clave2
            elif a==1:
                raiz.clave3 = raiz.rama3.clave1
            elif a==0:
                raiz.clave3 = raiz.rama3.clave0

            a=raiz.rama3.cuentas
            if a==4:
                raiz.rama4.rama0=raiz.rama3.rama4
            elif a==3:
                raiz.rama4.rama0 = raiz.rama3.rama3
            elif a==2:
                raiz.rama4.rama0 = raiz.rama3.rama2
            elif a==1:
                raiz.rama4.rama0 = raiz.rama3.rama1
            elif a==0:
                raiz.rama4.rama0 = raiz.rama3.rama0

            raiz.rama3.cuentas = raiz.rama3.cuentas - 1

        elif pos==3:
            raiz.rama3.cuentas = raiz.rama3.cuentas + 1
            raiz.rama3.rama1 = raiz.rama3.rama0
            raiz.rama3.clave0 = raiz.clave2

            a = raiz.rama2.cuentas - 1
            if a == 3:
                raiz.clave2 = raiz.rama2.clave3
            elif a == 2:
                raiz.clave2 = raiz.rama2.clave2
            elif a == 1:
                raiz.clave2 = raiz.rama2.clave1
            elif a == 0:
                raiz.clave2 = raiz.rama2.clave0

            a = raiz.rama2.cuentas
            if a == 4:
                raiz.rama3.rama0 = raiz.rama2.rama4
            elif a == 3:
                raiz.rama3.rama0 = raiz.rama2.rama3
            elif a == 2:
                raiz.rama3.rama0 = raiz.rama2.rama2
            elif a == 1:
                raiz.rama3.rama0 = raiz.rama2.rama1
            elif a == 0:
                raiz.rama3.rama0 = raiz.rama2.rama0

            raiz.rama2.cuentas = raiz.rama2.cuentas - 1

        elif pos==2:
            raiz.rama2.cuentas = raiz.rama2.cuentas + 1
            raiz.rama2.rama1 = raiz.rama2.rama0
            raiz.rama2.clave0 = raiz.clave1

            a = raiz.rama1.cuentas - 1
            if a == 3:
                raiz.clave1 = raiz.rama1.clave3
            elif a == 2:
                raiz.clave1 = raiz.rama1.clave2
            elif a == 1:
                raiz.clave1 = raiz.rama1.clave1
            elif a == 0:
                raiz.clave1 = raiz.rama1.clave0

            a = raiz.rama1.cuentas
            if a == 4:
                raiz.rama2.rama0 = raiz.rama1.rama4
            elif a == 3:
                raiz.rama2.rama0 = raiz.rama1.rama3
            elif a == 2:
                raiz.rama2.rama0 = raiz.rama1.rama2
            elif a == 1:
                raiz.rama2.rama0 = raiz.rama1.rama1
            elif a == 0:
                raiz.rama2.rama0 = raiz.rama1.rama0

            raiz.rama1.cuentas = raiz.rama1.cuentas - 1

        elif pos==1:
            raiz.rama1.cuentas = raiz.rama1.cuentas + 1
            raiz.rama1.rama1 = raiz.rama1.rama0
            raiz.rama1.clave0 = raiz.clave0

            a = raiz.rama0.cuentas - 1
            if a == 3:
                raiz.clave0 = raiz.rama0.clave3
            elif a == 2:
                raiz.clave0 = raiz.rama0.clave2
            elif a == 1:
                raiz.clave0 = raiz.rama0.clave1
            elif a == 0:
                raiz.clave0 = raiz.rama0.clave0

            a = raiz.rama0.cuentas
            if a == 4:
                raiz.rama1.rama0 = raiz.rama0.rama4
            elif a == 3:
                raiz.rama1.rama0 = raiz.rama0.rama3
            elif a == 2:
                raiz.rama1.rama0 = raiz.rama0.rama2
            elif a == 1:
                raiz.rama1.rama0 = raiz.rama0.rama1
            elif a == 0:
                raiz.rama1.rama0 = raiz.rama0.rama0

            raiz.rama0.cuentas = raiz.rama0.cuentas - 1

    #MoverIzq
    def movIzq(self,raiz,pos):
        i=0
        posv=0
        if pos==4:
            posv = raiz.rama4.cuentas + 1
            raiz.rama4.cuentas = raiz.rama4.cuentas + 1
            a = raiz.rama3.cuentas - 1
            if a==3:
                raiz.rama3.clave3 = raiz.clave3
                raiz.rama3.rama4 = raiz.rama4.rama0
            elif a==2:
                raiz.rama3.clave2 = raiz.clave3
                raiz.rama3.rama2 = raiz.rama4.rama0
            elif a==1:
                raiz.rama3.clave1 = raiz.clave3
                raiz.rama3.rama1 = raiz.rama4.rama0
            elif a==0:
                raiz.rama3.clave0= raiz.clave3
                raiz.rama3.rama0 = raiz.rama4.rama0
            raiz.clave3 = raiz.rama4.clave0
            raiz.rama4.rama0 = raiz.rama4.rama1
            raiz.rama4.cuentas = raiz.rama4.cuentas-1
            i = 1
        elif pos==3:
            posv = raiz.rama3.cuentas + 1
            raiz.rama3.cuentas = raiz.rama3.cuentas + 1
            a = raiz.rama2.cuentas - 1
            if a == 3:
                raiz.rama2.clave3 = raiz.clave2
                raiz.rama2.rama4 = raiz.rama3.rama0
            elif a == 2:
                raiz.rama2.clave2 = raiz.clave2
                raiz.rama2.rama2 = raiz.rama3.rama0
            elif a == 1:
                raiz.rama2.clave1 = raiz.clave2
                raiz.rama2.rama1 = raiz.rama3.rama0
            elif a == 0:
                raiz.rama2.clave0 = raiz.clave2
                raiz.rama2.rama0 = raiz.rama3.rama0
            raiz.clave2 = raiz.rama3.clave0
            raiz.rama3.rama0 = raiz.rama3.rama1
            raiz.rama3.cuentas = raiz.rama3.cuentas - 1
            i = 1
        elif pos==2:
            posv = raiz.rama2.cuentas + 1
            raiz.rama2.cuentas = raiz.rama2.cuentas + 1
            a = raiz.rama1.cuentas - 1
            if a == 3:
                raiz.rama1.clave3 = raiz.clave1
                raiz.rama1.rama4 = raiz.rama2.rama0
            elif a == 2:
                raiz.rama1.clave2 = raiz.clave1
                raiz.rama1.rama2 = raiz.rama2.rama0
            elif a == 1:
                raiz.rama1.clave1 = raiz.clave1
                raiz.rama1.rama1 = raiz.rama2.rama0
            elif a == 0:
                raiz.rama1.clave0 = raiz.clave1
                raiz.rama1.rama0 = raiz.rama2.rama0
            raiz.clave1 = raiz.rama2.clave0
            raiz.rama2.rama0 = raiz.rama2.rama1
            raiz.rama2.cuentas = raiz.rama2.cuentas - 1
            i = 1
        elif pos==1:
            #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQUI CAMBIE  CODIGO ORIGINAL  de raiz.rama0.clave3 = raiz.clave1 a =raiz.clave0
            posv = raiz.rama1.cuentas + 1
            raiz.rama1.cuentas = raiz.rama1.cuentas + 1
            a = raiz.rama0.cuentas - 1
            if a == 3:
                raiz.rama0.clave3 = raiz.clave1
                raiz.rama0.rama4 = raiz.rama1.rama0
            elif a == 2:
                raiz.rama0.clave2 = raiz.clave1
                raiz.rama0.rama2 = raiz.rama1.rama0
            elif a == 1:
                raiz.rama0.clave1 = raiz.clave1
                raiz.rama0.rama1 = raiz.rama1.rama0
            elif a == 0:
                raiz.rama0.clave0 = raiz.clave1
                raiz.rama0.rama0 = raiz.rama1.rama0
            raiz.clave0 = raiz.rama1.clave0
            raiz.rama1.rama0 = raiz.rama1.rama1
            raiz.rama1.cuentas = raiz.rama1.cuentas - 1
            i = 1
        elif pos==0:
            pass
        while i!=posv:
            if pos==0:
                if i==1:
                    raiz.rama0.clave0 = raiz.rama0.clave1
                    raiz.rama0.rama1 = raiz.rama0.rama2
                elif i==2:
                    raiz.rama0.clave1 = raiz.rama0.clave2
                    raiz.rama0.rama2 = raiz.rama0.rama3
                elif i==3:
                    raiz.rama0.clave2 = raiz.rama0.clave3
                    raiz.rama0.rama3 = raiz.rama0.rama4
            elif pos==1:
                if i==1:
                    raiz.rama1.clave0 = raiz.rama1.clave1
                    raiz.rama1.rama1 = raiz.rama1.rama2
                elif i==2:
                    raiz.rama1.clave1 = raiz.rama1.clave2
                    raiz.rama1.rama2 = raiz.rama1.rama3
                elif i==3:
                    raiz.rama1.clave2 = raiz.rama1.clave3
                    raiz.rama1.rama3 = raiz.rama1.rama4
            elif pos==2:
                if i==1:
                    raiz.rama2.clave0 = raiz.rama2.clave1
                    raiz.rama2.rama1 = raiz.rama2.rama2
                elif i==2:
                    raiz.rama2.clave1 = raiz.rama2.clave2
                    raiz.rama2.rama2 = raiz.rama2.rama3
                elif i==3:
                    raiz.rama2.clave2 = raiz.rama2.clave3
                    raiz.rama2.rama3 = raiz.rama2.rama4
            elif pos==3:
                if i==1:
                    raiz.rama3.clave0 = raiz.rama3.clave1
                    raiz.rama3.rama1 = raiz.rama3.rama2
                elif i==2:
                    raiz.rama3.clave1 = raiz.rama3.clave2
                    raiz.rama3.rama2 = raiz.rama3.rama3
                elif i==3:
                    raiz.rama3.clave2 = raiz.rama3.clave3
                    raiz.rama3.rama3 = raiz.rama3.rama4
            elif pos==4:
                if i==1:
                    raiz.rama4.clave0 = raiz.rama4.clave1
                    raiz.rama4.rama1 = raiz.rama4.rama2
                elif i==2:
                    raiz.rama4.clave1 = raiz.rama4.clave2
                    raiz.rama4.rama2 = raiz.rama4.rama3
                elif i==3:
                    raiz.rama4.clave2 = raiz.rama4.clave3
                    raiz.rama4.rama3 = raiz.rama4.rama4
            i=i+1



arbolb = ArbolB()
nueva = Clave('10')
arbolb.inserta(nueva)
nueva = Clave('20')
arbolb.inserta(nueva)
nueva = Clave('30')
arbolb.inserta(nueva)
nueva = Clave('40')
arbolb.inserta(nueva)
nueva = Clave('25')
arbolb.inserta(nueva)
nueva = Clave('15')
arbolb.inserta(nueva)
nueva = Clave('35')
arbolb.inserta(nueva)
nueva = Clave('05')
arbolb.inserta(nueva)
nueva = Clave('45')
arbolb.inserta(nueva)
nueva = Clave('11')
arbolb.inserta(nueva)
nueva = Clave('17')
arbolb.inserta(nueva)
nueva = Clave('43')
arbolb.inserta(nueva)
arbolb.graficarArbol(arbolb.p)

#arbolb.crearCarpeta(nueva,"prueba sub1")
#nueva.carpetas.graficarArbol(nueva.carpetas.p)