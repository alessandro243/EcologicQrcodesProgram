def clearLayout(layout):
    if layout is None:
        return
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget() 
        if widget is not None:
            widget.setParent(None)  
            widget.deleteLater() 
        else:
            
            child_layout = item.layout()
            if child_layout is not None:
                clearLayout(child_layout)