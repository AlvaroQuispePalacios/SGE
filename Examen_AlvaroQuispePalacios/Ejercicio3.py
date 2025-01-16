def formatear_resultado(func):    
    def envoltura():
        resultado = func()
        
    return envoltura



