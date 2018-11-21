Sub CheckerBoard()

  ' Loop through each row of the board
  For i = 1 To 8

    ' If row number is divisible by 2 then start painting
    ' the first cell black then alternate between red and black
    If (i Mod 2 = 0) Then

        Range("B" & i).Interior.ColorIndex = 1
        Range("D" & i).Interior.ColorIndex = 1
        Range("F" & i).Interior.ColorIndex = 1
        Range("H" & i).Interior.ColorIndex = 1

        Range("A" & i).Interior.ColorIndex = 3
        Range("C" & i).Interior.ColorIndex = 3
        Range("E" & i).Interior.ColorIndex = 3
        Range("G" & i).Interior.ColorIndex = 3

    ' Otherwise start painting the first cell red
    ' then alternate between black and red
    Else

        Range("B" & i).Interior.ColorIndex = 3
        Range("D" & i).Interior.ColorIndex = 3
        Range("F" & i).Interior.ColorIndex = 3
        Range("H" & i).Interior.ColorIndex = 3

        Range("A" & i).Interior.ColorIndex = 1
        Range("C" & i).Interior.ColorIndex = 1
        Range("E" & i).Interior.ColorIndex = 1
        Range("G" & i).Interior.ColorIndex = 1

    End If

  Next i

End Sub
