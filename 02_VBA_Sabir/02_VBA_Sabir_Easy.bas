'/*Easy*/

Sub Total_Volume():
	
	Dim ws As Worksheet
	Dim totalvolume As Double
	Dim I,j As Integer
	
	For Each ws In Worksheets
		totalvolume = 0
		j = 0
		
		ws.Range("I1").Value = "Ticker"
		ws.Range("J1").Value = "Total Volume"
		
		lastRow = Cells(Rows.Count, "A").End(xlUp).Row
		
		For i = 2 To lastRow
			
			If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
				
				totalvolume = totalvolume + ws.Cells(i, 7).Value
				
				ws.Range("I" & 2 + j).Value = ws.Cells(i, 1).Value
				ws.Range("J" & 2 + j).Value = totalvolume
				
				totalvolume = 0
				j = j + 1
				
			Else
				totalvolume = totalvolume + ws.Cells(i, 7).Value
				
			End If
			
		Next i
			
		totalvolume = 0
		j = 0
			
	Next ws
			
End Sub


