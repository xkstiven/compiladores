import pygame

ANCHO = 800
ALTO = 600
VERDE=[0,255,0]
NEGRO=[0,0,0]
GRIS=[137,137,137]
BLANCO=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    lb=None
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,50])
        self.image.fill(GRIS)
        self.rect= self.image.get_rect()
        self.var_x=0
        self.var_y=0

    def gravedad(self):
        if self.var_y==0:
            self.var_y = 1
        else:
            self.var_y += 0.25

        if self.rect.y >= ALTO-self.rect.height:
            self.rect.y = ALTO-self.rect.height
            self.var_y=0

    def update(self):
        self.gravedad()
        self.rect.x += self.var_x
        lc=pygame.sprite.spritecollide(self,self.lb,False)
        for b in lc:
            if self.var_x >0:
                self.rect.right=b.rect.left
            else:
                self.rect.left=b.rect.right

        self.rect.y += self.var_y
        lc=pygame.sprite.spritecollide(self,self.lb,False)
        for b in lc:
            if self.var_x >0:
                self.rect.bottom=b.rect.top
            else:
                self.rect.top=b.rect.bottom
            self.var_y=0


class Bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect= self.image.get_rect()
        self.rect.x = px
        self.rect.y = py




if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(NEGRO)

    todos=pygame.sprite.Group()
    bloques= pygame.sprite.Group()

    jp=Jugador()

    todos.add(jp)

    b=Bloque(80,40,650,500)
    todos.add(b)
    bloques.add(b)
    jp.lb=bloques

    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x =-4
                    #jp.var_y= 0
                if event.key == pygame.K_RIGHT:
                    jp.var_x =4
                    #jp.var_y= 0
                if event.key == pygame.K_UP:
                    jp.rect.y += -2
                    jp.var_y= -10
            '''
                if event.key == pygame.K_DOWN:
                    jp.var_x= 0
                    jp.var_y=5'''

        pantalla.fill(NEGRO)
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
