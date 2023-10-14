
def CentrarPantalla(parentWidth:int, parentHeight:int, widgetWidht:int, widgetHeight:int):
    x = int(parentWidth/2 - widgetWidht/2)
    y = int(parentHeight/2 - widgetHeight/2)
    return f'{widgetWidht}x{widgetHeight}+{x}+{y}'