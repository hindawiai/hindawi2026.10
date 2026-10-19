    .global _start
    .text
_start:
    mov $1, %rax
    mov $1, %rdi
    lea msg(%rip), %rsi
    mov $len, %rdx
    syscall
    mov $60, %rax
    xor %rdi, %rdi
    syscall
    .data
msg: .ascii "Hello from Hindawi assembly\n"
len = . - msg
