def buscar_persona(request):
    lista_personas = ['expedientes', 'carga_expediente', 'lista_expedientes', 'expedientes_finalizados', 'actualizar_expediente', 'buscar_expedientes', 
                        'correo', 'nuevo_envio', 'listar_correo', 'actualizar_correo', 'correo_finalizados', 'buscar_envio',
                        'libros', 'nuevo_libro', 'listar_libros', 'actualizar_libro',
                        'nueva_acta', 'listar_actas', 'detalle_acta', 'actualizar_acta', 'nueva_firma', 'buscar_acta']
    return {'lista_personas':lista_personas}

def buscar_exp(request):
    lista_expedientes = ['expedientes', 'carga_expediente', 'lista_expedientes', 'actualizar_expediente','expedientes_finalizados', 'buscar_expedientes']
    return {'lista_expedientes' : lista_expedientes}

def buscar_correo(request):
    lista_correos = ['correo', 'nuevo_envio', 'listar_correo', 'actualizar_correo', 'correo_finalizados', 'buscar_envio',]
    return {'lista_correos' : lista_correos}

def buscar_act(request):
    lista_actas = ['libros', 'nuevo_libro', 'listar_libros', 'actualizar_libro',
                   'nueva_acta', 'listar_actas', 'detalle_acta', 'actualizar_acta', 'nueva_firma', 'buscar_acta']
    return {'lista_actas' : lista_actas}
