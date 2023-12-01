from PyQt5.QtWidgets import QMessageBox

import conexion
from ventana import *
import var


class Clientes():
    #Pasarle dni al módulo para los tests
    def validarDNI():
        """

        Módulo que valida el DNI de un cliente

        """
        try:
            global dnivalido
            dnivalido = False
            #Comentar las 2 líneas de abajo para los tests
            dni = var.ui.txtdni.text()
            var.ui.txtdni.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # digito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayúsculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            #Comentar desde aquí hasta antes del return para los tests
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblvalidodni.setStyleSheet('QLabel {color: green;}')
                    var.ui.lblvalidodni.setText('V')
                    var.ui.txtdni.setStyleSheet('background-color: white;')
                    dnivalido = True
                else:
                    var.ui.lblvalidodni.setStyleSheet('QLabel {color: red;}')
                    var.ui.lblvalidodni.setText('X')
                    var.ui.txtdni.setStyleSheet('background-color: pink;')
            else:
                var.ui.lblvalidodni.setStyleSheet('QLabel {color: red;}')
                var.ui.lblvalidodni.setText('X')
                var.ui.txtdni.setStyleSheet('background-color: pink;')
            #Descomentar return para los tests
            #return dni
        except Exception as error:
            print('Error en módulo validar DNI', error)

    # def setSexo(self):
    #     try:
    #         if var.ui.rbtHome.isChecked():
    #             print('Marcado masculino')
    #         elif var.ui.rbtMujer.isChecked():
    #             print('Marcado femenino')
    #     except Exception as error:
    #         print('Error al seleccionar sexo ', error)
    #
    # def setPago(self):
    #     try:
    #         if var.ui.chkEfectivo.isChecked():
    #             print('Has seleccionado efectivo')
    #         if var.ui.chkTarjeta.isChecked():
    #             print('Has seleccionado tarjeta')
    #         if var.ui.chkTrans.isChecked():
    #             print('Has seleccionado tranferencia')
    #         if var.ui.chkCargoCuenta.isChecked():
    #             print('Has seleccionado cargo a cuenta')
    #     except Exception as error:
    #         print('Error al seleccionar forma de pago ', error)


    '''
    def cargaProv(self):
        try:
            var.ui.cmbProv.clear()
            prov = ["", "A Coruña", "Lugo", "Ourense", "Pontevedra"]
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en el módulo cargar provincia, ', error)
    '''

    def cargaProv(self):
        """

        Módulo que llama al método de conexión para cargar las provincias en el comboBox de la interfaz

        """
        try:
            var.ui.cmbProv.clear()
            prov = conexion.Conexion.cargaProvCon(self)
            nom = prov.values()
            for i in nom:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error en el módulo cargar provincia, ', error)

    # def selProv(prov):
    #     try:
    #         print('Has seleccionado la provincia de ', prov)
    #     except Exception as error:
    #         print('Error en el módulo seleccionar provincia, ', error)

    # def cargaMuni(self):
    #     try:
    #         var.ui.cmbMuni.clear()
    #         muni = ["", "a"]
    #         for i in muni:
    #             var.ui.cmbMuni.addItem(i)
    #     except Exception as error:
    #         print('Error en el módulo cargar municipio, ', error)

    def cargaMuni(self):
        """

        Módulo que llama a su correspondiente método en conexion para cargar los municipios en función de la provincia

        """
        try:
            var.ui.cmbMuni.clear()
            mun = conexion.Conexion.cargaMuniCon(self)
            for i in mun:
                var.ui.cmbMuni.addItem(i)
        except Exception as error:
            print('Error en el módulo cargar municipio, ', error)

    # def selMuni(muni):
    #     try:
    #         print('Has seleccionado el municipio de ', muni)
    #     except Exception as error:
    #         print('Error en el módulo seleccionar municipio, ', error)

    def cargarFecha(qDate):
        """

        Módulo que da formato a la fecha y la cargar en el LineEdit de la interfaz

        """
        try:
            data = (str(qDate.day()).zfill(0)+ '/'+ str(qDate.month()).zfill(0) + '/' + str(qDate.year()))
            #data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            if var.ui.tabPrograma.currentIndex()==0:
                var.ui.txtAlta.setText(str(data))
            elif var.ui.tabPrograma.currentIndex()==1:
                var.ui.txtFechaFac.setText(str(data))
            var.dlgCalendar.hide()
        except Exception as error:
            print('Error cargar fecha en txtFecha', error)

    def mayuscNome():
        """

        Módulo que pone en mayúsculas la inicial del nombre de un cliente

        """
        try:
            nome = var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.capitalize())  # capitalize pone en mayus la primera letra de la primera palabra
        except Exception as error:
            print('Error al escribir el nombre ', error)

    def mayuscApe():
        """

        Módulo que pone en mayúsculas las iniciales de los apellidos de un cliente

        """
        try:
            ape = var.ui.txtApe.text()
            var.ui.txtApe.setText(ape.title())  # title pone en mayusc la primera de cada palabra
        except Exception as error:
            print('Error al escribir los apellidos ', error)

    def mayuscDir():
        """

        Módulo que pone en mayúsculas las iniciales de la dirección de un cliente

        """
        try:
            dir = var.ui.txtDir.text()
            var.ui.txtDir.setText(dir.title())
        except Exception as error:
            print('Error al escribir la dirección ', error)

    def envio(self):
        """

        Módulo que asigna un texto u otro al label al lado del spinbox dependiendo del número

        """
        try:
            if var.ui.spinEnvio.value() == 0:
                var.ui.lblEnvio.setText('Recogida por cliente')
            elif var.ui.spinEnvio.value() == 1:
                var.ui.lblEnvio.setText('Envío Nacional Paquetería Express Urgente')
            elif var.ui.spinEnvio.value() == 2:
                var.ui.lblEnvio.setText('Envío Nacional Paquetería Normal')
            elif var.ui.spinEnvio.value() == 3:
                var.ui.lblEnvio.setText('Envío Interncional')
        except Exception as error:
            print('Error en modulo envío', error)

    def guardaCli(self):
        """

        Módulo que recoge los datos de un cliente para cargarlos en la tabla de la interfaz
        y mandárselos a su correspondiente método en conexion para guardarlo en la BD

        """
        try:
            # Preparamos el registro
            newCli = []
            cliente = [var.ui.txtdni, var.ui.txtAlta, var.ui.txtApe, var.ui.txtNome, var.ui.txtDir]  # para la BD
            tabCli = []  # para la tableView
            client = [var.ui.txtdni, var.ui.txtApe, var.ui.txtNome, var.ui.txtAlta]
            # código para cargar la tabla
            for i in cliente:
                newCli.append(i.text())
            for i in client:
                tabCli.append(i.text())
            newCli.append(var.ui.cmbProv.currentText())
            newCli.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHome.isChecked:
                newCli.append("Hombre")
            elif var.ui.rbtMujer.isChecked:
                newCli.append("Mujer")
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo cuenta')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            pagos = set(pagos)  # evita duplicados
            tabCli.append(', '.join(pagos))
            newCli.append(', '.join(pagos))
            newCli.append(var.ui.spinEnvio.value())

            # cargamos la tabla
            if dnivalido:
                row = 0
                column = 0
                var.ui.tabCliente.insertRow(row)
                for campo in tabCli:
                    cell = QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabCliente.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.altaCli(newCli)
            else:
                # print('DNI no válido')
                msgBox = QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                msgBox.setMinimumSize(1024, 1024)  # no hace nada
                msgBox.setWindowTitle('Aviso DNI')
                msgBox.setText("DNI inválido")
                msgBox.exec()
        except Exception as error:
            print('Error al guardar clientes ', error)

    def limpiarForm(self):
        """

        Módulo que deja en blanco los campos de datos de un cliente

        """
        try:
            var.ui.txtdni.setText("")
            var.ui.txtApe.setText("")
            var.ui.txtNome.setText("")
            var.ui.txtDir.setText("")
            var.ui.txtAlta.setText("")
            #var.ui.cmbProv.clear
            #var.ui.cmbMuni.clear
            var.ui.chkTrans.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            # Selecciona el "" que creamos cuando hicimos los comboBox
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMuni.setCurrentIndex(0)
            # Primero quitar exclusividad y luego volver a ponerla
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtHome.setChecked(False)
            var.ui.rbtMujer.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.spinEnvio.setValue(0)

        except Exception as error:
            print('Error al limpiar el formulario ', error)

    def cargaCli(self):
        """

        Módulo que seleccionando un cliente de la tabla de la interfaz, lo carga en la parte superior
        rellenando los campos correspondientes. Para esto llama al método oneClie de conexion.

        """
        try:
            fila = var.ui.tabCliente.selectedItems()
            datos = [var.ui.txtdni, var.ui.txtApe, var.ui.txtNome, var.ui.txtAlta]

            if fila:
                row = [dato.text() for dato in fila]
                var.ui.txtDNIFac.setText(row[0])
                var.ui.lblNomFac.setText(row[1] + ' ' + row[2])
            print(row)
            for i, dato in enumerate(datos):  # cargamos los datos en las cajas de texto
                dato.setText(row[i])
            if 'Efectivo' in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if 'Tarjeta' in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if 'Transferencia' in row[4]:
                var.ui.chkTrans.setChecked(True)
            if 'Cargo' in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)

            registro = conexion.Conexion.oneClie(row[0])
            print(registro)
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMuni.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHome.setChecked(True)
            elif str(registro[3]) == 'Mujer':
                var.ui.rbtMujer.setChecked(True)
            var.ui.spinEnvio.setValue(int(registro[4]))


        except Exception as error:
            print('Error al cargar datos de un cliente ', error)

    def modifCli(self):
        """

        Método que recoge las modificaciones hechas a un cliente para mandárselas a cargarTabCli en conexión,
        para que este lo guarde en la BD. Y llama a cargarTabCli para recargar la tabla de clientes de la interfaz.

        """
        try:
            modcliente = []
            cliente = [var.ui.txtdni, var.ui.txtAlta, var.ui.txtApe, var.ui.txtNome, var.ui.txtDir]
            for i in cliente:
                modcliente.append(i.text())
            modcliente.append(var.ui.cmbProv.currentText())
            modcliente.append(var.ui.cmbMuni.currentText())
            if var.ui.rbtHome.isChecked:
                modcliente.append("Hombre")
            elif var.ui.rbtMujer.isChecked:
                modcliente.append("Mujer")
            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append('Cargo cuenta')
            if var.ui.chkTrans.isChecked():
                pagos.append('Transferencia')
            if var.ui.chkEfectivo.isChecked():
                pagos.append('Efectivo')
            if var.ui.chkTarjeta.isChecked():
                pagos.append('Tarjeta')
            pagos = set(pagos)
            modcliente.append(', '.join(pagos))
            modcliente.append(var.ui.spinEnvio.value())
            conexion.Conexion.modifCli(modcliente)
            conexion.Conexion.cargarTabCli(self)

        except Exception as error:
            print('Error al modificar un cliente ', error)

    def bajaCli(self):
        """

        Método que envía el DNI de un cliente a bajaCli en conexion para que lo elimine,
        y llama a cargarTabCli para recargar la tabla de clientes de la interfaz.

        """
        try:
            dni = var.ui.txtdni.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargarTabCli(self)
        except Exception as error:
            print('Error al eliminar un cliente ', error)


