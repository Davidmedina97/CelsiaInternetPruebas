2.1. Elabore un diagrama de componentes de la aplicación. Debe cargar el archivo en la siguiente ruta del repositorio:


2.2. ¿Qué mecanismos de seguridad incluirías en la aplicación para garantizar la protección del acceso a los datos?

RTA: OAuth aunthentication, jwt, validación de datos con Pydantic y configuración de del CORs

2.3. ¿Qué estrategia de escalabilidad recomendarías para la aplicación considerando que el crecimiento proyectado será de 1,000,000 de clientes por año?

RTA:Aquitectura de microservicios, servicios en la nube y optimización de base de datos

2.4. ¿Qué patrón o patrones de diseño recomendarías para esta solución y cómo se implementarían? (Justifique)

RTA: Patron de micro servicios: Este permite dividir la aplicación e servicios pequeños que pueden ser desarrollados y desplegados de una forma más facil y autonoma. Esto ayudaria a suplir nececidades especificas con cada microservicio, lo que facilita el matenimiento y escalabilidad.

Patron de cache: Esto ayuda a mejorar el rendimiento en las bases de datos.

2.5. ¿Qué recomendaciones harías para optimizar el manejo y la persistencia de datos de la aplicación, teniendo en cuenta que esta aplicación tiene una alta transaccionalidad?

RTA: - Normalización y desnormalización selectiva
    - Uso de indices
    - Implementación de cache
    - Optimización de consultas
    - Monitoreo y ajustes
    - Uso de bases de datos no SQl

1. Redes
3.1. Explica la diferencia entre un router y un switch. ¿Cuándo usarías cada uno?
 La diferencia es que un router conecta diferentes redes dirigiendo su trafico y el switch conecta los diferentes dispositivos dentro de una red LAN.
Router se usa cuando se necesita conectar la red Local a otra red
Switch se usa cuando necesitas conecta varios dispositivos en la misma red Local

3.2. Describe las siete capas del modelo OSI y menciona brevemente la función principal de cada una

Capa Fisica: Transmite y recibe datos
Capa de enlace: Proporciona el enlace entre dos nodos conectados
Capa de red: gestiona el direccionamiento y enrutamiento
Capa de transporte: Asegura la transferencia de datos entre dos sistemas
Capa de Seccion: Administra las seciones entre aplicaciones
Capa de presentación: Traduce los datos
capa de aplicacion: Da los servicios de red que interatuan directamente con el usuario final.

3.3. Explica las diferencias entre los protocolos TCP y UDP. Dar un ejemplo de cuándo usarías cada uno?

Las diferencias son: TCP es orientado a conexión, garantiza la entrega de datos, ajusta la transmisión de datos segun la capacidad del receptor, consume más recursos.

UDP es sin conexión, es más veloz pero no garantiza la entrega de datos, no es fiable, consume pocos recursos

3.4. ¿Qué es una máscara de subred y cómo se utiliza para dividir una red en subredes más pequeñas?

Una máscara de subred es un número de 32 bits que se utiliza en redes IP para dividir una red en subredes más pequeñas. Se ajusta la máscara de subred para incluir más bits en la parte de la red. Esto se conoce como “subnetting”

3.5. ¿Puedes mencionar algunos protocolos de enrutamiento dinámico y explicar brevemente cómo funcionan?

 RIP: Utiliza el número de saltos (hops) como métrica para determinar la mejor ruta.
 OSPF: enrutamiento de estado de enlace que utiliza un algoritmo para calcular la ruta más corta
 EIGRP: Utiliza una métrica ancho de banda, retraso, carga y confiabilidad.
 BGP: Utiliza una métrica basada en políticas y atributos de ruta.

1. Gestión de Proyectos
4.1. ¿En qué grupos de procesos de dirección de proyectos es creado un presupuesto detallado del proyecto?

Grupo de Procesos de Planificación

4.2. ¿En qué grupo de procesos de la dirección de proyectos es creada el acta de constitución del proyecto?

Grupo de Procesos de Inicio

4.3. El equipo de proyecto acaba de completar el primer cronograma y presupuesto del proyecto. La próxima cosa a hacer es:

Desarrollar el plan de Gestion de Proyecto.

4.4. Un primer cronograma del proyecto puede ser creado solamente después de crear: La estructura de desglose del trabajo


4.5. Una persona que debe estar al mando durante la planificación de la gestión del proyecto es: Director del proyecto

4.6. ¿Cuál de son las entradas del grupo de procesos de inicio de un proyecto?
 - Acta de constitución del proyecto
 - Registro de interesados
 - Declaración del trabajo del proyecto
 - Factores ambientales de la empresa
 - Activos de los procesos de la organización

4.7. El patrocinador del proyecto acaba de aprobar el acta de constitución del proyecto, ¿cuál es la próxima cosa a hacer?

4.8. Acaban de ser establecidas las restricciones de alto nivel del cronograma del proyecto. ¿En qué grupo de procesos de dirección de proyectos se encuentra?

4.9. ¿Qué grupos de procesos deben ser incluidos en cada proyecto?

4.10. ¿Qué grupo de procesos de la dirección de proyecto necesita normalmente el mayor tiempo y número de recursos?

5. Caso práctico
Celsia internet en su proceso de expansión, se ha fijado como meta un crecimiento para los proximos 5 años donde se espera tener un millon de clientes. Para el que el proceso de facturación y recaudo sea efectivo, se requiere que el sistema de liquidación mensual de procese en los tiempos de corte establecidos de acuerdo con los ciclos de facturación definidos, los servicios que han sido prestados a sus clientes y las novedades reportadas en cada periodo. Que estrategias implementaría en el desarrollo de los componentes de liquidación y facturación masiva de servicios por ciclo y el recaudo de los pagos de las factura, buscando que el sistema sea robusto, escalable, resiliente, confiable y mantenible en el tiempo, ademas de la seguridad de la infomración y el tratamiento de los datos personales de los clientes.

Describa o diseñe las estrategias que incluiría para dar solución a los requerimientos solicitados en la implementación de los componentes descritos (Justifique la priorización de ciertos atributos sobre otros atributos de calidad en la propuesta de solución).

RTA: Estrategias para el Sistema de Liquidación y Facturación
Arquitectura en Microservicios:

Objetivo: Escalabilidad y resiliencia.
Acción: Dividir el sistema en servicios independientes (liquidación, facturación, recaudo) para facilitar la escalabilidad y la recuperación ante fallos.
Escalabilidad Horizontal:

Objetivo: Manejar el crecimiento de usuarios y datos.
Acción: Utilizar contenedores (Docker) y orquestación (Kubernetes) para gestionar la carga y escalar los servicios.
Resiliencia y Recuperación:

Objetivo: Minimizar el impacto de fallos.
Acción: Implementar redundancia, copias de seguridad automáticas y monitoreo constante.
Seguridad y Protección de Datos:

Objetivo: Cumplir con normativas y proteger datos personales.
Acción: Aplicar cifrado, autenticación robusta, y políticas de privacidad conforme a regulaciones (GDPR, CCPA).
Confiabilidad y Mantenibilidad:

Objetivo: Asegurar el funcionamiento continuo y facilitar el mantenimiento.
Acción: Realizar pruebas automatizadas y mantener una documentación actualizada.
Priorización
Seguridad y Protección de Datos
Escalabilidad y Rendimiento
Resiliencia y Recuperación
Confiabilidad y Mantenibilidad
Arquitectura y Diseño del Sistema