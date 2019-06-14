Attribute VB_Name = "Test"
'For avoiding any possible error,
'the values in the ticker column must be sorted,
'and the output area must be empty before executing the code.

Sub Test()
    Range("I1") = "Ticker"
    Range("J1") = "Total Stock Value"
    Range("K1") = "Ticker Quantity"
    Dim i As Long
    Dim j As Long
    Dim k As Integer
    Dim groupTicker As String
    Dim last_row As Long
    
    last_row = Cells(Rows.Count, 1).End(xlUp).Row
    
    j = 2
    k = 1
    groupTicker = Cells(2, 1).Value
    
    For i = 2 To last_row
    
        If StrComp(Cells(i, 1).Value, groupTicker) <> 0 Then
            groupTicker = Cells(i, 1).Value
            j = j + 1
            k = 1
        End If
        
        Cells(j, 9).Value = groupTicker
        Cells(j, 10) = Cells(j, 10) + Cells(i, 7)
        Cells(j, 11) = k
        
        k = k + 1
        
    Next i
End Sub
