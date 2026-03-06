from tienda.models import Cliente, Producto, Pedido
from django.db.models import Avg, Sum, Max, Min, Count

# 5 CONSULTAS ENTRE CLIENTE, PRODUCTO Y PEDIDO

# 1. Clientes, sus pedidos y los productos de cada pedido
print("1. Clientes con sus pedidos y productos:")
for cliente in Cliente.objects.prefetch_related('pedidos__productos'):
    for pedido in cliente.pedidos.all():
        print(f"  {cliente.nombre} - Pedido #{pedido.id} ({pedido.estado}): {[p.nombre for p in pedido.productos.all()]}")

# 2. Pedidos con estado PAGADO, el cliente que lo hizo y los productos que contiene
print("\n2. Pedidos PAGADOS con cliente y productos:")
for pedido in Pedido.objects.filter(estado="PAGADO").prefetch_related('productos').select_related('cliente'):
    print(f"  {pedido.cliente.nombre} - Pedido #{pedido.id}: {[p.nombre for p in pedido.productos.all()]}")

# 3. Total gastado por cliente sumando los precios de los productos en sus pedidos
print("\n3. Total gastado por cada cliente:")
print(Cliente.objects.annotate(total_gastado=Sum('pedidos__productos__precio')).values('nombre', 'total_gastado'))

# 4. Productos más pedidos con cuántos clientes distintos los han pedido
print("\n4. Productos y cantidad de clientes distintos que los han pedido:")
print(Producto.objects.annotate(clientes=Count('pedidos__cliente', distinct=True)).values('nombre', 'clientes').order_by('-clientes'))

# 5. Clientes activos con pedidos ENVIADOS y los productos de esos pedidos
print("\n5. Clientes activos con pedidos ENVIADOS y sus productos:")
for cliente in Cliente.objects.filter(activo=True, pedidos__estado="ENVIADO").prefetch_related('pedidos__productos').distinct():
    for pedido in cliente.pedidos.filter(estado="ENVIADO"):
        print(f"  {cliente.nombre} - Pedido #{pedido.id}: {[p.nombre for p in pedido.productos.all()]}")