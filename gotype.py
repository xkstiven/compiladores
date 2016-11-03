# gotype.py
# coding: utf-8
'''
Sistema de Tipos de mini Go
===========================
Este archivo define las clases de representación de tipos.  Esta es una
clase general usada para representar todos los tipos.  Cada tipo es
entonces una instancia singleton de la clase tipo.

        class GoType(object):
                pass

        int_type = GoType("int",...)
        float_type = GoType("float",...)
        string_type = GoType("string", ...)

El contendo de la clase tipo es enteramente suya.  Sin embargo, será
mínimamente necesario el codificar cierta información sobre:

        a.  Que operaciones son soportadas (+, -, *, etc.).
        b.  El tipo resultante de cada operación
        c.  Valores por defecto para las instancias nuevas de cada tipo
        d.  Métodos para chequeo-tipo de operadores binarios y unarios
        e.  Mantener un registro de tipos (pe. 'int', 'float') para las
            instancias (pe. 'int_type', 'float_type', 'string_type', etc.)

Una vez que se haya definido los tipos incorporado, se deberá segurar

que sean registrados en la tabla de símbolos o código que compruebe
los nombres de tipo en 'gocheck.py'.
'''
class GoType(object):
        '''
        Clase que representa un tipo en el lemguaje mini go.  Los tipos
        son declarados como instancias singleton de este tipo.
        '''
        def __init__(self, name, bin_ops=set(), un_ops=set()):
                '''
                Deberá ser implementada por usted y averiguar que almacenar
                '''
                self.name = name
                self.bin_ops = bin_ops
                self.un_ops = un_ops


# Crear instancias específicas de los tipos.  Usted tendrá que adicionar
# los argumentos apropiados dependiendo de su definición de GoType
int_type = GoType("int",
        set(('PLUS', 'MINUS', 'TIMES', 'DIVIDE','LE', 'LT', 'EQ', 'NE', 'GT', 'GE')),
        set(('PLUS', 'MINUS')),
        )
float_type = GoType("float",
        set(('PLUS', 'MINUS', 'TIMES', 'DIVIDE','LE', 'LT', 'EQ', 'NE', 'GT', 'GE')),
        set(('PLUS', 'MINUS')),
        )
string_type = GoType("string",
        set(('PLUS',)),
        set(),
        )
boolean_type = GoType("bool",
        set(('LAND', 'LOR', 'EQ', 'NE')),
        set(('LNOT',))
        )
# En el código de verificación, deberá hacer referencia a los
# objetos de tipos de arriba.  Piense en como va a querer tener
# acceso a ellos.
