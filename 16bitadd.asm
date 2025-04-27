data segment
    a dw 2205h    ; First BCD number
    b dw 1104h    ; Second BCD number
    c dw ?        ; Result lower 16 bits
    d dw ?        ; Result upper 16 bits (carry)
    msg_result db 0Dh,0Ah, 'Result: $'
data ends

code segment
assume cs:code, ds:data
start:
    mov ax, data
    mov ds, ax

    ; Add BCD numbers
    mov ax, a
    mov bx, b

    ; Lower byte addition
    mov al, al
    add al, bl
    daa
    mov dl, al

    ; Higher byte addition with carry
    mov al, ah
    adc al, bh
    daa
    mov dh, al

    ; Save result
    mov dx, dx      ; DX has combined result
    mov c, dx

    ; Final carry handling
    xor ax, ax
    adc ax, 0
    mov d, ax

    ; Display result
    ; Show "Result: "
    mov ah, 09h
    lea dx, msg_result
    int 21h

    ; Check if there was a carry (d != 0)
    mov ax, d
    cmp ax, 0
    je skip_carry
    ; If carry exists, print '1'
    mov dl, '1'
    mov ah, 02h
    int 21h

skip_carry:
    ; Now print each digit from DX (which has the BCD result)

    mov ax, c
    mov ah, al        ; Move lower byte to AH
    shr ah, 4         ; Higher nibble (first digit)
    call display_digit

    mov ax, c
    and al, 0Fh       ; Lower nibble (second digit)
    mov ah, 0
    call display_digit

    mov ax, c
    mov ah, bh        ; Higher byte (third and fourth digits)
    shr ah, 4
    call display_digit

    mov ax, c
    mov ah, bh
    and ah, 0Fh
    call display_digit

    ; Exit program
    mov ah, 4Ch
    int 21h

; Subroutine to display a single digit
display_digit proc
    add ah, 30h        ; Convert number to ASCII
    mov dl, ah
    mov ah, 02h
    int 21h
    ret
display_digit endp

code ends
end start
