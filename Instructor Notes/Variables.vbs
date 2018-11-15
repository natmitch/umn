    ' variable can be declared on the same line
    ' if they are of the same types
    Dim var1, var2 As String
    
    var1 = "3"
    var2 = "5"

    ' this will print 8 as VBA converts them
    ' to number as a result of the plus sign
    MsgBox(var1 + var1)

    ' this will print 35 as we use the "&"
    ' as concatenation of two strings
    MsgBox(var1 & var2)

    Dim var3 as Integer
    var3 = 7
    ' this will give a TypeMixMatch error
    MsgBox (var1 + var2)
    
    ' convert var2 to an integer
    ' this will print 10
    MsgBox(int(var1) + var3)

    
    Dim name As String
    name = "Gandalf"

    'MsgBox (name)

    ' Basic String Concatenation (Combination)
    ' ----------------------------------------
    Dim title As String
    title = "The Great"

    Dim fullname As String
    fullname = name + " " + title

    'MsgBox (fullname)

    ' Basic Integer, Double, Long Variables
    ' ----------------------------------------
    Dim age1 As Integer
    Dim age2 As Integer
    age1 = 5
    age2 = 10

    Dim price As Double
    Dim tax As Double
    price = 19.99
    tax = 0.05

    Dim lightspeed As Long
    lightspeed = 299792458

    ' Basic Numeric manipulation
    ' ----------------------------------------
    'MsgBox (age1 + age2)
    Cells(1, 1).Value = price * (1 + tax)

    ' String, Numeric Combination (Casting)
    ' ----------------------------------------
    MsgBox ("I am " + Str(age1) + " years old.")

    ' Booleans
    ' ----------------------------------------
    Dim money_grows_on_trees As Boolean
    money_grows_on_trees = False

End Sub
