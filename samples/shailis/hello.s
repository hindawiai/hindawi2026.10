.intel_syntax noprefix
.global _start
.text
_start:
    MOV EAX, 4
    MOV EBX, 1
    LEA ECX, msg
    MOV EDX, 28
    INT 0x80
    MOV EAX, 1
    XOR EBX, EBX
    INT 0x80
.data
msg: .ascii "Hello from Hindawi assembly\n"
