import conexion
from ventana import *
import var
import locale
locale.setlocale( locale.LC_ALL, '' )


class Productos():
    # def guardaProd(self):
    #     try:
    #         newProd = []
    #         producto = [var.ui.txtProd, var.ui.txtPrecio]
    #         #tabProd = []
    #         #prod = [var.ui.txtProd, var.ui.txtPrecio]
    #         for i in producto:
    #             newProd.append(i.text())
    #         #for i in prod:
    #         #    tabProd.append(i.text())
    #         #row = 0
    #         #column = 0
    #         #var.ui.tabProd.insertRow(row)
    #         # for campo in tabProd:
    #         #     cell = QtWidgets.QTableWidgetItem(str(campo))
    #         #     var.ui.tabProd.setItem(row, column, cell)
    #         #     column += 1
    #         conexion.Conexion.altaProd(newProd)
    #         conexion.Conexion.cargarTabProd(self)
    #     except Exception as error:
    #         print('Error al guardar producto ', error)

    def guardaProd(self):
        """

        Método que recoge los valores de los campos de producto y se los manda al método altaProd en conexion
        para crear un nuevo producto en la BD. Luego, llama al método cargarTabProd para recargar la tabla productos
        en la interfaz.

        """
        try:
            registro = []
            producto = var.ui.txtProd.text()
            producto = producto.title()
            registro.append(producto)
            precio = var.ui.txtPrecio.text()
            precio = precio.replace(',', '.')  # necesita estar con punto como en américa
            #precio = locale.currency(float(precio))
            registro.append(precio)
            conexion.Conexion.altaProd(registro)
            conexion.Conexion.cargarTabProd(self)

        except Exception as error:
            print('Error en alta productos: ', error)

    def cargaProd(self):
        """

        Módulo que carga los datos de un producto en la parte superior de la interfaz al hacer click en un
        producto de la tabla productos de la interfaz

        """
        try:
            fila = var.ui.tabProd.selectedItems()
            datos = [var.ui.txtCod, var.ui.txtProd, var.ui.txtPrecio]

            if fila:
                row = [dato.text() for dato in fila]
            print(row)
            for i, dato in enumerate(datos):
                dato.setText(row[i])

        except Exception as error:
            print('Error al cargar datos de un producto ', error)

    def bajaProd(self):
        """

        Método que dado el nombre de un producto, lo manda a bajaProd en conexion para eliminarlo y
        después, llama a cargarTabProd para recargar la tabla productos de la interfaz

        """
        try:
            producto = var.ui.txtProd.text()
            conexion.Conexion.bajaProd(producto)
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print('Error al eliminar un producto ', error)

    def modifProd(self):
        """

        Módulo que recoge los datos de un producto y los manda a cargarTabProd en conexion para actualizar
        sus valores. A continuación llama a cargarTabProd para recargar la tabla productos de la interfaz

        """
        try:
            modprod = []
            producto = [var.ui.txtCod, var.ui.txtProd, var.ui.txtPrecio]
            for i in producto:
                modprod.append(i.text())
            conexion.Conexion.modifProd(modprod)
            conexion.Conexion.cargarTabProd(self)

        except Exception as error:
            print('Error al modificar un producto ', error)

    def buscarProd(self):
        """

        Método dado el nombre de un producto, carga sus datos en la tabla productos de la interfaz

        """
        try:
            prod = var.ui.txtBuscar.text()
            conexion.Conexion.buscarProducto(prod)
        except Exception as error:
            print('Error al buscar un producto ', error)

    def limpiaFormProd(self):
        """

        Método que en blanco los campos de producto en la interfaz.

        """
        try:
            var.ui.txtCod.setText("")
            var.ui.txtProd.setText("")
            var.ui.txtPrecio.setText("")
            var.ui.txtBuscar.setText("")
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print('Error al limpiar formulario productos ', error)

















