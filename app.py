import pygame
import random
from pygame import mixer
pygame.font.init()
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)


#BACKGROUND MUSIC
bg_music=pygame.mixer.Sound("music.ogg")
bg_music.set_volume(0.2)






# SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


# GLOBALS VARIABLES

shapes = [S, J, T, I, O, L, Z]
shape_colors = [(173,255,47), (0,0,205), (128,0,128), (0,191,255), (255,255,0), (255,165,0), (255,0,0)]
# index 0 - 6 represent shape
block_size=30
w_width = 800
w_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 30 height per block
pause= False
icon=pygame.image.load('icon2.png')
icon_small = pygame.transform.scale(icon, (800, 600))
top_left_x = (w_width - play_width) // 2
top_left_y = w_height - play_height
score=0
level=0
quitval= False
resetval= False
#CLASS
class Piece:

      x = 10 # Number of columns, set default to 10
      y = 20 # Number of rows, set default to 20
      shape = 0 # Shape of piece, set default to 0
      color = () # Color of shape
      rotation = 0 #Current orientation/rotation, default set to 0
# This is a constructor
      def __init__(self, column, row, shape):

             # The values in parameters are assigned to the new object of type 'Piece'
            self.x = column
            self.y = row
            self.shape = shape
            self.color = shape_colors[shapes.index(shape)]
            self.rotation = 0

def game():
      window.fill((0,0,0))
      global score
      global level
      score=0
      level=0
      bg_music.play(-1)
      run = True
      tetris_icon(20,20,run)
      
# Our game runs until 'run' is made 'False'
      while run:
# Fill the window with Black Colour (RGB Value)
            window.fill (( 0,0,0 ))
            #pygame.mixer.unpause()
            
# Display this text in the middle of the window
            draw_text_start("Press start button to begin!", 60, (255, 255, 255), window)
            start_button()
# Update the screen
            pygame.display.update()

            # Track every event while the game is running
            for event in pygame.event.get():
            # If user clicks on the 'cross' to quit, make run = False
                  if event.type == pygame.QUIT:
                        run = False
                        
      pygame.quit()


def start_button():

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if 300+200 > mouse[0] > 300 and 380+100 > mouse[1] > 380:
            pygame.draw.rect(window, (0,255,127),(300,380,200,100))
            if click[0] == 1 :
                  play()
                     
      else:
            pygame.draw.rect(window, (0,250,154),(300,380,200,100))
      
      button_text = pygame.font.SysFont("arial",40,bold= True)
      label= button_text.render('Start',1,(0,0,0))
      window.blit(label,(355,410))

def draw_text_start(text, size, color, surface):
      # Which font do you want to use?
      font = pygame.font.SysFont('comicsans', size, bold=True)
      # Render the Text using font
      label = font.render(text, 1, color)
      # Print the Text using label
      surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y +
      play_height/2 - label.get_height()/2-100))

def draw_text_middle(text, size, color, surface):
      # Which font do you want to use?
      font = pygame.font.SysFont('comicsans', size, bold=True)
      # Render the Text using font
      label = font.render(text, 1, color)
      # Print the Text using label
      surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y +
      play_height/2 - label.get_height()/2))


def tetris_icon(x,y,run):
      
      window.blit(icon_small,(x-25,y+20))
      font = pygame.font.SysFont('arial',50)
      # Render the Text using font
      label = font.render("Tetris", 1, (192,192,192))
      # Print the Text using label
      window.blit(label, ( x+320, y+200))
      pygame.display.update()
      clock=pygame.time.Clock()
      pygame.time.wait(800)
      clock.tick()
      pygame.display.update()

def help_text():
      
      font = pygame.font.SysFont('arial', 13)
      label = font.render("move left                ←", 1, (105,105,105))
      window.blit(label, (40,205))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("move right              →", 1, (105,105,105))
      window.blit(label, (40,225))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("move down            ↓", 1, (105,105,105))
      window.blit(label, (40,245))
      font = pygame.font.SysFont('arial',13)
      label = font.render("change shape       ↑", 1, (105,105,105))
      window.blit(label, (40,265))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("pause/unpause     space", 1, (105,105,105))
      window.blit(label, (40,285))

