 
        fet = QgsFeature()
     #Dir = float(self.dlg.ui.radLeft.isChecked()
        layers = QgsProject.instance().mapLayers().values()
        Lexists = False
        vl = None  # Initialize vl outside the loop
        pr = None

        # Check to see if the virtual layer already exists
        for layer in layers:
            if layer.name() == "test-layer":
                Lexists = True
                vl = layer
                pr = vl.dataProvider()
                vl.startEditing()
                break

        # If it doesn't exist, create it
        if not Lexists:
            # Create the layer
            vl = QgsVectorLayer("Linestring", "test-layer", "memory")
            pr = vl.dataProvider()
            vl.startEditing()

        # Assuming path_geometry is defined elsewhere
        #nline = path_geometry.parallel_offset(2.0, 'right', resolution=16, join_style=1, mitre_limit=10.0)

        # Convert QgsGeometry to Shapely LineString
        line = LineString(geom.asPolyline())

        
        
       
        
        # Check if the line is multi-part
        if line.is_empty or not line.is_simple or line.geom_type.startswith('Multi') or  line.geom_type.startswith( 'LineString') :
            # Iterate over each part
            for part in line.geoms:
                # Perform parallel offset for each part
                nline = part.parallel_offset(2.0, 'right', join_style=1, mitre_limit=10.0)
                # Convert Shapely LineString back to QgsGeometry and add it to your output
                nline_qgis = QgsGeometry.fromPolyline([QgsPoint(x, y) for x, y in nline.coords])
                # Use nline_qgis as your new geometry
        else:
            # If it's a single-part geometry, perform parallel offset directly
            nline = line.parallel_offset(2.0, 'right', join_style=1, mitre_limit=10.0)
            # Convert Shapely LineString back to QgsGeometry
            nline_qgis = QgsGeometry.fromPolyline([QgsPoint(x, y) for x, y in nline.coords])
            # Use nline_qgis as your new geometry


        # Create a new feature
        fet = QgsFeature()
        fet.setGeometry(QgsGeometry.fromWkt(str(nline_qgis)))
        #fet.setAttributes([2.0, 'right', 1])

        # Add the feature to the provider
        pr.addFeatures([fet])

        # Commit changes if the layer is new
        if not Lexists:
            vl.commitChanges()

        # Add the layer to the project
       # QgsProject.instance().addMapLayer(vl)

        

        
