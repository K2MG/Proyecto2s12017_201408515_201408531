# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
escritorio = os.path.expanduser("~/Desktop")
from bitarray import bitarray
#----------------------------------------------------------------------------------------------
class nodoArchivo:
    def __init__(self, nombreArchivo, bitArray):
        self.nombreArchivo = nombreArchivo
        self.archivo = bitArray
        self.izquierdo = None
        self.derecho = None
        self.fe = 0
class AVL:
    def __init__(self):
        self.raizG=None
    def esHoja(self, nodo):
        if nodo==None:
            return False
        if nodo.derecho!=None or nodo.izquierdo!=None:
            return False
        return True
    def factorEquilibrio(self, raiz):
        if raiz==None:
            return raiz, 0
        if self.esHoja(raiz):
            raiz.fe = 0
            return raiz, 1
        elif raiz.izquierdo and raiz.derecho:
            raiz.izquierdo, valorIz = self.factorEquilibrio(raiz.izquierdo)
            raiz.derecho, valorDer = self.factorEquilibrio(raiz.derecho)
            raiz.fe = valorDer - valorIz
            if valorDer> valorIz:
                return raiz, (1+valorDer)
            else:
                return raiz, (1+valorIz)
        elif raiz.izquierdo:
            raiz.izquierdo, valorIz = self.factorEquilibrio(raiz.izquierdo)
            raiz.fe = valorIz*(-1)
            return raiz, (1+ valorIz)
        elif raiz.derecho:
            raiz.derecho, valorDer = self.factorEquilibrio(raiz.derecho)
            raiz.fe = valorDer
            return raiz, (1+ valorDer)
        return raiz
    def rotacionII(self, rai):
        n0 = rai
        n1 = rai.izquierdo
        n0.izquierdo = n1.derecho
        n1.derecho = n0
        return n1
    def rotacionID(self, rai):
        n0 = rai
        n1 = rai.izquierdo
        n2 = rai.izquierdo.derecho
        n0.izquierdo = n2.derecho
        n1.derecho = n2.izquierdo
        n2.derecho = n0
        n2.izquierdo = n1
        return n2
    def rotacionDD(self, rai):
        n0 = rai
        n1 = rai.derecho
        n0.derecho = n1.izquierdo
        n1.izquierdo = n0
        return n1
    def rotacionDI(self, rai):
        n0 = rai
        n1 = rai.derecho
        n2 = rai.derecho.izquierdo
        n0.derecho = n2.izquierdo
        n1.izquierdo = n2.derecho
        n2.derecho = n1
        n2.izquierdo = n0
        return n2
    def evaluarCasosAVL(self, ra):
        if ra.fe==-2:
            if ra.izquierdo.fe==-1:
                ra = self.rotacionII(ra)
            else:
                ra = self.rotacionID(ra)
        if ra.fe==2:
            if ra.derecho.fe==1:
                ra = self.rotacionDD(ra)
            else:
                ra = self.rotacionDI(ra)
        return ra
    def recorrerArbol(self, ra):
        if ra==None:
            return
        if ra.izquierdo:
           ra.izquierdo = self.recorrerArbol(ra.izquierdo)
        if ra.derecho:
            ra.derecho = self.recorrerArbol(ra.derecho)
        if ra.fe == 2 or ra.fe==-2:
            ra = self.evaluarCasosAVL(ra)
            ra, val = self.factorEquilibrio(ra)
            ra = self.recorrerArbol(ra)
        return ra
    def insertarArchivo(self, nodoN, raiz):
        if raiz==None:
            raiz = nodoN
        else:
            if raiz.nombreArchivo > nodoN.nombreArchivo:
                raiz.izquierdo = self.insertarArchivo(nodoN, raiz.izquierdo)
            else:
                raiz.derecho = self.insertarArchivo(nodoN,raiz.derecho)
        return raiz
    def eliminarArchivo(self, raiz, nombreArchivo):
        if raiz == None:
            return raiz
        elif raiz.nombreArchivo > nombreArchivo:
            raiz.izquierdo = self.eliminarArchivo(raiz.izquierdo, nombreArchivo)
        elif raiz.nombreArchivo < nombreArchivo:
            raiz.derecho = self.eliminarArchivo(raiz.derecho, nombreArchivo)
        else:
            q = raiz
            if q.izquierdo == None:
                raiz = q.derecho
            elif q.derecho== None:
                raiz = q.izquierdo
            else:
                raiz = self.reemplazar(q)
            q = None
        return raiz
    def reemplazar(self, aux):
        p = aux
        a = aux.izquierdo
        while a.derecho:
            p = a
            a = a.derecho
        aux.nombreArchivo = a.nombreArchivo
        aux.archivo = a.archivo
        if p == aux:
            p.izquierdo = a.izquierdo
        else:
            p.derecho = a.izquierdo
            #aux = a
        return aux
    def existeArchivo(self, b, nombreArchivo):
        if b==None:
            return False
        if b.nombreArchivo == nombreArchivo:
            return True
        elif b.nombreArchivo > nombreArchivo:
            if b.izquierdo:
                return self.existeArchivo(b.izquierdo, nombreArchivo)
            else:
                return False
        else:
            if b.derecho:
                return self.existeArchivo(b.derecho, nombreArchivo)
            else:
                return False
    def graficarAVL(self, raiz):
        if raiz==None:
            print"esta vacio :("
            return
        file = open(escritorio+"\\avl.dot", "w")
        file.write("digraph G{\n")
        file.write(self.graficarNodoAVL(raiz))
        file.write("}\n")
        file.close()
        os.system("dot -Tpng "+escritorio+"\\avl.dot > "+escritorio+"\\avl.png")
    def graficarNodoAVL(self, nodo):
        cadena = "nodo"+self.obtenerHASH(nodo)+"[label=\"<f0>|<f1>"+nodo.nombreArchivo+"|<f2>\", shape=record,style=filled,fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n"
        if nodo.izquierdo:
            cadena+=self.graficarNodoAVL(nodo.izquierdo)
            cadena+= "nodo"+self.obtenerHASH(nodo)+":f0 -> "+"nodo"+self.obtenerHASH(nodo.izquierdo)+"\n"
        if nodo.derecho:
            cadena += self.graficarNodoAVL(nodo.derecho)
            cadena += "nodo" + self.obtenerHASH(nodo) + ":f2 -> " + "nodo" + self.obtenerHASH(nodo.derecho)+"\n"
        return cadena
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def modificarArchivo(self, nombreArchivo,raiz):
        if raiz==None:
            return raiz
        if raiz.nombreArchivo == nombreArchivo:
            return raiz
        if raiz.nombreArchivo<nombreArchivo:
            raiz.derecho = self.modificarArchivo(nombreArchivo, raiz.derecho)
        if raiz.nombreArchivo>nombreArchivo:
            raiz.izquierdo = self.modificarArchivo(nombreArchivo, raiz.izquierdo)
        return raiz
