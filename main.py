import locale

import facturas
import informes
import products
from aviso import *
from ventana import *
from windowCal import *
import sys, var, events, conexion, clients, locale
from datetime import *
locale.setlocale(locale.LC_ALL, 'es-ES')

'''

Meter esto en ventana.py
import img.backup
import img.bin
import img.calendario
import img.carpeta
import img.cerrar
import img.imprimir
import img.invoid
import img.limpiar
import img.ojo
import img.restore

'''

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''

        clase calendario

        '''
        super(DialogCalendar, self).__init__()
        var.dlgCalendar = Ui_windowCal()
        var.dlgCalendar.setupUi(self)
        diactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgCalendar.calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diactual)))
        var.dlgCalendar.calendar.clicked.connect(clients.Clientes.cargarFecha)


class DialogAviso(QtWidgets.QDialog):
    '''

    si da error añadir esto en aviso.py

    self.btnboxaviso.accepted.connect(aviso.accept)
    self.btnboxaviso.rejected.connect(aviso.reject)

    '''

    def __init__(self):
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_aviso()
        var.dlgaviso.setupUi(self)
        # Otra manera de solucionar el error sin hacer el copia-pega
        var.dlgaviso.btnboxaviso.accepted.connect(self.accept)
        var.dlgaviso.btnboxaviso.rejected.connect(self.reject)


class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''

        ventana abrir explorador windows

        '''
        super(FileDialogAbrir, self).__init__()


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        conexion.Conexion.create_db(var.filedb)
        '''
        
        Eventos de botón
        
        '''
        # var.ui.btnsalir.clicked.connect(events.Eventos.Salida)
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.setSexo)
        # var.ui.chGroupPago.buttonClicked.connect(clients.Clientes.setPago)
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnLimpiaForm.clicked.connect(clients.Clientes.limpiarForm)
        var.ui.btnBaja.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnMod.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnGrabaProd.clicked.connect(products.Productos.guardaProd)
        var.ui.btnBorraProd.clicked.connect(products.Productos.bajaProd)
        var.ui.btnModProd.clicked.connect(products.Productos.modifProd)
        var.ui.btnBuscar.clicked.connect(products.Productos.buscarProd)
        var.ui.btnBuscaCliFac.clicked.connect(facturas.Facturas.buscaCli)
        var.ui.btnFechaFac.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnFacturar.clicked.connect(facturas.Facturas.altaFac)
        var.ui.btnPdfCli.clicked.connect(informes.Informes.ListadoCliente)
        var.ui.btnReportArticulos.clicked.connect(informes.Informes.ListadoArticulo)
        var.ui.btnReportCli.clicked.connect(events.Eventos.Imprimir)
        var.ui.btnLimpiaFormProd.clicked.connect(products.Productos.limpiaFormProd)
        var.ui.btnImprimirFactura.clicked.connect(informes.Informes.factura)
        var.ui.btnLimpiaFormFacturas.clicked.connect(facturas.Facturas.limpiarFacturas)
        var.ui.btnBorrarVenta.clicked.connect(conexion.Conexion.borrarVenta)
        '''
        
        Eventos de la barra de menús
        
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salida)
        var.ui.actionAbrir.triggered.connect(events.Eventos.Abrir)
        var.ui.actionCrear_backup.triggered.connect(events.Eventos.Backup)
        var.ui.actionRestaurar.triggered.connect(events.Eventos.Restaurar)
        var.ui.actionImportar_datos.triggered.connect(events.Eventos.ImportarDatos)
        var.ui.actionExportar_datos.triggered.connect(events.Eventos.ExportarDatos)
        var.ui.actionImprimir.triggered.connect(events.Eventos.Imprimir)
        var.ui.actionAutor.triggered.connect(events.Eventos.Autor)
        var.ui.actionContacto.triggered.connect(events.Eventos.Contacto)
        var.ui.actionVersion.triggered.connect(events.Eventos.Version)
        '''
        
        Eventos caja de texto
        
        '''
        var.ui.txtdni.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.mayuscNome)
        var.ui.txtApe.editingFinished.connect(clients.Clientes.mayuscApe)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.mayuscDir)
        var.txtCantidad = QtWidgets.QLineEdit()
        var.txtCantidad.editingFinished.connect(facturas.Facturas.totalLineaVenta)
        '''
        
        Eventos QTwidget
        
        '''
        events.Eventos.resizeTablaCli(self)
        events.Eventos.resizeTablaArticulos(self)
        events.Eventos.resizeTablaFacturas(self)
        events.Eventos.resizeTablaVentas(self)
        var.ui.tabCliente.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabCliente.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabProd.clicked.connect(products.Productos.cargaProd)
        var.ui.tabProd.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabFacturas.clicked.connect(facturas.Facturas.cargaFac)
        var.ui.tabFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabVentas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        # facturas.Facturas.preparaLineaVenta(self)
        facturas.Facturas.cargarLineaVenta(0)
        '''
        
        Base de datos
        
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTabCli(self)
        conexion.Conexion.cargarTabProd(self)
        conexion.Conexion.cargaTabFacturas(self)
        '''
        
        Eventos de comboBox
        
        '''
        clients.Clientes.cargaProv(self)
        # var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.cmbProv.currentIndexChanged.connect(clients.Clientes.cargaMuni)
        # var.ui.cmbMuni.activated[str].connect(clients.Clientes.selMuni)
        conexion.Conexion.cargarCmbProducto(self)
        var.cmbproducto.currentIndexChanged.connect(facturas.Facturas.procesoVenta)
        '''
        
        spinbox
        
        '''
        var.ui.spinEnvio.valueChanged.connect(clients.Clientes.envio)
        ''' 
        
        barra de estado
        
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        day = datetime.now()
        var.ui.lblFecha.setText(day.strftime('%A, %d del %B de %Y'))
        '''
        
        Eventos menú herramientas
        
        '''
        var.ui.actionvarSalir.triggered.connect(events.Eventos.Salida)
        var.ui.actionvarOpen.triggered.connect(events.Eventos.Abrir)
        var.ui.actionvarBackup.triggered.connect(events.Eventos.Backup)
        var.ui.actionvarBackupRestaurar.triggered.connect(events.Eventos.Restaurar)
        var.ui.actionvarImprimir.triggered.connect(events.Eventos.Imprimir)
        var.ui.actionListado_clientes.triggered.connect(informes.Informes.ListadoCliente)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    ventana = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - ventana.width()) // 2
    y = (desktop.height() - ventana.height()) // 2
    ventana.move(x, y)
    var.dlgaviso = DialogAviso()
    var.dlgCalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    ventana.show()
    sys.exit(app.exec())
