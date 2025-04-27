data segment
    num dw 5          ; Given number to check (change as needed)
    msg_even db 'Number is Even$'
    msg_odd db 'Number is Odd$'
data ends

code segment
assume cs:code, ds:data
start:
    mov ax, data      
    mov ds, ax

    mov ax, num       
    and al, 1         ; Only need to check AL, not full AX
    jz even_number    

odd_number:
    lea dx, msg_odd   
    mov ah, 09h       
    int 21h           
    jmp end_program   

even_number:
    lea dx, msg_even  
    mov ah, 09h       
    int 21h           

end_program:
    mov ah, 4Ch       
    int 21h
code ends
end start