#-----------------------------------------------------------------------------------------------
class nodoHash:

    def __init__(self, nombre, direccion, descripcion, hora, tamanio):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.hora = hora
        self.tabla = [None]*tamanio
        self.visitas = 0
class tablaEventos:
    def __init__(self):
        self.tablaInicial = nodoHash("", "", "", "", 7)
        self.tablaInicial = self.inicializarTabla(self.tablaInicial)
    def inicializarTabla(self, tabla):
        tam = len(tabla.tabla)
        for item in range(0,tam,1):
            nuevo = nodoHash("", "", "", "", 0)
            tabla.tabla[item] = nuevo
        return tabla
    def devolverPosicion(self, ascii, tamanioTabla):
        ascii = ascii*ascii
        return ascii%tamanioTabla
    def evaluarRehash(self):
        tam = len(self.tablaInicial.tabla)
        contador = 0
        for i in range(0, tam, 1):
            if self.tablaInicial.tabla[i].nombre!="":
                contador+=1
        if contador>(tam/2):
            return True
        return False
    def primoMasCercano(self):
        bandera = False
        i = len(self.tablaInicial.tabla)+1
        while i>0:
            for ii in range(2,9,1):
                if i%ii == 0:
                    bandera = True
                    break
            if bandera == False:
                break
            else:
                bandera = False
                i = i+1
        return i
    def obtenerASCII(self, cadena):
        asciiTot = 0
        for i in range(0, len(cadena), 1):
            asciiTot = asciiTot + ord(cadena[i])
        return asciiTot
    def insertar(self, nombre, descripcion, direccion, hora):
        if len(nombre)>0:
            asciiTot = 0
            for i in range(0, len(nombre), 1):
                asciiTot = asciiTot + ord(nombre[i])

            k = self.devolverPosicion(asciiTot, len(self.tablaInicial.tabla))
            if k< len(self.tablaInicial.tabla):
                nuevo = nodoHash(nombre, direccion, descripcion, hora, 0)
                self.tablaInicial = self.insertarRecursivo(nuevo, k, self.tablaInicial)
                if self.evaluarRehash():
                    self.tablaInicial = self.rehash()
    def insertarRecursivo(self, nodoNuevo, k, inicio):
        #k = k%len(inicio.tabla)
        if inicio.tabla[k].nombre == "":
            nodoNuevo.visitas = inicio.tabla[k].visitas
            inicio.tabla[k] = nodoNuevo
        else:
            aux = k+ inicio.tabla[k].visitas+1
            inicio.tabla[k].visitas+=1
            self.insertarRecursivo(nodoNuevo, aux, inicio)
        return inicio
    def rehash(self):
        reha = nodoHash("","", "", "", self.primoMasCercano())
        self.inicializarTabla(reha)
        for i in range(0, len(self.tablaInicial.tabla),1):
            if self.tablaInicial.tabla[i].nombre!="":
                asciiTot = 0
                for ii in range(0, len(self.tablaInicial.tabla[i].nombre), 1):
                    asciiTot = asciiTot + ord(self.tablaInicial.tabla[i].nombre[ii])
                k = self.devolverPosicion(asciiTot, len(reha.tabla))
                self.tablaInicial.tabla[i].visitas = 0
                reha = self.insertarRecursivo(self.tablaInicial.tabla[i], k, reha)
        return reha
    def eliminar(self, nombre, posicion):
        if posicion< len(self.tablaInicial.tabla) and posicion>=0:
            if self.tablaInicial.tabla[posicion].nombre == nombre:
                self.tablaInicial.tabla[posicion].nombre = ""
                self.tablaInicial.tabla[posicion].direccion = ""
                self.tablaInicial.tabla[posicion].hora = ""
                self.tablaInicial.tabla[posicion].descripcion = ""
                return
            else:
                aux = posicion + self.tablaInicial.tabla[posicion].visitas + 1
                self.tablaInicial.tabla[posicion].visitas=self.tablaInicial.tabla[posicion].visitas-1
                self.eliminar(nombre,aux)
    def modificar(self, nombre, posicion, descripcion):
        if posicion< len(self.tablaInicial.tabla) and posicion>=0:
            if self.tablaInicial.tabla[posicion].nombre == nombre:
                self.tablaInicial.tabla[posicion].descripcion = descripcion
            else:
                aux = posicion + self.tablaInicial.tabla[posicion].visitas + 1
                self.eliminar(nombre,aux)
    def graficar(self):
        contador = 0
        file = open(escritorio+ "\\hash.dot","w")
        file.write("digraph a{\nrankdir = LR; \ndpi = 500;\nsplines=false; \"nodo\" [ shape = none label=<<TABLE border= \"4\" > \n")
        for item in self.tablaInicial.tabla:
            file.write("<TR>")
            if item.nombre!="":
                file.write("<TD> Nombre: "+ item.nombre+ " Descripcion: "+ item.descripcion+ "\n"+str(contador)+" </TD>\n" )
            else:
                file.write("<TD>      </TD>\n")
            contador+=1
            file.write("</TR>\n")
        file.write("</TABLE>>];\n")
        file.write("}\n")
        file.close()
        os.system("dot -Tpng " + escritorio + "\\hash.dot > " + escritorio + "\\hash.png")
    def estaVacia(self):
        for item in self.tablaInicial.tabla:
            if item.nombre!="":
                return False
        return True
    def eventosPorDia(self, anio, mes, dia):
        cadena = ""
        for item in self.tablaInicial.tabla:
            if item.nombre!="":
                cadena+= anio+","+mes+","+dia+","+item.nombre+","+item.descripcion+","+item.direccion+","+item.hora+","
        return cadena