def pause_text(text, size, color, surface):
      # Which font do you want to use?
      font = pygame.font.SysFont('comicsans', size, bold=True)
      # Render the Text using font
      label = font.render(text, 1, color)
      # Print the Text using label
      surface.blit(label, (top_left_x - 80, top_left_y + 350))




def move_piece(event,current_piece):
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                              current_piece.x -= 1
                              if not valid_space(current_piece,grid):
                                    current_piece.x += 1

                        elif event.key == pygame.K_RIGHT:
                              current_piece.x += 1
                              if not valid_space(current_piece,grid):
                                    current_piece.x -= 1

                        elif event.key == pygame.K_DOWN:
                              current_piece.y += 1
                              if not valid_space(current_piece,grid):
                                    current_piece.y -= 1
                        elif event.key == pygame.K_UP:
                              current_piece.rotation = current_piece.rotation + 1% len(current_piece.shape)
                              if not valid_space(current_piece, grid):
                                    current_piece.rotation = current_piece.rotation - 1% len(current_piece.shape)
                        
                
def paused():

      pygame.mixer.pause()
      pause = True
      window.fill((47,79,79))
      draw_text_middle("PAUSED",60,(192,192,192),window)
      pause_text("PRESS SPACE TO CONTINUE",40,(220,220,220),window)
      
      pygame.display.update()
      clock=pygame.time.Clock()
      clock.tick(5)

      while pause:
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                              pygame.mixer.unpause()
                              pause= False

                  if event.type == pygame.QUIT:
                        pygame.display.quit()
                        quit()

def get_speed(level):


      if   level==0:
            speed = 1
      if level==1:
            speed=0.5
      if level==2:
            speed= 0.25
      if level==3:
            speed=0.125
     

      return speed

def play():
# A global variable grid
      global grid
# The positions already occupied
      locked_positions = { }
# create_grid returns the created grid
      grid = create_grid(locked_positions)
      
      change_piece=False
      run =True
      current_piece=get_shape()
      next_piece=get_shape()
      clock=pygame.time.Clock()
      fall_time=0
      while run:
            
            fall_speed=update_level(score)
            grid=create_grid(locked_positions)
            fall_time += clock.get_rawtime()
            clock.tick()

            if fall_time/1000>=fall_speed:
                  fall_time =0
                  current_piece.y += 1
                  if not(valid_space(current_piece,grid)) and current_piece.y>0:
                        current_piece.y -= 1
                        change_piece= True

            
            
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        run=False
                        pygame.display.quit()
                        quit()
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                              pause=True
                              paused()

                  move_piece(event,current_piece)




            shape_pos = convert_shape_format(current_piece)                 
            for i in range(len(shape_pos)):
                  x,y =shape_pos[i]
                  if y> -1:
                        grid[y][x] = current_piece.color            
            
            if change_piece:
                  for pos in shape_pos:
                        p= (pos[0],pos[1])
                        locked_positions[p] = current_piece.color

                  current_piece =next_piece
                  next_piece = get_shape()
                  change_piece = False
                  clear_rows(grid,locked_positions)

            
            draw_window(window)
            draw_next_shape(next_piece,window)
            update_level(score)
            pygame.display.update()

            if check_lost(locked_positions):
                  run = False
      window.fill((0,0,0))
      draw_text_middle("YOU LOST",80,(255,255,255),window)

      pygame.display.update()
      pygame.time.delay(2000)

def clear_rows(grid,locked):
      global score
      inc =0
      for i in range(len(grid)-1,-1,-1):
            row=grid[i]
            if(0,0,0) not in row:
                  inc+=1
                  ind = i
                  for j in range(len(row)):
                        try:
                              del locked[(j,i)]
                        except:
                              continue
      if inc>0:
            temp = sorted(list(locked), key = lambda x: x[1])
            for key in temp[::-1]:
                  x,y=key
                  if y<ind:
                        newkey=(x,y+inc)
                        locked[newkey]=locked.pop(key)
            score+=(10*inc)       
