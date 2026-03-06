import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')
django.setup()

from tienda.models import Producto, Cliente, Pedido
from django.db.models import Avg, Sum, Max, Min, Count


# PRIMERAS CONSULTAS, SON LAS 20 DE UNA MISMA TABLA

# 1. Todos los productos
print("1. Todos los productos:")
print(Producto.objects.all())

# 2. Total de productos
print("\n2. Total de productos:")
print(Producto.objects.count())

# 3. Producto más barato
print("\n3. Producto más barato:")
print(Producto.objects.order_by('precio').first())

# 4. Producto más caro
print("\n4. Producto más caro:")
print(Producto.objects.order_by('-precio').first())

# 5. Productos con precio menor a $10
print("\n5. Productos con precio menor a $10:")
print(Producto.objects.filter(precio__lt=10))

# 6. Productos con precio mayor a $20
print("\n6. Productos con precio mayor a $20:")
print(Producto.objects.filter(precio__gt=20))

# 7. Productos entre $5 y $15
print("\n7. Productos entre $5 y $15:")
print(Producto.objects.filter(precio__gte=5, precio__lte=15))

# 8. Buscar producto por nombre exacto
print("\n8. Buscar producto por nombre exacto:")
print(Producto.objects.filter(nombre="Arduino Uno R3"))

# 9. Productos que contengan 'sensor' en el nombre
print("\n9. Productos que contengan 'sensor' en el nombre:")
print(Producto.objects.filter(nombre__icontains="sensor"))

# 10. Productos que contengan 'WiFi' en la descripción
print("\n10. Productos que contengan 'WiFi' en la descripción:")
print(Producto.objects.filter(descripcion__icontains="WiFi"))

# 11. Productos ordenados por precio de menor a mayor
print("\n11. Productos ordenados por precio de menor a mayor:")
print(Producto.objects.order_by('precio'))

# 12. Productos ordenados por precio de mayor a menor
print("\n12. Productos ordenados por precio de mayor a menor:")
print(Producto.objects.order_by('-precio'))

# 13. Los primeros 5 productos
print("\n13. Los primeros 5 productos:")
print(Producto.objects.all()[:5])

# 14. Solo nombre y precio de todos los productos
print("\n14. Solo nombre y precio:")
print(Producto.objects.values('nombre', 'precio'))

# 15. Precio promedio
print("\n15. Precio promedio:")
print(Producto.objects.aggregate(promedio=Avg('precio')))

# 16. Suma total de precios
print("\n16. Suma total de precios:")
print(Producto.objects.aggregate(total=Sum('precio')))

# 17. Precio máximo y mínimo
print("\n17. Precio máximo y mínimo:")
print(Producto.objects.aggregate(maximo=Max('precio'), minimo=Min('precio')))

# 18. Productos ordenados alfabéticamente
print("\n18. Productos ordenados alfabéticamente:")
print(Producto.objects.order_by('nombre'))

# 19. Verificar si existe un producto
print("\n19. ¿Existe 'Soldador 30W'?:")
print(Producto.objects.filter(nombre="Soldador 30W").exists())

# 20. Obtener producto por id
print("\n20. Producto con id=1:")
print(Producto.objects.get(id=1))


# 20 CONSULTAS PARA LA TABLA CLIENTES

# 1. Todos los clientes
print("\n--- CLIENTES ---")
print("\n1. Todos los clientes:")
print(Cliente.objects.all())

# 2. Total de clientes
print("\n2. Total de clientes:")
print(Cliente.objects.count())

# 3. Clientes activos
print("\n3. Clientes activos:")
print(Cliente.objects.filter(activo=True))

# 4. Clientes inactivos
print("\n4. Clientes inactivos:")
print(Cliente.objects.filter(activo=False))

# 5. Buscar cliente por nombre exacto
print("\n5. Buscar cliente por nombre exacto:")
print(Cliente.objects.filter(nombre="Carlos Mendoza"))

# 6. Clientes cuyo nombre contenga 'an'
print("\n6. Clientes cuyo nombre contenga 'an':")
print(Cliente.objects.filter(nombre__icontains="an"))

# 7. Clientes con correo de Gmail
print("\n7. Clientes con correo Gmail:")
print(Cliente.objects.filter(correo__icontains="gmail.com"))

# 8. Clientes con correo de Hotmail
print("\n8. Clientes con correo Hotmail:")
print(Cliente.objects.filter(correo__icontains="hotmail.com"))

# 9. Primer cliente registrado
print("\n9. Primer cliente registrado:")
print(Cliente.objects.order_by('fecha_registro').first())

# 10. Último cliente registrado
print("\n10. Último cliente registrado:")
print(Cliente.objects.order_by('-fecha_registro').first())

# 11. Clientes ordenados alfabéticamente
print("\n11. Clientes ordenados alfabéticamente:")
print(Cliente.objects.order_by('nombre'))