#-----------------------------------------------------------------------------------------------
class nodoDia:
    siguiente = None
    anterior = None
    dia = ""
    eventos = None
    #hash
    def __init__(self, dia):
        self.siguiente = None
        self.anterir = None
        self.dia = dia
        self.eventos = tablaEventos()
    def graficarEve(self):
        print("GraficandoEventos")
        self.eventos.graficar()
class nodoMatriz:
    arriba = None
    abajo = None
    izquierda = None
    derecha = None
    lista = None
    anio = ""
    mes = ""
    def __init__(self, anio , mes):
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.anio = anio
        self.mes = mes
        self.lista = listaAsociadaNodoMatriz()
class nodoCabezaHorizontal:
    siguiente = None
    anterior = None
    anio = ""
    lista = None

    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.anio = valor
        self.lista = listaAsociadaCabeceraHorizontal()
class nodoCabezaVertical:
    siguiente = None
    anterior = None
    mes  = ""
    lista = None

    def __init__(self, valor):
        self.siguiente = None
        self.anterior = None
        self.mes = valor
        self.lista = listaAsociadaCabeceraVertical()
class listaAsociadaNodoMatriz:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    # metodo para insertar recibe como parametro nuevo que es un nodoUsuario
    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo
            nuevo.siguiente = None
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
    def existe(self, dia):
        temporal=self.primero
        while temporal:
            if temporal.dia == dia:
                return True
            temporal = temporal.siguiente
        return False
    def existeDia(self, dia):
        temporal = self.primero
        while temporal!=None:
            if temporal.dia == dia:
                return True
            temporal = temporal.siguiente
        return False
    def eliminar(self, dia):
        temporal = self.primero
        while temporal:
            if temporal.dia == dia:
                casos = self.posicion(temporal)
                if casos == 0:
                    self.primero = self.ultimo = None
                elif casos == 3:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                elif casos == 1:
                    self.primero = self.primero.siguiente
                    self.primero.anterior = None
                else:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                return
            temporal = temporal.siguiente
    def posicion(self, nodo):
        if nodo.siguiente !=None and nodo.anterior!=None:
            return 3
        if nodo.siguiente == None and nodo.anterior == None:
            return 0
        if  nodo.siguiente == None:
            return 2
        if nodo.anterior == None:
            return 1
class listaAsociadaCabeceraHorizontal:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, nuevo):
        if (self.primero == None):
            self.primero = self.ultimo = nuevo
            return

        if nuevo.mes < self.primero.mes:
            nuevo.abajo = self.primero
            nuevo.arriba = None
            self.primero.arriba = nuevo
            self.primero = nuevo
            return
        elif nuevo.mes > self.ultimo.mes:
            nuevo.abajo = None
            nuevo.arriba = self.ultimo
            self.ultimo.abajo = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.mes > nuevo.mes:
                    nuevo.arriba = temporal.arriba
                    nuevo.abajo = temporal
                    temporal.arriba.abajo = nuevo
                    temporal.arriba = nuevo
                    return
                temporal = temporal.abajo

    # recibe como parametro y que es la letra inicial de la direccion de correo
    def eliminar(self, y):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.mes == y:
                if self.primero == temporal and temporal.abajo != None:
                    self.primero.abajo.arriba = None
                    self.primero = self.primero.abajo
                    return
                elif self.primero == temporal and temporal.abajo == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.arriba
                    self.ultimo.abajo = None
                    return
                else:
                    temporal.abajo.arriba = temporal.arriba
                    temporal.arriba.abajo = temporal.abajo
                    return
            else:
                temporal = temporal.abajo
class listaAsociadaCabeceraVertical:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    # nuevo es un nodo matriz
    def agregar(self, nuevo):
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.anio < self.primero.anio:
            nuevo.derecha = self.primero
            nuevo.izquierda = None
            self.primero.izquierda = nuevo
            self.primero = nuevo
            return
        elif nuevo.anio > self.ultimo.anio:
            nuevo.derecha = None
            nuevo.izquierda = self.ultimo
            self.ultimo.derecha = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.anio > nuevo.anio:
                    nuevo.izquierda = temporal.izquierda
                    nuevo.derecha = temporal
                    temporal.izquierda.derecha = nuevo
                    temporal.izquierda = nuevo
                    return
                temporal = temporal.derecha
    # recibe como parametro x que
    def eliminar(self, x):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.anio == x:
                if self.primero == temporal and temporal.derecha != None:
                    self.primero.derecha.izquierda = None
                    self.primero = self.primero.derecha
                    return
                elif self.primero == temporal and temporal.derecha == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.izquierda
                    self.ultimo.derecha = None
                    return
                else:
                    temporal.derecha.izquierda = temporal.izquierda
                    temporal.izquierda.derecha = temporal.derecha
                    return
            else:
                temporal = temporal.derecha