def intro_text():
      font = pygame.font.SysFont('arial', 13)
      label = font.render("Welcome to the Classic TETRIS", 1, (105,105,105))
      window.blit(label, (35,420))
      font = pygame.font.SysFont('arial', 11)
      label = font.render("During a single gamerun your SCORE", 1, (105,105,105))
      window.blit(label, (35, 450))
      font = pygame.font.SysFont('arial', 11)
      label = font.render("and LEVEL progress will be saved", 1, (105,105,105))
      window.blit(label, (45, 462))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("GAME consists of 4 LEVELS", 1, (105,105,105))
      window.blit(label, (47, 480))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("starting from 0 ", 1, (105,105,105))
      window.blit(label, (85 , 492))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("You unlock new levels at the ", 1, (105,105,105))
      window.blit(label, (45, 510 ))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("SCORE of 50, 150 AND 300", 1, (105,105,105))
      window.blit(label, (45, 525))
      font = pygame.font.SysFont('arial', 13)
      label = font.render("With each level speed increases", 1, (105,105,105))
      window.blit(label, (35, 545))
      font = pygame.font.SysFont('arial', 11)
      label = font.render("RESET button will remove all your", 1, (255,0,0))
      window.blit(label, (45, 565))
      font = pygame.font.SysFont('arial', 11)
      label = font.render("SCORE and LEVEL progress", 1, (255,0,0))
      window.blit(label, (55, 580))

def draw_window(surface):
      surface.fill((0,0,0))
      font=pygame.font.SysFont('arial',50,bold= False)
      label=font.render('TETRIS',1,(255,255,255))
      surface.blit(label,(top_left_x+play_width/2-(label.get_width()/2),30))

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  pygame.draw.rect(surface,grid[i][j],(top_left_x + j*30, top_left_y + i*30, block_size, block_size),0)


      draw_grid(surface,20,10)
      pygame.draw.rect(surface,(128,128,128),(top_left_x,top_left_y,play_width,play_height),5)
      pygame.draw.rect(surface,(50,50,50),(26,188,180,120),1)
      help_text()
      pygame.draw.rect(surface,(50,50,50),(26,400,180,200),1)
      intro_text()
      pause_button(surface)
      reset_button(surface)
      quit_button(surface)


def pause_button(surface):

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if 630+80 > mouse[0] > 630 and 530+30 > mouse[1] > 530:
            pygame.draw.rect(surface, (240,128,128),(630,530,80,30))
            if click[0] == 1 :
                  paused()
                     
      else:
            pygame.draw.rect(surface, (250,128,114),(630,530,80,30))
      
      button_text = pygame.font.SysFont("freesansbold",22)
      label= button_text.render('PAUSE',1,(0,0,0))
      surface.blit(label,(645,540))


def reset_button(surface):

      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if 630+80 > mouse[0] > 630 and 575+30 > mouse[1] > 575:
            pygame.draw.rect(surface, (255,127,80),(630,575,80,30))
            if click[0] == 1 :
                  reset_window()
                     
      else:
            pygame.draw.rect(surface, (255,99,71),(630,575,80,30))
      
      button_text = pygame.font.SysFont("freesansbold",22)
      label= button_text.render('RESET',1,(0,0,0))
      surface.blit(label,(645,585))
      

def quit_button(surface):
      mouse = pygame.mouse.get_pos()
      click = pygame.mouse.get_pressed()
      if 630+80 > mouse[0] > 630 and 620+30 > mouse[1] > 620:
            pygame.draw.rect(surface,(216,191,216),(630,620,80,30))
            if click[0] == 1 :
                  quit_window()

      else:
            pygame.draw.rect(surface,(221,160,221),(630,620,80,30))


      button_text = pygame.font.SysFont("freesansbold",22)
      label= button_text.render('QUIT',1,(0,0,0))
      surface.blit(label,(652,630))

 


def quit_window():
      pygame.mixer.pause()
      quitval = True
      window.fill((47,79,79))
      draw_text_middle("Press ESCAPE to quit and any other key to return to the game screen",28,(211,211,211),window)
      pygame.display.update()
      clock=pygame.time.Clock()
      clock.tick(5)

      while quitval:
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                              pygame.quit()
                              quit()
                        else:
                              pygame.mixer.unpause()

                              quitval= False

                  if event.type == pygame.QUIT:
                        pygame.display.quit()
                        quit()
                  
