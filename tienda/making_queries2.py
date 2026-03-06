from tienda.models import Cliente, Producto, Pedido
from django.db.models import Avg, Sum, Max, Min, Count

# 10 CONSULTAS ENTRE CLIENTE Y PRODUCTO

# 1. Clientes que han pedido el producto "Arduino Uno R3"
print("1. Clientes que han pedido Arduino Uno R3:")
print(Cliente.objects.filter(pedidos__productos__nombre="Arduino Uno R3").distinct())

# 2. Productos que ha pedido el cliente "Carlos Mendoza"
print("\n2. Productos pedidos por Carlos Mendoza:")
print(Producto.objects.filter(pedidos__cliente__nombre="Carlos Mendoza").distinct())

# 3. Clientes que han pedido productos con precio mayor a $20
print("\n3. Clientes que han pedido productos mayores a $20:")
print(Cliente.objects.filter(pedidos__productos__precio__gt=20).distinct())

# 4. Productos pedidos por clientes activos
print("\n4. Productos pedidos por clientes activos:")
print(Producto.objects.filter(pedidos__cliente__activo=True).distinct())

# 5. Clientes que han pedido productos que contengan "sensor" en el nombre
print("\n5. Clientes que han pedido algún sensor:")
print(Cliente.objects.filter(pedidos__productos__nombre__icontains="sensor").distinct())

# 6. Cantidad de productos distintos pedidos por cada cliente
print("\n6. Cantidad de productos por cliente:")
print(Cliente.objects.annotate(total_productos=Count('pedidos__productos')).values('nombre', 'total_productos'))

# 7. Clientes que han pedido más de 3 productos en total
print("\n7. Clientes con más de 3 productos pedidos:")
print(Cliente.objects.annotate(total=Count('pedidos__productos')).filter(total__gt=3).values('nombre', 'total'))

# 8. Precio promedio de los productos pedidos por cada cliente
print("\n8. Precio promedio de productos por cliente:")
print(Cliente.objects.annotate(promedio=Avg('pedidos__productos__precio')).values('nombre', 'promedio'))

# 9. Productos que nunca han sido pedidos
print("\n9. Productos que nunca han sido pedidos:")
print(Producto.objects.filter(pedidos__isnull=True))

# 10. Clientes que han pedido el producto más caro
print("\n10. Clientes que han pedido el producto más caro:")
precio_max = Producto.objects.aggregate(Max('precio'))['precio__max']
print(Cliente.objects.filter(pedidos__productos__precio=precio_max).distinct())