class listaCabecerasHorizontales:
    listaVertical = None
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.listaVertical = listaAsociadaCabeceraHorizontal()
    def insertar(self, anio):
        nuevo = nodoCabezaHorizontal(anio)
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.anio < self.primero.anio:
            nuevo.siguiente = self.primero
            nuevo.anterior = None
            self.primero.anterior = nuevo
            self.primero = nuevo
            return
        elif nuevo.anio > self.ultimo.anio:
            nuevo.siguiente = None
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.anio > nuevo.anio:
                    nuevo.anterior = temporal.anterior
                    nuevo.siguiente = temporal
                    temporal.anterior.siguiente = nuevo
                    temporal.anterior = nuevo
                    return
                temporal = temporal.siguiente
    def eliminar(self, anio):
        if self.primero == None:
            return
        temporal = self.primero
        while temporal != None:
            if temporal.anio == anio:
                if self.primero == temporal and temporal.siguiente != None:
                    self.primero.siguiente.anterior = None
                    self.primero = self.primero.siguiente
                    return
                elif self.primero == temporal and temporal.siguiente == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    return
                else:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                    return
            else:
                temporal = temporal.siguiente
    def existeNodoMatriz(self, anio, mes):
        if self.primero == None:
            return False
        temporal = self.primero
        while temporal != None:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux != None:
                    if aux.mes == mes:
                        return True
                    aux = aux.abajo
            temporal = temporal.siguiente
        return False
    def noTieneNada(self, anio):
        temporal = self.primero
        while temporal != None:
            if temporal.anio == anio:
                if temporal.lista.primero == None:
                    return True
            temporal = temporal.siguiente
        return False
    def existeH(self, anio):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                return True
            temporal = temporal.siguiente
        return False
    def insertarDirectoANodo(self, anio, mes, dia, evento, descripcion, direccion, hora):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        if aux.lista.existe(dia):

                            aux2 = aux.lista.primero
                            while aux2:
                                if aux2.dia == dia:
                                    aux2.eventos.insertar(evento, descripcion, direccion, hora)
                                    return
                                aux2 = aux2.siguiente
                        else:
                            nuevo = nodoDia(dia)
                            aux.lista.insertar(nuevo)
                            aux2 = aux.lista.primero
                            while aux2:
                                if aux2.dia == dia:
                                    aux2.eventos.insertar(evento, descripcion, direccion, hora)
                                    return
                                aux2 = aux2.siguiente
                            return
                    aux = aux.abajo
            temporal = temporal.siguiente
        return
    def eliminarEnNodo(self, anio, mes, dia, evento):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        aux2 = aux.lista.primero
                        while aux2:
                            if aux2.dia==dia:
                                tam = len(aux2.eventos.tablaInicial.tabla)
                                posicion = aux2.eventos.devolverPosicion(aux2.eventos.obtenerASCII(evento),tam)
                                aux2.eventos.eliminar(evento,posicion)
                                if aux2.eventos.estaVacia():
                                    aux.lista.eliminar(dia)
                                return
                            aux2 = aux2.siguiente
                    aux = aux.abajo
            temporal = temporal.siguiente
        return
    def graficarEventosPorDia(self, anio, mes, dia):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                print("anio\n")
                temporal2 = temporal.lista.primero
                while temporal2:
                    if temporal2.mes==mes:
                        print("mes\n")
                        aux = temporal2.lista.primero
                        while aux:
                            if aux.dia == dia:
                                print("dia:"+aux.dia+"\n")
                                aux.graficarEve()
                                return
                            aux = aux.siguiente
                    temporal2 = temporal2.abajo
            temporal = temporal.siguiente
    def nodoVacio(self, anio, mes):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        if aux.lista.primero == None:
                            return True
                        else:
                            return False
                    aux = aux.abajo
            temporal = temporal.siguiente
        return False
    def modificarEvento(self, anio, mes, dia, evento, nuevaD):
        temporal = self.primero
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        aux1 = aux.lista.primero
                        while aux1:
                            if aux1.dia == dia:
                                tam = len(aux1.eventos.tablaInicial.tabla)
                                posicion = aux1.eventos.devolverPosicion(aux1.eventos.obtenerASCII(evento), tam)
                                aux1.eventos.modificar(evento, posicion, nuevaD)
                                return
                            aux1 = aux1.siguiente
                    aux = aux.abajo
            temporal = temporal.siguiente
class listaCabecerasVerticales:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def insertar(self, mes):
        nuevo = nodoCabezaVertical(mes)
        if self.primero == None:
            self.primero = self.ultimo = nuevo
            return

        if nuevo.mes < self.primero.mes:
            nuevo.siguiente = self.primero
            nuevo.anterior = None
            self.primero.anterior = nuevo
            self.primero = nuevo
            return
        elif nuevo.mes > self.ultimo.mes:
            nuevo.siguiente = None
            nuevo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
            return
        else:
            temporal = self.primero
            while temporal != None:
                if temporal.mes > nuevo.mes:
                    nuevo.anterior = temporal.anterior
                    nuevo.siguiente = temporal
                    temporal.anterior.siguiente = nuevo
                    temporal.anterior = nuevo
                    return
                temporal = temporal.siguiente
    def eliminar(self, mes):
        if self.primero == None:
            return

        temporal = self.primero
        while temporal != None:
            if temporal.mes == mes:
                if self.primero == temporal and temporal.siguiente != None:
                    self.primero.siguiente.anterior = None
                    self.primero = self.primero.siguiente
                    return
                elif self.primero == temporal and temporal.siguiente == None:
                    self.primero = self.ultimo = None
                    return
                elif self.ultimo == temporal:
                    self.ultimo = self.ultimo.anterior
                    self.ultimo.siguiente = None
                    return
                else:
                    temporal.siguiente.anterior = temporal.anterior
                    temporal.anterior.siguiente = temporal.siguiente
                    return
            else:
                temporal = temporal.siguiente
    def existeMes(self, mes):
        if self.primero == None:
            return False
        temporal = self.primero
        while temporal != None:
            if temporal.mes == mes:
                return True
            temporal = temporal.siguiente
        return False
    def noTieneNada(self, mes):
        temporal = self.primero
        while temporal != None:
            if temporal.mes == mes:
                if temporal.lista.primero == None:
                    return True
            temporal = temporal.siguiente
        return False
    def existeV(self, mes):
        temporal = self.primero
        while temporal:
            if temporal.mes == mes:
                return True
            temporal = temporal.siguiente
        return False
