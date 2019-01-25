Sub Checkerboard()

    For i = 1 To 8
          
        For j = 1 To 8
        
        
            'Fill every other even row even col cell red
            If i Mod 2 = 0 And j Mod 2 = 0 Then
            Cells(i, j).Interior.ColorIndex = 3
            
            End If
            
            
            'Fill every other odd row odd col cell red
            If i Mod 2 <> 0 And j Mod 2 <> 0 Then
            Cells(i, j).Interior.ColorIndex = 3
            
            End If
            
            
            
            'Fill every other even row odd col cell black
            If i Mod 2 = 0 And j Mod 2 <> 0 Then
            Cells(i, j).Interior.ColorIndex = 1
            
            End If
            
            
            'Fill every other odd row even col cell black
            If i Mod 2 <> 0 And j Mod 2 = 0 Then
            Cells(i, j).Interior.ColorIndex = 1
            
            End If
        
        Next j
    
    Next i

End Sub
