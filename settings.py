import  pygame
class Hero():
    def __init__(self,screen_rect):
        self.screen_rect = screen_rect
        self.image= pygame.image.load("hero2.bmp")
        self.rect=self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery= 400
        self.speed = 1
        self.walk = False
        self.orientation=1
    def blitme(self):
        if (self.orientation==1 and self.walk==True):
            self.rect.centerx+=self.speed
        if (self.orientation == 2 and self.walk == True):
            self.rect.centerx -= self.speed
        if (self.orientation == 3 and self.walk == True):
            self.rect.centery +=self.speed
        if (self.orientation == 4 and self.walk == True):
            self.rect.centery -= self.speed
        self.screen_rect.blit(self.image,self.rect)