# 12. Clientes ordenados alfabéticamente de forma inversa
print("\n12. Clientes ordenados de forma inversa:")
print(Cliente.objects.order_by('-nombre'))

# 13. Solo los primeros 5 clientes
print("\n13. Primeros 5 clientes:")
print(Cliente.objects.all()[:5])

# 14. Solo nombre y correo de todos los clientes
print("\n14. Solo nombre y correo:")
print(Cliente.objects.values('nombre', 'correo'))

# 15. Verificar si existe un cliente
print("\n15. ¿Existe 'Laura Ríos'?:")
print(Cliente.objects.filter(nombre="Laura Ríos").exists())

# 16. Obtener cliente por id
print("\n16. Cliente con id=1:")
print(Cliente.objects.get(id=1))

# 17. Clientes que tienen al menos un pedido
print("\n17. Clientes con al menos un pedido:")
print(Cliente.objects.filter(pedidos__isnull=False).distinct())

# 18. Clientes sin pedidos
print("\n18. Clientes sin pedidos:")
print(Cliente.objects.filter(pedidos__isnull=True))

# 19. Cantidad de pedidos por cliente
print("\n19. Cantidad de pedidos por cliente:")
print(Cliente.objects.annotate(total_pedidos=Count('pedidos')).values('nombre', 'total_pedidos'))

# 20. Clientes con más de 1 pedido
print("\n20. Clientes con más de 1 pedido:")
print(Cliente.objects.annotate(total_pedidos=Count('pedidos')).filter(total_pedidos__gt=1).values('nombre', 'total_pedidos'))


# 20 CONSULTAS PARA LA TABLA PEDIDOS

# 1. Todos los pedidos
print("\n--- PEDIDOS ---")
print("\n1. Todos los pedidos:")
print(Pedido.objects.all())

# 2. Total de pedidos
print("\n2. Total de pedidos:")
print(Pedido.objects.count())

# 3. Pedidos con estado CREADO
print("\n3. Pedidos con estado CREADO:")
print(Pedido.objects.filter(estado="CREADO"))

# 4. Pedidos con estado PAGADO
print("\n4. Pedidos con estado PAGADO:")
print(Pedido.objects.filter(estado="PAGADO"))

# 5. Pedidos con estado ENVIADO
print("\n5. Pedidos con estado ENVIADO:")
print(Pedido.objects.filter(estado="ENVIADO"))

# 6. Pedidos con estado CERRADO
print("\n6. Pedidos con estado CERRADO:")
print(Pedido.objects.filter(estado="CERRADO"))

# 7. Pedido más reciente
print("\n7. Pedido más reciente:")
print(Pedido.objects.order_by('-fecha').first())

# 8. Pedido más antiguo
print("\n8. Pedido más antiguo:")
print(Pedido.objects.order_by('fecha').first())

# 9. Pedidos de un cliente específico
print("\n9. Pedidos de Carlos Mendoza:")
print(Pedido.objects.filter(cliente__nombre="Carlos Mendoza"))

# 10. Pedidos que contienen un producto específico
print("\n10. Pedidos que contienen Arduino Uno R3:")
print(Pedido.objects.filter(productos__nombre="Arduino Uno R3"))

# 11. Pedidos ordenados por fecha de más reciente a más antiguo
print("\n11. Pedidos ordenados por fecha descendente:")
print(Pedido.objects.order_by('-fecha'))

# 12. Primeros 5 pedidos
print("\n12. Primeros 5 pedidos:")
print(Pedido.objects.all()[:5])

# 13. Cantidad de pedidos por estado
print("\n13. Cantidad de pedidos por estado:")
print(Pedido.objects.values('estado').annotate(total=Count('id')))

# 14. Pedidos que tienen más de 3 productos
print("\n14. Pedidos con más de 3 productos:")
print(Pedido.objects.annotate(total_productos=Count('productos')).filter(total_productos__gt=3).values('id', 'total_productos'))

# 15. Cantidad de productos por pedido
print("\n15. Cantidad de productos por pedido:")
print(Pedido.objects.annotate(total_productos=Count('productos')).values('id', 'total_productos'))

# 16. Verificar si existe un pedido con estado PAGADO
print("\n16. ¿Existe algún pedido PAGADO?:")
print(Pedido.objects.filter(estado="PAGADO").exists())

# 17. Obtener pedido por id
print("\n17. Pedido con id=1:")
print(Pedido.objects.get(id=1))

# 18. Pedidos que NO están cerrados
print("\n18. Pedidos que no están cerrados:")
print(Pedido.objects.exclude(estado="CERRADO"))

# 19. Pedido con mayor cantidad de productos
print("\n19. Pedido con mayor cantidad de productos:")
print(Pedido.objects.annotate(total_productos=Count('productos')).order_by('-total_productos').first())

# 20. Solo id, cliente y estado de todos los pedidos
print("\n20. Id, cliente y estado de todos los pedidos:")
print(Pedido.objects.values('id', 'cliente__nombre', 'estado'))

