# -*- coding: utf-8 -*-

from .vendas import (AdicionarOrcamentoVendaView, AdicionarPedidoVendaView, OrcamentoVendaListView,
                     OrcamentoVendaVencidosListView, OrcamentoVendaVencimentoHojeListView, PedidoVendaListView,
                     PedidoVendaAtrasadosListView, PedidoVendaEntregaHojeListView, EditarOrcamentoVendaView,
                     EditarPedidoVendaView, GerarPedidoVendaView, CancelarOrcamentoVendaView,
                     CancelarPedidoVendaView, GerarCopiaOrcamentoVendaView, GerarCopiaPedidoVendaView,
                     GerarPDFOrcamentoVenda, GerarPDFPedidoVenda, AdicionarProspectView, ProspectListView, 
                     EditarProspectView, AdicionarContatoProspectView,
                     ContratarProspectView)
from .pagamento import *
from .ajax_views import InfoVenda
