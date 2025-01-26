Require mklicense

Output ../preview/out1.gif

Set Width 2000
Set Height 1000
Set TypingSpeed 100ms
Set WindowBar Colorful

Env MKLICENSE_FACTORY ""

Type "mklicense"
Enter
Sleep 3s
Enter
Sleep 2s
Tab
Sleep 1s
Type "2025"
Sleep 1s
Tab
Sleep 1s
Type "John Doe"
Sleep 1s
Tab
Sleep 1s
Enter
Down
Sleep 500ms
Down
Enter
Sleep 1s
Tab
Sleep 1s
Enter
Sleep 1s
Type "cat LICENSE* | head -n 10"
Enter
Sleep 4s

Hide
Type "rm LICENSE*"
Enter