class matriz:
    def __init__(self):
        self.verticales = listaCabecerasVerticales()
        self.horizontales = listaCabecerasHorizontales()
    def insertar(self, anio, mes, dia, nombreEvento, descripcion, direccion, hora):
       # print(usuario+"   "+password)
        if self.verticales.existeV(mes) == False:
            self.verticales.insertar(mes)

        if self.horizontales.existeH(anio) == False:
            self.horizontales.insertar(anio)

        if self.horizontales.existeNodoMatriz(anio, mes) == False:
            nodom = nodoMatriz(anio, mes)
            tm = self.horizontales.primero
            while tm != None:
                if tm.anio == anio:
                    tm.lista.agregar(nodom)
                    break
                tm = tm.siguiente
            tm2 = self.verticales.primero
            while tm2 != None:
                if tm2.mes == mes:
                    tm2.lista.agregar(nodom)
                    break
                tm2 = tm2.siguiente

        self.horizontales.insertarDirectoANodo(anio, mes, dia,nombreEvento,descripcion,direccion,hora)
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def graficarMatriz(self):
        if self.horizontales.primero == None or self.verticales.primero == None:
            return
        cabeza = self.horizontales.primero
        lateral = self.verticales.primero
        file = open(escritorio+"\\matriz.dot", "w")
        file.write("digraph G{\n")
        file.write("\"nodoR\"[label=\"Inicio\", style = filled, fillcolor = \"red:yellow\", shape = \"box\", gradientangle=\"90\", group = rr]\n")
        file.write("{rank = same; \"nodoR\" \"nodoc" + self.obtenerHASH(cabeza) + "\"}\n")
        file.write("\"nodoR\" -> \"nodoc" + self.obtenerHASH(cabeza) + "\"\n")
        # graficando cabezas
        while cabeza != None:

            file.write("\"nodoc" + self.obtenerHASH(cabeza) + "\"[label = \"" + cabeza.anio + "\", style = filled, fillcolor = \"red:yellow\",shape = \"box\", gradientangle=\"90\", group = r" + self.obtenerHASH(cabeza) + "]\n")
            if cabeza.siguiente != None:
                file.write("{rank = same; \"nodoc" + self.obtenerHASH(cabeza) + "\"  \"nodoc" + self.obtenerHASH(
                    cabeza.siguiente) + "\"}\n")
                file.write("\"nodoc" + self.obtenerHASH(cabeza) + "\" -> \"nodoc" + self.obtenerHASH(cabeza.siguiente) + "\"\n")
            if cabeza.anterior != None:
                file.write("{rank = same; \"nodoc" + self.obtenerHASH(cabeza) + "\"  \"nodoc" + self.obtenerHASH(
                    cabeza.anterior) + "\"}\n")
                file.write("\"nodoc" + self.obtenerHASH(cabeza) + "\" -> \"nodoc" + self.obtenerHASH(cabeza.anterior) + "\"\n")
            cabeza = cabeza.siguiente
        file.write("\"nodoR\" -> \"nodol" + self.obtenerHASH(lateral) + "\"\n")
        while lateral != None:
            file.write("\"nodol" + self.obtenerHASH(
                lateral) + "\"[label = \"" + lateral.mes + "\", style = filled, fillcolor = \"red:yellow\",shape = \"box\", gradientangle=\"90\", group = rr]\n")
            if lateral.siguiente != None:
                file.write(
                    "\"nodol" + self.obtenerHASH(lateral) + "\" -> \"nodol" + self.obtenerHASH(lateral.siguiente) + "\"\n")
            if lateral.anterior != None:
                file.write(
                    "\"nodol" + self.obtenerHASH(lateral) + "\" -> \"nodol" + self.obtenerHASH(lateral.anterior) + "\"\n")
            lateral = lateral.siguiente
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            file.write("subgraph s" + self.obtenerHASH(cabeza) + "{\n")
            while enMatriz != None:
                file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\"[label = \"" + enMatriz.lista.primero.dia + "\", style = filled, fillcolor = \"red:yellow\",shape = \"box\", gradientangle=\"90\", group = r" + self.obtenerHASH(cabeza) + "]\n")
                if enMatriz.lista.primero.siguiente != None:
                    tm = enMatriz.lista.primero.siguiente
                    file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\" -> \"nodoS" + self.obtenerHASH(tm) + "\"\n")
                    file.write("\"nodoS" + self.obtenerHASH(tm) + "\" -> " + "\"nodoc" + self.obtenerHASH(
                        enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\"\n")
                    while tm != None:
                        file.write("\"nodoS" + self.obtenerHASH(
                            tm) + "\"[label = \"" + tm.dia + "\", style = filled, fillcolor = \"red:yellow\", gradientangle=\"90\",shape = \"box\"]\n")
                        if tm.siguiente != None:
                            file.write(
                                "\"nodoS" + self.obtenerHASH(tm) + "\" -> \"nodoS" + self.obtenerHASH(tm.siguiente) + "\"\n")
                            file.write(
                                "\"nodoS" + self.obtenerHASH(tm.siguiente) + "\" -> \"nodoS" + self.obtenerHASH(tm) + "\"\n")
                        tm = tm.siguiente
                enMatriz = enMatriz.abajo
            file.write("}\n")
            cabeza = cabeza.siguiente
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            while enMatriz != None:
                if enMatriz.derecha != None:
                    file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\" -> \"" + "nodoc" + self.obtenerHASH(enMatriz.derecha) + "l" + self.obtenerHASH(
                        enMatriz.derecha) + "\"\n")
                    file.write("{rank = same; " + " \"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\"  " + "\"nodoc" + self.obtenerHASH(enMatriz.derecha) + "l" + self.obtenerHASH(
                        enMatriz.derecha) + "\"}\n")
                if enMatriz.izquierda != None:
                    file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\" -> \"" + "nodoc" + self.obtenerHASH(enMatriz.izquierda) + "l" + self.obtenerHASH(
                        enMatriz.izquierda) + "\"\n")
                    file.write("{rank = same; " + " \"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\"  " + "\"nodoc" + self.obtenerHASH(enMatriz.izquierda) + "l" + self.obtenerHASH(
                        enMatriz.izquierda) + "\"}\n")
                if enMatriz.abajo != None:
                    file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\" -> " + "\"nodoc" + self.obtenerHASH(enMatriz.abajo) + "l" + self.obtenerHASH(
                        enMatriz.abajo) + "\"\n")
                    # file.write("{rank = same; " + " nodoc" + enMatriz.anio + "l" + enMatriz.inicialDireccion + " " + "nodoc" + enMatriz.arriba.anio + "l" + enMatriz.arriba.inicialDireccion)
                if enMatriz.arriba != None:
                    file.write("\"nodoc" + self.obtenerHASH(enMatriz) + "l" + self.obtenerHASH(
                        enMatriz) + "\" -> \"" + "nodoc" + self.obtenerHASH(enMatriz.arriba) + "l" + self.obtenerHASH(
                        enMatriz.arriba) + "\"\n")
                    # file.write("{rank = same; " + " nodoc" + enMatriz.anio + "l" + enMatriz.inicialDireccion + " " + "nodoc" + enMatriz.arriba.anio + "l" + enMatriz.arriba.inicialDireccion)
                enMatriz = enMatriz.abajo
            cabeza = cabeza.siguiente

        lateral = self.verticales.primero
        while lateral != None:
            enMatriz = lateral.lista.primero
            if lateral.lista.primero != None:
                file.write("\"nodol" + self.obtenerHASH(lateral) + "\" -> \"" + "nodoc" + self.obtenerHASH(
                    enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\"\n")
                file.write("{rank = same; " + "\"nodol" + self.obtenerHASH(lateral) + "\"  " + "\"nodoc" + self.obtenerHASH(
                    enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\"}\n")
            lateral = lateral.siguiente
        # file.write("}\n")
        cabeza = self.horizontales.primero
        while cabeza != None:
            enMatriz = cabeza.lista.primero
            if cabeza.lista.primero != None:
                file.write("\"nodoc" + self.obtenerHASH(cabeza) + "\" -> \"nodoc" + self.obtenerHASH(
                    enMatriz) + "l" + self.obtenerHASH(enMatriz) + "\"\n")
            cabeza = cabeza.siguiente

        file.write("}\n")
        file.close()
        os.system("dot -Tpng "+escritorio+"\\matriz.dot > "+escritorio+"\\matriz.png")
    def eliminar(self, anio, mes, dia, evento):
        if self.verticales.existeV(mes) == False:
            return " "

        if self.horizontales.existeH(anio) == False:
            return " "

        if self.horizontales.existeNodoMatriz(anio, mes) == False:
            return " "
        self.horizontales.eliminarEnNodo(anio, mes, dia, evento)
        if self.horizontales.nodoVacio(anio,mes):
            # print "pasa eliminacion desde nodoMatriz"
            temporal = self.horizontales.primero
            while temporal != None:
                if temporal.anio == anio:
                    #       print "entra eliminacion de la lista asociada a nodo horizontal"
                    temporal.lista.eliminar(mes)
                    #      print"pasa eliminacion de la lista asociada a nodo horizontal"
                    break
                temporal = temporal.siguiente
            if self.horizontales.noTieneNada(anio) == True:
                # print "entra a la eliminacion de nodo horizontal"
                self.horizontales.eliminar(anio)
                # print"pasa eliminacion de nodo horizontal"
            temporal2 = self.verticales.primero
            while temporal2 != None:
                if temporal2.mes == mes:
                    #   print "entra eliminacion de la lista asociada a nodo vertical"
                    temporal2.lista.eliminar(anio)
                    #  print "pasa eliminacion de la lista asociada a nodo vertical"
                    break
                temporal2 = temporal2.siguiente
            if self.verticales.noTieneNada(mes) == True:
                # print "entra eliminacion de nodo vertical"
                self.verticales.eliminar(mes)
                # print "pasa eliminacion de nodo vertical"
    def devolverEventosPorDia(self, anio, mes, dia):
        temporal = self.horizontales.primero
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        aux2 = aux.lista.primero
                        while aux2:
                            if aux2.dia == dia:
                                return aux2.eventos.eventosPorDia(anio,mes,dia)
                            aux2 = aux2.siguiente
                    aux = aux.abajo
            temporal = temporal.siguiente
        return ""
    def devolverEventosPorAnio(self, anio):
        temporal = self.horizontales.primero
        cadena = ""
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    aux2 = aux.lista.primero
                    while aux2:
                        cadena += aux2.eventos.eventosPorDia(temporal.anio,aux.mes,aux2.dia)
                        aux2 = aux2.siguiente
                    aux = aux.siguiente
                return cadena
            temporal = temporal.siguiente
        return cadena
    def devolverEventosPorMes(self, anio, mes):
        temporal = self.horizontales.primero
        cadena = ""
        while temporal:
            if temporal.anio == anio:
                aux = temporal.lista.primero
                while aux:
                    if aux.mes == mes:
                        aux2 = aux.lista.primero
                        while aux2:
                            cadena += aux2.eventos.eventosPorDia(temporal.anio,aux.mes,aux2.dia)
                            aux2 = aux2.siguiente
                        return cadena
                    aux = aux.abajo
            temporal = temporal.siguiente
        return cadena
    def devolverTodosEventos(self):
        temporal = self.horizontales.primero
        cadena = ""
        while temporal:
            aux = temporal.lista.primero
            while aux:
                aux2 = aux.lista.primero
                while aux2:
                    cadena+=aux2.eventos.eventosPorDia(temporal.anio, aux.mes, aux2.dia)
                    aux2 = aux2.siguiente
                aux = aux.abajo
            temporal = temporal.siguiente
        return cadena

#-----------------------------------------------------------------------------------------------
class nodoBitacora:
    def __init__(self, accion):
        self.accion = accion
        self.siguiente = None
class listaBitacora:
    def __init__(self):
        self.primero = None
    def insertar(self, nuevo):
        if self.primero == None:
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
    def graficar(self):
        if self.primero == None:
            return
        temporal = self.primero
        file = open(escritorio + "\\bitacora.dot", "w")
        file.write("digraph G{\n")
        while temporal != None:
            file.write("nodo" + self.obtenerHASH(
                temporal) + "[label=\"Evento: " + temporal.accion + "\", style = filled, shape= \"box\", fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n")
            if temporal.siguiente != None:
                file.write(
                    "nodo" + self.obtenerHASH(temporal) + " -> " + "nodo" + self.obtenerHASH(temporal.siguiente) + "\n")
            temporal = temporal.siguiente
        file.write("}")
        file.close()
        os.system("dot -Tpng " + escritorio + "\\bitacora.dot > " + escritorio + "\\bitacora.png")
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
class nodoUsuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.calendario = matriz()
        self.drive = "No"
        self.siguiente = None
        self.anterior = None
        self.bitacora = listaBitacora()
class listaUsurios:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)
    def insertarUsuario(self,nombre,password):
        nuevo = nodoUsuario(nombre,password)
        if self.primero == None:
            self.primero = self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
    def insertarEvento(self, usuario, idEvento, descripcionEvento, hora, lugar,anio, mes, dia):
        if self.primero==None:
            return
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                temporal.calendario.insertar(anio, mes, dia, idEvento, descripcionEvento, lugar, hora)
                na = nodoBitacora("Creo Evento")
                temporal.bitacora.insertar(na)
                temporal.bitacora.graficar()
                return
            temporal = temporal.siguiente
    def eliminarEvento(self, usuario, anio, mes, dia, evento):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                 temporal.calendario.eliminar(anio,mes,dia,evento)
                 na = nodoBitacora("Elimino Evento")
                 temporal.bitacora.insertar(na)
                 temporal.bitacora.graficar()
                 return
            temporal = temporal.siguiente
    def modificarEvento(self, usuario, anio, mes, dia, evento, nuevaD):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                temporal.calendario.modificarEvento(anio, mes, dia, evento, nuevaD)
                na = nodoBitacora("Modifico Evento")
                temporal.bitacora.insertar(na)
                temporal.bitacora.graficar()
                return
            temporal = temporal.siguiente

        #self.ma.horizontales.modificarEvento(anio, mes, dia, evento, "Si lo modificamosPapu")
    def graficarUsuarios(self):
        if self.primero ==  None:
            return
        temporal = self.primero
        file = open(escritorio + "\\usuarios.dot", "w")
        file.write("digraph G{\n")
        while temporal != None:
            file.write("nodo" + self.obtenerHASH(
                temporal) + "[label=\"Nombre: " + temporal.nombre + "\n Drive:"+temporal.drive+"\", style = filled, shape= \"box\", fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n")
            if temporal.siguiente != None:
                file.write(
                    "nodo" + self.obtenerHASH(temporal) + " -> " + "nodo" + self.obtenerHASH(temporal.siguiente) + "\n")
            if temporal.anterior != None:
                file.write(
                    "nodo" + self.obtenerHASH(temporal) + " -> " + "nodo" + self.obtenerHASH(temporal.anterior) + "\n")
            temporal = temporal.siguiente
        file.write("}")
        file.close()
        os.system("dot -Tpng " + escritorio + "\\usuarios.dot > " + escritorio + "\\usuarios.png")
    def vincularDrive(self, usuarioC, usuarioD):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuarioC:
                temporal.drive = usuarioD
                na = nodoBitacora("Vinculo cuenta Drive")
                temporal.bitacora.insertar(na)
                temporal.bitacora.graficar()
                return
            temporal = temporal.siguiente
    def existeUsuario(self, usuario):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                return True
            temporal = temporal.siguiente
        return False
    def graficarCalendario(self, usuario):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                temporal.calendario.graficarMatriz()
                return
            temporal = temporal.siguiente
    def graficarEventosPorDiaa(self, usuario, anio, mes, dia):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                temporal.calendario.horizontales.graficarEventosPorDia(anio, mes, dia)
                return
            temporal = temporal.siguiente
    def devolverUsuarios(self):
        cadena = ""
        temporal = self.primero
        while temporal:
            if temporal.siguiente==None:
                cadena+= temporal.nombre
            else:
                cadena+= temporal.nombre+","
        return cadena
    def verificarLogin(self, usuario, password):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                if temporal.password == password:
                    na = nodoBitacora("Se logueo")
                    temporal.bitacora.insertar(na)
                    temporal.bitacora.graficar()
                    return True
                else:
                    return False
            temporal = temporal.siguiente
        return False
    def eventosPorDia(self, usuario, anio, mes, dia):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                return temporal.calendario.devolverEventosPorDia(anio,mes,dia)
            temporal = temporal.siguiente
        return ""
    def eventosPorAnio(self, usuario, anio):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                return temporal.calendario.devolverEventosPorAnio(anio)
            temporal = temporal.siguiente
        return ""
    def eventosPorMes(self, usuario, anio, mes):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                return temporal.calendario.devolverEventosPorMes(anio, mes)
            temporal = temporal.siguiente
        return ""
    def eventosPorUsuario(self, usuario):
        temporal = self.primero
        while temporal:
            if temporal.nombre == usuario:
                return temporal.calendario.devolverTodosEventos()
            temporal = temporal.siguiente
        return ""
#-----------------------------------------------------------------------------------------------

usuarios = listaUsurios()
usuarios.insertarUsuario("prueba","123")
usuarios.insertarEvento("prueba","Evento Prueba","esto es una prueba", "9:00","la casa de kevin", "2017","Mayo","8")
usuarios.insertarEvento("prueba","Evento Prueba2","esto es una prueba", "9:00","la casa de kevin", "2017","Mayo","8")
def otro(request):
    usuario = request.GET['u']
    password = request.GET['p']
    if usuarios.existeUsuario(usuario):
        return HttpResponse('Ya existe')
    else:
        usuarios.insertarUsuario(usuario, password)
        usuarios.graficarUsuarios()
        return HttpResponse('exito')
    return HttpResponse('otro')

def insertarUsuario2(request):
    usuario = request.GET['usuario']
    password = request.GET['password']
    if usuarios.existeUsuario(usuario):
        return HttpResponse('Ya existe')
    else:
        usuarios.insertarUsuario(usuario, password)
        usuarios.graficarUsuarios()
        return HttpResponse('exito')


def verificarLogin(request):
    usuario = request.GET['usuario']
    password = request.GET['password']
    if usuarios.verificarLogin(usuario,password):
        return HttpResponse('si')
    else:
        return HttpResponse('no')

def insertarUsuario(request):
    usuario = request.GET['usuario']
    password = request.GET['password']
    if usuarios.existeUsuario(usuario):
        return HttpResponse('Ya existe')
    else:
        usuarios.insertarUsuario(usuario,password)
        usuarios.graficarUsuarios()
        return HttpResponse('exito')
def nuevoEvento(request):
    usuario = request.GET['usuario']
    evento = request.GET['evento']
    evento = evento.replace("\"", "")
    descripcion = request.GET['descripcion']
    descripcion = descripcion.replace("\"", "")
    hora = request.GET['hora']
    lugar = request.GET['lugar']
    lugar = lugar.replace("\"", "")
    dia = request.GET['dia']
    mes = request.GET['mes']
    anio = request.GET['anio']
    usuarios.insertarEvento(usuario,evento,descripcion,hora,lugar,anio,mes,dia)
    usuarios.graficarEventosPorDiaa(usuario, anio, mes, dia)
    usuarios.graficarCalendario(usuario)
    return HttpResponse('si')
def eliminarEvento(request):
    usuario = request.GET['usuario']
    evento = request.GET['evento']
    evento = evento.replace("\"", "")
    dia = request.GET['dia']
    mes = request.GET['mes']
    anio = request.GET['anio']
    usuarios.eliminarEvento(usuario,anio,mes,dia,evento)
    usuarios.graficarEventosPorDiaa(usuario,anio,mes,dia)
    return HttpResponse('si')
def modificarEvento(request):
    usuario = request.GET['usuario']
    evento = request.GET['evento']
    evento = evento.replace("\"", "")
    eventoN = request.GET['nuevoE']
    eventoN = eventoN.replace("\"", "")
    descripcion = request.GET['descripcion']
    descripcion = descripcion.replace("\"", "")
    hora = request.GET['hora']
    lugar = request.GET['lugar']
    lugar = lugar.replace("\"", "")
    dia = request.GET['dia']
    mes = request.GET['mes']
    anio = request.GET['anio']
    usuarios.eliminarEvento(usuario, anio, mes, dia, evento)
    usuarios.insertarEvento(usuario, eventoN, descripcion, hora, lugar, anio, mes, dia)
    usuarios.graficarEventosPorDiaa(usuario, anio, mes, dia)
    return HttpResponse("si")
def eventosPorDia(request):
    usuario = request.GET['usuario']
    anio = request.GET['anio']
    mes = request.GET['mes']
    dia = request.GET['dia']
    return HttpResponse(usuarios.eventosPorDia(usuario,anio,mes,dia))
def eventosPorAnio(request):
    usuario = request.GET['usuario']
    anio = request.GET['anio']
    return HttpResponse(usuarios.eventosPorAnio(usuario,anio))
def eventosPorMes(request):
    usuario = request.GET['usuario']
    anio = request.GET['anio']
    mes = request.GET['mes']
    return HttpResponse(usuarios.eventosPorMes(usuario,anio,mes))
def eventosPorUsuario(request):
    usuario = request.GET['usuario']
    print(usuarios.eventosPorUsuario(usuario))
    return  HttpResponse(usuarios.eventosPorUsuario(usuario))