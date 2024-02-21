import pygame

pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Equis Cero")

fondo = pygame.image.load('static/tic tac.png')
equis = pygame.image.load('static/cross.png')
cero = pygame.image.load('static/letter-o.png')

fondo = pygame.transform.scale(fondo, (450,450))
equis = pygame.transform.scale(equis, (125,125))
cero = pygame.transform.scale(cero, (125,125))

coor = [[(20,13),(165,13),(310,13)],
        [(20,160),(165,160),(310,160)],
        [(20,310),(165,310),(310,310)]]

tablero = [['','',''],
           ['','',''],
           ['','','']]

turno = 'X'
game_over = False
clock = pygame.time.Clock()

def graficar_board():
   screen.blit(fondo,(0,0))
   for fila in range(3):
      for col in range(3):
         if tablero[fila][col] == 'X':
            dibujar_x(fila,col)
         elif tablero[fila][col] == 'O':
            dibujar_o(fila,col)
         
def dibujar_x(fila,col):
   screen.blit(equis, coor[fila][col])
   
def dibujar_o(fila,col):
   screen.blit(cero, coor[fila][col])

def verificar_ganador():
   for i in range(3):
      if tablero [i][0] == tablero[i][1] == tablero[i][2] != '':
         return True
      if tablero [0][i] == tablero[1][i] == tablero[2][i] != '':
         return True
   if tablero [0][0] == tablero[1][1] == tablero[2][2] != '':
         return True
   if tablero [0][2] == tablero[1][1] == tablero[2][0] != '':
         return True
   return False
      

while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        game_over = True
       elif event.type == pygame.MOUSEBUTTONDOWN:
        mouseX, mouseY = event.pos
        if (mouseX >= 20 and mouseX < 340) and (mouseY >= 30 and mouseY < 350):
         fila = (mouseY - 30) // 125
         col = (mouseX - 20) // 125
         if tablero[fila][col] == '':
            tablero[fila][col] = turno
            fin_juego = verificar_ganador()
            if fin_juego:
               print(f"El jugador {turno} ha ganado!!")
               game_over = True
         turno = 'O' if turno == 'X' else 'X'
    graficar_board()

    pygame.display.update()

pygame.quit()