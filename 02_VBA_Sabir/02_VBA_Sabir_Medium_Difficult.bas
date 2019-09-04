
'*Medium-Difficult*/'
Sub SotckMac()
    Dim xSh As Worksheet
    Dim StockTicker As String
    Dim maxStockTicker, minStockTicker, maxStockTickerVol As String
    Dim TotalVolume, MaxTotalVolume As Double
    Dim i, y, x, z As Long
    Dim RangeRow As Long
    Dim LastRow As Long
    Dim OpenPrice As Double
    Dim ClosePrice As Double
    Dim YearDiff As Double
    Dim YearPercentage As Double
    Dim max As Double
    Dim min As Double
    
    Application.ScreenUpdating = False
    For Each xSh In Worksheets
        xSh.Select
'Initialize variables
    
    TotalVolume = 0
    OpenPrice = 0
    StockTicker = "A"
    RangeRow = 2
    LastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    
'Add headers
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Volume"
    Cells(2, 14).Value = "Greatest % Increase:"
    Cells(3, 14).Value = "Greatest % Decrease:"
    Cells(4, 14).Value = "Greatest Total Volume:"
    Cells(1, 16).Value = "Ticker"
    Cells(1, 17).Value = "Value"
    
    
    
'Compute data for each ticker
    For i = 2 To LastRow
        StockTicker = Cells(i, 1).Value
        
        If OpenPrice = 0 Then
            OpenPrice = Cells(i, 3).Value
        End If
        
        If Cells(i - 1, 1) = Cells(i, 1) And Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            
            TotalVolume = TotalVolume + Cells(i, 7).Value
            ClosePrice = Cells(i, 6).Value
            
            YearDiff = ClosePrice - OpenPrice
            
            If OpenPrice = 0 Then
                
                OpenPrice = 0.01
                
            Else
                
                YearPercentage = YearDiff / OpenPrice
                
            End If
            
            Range("I" & RangeRow).Value = StockTicker
            Range("J" & RangeRow).Value = YearDiff

            Range("K" & RangeRow).Value = YearPercentage
            Range("K" & RangeRow).NumberFormat = "0.00%"
            
            Range("L" & RangeRow).Value = TotalVolume
            
            If YearDiff < 0 Then
                Range("J" & RangeRow).Interior.ColorIndex = 3
                Range("J" & RangeRow).Font.ColorIndex = 1
            Else
                Range("J" & RangeRow).Interior.ColorIndex = 4
                Range("J" & RangeRow).Font.ColorIndex = 1
            End If
            
            
            RangeRow = RangeRow + 1
            TotalVolume = 0
            OpenPrice = 0
            
'MsgBox ticker
            
        Else
            TotalVolume = TotalVolume + Cells(i, 7).Value
        End If
        
        Next i
        
        
'Get greatest value
        max = 0
        min = 1
        MaxTotalVolume = 0
        
        For y = 2 To Cells(Rows.Count, 11).End(xlUp).Row
            If Cells(y, 11).Value > max Then
                max = Cells(y, 11).Value
                maxStockTicker = Cells(y, 9)
            End If
            Next y
            
            For z = 2 To Cells(Rows.Count, 12).End(xlUp).Row
                If Cells(z, 12).Value > MaxTotalVolume Then
                    MaxTotalVolume = Cells(z, 12).Value
                    maxStockTickerVol = Cells(z, 9)
                End If
                Next z
                
                
'Get mininum value
                For x = 2 To Cells(Rows.Count, 11).End(xlUp).Row
                    If Cells(x, 11).Value < min Then
                        min = Cells(x, 11).Value
                        minStockTicker = Cells(x, 9)
                    End If
                    Next x
                    
'Display
                    Range("P2").Value = maxStockTicker
                    Range("Q2").Value = max
                    Range("Q2").NumberFormat = "0.00%"
                    
                    Range("P3").Value = minStockTicker
                    Range("Q3").Value = min
                    Range("Q3").NumberFormat = "0.00%"
                    
                    Range("P4").Value = maxStockTickerVol
                    Range("Q4").Value = MaxTotalVolume
                    
    
                    
        

    Next
    Application.ScreenUpdating = True
    

End Sub
        
