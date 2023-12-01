from PyQt5 import QtSql
from reportlab.pdfgen import canvas
import os, var
from datetime import datetime
import conexion

class Informes:

    def ListadoCliente(self):
        """

        Método que genera un pdf con todos los clientes

        """
        try:
            var.cv = canvas.Canvas('informes/listadoclientes.pdf')
            Informes.cabecera(self)

            #var.cv.setFont('Helvetica-Bold', 16)
            # var.cv.drawString(100, 750, 'Listado clientes')
            # var.cv.line(30,400,500,400) #línea
            # var.cv.circle(150,100,100, stroke= 1, fill= 1)
            # text = "Este es un ejemplo de párrafo en el informe \nque estoy creando"
            # var.cv.setFont("Courier-Oblique", 10)
            # var.cv.drawString(100, 300, text)

            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size = 10)
            textoTitulo = 'Listado Clientes'
            Informes.pie(textoTitulo)
            var.cv.drawString(255, 690, textoTitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['DNI', 'Nombre', 'Formas de pago']
            var.cv.drawString(70, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(370, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select dni, apellidos, nombre, pago from clientes order by apellidos, nombre')
            var.cv.setFont('Helvetica', size = 8)
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textoTitulo)
                        var.cv.drawString(255, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['DNI', 'Nombre', 'Formas de pago']
                        var.cv.drawString(70, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655

                    var.cv.setFont('Helvetica', size= 8)
                    var.cv.drawString(i, j, str(query.value(0)))
                    var.cv.drawString(i+140, j, str(query.value(1) + ', ' + query.value(2)))
                    var.cv.drawString(i+310, j, str(query.value(3)))
                    j = j - 20

            #var.ui.setTitle("Listado clientes")
            #var.ui.setAuthor("Departamento de administración")

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('clientes.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont +1

        except Exception as error:
            print('Error al hacer el informe ', error)

    def cabecera(self):
        """

        Método que da formato a la cabecera de los informes

        """
        try:
            logo = '.\\img\linux.png'
            var.cv.line(40,800,530,800)
            var.cv.setFont('Helvetica-Bold', 14)
            var.cv.drawString(50,785, "Import-Export Vigo")
            var.cv.setFont('Helvetica', 10)
            var.cv.drawString(50,770, "CIF 00000000")
            var.cv.drawString(50, 755, "Dirección Avenida Galicia 101")
            var.cv.drawString(50, 740, "Vigo - 123 - Spain")
            var.cv.drawString(50, 725, "mail: correo@mail.com")
            var.cv.drawImage(logo, 425,725)
            var.cv.line(40,710,530,710)

        except Exception as error:
            print('Error al hacer la cabecera del informe ', error)

    def pie(texto):
        """

        Método que da formato al pie de los informes

        """
        try:
            var.cv.line(50, 50, 530, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d/%m/%Y %H.%M.%S')
            var.cv.setFont('Helvetica', size = 6)
            var.cv.drawString(70, 40, str(fecha))
            var.cv.drawString(255, 40, str(texto))
            var.cv.drawString(500, 40, str('Página %s' %var.cv.getPageNumber()))

        except Exception as error:
            print('Error al creación pie del informe ', error)

    def ListadoArticulo(self):
        """

        Método que genera un pdf con todos los artículos

        """
        try:
            var.cv = canvas.Canvas('informes/listadoproductos.pdf')
            Informes.cabecera(self)

            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size = 10)
            textoTitulo = 'Listado Artículos'
            Informes.pie(textoTitulo)
            var.cv.drawString(255, 690, textoTitulo)
            var.cv.line(40, 685, 530, 685)
            items = ['Código', 'Artículos', 'Precio/kg']
            var.cv.drawString(70, 675, items[0])
            var.cv.drawString(210, 675, items[1])
            var.cv.drawString(370, 675, items[2])
            var.cv.line(40, 670, 530, 670)
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, nombre, precio from productos')
            var.cv.setFont('Helvetica', size = 8)
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440, 30, 'Página siguiente...')
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textoTitulo)
                        var.cv.drawString(255, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ['Código', 'Artículos', 'Precio/kg']
                        var.cv.drawString(70, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(370, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655

                    var.cv.setFont('Helvetica', size= 8)
                    var.cv.drawRightString(i, j, str(query.value(0)))
                    var.cv.drawString(i+140, j, str(query.value(1)))
                    var.cv.drawString(i+310, j, str(query.value(2)))
                    j = j - 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('productos.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont +1

        except Exception as error:
            print('Error al hacer el informe ', error)

    def factura(self):
        """

        Método que genera un pdf con todas las facturas

        """
        try:
            var.cv = canvas.Canvas('informes/factura.pdf')
            var.cv.setTitle('Factura')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=12)
            textotitulo = 'FACTURA'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            codfac = var.ui.lblNumFactura.text()

            #Añadir datos del cliente
            #falta algo
            var.cv.setFont('Helvetica-Bold', size=12)
            var.cv.drawString(250, 785, 'Datos Cliente')
            var.cv.setFont('Helvetica', size=8)
            query = QtSql.QSqlQuery()
            query.prepare('select direccion, municipio, provincia from clientes where dni = :dni')
            query.bindValue(':dni', str(var.ui.txtDNIFac.text()))
            if query.exec_():
                dir = []
                while query.next():
                    dir.append((query.value(0)))
                    dir.append((query.value(1)))
                    dir.append((query.value(2)))
            var.cv.drawString(250, 770, 'CIF: ' + var.ui.txtDNIFac.text())
            var.cv.drawString(250, 760, 'Cliente: ' + var.ui.lblNomFac.text())
            var.cv.drawString(250, 750, 'Dirección: ' + str(dir[0]))
            var.cv.drawString(250, 740, 'Localidad: ' + str(dir[1]))
            var.cv.drawString(250, 730, 'Provincia: ' + str(dir[2]))

            var.cv.setFont('Helvetica-Bold', size=12)
            var.cv.drawString(255, 690, textotitulo + ': ' + str(codfac))
            var.cv.setFont('Helvetica', size=8)
            var.cv.line(40, 685, 530, 685)
            items = ['Venta', 'Artículo', 'Precio', 'Cantidad', 'Total']
            var.cv.drawString(60, 675, items[0])
            var.cv.drawString(150, 675, items[1])
            var.cv.drawString(290, 675, items[2])
            var.cv.drawString(390, 675, items[3])
            var.cv.drawString(490, 675, items[4])
            var.cv.line(40, 670, 530, 670)
            suma = 0.0
            query = QtSql.QSqlQuery()
            query.prepare('select codventa,precio,cantidad, codprod from ventas where codfac = :codfac')
            query.bindValue(':codfac', int(codfac))
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    codventa = query.value(0)
                    precio = str('{:.2f}'.format(round(query.value(1), 2)))
                    cantidad = str('{:.2f}'.format(round(query.value(2), 2)))
                    articulo = conexion.Conexion.buscaArt(str(query.value(3)))
                    suma = suma + (round(query.value(1), 2) * round(query.value(2), 2))
                    total = str('{:.2f}'.format(round(query.value(1) * query.value(2), 2))).replace(',', '.') + ' €'

                    var.cv.setFont('Helvetica', size=8)
                    var.cv.drawCentredString(i + 20, j, str(codventa))
                    var.cv.drawString(i + 100, j, str(articulo))
                    var.cv.drawString(i + 230, j, str(precio) + '€')
                    var.cv.drawString(i + 350, j, str(cantidad))
                    var.cv.drawString(i + 440, j, str(total))
                    j = j - 20
                var.cv.setFont('Helvetica', size=8)
                subTotal = var.ui.lblSubTotal.text()
                iva = var.ui.lblIva.text()
                final = var.ui.lblTotal.text()
                var.cv.drawRightString(i + 469, j - 20, "Sub Total: " + subTotal)
                var.cv.drawRightString(i + 469, j - 40, "IVA: " + iva)
                var.cv.drawRightString(i + 469, j - 60, "Total: " + final)

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error en informes productos, ', error)



















