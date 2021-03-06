#from django.conf.urls import patterns, url
from django.urls import path
from Consultas.views import *
urlpatterns= [		  path('listado_Clientes/',listado_Clientes_view),
					  path('listado_Combustibles/',listado_Combustibles_view),
					  path('listado_Estaciones/',listado_Estaciones_view),
					  path('listado_Surtidores/',listado_Surtidores_view),
					  path('listado_Manhguera/',listado_Manhguera_view),
					  path('listado_Serafin/',listado_Serafin_view),
					  path('listado_Mangueras_tabla/',listado_Mangueras_tabla_view),
					  path('listado_creditos/',listado_creditos_view),
					  path('listado_compras/',listado_compras_view),
					  path('listado_descuentos/',listado_descuentos_view),
					  path('listado_gastos/',listado_gastos_view),
					  path('listado_depositos/',listado_depositos_view),
					  path('listado_pagos/',listado_pagos_view),
					  path('listado_PrecioCombustible/',listado_PrecioCombustible_view),
					  path('listado_Tanques_ajax/',listado_Tanques_ajax_view),
					  path('listado_Tanques_tabla/',listado_Tanques_tabla_view),
					  path('reporte_diario_ajax/',reporte_diario_ajax_view),
					  path('lectura_Xreporte_ajax/',lectura_Xreporte_ajax_view),
					  path('listado_creditos_reporte/',listado_creditos_reporte_view),
					  path('listado_gastos_reporte/',listado_gastos_reporte_view),
					  path('listado_depositos_reporte/',listado_depositos_reporte_view),
					  path('Movimiento_vista_reporte/',Movimiento_vista_reporte_view),
					  path('listado_pagos_reporte/',listado_pagos_reporte_view),
					  path('listado_reportes/',listado_reportes_view),
					  path('listado_reportes_ajax/',listado_reportes_ajax_view),
					  path('listado_Tarjetas/',listado_Tarjetas_view),
					  path('listado_tarjetas_reporte/',listado_tarjetas_reporte_view),
					  path('listado_descuentos_reporte/',listado_descuentos_reporte_view),
					  path('listado_serafin_reporte/',listado_serafin_reporte_view),
					  path('listado_movimientos_reporte/',listado_movimientos_reporte_view),
					  path('listado_heart/',listado_heart_view),
					  #path('analizar_rf/',analizar_rf_view),
					  #path('analizar_rf_train/',analizar_rf_train_view),
					  #reportes mensuales
					  path('reporte_sa_compra_mes_ajax/',reporte_sa_compra_mes_ajax_view),
					  path('reporte_creditos_mes_ajax/',reporte_creditos_mes_ajax_view),
					  path('listado_gastos_mes_ajax/',listado_gastos_mes_view),
					  path('listado_gastos_reporte_mes/',listado_gastos_reporte_mes_view),
					  path('listado_creditos_reporte_mes/',listado_creditos_reporte_mes_view),
					  path('listado_credito_mes_ajax/',listado_credito_mes_view),
					  path('reporte_creditos_mes_cliente_ajax/',reporte_creditos_mes_cliente_ajax_view),
					  path('listado_Tarjeta_mes_ajax/',listado_Tarjeta_mes_view),
					  path('reporte_tarjeta_mes_tipo_ajax/',reporte_tarjeta_mes_tipo_ajax_view),
					  path('listado_tarjeta_reporte_mes/',listado_tarjeta_reporte_mes_view),
					  path('listado_descuentos_mes_ajax/',listado_descuentos_mes_view),
					  path('reporte_descuentos_mes_cliente_ajax/',reporte_descuentos_mes_cliente_ajax_view),
					  path('listado_Descuento_reporte_mes/',listado_Descuento_reporte_mes_view),
					  path('listado_pagos_mes_ajax/',listado_pagos_mes_view),
					  path('reporte_Pagos_mes_cliente_ajax/',reporte_Pagos_mes_cliente_ajax_view),
					  path('listado_Pago_reporte_mes/',listado_Pago_reporte_mes_view),

					  ]