def reset_window():
      pygame.mixer.pause()
      resetval = True
      window.fill((47,79,79))
      draw_text_middle("Press 'R' key to reset and any other key to return to the game screen",25,(211,211,211),window)
      pygame.display.update()
      clock=pygame.time.Clock()
      clock.tick(5)

      while resetval:
            for event in pygame.event.get():
                  if event.type == pygame.KEYUP:
                        if event.key == pygame.K_r:
                              bg_music.stop()
                              game()
                        else:
                              pygame.mixer.unpause()

                              resetval= False

                  if event.type == pygame.QUIT:
                        pygame.display.quit()
                        quit()
                  
      

def draw_grid(surface,row,col):
      sx=top_left_x
      sy=top_left_y
      for i in range(row):
            pygame.draw.line(surface,(128,128,128),(sx , sy + i*30), (sx + play_width, sy + i*30))

            for j in range(col):
                  pygame.draw.line(surface,(128,128,128),(sx+j*30,sy),(sx+j*30,sy+play_height))

def draw_next_shape(piece,surface):
      font=pygame.font.SysFont('comicsans',30)
      label=font.render('Next Shape',1,(255,255,255))

      sx=top_left_x+play_width+50
      sy=top_left_y+play_height/2-100

      format=piece.shape[piece.rotation % len(piece.shape)]

      i=0
      for line in format:
            row=list(line)
            j=0
            for column in row:
                  if column=='0':
                        pygame.draw.rect(surface,piece.color,(sx+j*30,sy+i*25,30,30),0)

                  j+=1
            i+=1
      surface.blit(label,(sx+15,sy-30))
      update_score(surface)

def update_score(surface):
 
      text= "Score: " + str(score)
      
      font=pygame.font.SysFont('comicsans',40)
      label=font.render(text,1,(255,255,255))
      sx=top_left_x+play_width+40
      sy=top_left_y+play_height/2 - 100
      surface.blit(label,(sx+25,sy+140))

def update_level(score):
      if score<50:
            level=0
            s=get_speed(level)
      if score>=50 and score<150:
            level=1
            s=get_speed(level)
      elif score>=150 and score<300:
            level=2
            s=get_speed(level)
      elif score>=300:
            level=3
            s=get_speed(level)
      font=pygame.font.SysFont('arial',20,bold=True)
      text2="LEVEL : " + str(level)
      label2= font.render(text2,2,(119,136,153))
      sx=top_left_x+play_width+40
      sy=top_left_y+play_height/2 - 100
      window.blit(label2,(sx+35,sy+190))
      
      return s

      

def check_lost(positions):
      for pos in positions:
            x,y = pos

            if y<1:
                  return True
      return False

def valid_space(piece,grid):
      accepted_positions=[[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
      accepted_positions=[j for sub in accepted_positions for j in sub]
      formatted=convert_shape_format(piece)

      for pos in formatted:
            if pos not in accepted_positions:
                  if pos[1]>-1:
                        return False
      return True

def convert_shape_format(piece):
      positions=[]
      format=piece.shape[piece.rotation % len(piece.shape)]

      i=0
      for line in format:
            row=list(line)
            j=0
            for column in row:
                  if column=='0':
                        positions.append((piece.x+ j, piece.y+ i))
                  j += 1
            i +=1

      k=0
      for pos in positions:
            positions[k]=(pos[0]-2,pos[1]-4)
            k+=1
      return positions

def get_shape():
      newPiece=Piece(5,0,random.choice(shapes))
      return newPiece   

def create_grid(locked_positions):
      grid=[[(0,0,0)for x in range(10)]for y in range(20)]

      for i in range(len(grid)):
            for j in range(len(grid[i])):
                  if (j,i) in locked_positions:
                        c=locked_positions[(j,i)]
                        grid[i][j] = c
      return grid



window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption('TETRIS')
game()