data segment
    num db 10110101b    ; 8-bit binary number
    ones_count db ?     ; To store the count of 1's
    zeros_count db ?    ; To store the count of 0's
    msg_ones db 'Number of 1''s: $'
    newline db 0Dh,0Ah,'$'    ; New line for clarity
    msg_zeros db 'Number of 0''s: $'
data ends

code segment
assume cs:code, ds:data

start:
    mov ax, data     ; Initialize data segment
    mov ds, ax

    mov al, num      ; Load number into AL
    mov ah, al       ; Copy original number into AH (backup)

    mov bl, 8        ; Set bit count to 8
    xor ch, ch       ; Clear 1's count (CH)
    xor cl, cl       ; Clear 0's count (CL)

count_bits:
    shr al, 1        ; Shift right, bit moves into CF
    jc count_one     ; If CF=1, it's a 1
    inc cl           ; Otherwise increment 0's count
    jmp next_bit

count_one:
    inc ch           ; Increment 1's count

next_bit:
    dec bl           ; Decrement bit counter
    jnz count_bits   ; Repeat until 0

    ; Store the results
    mov ones_count, ch
    mov zeros_count, cl

    ; Display number of 1's
    lea dx, msg_ones
    mov ah, 9
    int 21h

    mov al, ch       ; Load 1's count
    add al, 30h      ; Convert to ASCII
    mov dl, al
    mov ah, 2
    int 21h

    ; Newline after number of 1's
    lea dx, newline
    mov ah, 9
    int 21h

    ; Display number of 0's
    lea dx, msg_zeros
    mov ah, 9
    int 21h

    mov al, cl       ; Load 0's count
    add al, 30h      ; Convert to ASCII
    mov dl, al
    mov ah, 2
    int 21h

    ; Exit program
    mov ah, 4Ch
    int 21h

code ends
end start
